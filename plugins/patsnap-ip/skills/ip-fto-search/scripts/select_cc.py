#!/usr/bin/env python3
"""Prepare a complete catalogue; freeze and validate an explicit user choice.

Offline only. This validates records, not human identity or FTO coverage.
"""

import argparse
import hashlib
import html
import json
import sys
from pathlib import Path


def check_failure(value):
    if isinstance(value, dict) and (
        value.get("isError") is True
        or value.get("success") is False
        or value.get("status") == "error"
    ):
        raise ValueError("Screening 回执包含失败标志；不能生成可提交的 CC 名单。")


def evidence_value(document, pointer):
    """Resolve a JSON Pointer without assuming a service output schema."""
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("证据须定位到实际结果中的非根 JSON Pointer。")
    value = document
    for token in pointer[1:].split("/"):
        if any(i + 1 == len(token) or token[i + 1] not in "01" for i, char in enumerate(token) if char == "~"):
            raise ValueError("JSON Pointer 转义无效。")
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            if not token.isdigit() or str(int(token)) != token:
                raise ValueError("JSON Pointer 数组索引无效。")
            index = int(token)
            if index >= len(value):
                raise ValueError("证据定位超出结果范围。")
            value = value[index]
        elif isinstance(value, dict) and token in value:
            value = value[token]
        else:
            raise ValueError("证据定位不存在。")
    if value is None or value == "" or value == [] or value == {}:
        raise ValueError("证据定位指向空内容。")
    return value


def screening_items(receipt):
    """Read a local, source-linked FTO Screening record without guessing service fields."""
    check_failure(receipt)
    if not isinstance(receipt, dict) or receipt.get("schema_version") != "fto-screening-evidence-2":
        raise ValueError("须先核对完整 screen_patents_for_FTO 回执并建立本地筛选记录。")
    if receipt.get("results_complete") is not True:
        raise ValueError("任务或结果分页未完成，不能冻结候选目录。")
    sources = receipt.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("缺少原始结果来源。")
    documents, paths = [], set()
    for source in sources:
        if not isinstance(source, dict) or not isinstance(source.get("path"), str):
            raise ValueError("结果来源须有真实文件与散列。")
        actual, raw = file_record(source["path"])
        if source != actual or actual["path"] in paths:
            raise ValueError("结果来源已变更、记录不符或重复。")
        paths.add(actual["path"])
        value = json.loads(raw)
        check_failure(value)
        documents.append(value)
    submitted = receipt.get("submitted_pns")
    remaps = receipt.get("identity_remaps")
    unresolved = receipt.get("unresolved_pns")
    nonreturned = receipt.get("nonreturned_pns")
    for label, values in [("提交PN", submitted), ("未解析PN", unresolved), ("未返回PN", nonreturned)]:
        if not isinstance(values, list) or not all(isinstance(x, str) and x.strip() for x in values) or len(set(values)) != len(values):
            raise ValueError(f"{label}须为不重复的实际公开号列表。")
    if set(unresolved).intersection(nonreturned):
        raise ValueError("同一PN不能同时标记未解析和未返回。")
    if not isinstance(remaps, list):
        raise ValueError("identity_remaps须为数组，可为空。")
    remap_inputs, remap_outputs = set(), set()
    for item in remaps:
        if not isinstance(item, dict):
            raise ValueError("identity_remaps条目须为对象。")
        input_pn, returned_pn, reason = item.get("input_pn"), item.get("returned_pn"), item.get("reason")
        if not all(isinstance(x, str) and x.strip() for x in [input_pn, returned_pn, reason]):
            raise ValueError("身份映射须包含非空input_pn、returned_pn和核验理由。")
        if input_pn in remap_inputs or input_pn not in submitted:
            raise ValueError("身份映射输入PN重复或不属于提交集合。")
        remap_inputs.add(input_pn)
        remap_outputs.add(returned_pn)
    if remap_inputs.intersection(unresolved) or remap_inputs.intersection(nonreturned):
        raise ValueError("已映射输入PN不能同时标记未解析或未返回。")
    records = receipt.get("records")
    if not isinstance(records, list):
        raise ValueError("缺少逐项筛选记录。")
    seen, selected = set(), []
    for position, item in enumerate(records, 1):
        if not isinstance(item, dict):
            raise ValueError("筛选记录须为对象。")
        pid = item.get("patent_id")
        if not isinstance(pid, str) or not pid.strip() or pid in seen:
            raise ValueError("筛选身份缺失或重复。")
        seen.add(pid)
        if not isinstance(item.get("pn"), str):
            raise ValueError("PN 须为核对后的字符串，可为空。")
        refs = item.get("evidence_refs")
        if not isinstance(refs, list) or not refs:
            raise ValueError("每项判断必须有实际结果定位。")
        for ref in refs:
            if not isinstance(ref, dict) or type(ref.get("source_index")) is not int or not 1 <= ref["source_index"] <= len(documents):
                raise ValueError("证据来源序号无效。")
            evidence_value(documents[ref["source_index"] - 1], ref.get("pointer"))
        selected.append({"patent_id": pid, "pn": item["pn"], "screening_decision": "returned_candidate", "source_position": position})
    returned_pns = {x["pn"] for x in selected}
    if "" in returned_pns or returned_pns.intersection(unresolved) or returned_pns.intersection(nonreturned):
        raise ValueError("返回候选PN与未解析／未返回集合冲突。")
    unexpected = returned_pns - set(submitted)
    if unexpected - remap_outputs:
        raise ValueError("存在未核验的输入外返回PN。")
    represented_inputs = (returned_pns & set(submitted)) | remap_inputs
    if represented_inputs | set(unresolved) | set(nonreturned) != set(submitted):
        raise ValueError("提交PN没有完整映射到返回、未解析或未返回集合。")
    return selected


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def file_record(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "sha256": sha(raw)}, raw


def collect_candidates(paths):
    candidates, sources, by_id = [], [], {}
    for group, path in enumerate(paths, 1):
        source, raw = file_record(path)
        if any(x["path"] == source["path"] for x in sources):
            raise ValueError("同一 Screening 文件不能作为两个分组。")
        items = screening_items(json.loads(raw))
        sources.append({**source, "returned_count": len(items)})
        for item in items:
            pid, pn = item["patent_id"], item["pn"]
            origin = {"source_index": group, "screening_position": item["source_position"]}
            if pid in by_id:
                row = by_id[pid]
                if row["pn"] != pn:
                    raise ValueError("跨回执同 ID 的 PN 不一致，先核对身份。")
                row["origins"].append(origin)
            else:
                row = {"row_id": f"S{len(candidates) + 1:03d}", "patent_id": pid,
                       "pn": pn, "screening_decision": item["screening_decision"], "origins": [origin]}
                candidates.append(row)
                by_id[pid] = row
    return sources, candidates


def prepare_catalog(paths, case_id, input_version, scope, language="zh", metadata=None):
    if language not in {"zh", "en"}:
        raise ValueError("页面仅内置 zh/en；其他交付语言须先完整本地化。")
    if not all(isinstance(x, str) and x.strip() for x in [case_id, input_version, scope]):
        raise ValueError("案件、输入版本和范围说明不能为空。")
    sources, candidates = collect_candidates(paths)
    if not sources:
        raise ValueError("必须提供有真实结果来源的本地筛选记录。")
    if metadata is not None:
        display = metadata.get("by_patent_id") if isinstance(metadata, dict) else None
        if not isinstance(display, dict):
            raise ValueError("metadata 必须包含 by_patent_id 对象。")
        allowed = {"title", "assignees", "jurisdiction", "legal_status", "screening_reason", "completeness", "url", "source_ref"}
        for row in candidates:
            data = display.get(row["patent_id"], {})
            if not isinstance(data, dict):
                raise ValueError("metadata 条目必须为对象。")
            row["display"] = {k: v for k, v in data.items() if k in allowed}
    catalog = {
        "schema_version": "fto-cc-catalog-3", "case_id": case_id, "input_version": input_version,
        "scope": scope, "output_language": language, "batch_limit": 10,
        "status": "awaiting_user_strategy" if candidates else "no_candidates",
        "sources": sources, "candidate_count": len(candidates), "candidates": candidates,
        "order": "source_order" if len(sources) == 1 else "group_order_not_global_rank",
    }
    catalog["catalog_sha256"] = sha(canonical(catalog))
    return catalog


def check_catalog(catalog):
    if not isinstance(catalog, dict) or catalog.get("schema_version") != "fto-cc-catalog-3":
        raise ValueError("不是当前版本的候选目录。")
    unhashed = {k: v for k, v in catalog.items() if k != "catalog_sha256"}
    if sha(canonical(unhashed)) != catalog.get("catalog_sha256"):
        raise ValueError("目录已改变；不能沿用旧选择。")
    sources, rows = collect_candidates([x["path"] for x in catalog["sources"]])
    if sources != catalog["sources"]:
        raise ValueError("源回执已改变；须重建目录并由用户重新选择。")
    identities = [{k: v for k, v in x.items() if k != "display"} for x in catalog["candidates"]]
    if rows != identities or catalog["candidate_count"] != len(rows):
        raise ValueError("目录与有来源的筛选记录不符。")
    if catalog.get("batch_limit") != 10:
        raise ValueError("本地核验批次大小为 10。")
    expected = "awaiting_user_strategy" if rows else "no_candidates"
    if catalog.get("status") != expected:
        raise ValueError("目录状态无效。")


def filtered_candidates(catalog, criteria):
    """Exact metadata matching; unknowns remain eligible until explicitly reviewed."""
    allowed = {"assignees", "legal_status", "jurisdiction"}
    if not isinstance(criteria, dict) or not criteria or not set(criteria) <= allowed:
        raise ValueError("过滤条件必须为已支持的非空字段对象。")
    for values in criteria.values():
        if not isinstance(values, list) or not values or not all(isinstance(x, str) and x.strip() for x in values) or len(values) != len(set(values)):
            raise ValueError("每个过滤字段须为非空、不重复的字符串值列表。")
    eligible, unknown = [], []
    for row in catalog["candidates"]:
        display = row.get("display", {})
        missing, mismatch = False, False
        for field, values in criteria.items():
            raw = display.get(field)
            actual = raw if field == "assignees" and isinstance(raw, list) else [raw]
            actual = [x for x in actual if isinstance(x, str) and x.strip()]
            if not actual:
                missing = True
            elif not set(values).intersection(actual):
                mismatch = True
        if not mismatch:
            eligible.append(row["patent_id"])
            if missing:
                unknown.append(row["patent_id"])
    return eligible, unknown


def confirm_selection(catalog, choice_path, user_action_path):
    check_catalog(catalog)
    choice_record, raw = file_record(choice_path)
    choice = json.loads(raw)
    if not isinstance(choice, dict) or choice.get("schema_version") != "fto-cc-choice-3":
        raise ValueError("选择记录须使用有效结构并明确全部／部分及全文策略。")
    if choice.get("catalog_sha256") != catalog["catalog_sha256"]:
        raise ValueError("用户选择属于其他目录或版本。")
    ids = choice.get("selected_patent_ids")
    if not isinstance(ids, list) or not all(isinstance(x, str) and x.strip() for x in ids):
        raise ValueError("用户选择须为合法 ID 数组。")
    if not ids:
        raise ValueError("未选择对象；不能生成可提交 CC 批次。")
    if len(set(ids)) != len(ids):
        raise ValueError("选择包含重复 ID。")
    known = {x["patent_id"] for x in catalog["candidates"]}
    if not set(ids) <= known:
        raise ValueError("用户选择包含最终 Screening 目录之外的对象。")
    strategy, evidence_mode = choice.get("strategy"), choice.get("evidence_mode")
    if strategy not in {"all", "subset"} or evidence_mode not in {"claims", "fulltext"}:
        raise ValueError("全部／部分及说明书全文选项必须分别明确，不能使用默认值。")
    method, criteria, unknown = None, {}, []
    if strategy == "all":
        if set(ids) != known:
            raise ValueError("全部策略必须包含完整目录，不能被搜索或过滤视图截断。")
        if choice.get("filters") or choice.get("subset_method"):
            raise ValueError("全部策略不能同时带部分筛选条件。")
    else:
        method = choice.get("subset_method")
        if method not in {"manual", "filters"}:
            raise ValueError("部分策略须标明手动选择或字段过滤。")
        criteria = choice.get("filters", {})
        if criteria or method == "filters":
            eligible, unknown = filtered_candidates(catalog, criteria)
            if method == "filters" and set(ids) != set(eligible):
                raise ValueError("字段筛选结果与 IDs 不符；未知项不得静默删去，手动调整应标 manual。")
    action_record, action_raw = file_record(user_action_path)
    if not action_raw.strip():
        raise ValueError("实际用户回复／动作记录不能为空；脚本不能认证真人来源。")
    chosen = set(ids)
    # Preserve catalogue order, never infer selection from position or metadata.
    selected = [{k: v for k, v in row.items() if k != "display"}
                for row in catalog["candidates"] if row["patent_id"] in chosen]
    ordered_ids = [x["patent_id"] for x in selected]
    batches = [{"batch": i // 10 + 1, "patent_ids": ordered_ids[i:i + 10]}
               for i in range(0, len(ordered_ids), 10)]
    return {
        "schema_version": "fto-cc-selection-3", "status": "user_confirmed",
        "case_id": catalog["case_id"], "input_version": catalog["input_version"],
        "catalog_sha256": catalog["catalog_sha256"], "sources": catalog["sources"],
        "selection_rule": "explicit_user_choice", "choice_record": choice_record,
        "user_action_record": action_record, "strategy": strategy, "evidence_mode": evidence_mode,
        "subset_method": method, "filters": criteria, "filter_unknown_patent_ids": unknown,
        "batch_limit": 10, "batch_count": len(batches), "batches": batches,
        "candidate_count": catalog["candidate_count"], "selected_count": len(selected),
        "deferred_count": catalog["candidate_count"] - len(selected), "selected": selected,
        "patent_ids": ordered_ids,
        "scope_language_window_and_human_origin": "verify_separately",
    }


def validate_selection(catalog, selection):
    if not isinstance(selection, dict) or selection.get("schema_version") != "fto-cc-selection-3" or selection.get("status") != "user_confirmed":
        raise ValueError("没有当前版本的用户确认名单；不能调用 CC。")
    expected = confirm_selection(catalog, selection["choice_record"]["path"], selection["user_action_record"]["path"])
    if selection != expected:
        raise ValueError("冻结名单或用户选择记录已改变；先核对版本。")
    return selection["patent_ids"]


def lifecycle_ready(selection, lifecycle, ids):
    if not isinstance(lifecycle, dict) or lifecycle.get("schema_version") != "fto-lifecycle-gate-1":
        raise ValueError("CC 前缺少生命周期与采用文本门记录。")
    if lifecycle.get("selection_sha256") != sha(canonical(selection)):
        raise ValueError("生命周期门记录与当前客户选择版本不一致。")
    if not isinstance(lifecycle.get("assessment_date"), str) or not lifecycle["assessment_date"].strip():
        raise ValueError("生命周期门缺少评估时点。")
    reviews = lifecycle.get("reviews")
    if not isinstance(reviews, list) or not all(isinstance(r, dict) and isinstance(r.get("patent_id"), str) for r in reviews):
        raise ValueError("生命周期门逐件记录结构不符。")
    indexed = {r["patent_id"]: r for r in reviews}
    if len(indexed) != len(reviews) or not set(indexed) <= set(selection["patent_ids"]):
        raise ValueError("生命周期门存在重复或名单外对象。")
    allowed_text = {
        "active_grant": {"current_grant_claims", "current_post_grant_claims"},
        "pending_application": {"current_pending_claims", "published_pending_claims"},
    }
    ready = []
    for pid in ids:
        review = indexed.get(pid)
        if not review:
            raise ValueError(f"本批缺少生命周期与采用文本核验：{pid}")
        eligibility = review.get("eligibility")
        if eligibility not in allowed_text:
            label = review.get("status_label") or eligibility or "unknown"
            raise ValueError(f"本批对象不得进入 CC，须先排除或补核：{pid} ({label})")
        if review.get("text_basis") not in allowed_text[eligibility]:
            raise ValueError(f"采用文本与当前权利状态不匹配：{pid}")
        if not isinstance(review.get("adopted_pn"), str) or not review["adopted_pn"].strip():
            raise ValueError(f"缺少 CC 采用文献号：{pid}")
        if not isinstance(review.get("status_label"), str) or not review["status_label"].strip():
            raise ValueError(f"缺少有来源的状态说明：{pid}")
        for field in ["lifecycle_record", "text_record"]:
            record = review.get(field)
            if not isinstance(record, dict) or not record.get("path"):
                raise ValueError(f"缺少 {field}：{pid}")
            actual, raw = file_record(record["path"])
            if not raw.strip() or actual != record:
                raise ValueError(f"生命周期或采用文本来源为空／已变更：{pid}")
        ready.append({"patent_id": pid, "adopted_pn": review["adopted_pn"],
                      "eligibility": eligibility, "text_basis": review["text_basis"]})
    return ready


def ready_batch(selection, batch_number, lifecycle=None, evidence=None):
    if type(batch_number) is not int or not 1 <= batch_number <= len(selection["batches"]):
        raise ValueError("批次不存在。")
    ids = selection["batches"][batch_number - 1]["patent_ids"]
    if not 0 < len(ids) <= 10:
        raise ValueError("本流程每个核验批次须为 1–10 篇。")
    ready = lifecycle_ready(selection, lifecycle, ids)
    if selection["evidence_mode"] == "fulltext":
        if not isinstance(evidence, dict) or evidence.get("schema_version") != "fto-fulltext-review-1" or evidence.get("selection_sha256") != sha(canonical(selection)):
            raise ValueError("全文模式需要与本次选择版本一致的取证／分析记录。")
        reviews = evidence.get("reviews")
        if not isinstance(reviews, list) or not all(isinstance(r, dict) and isinstance(r.get("patent_id"), str) for r in reviews):
            raise ValueError("全文分析记录结构不符。")
        indexed = {r["patent_id"]: r for r in reviews}
        if len(indexed) != len(reviews) or not set(indexed) <= set(selection["patent_ids"]):
            raise ValueError("全文分析记录存在重复或名单外对象。")
        for pid in ids:
            review = indexed.get(pid, {})
            if review.get("status") != "complete":
                raise ValueError(f"本批全文取得／分析未完成：{pid}")
            for field in ["source_record", "analysis_record"]:
                record = review.get(field)
                if not isinstance(record, dict) or not record.get("path"):
                    raise ValueError(f"缺少 {field}：{pid}")
                actual, raw = file_record(record["path"])
                if not raw.strip() or actual != record:
                    raise ValueError(f"全文来源或分析文件为空／已变更：{pid}")
    return ready


def save_new(path, content):
    path = Path(path)
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise ValueError(f"输出已存在且不同；请另建版本：{path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def json_text(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def render_html(catalog):
    template = (Path(__file__).resolve().parents[1] / "assets" / "cc-selector.html").read_text(encoding="utf-8")
    # Prevent raw document text from closing the JSON script or injecting markup.
    data = json_text(catalog).replace("&", "\\u0026").replace("<", "\\u003c").replace(">", "\\u003e")
    title = "选择要进一步逐项检查的候选专利" if catalog["output_language"] == "zh" else "Choose the patents for detailed review"
    return template.replace("__LANG__", catalog["output_language"]).replace("__TITLE__", html.escape(title)).replace("__CATALOG_JSON__", data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    prep = subs.add_parser("prepare", help="Complete catalogue and empty selection UI; no CC list")
    prep.add_argument("--screening", type=Path, action="append", required=True)
    prep.add_argument("--case-id", required=True)
    prep.add_argument("--input-version", required=True)
    prep.add_argument("--scope", required=True)
    prep.add_argument("--language", choices=["zh", "en"], default="zh")
    prep.add_argument("--metadata", type=Path)
    prep.add_argument("--out", type=Path, required=True)
    prep.add_argument("--html", type=Path, required=True)
    conf = subs.add_parser("confirm", help="Freeze received explicit user choice")
    conf.add_argument("--catalog", type=Path, required=True)
    conf.add_argument("--choice", type=Path, required=True)
    conf.add_argument("--user-action", type=Path, required=True)
    conf.add_argument("--out", type=Path, required=True)
    valid = subs.add_parser("validate", help="Validate frozen selection immediately before CC")
    valid.add_argument("--catalog", type=Path, required=True)
    valid.add_argument("--selection", type=Path, required=True)
    valid.add_argument("--lifecycle", type=Path, required=True)
    valid.add_argument("--batch", type=int, required=True)
    valid.add_argument("--evidence", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            metadata = json.loads(args.metadata.read_bytes()) if args.metadata else None
            catalog = prepare_catalog(args.screening, args.case_id, args.input_version, args.scope, args.language, metadata)
            save_new(args.out, json_text(catalog))
            save_new(args.html, render_html(catalog))
            result = {"status": catalog["status"], "candidates": catalog["candidate_count"],
                      "cc_selected": 0, "catalog": str(args.out.resolve()), "html": str(args.html.resolve())}
        elif args.command == "confirm":
            catalog = json.loads(args.catalog.read_bytes())
            selection = confirm_selection(catalog, args.choice, args.user_action)
            save_new(args.out, json_text(selection))
            result = {"status": selection["status"], "cc_selected": selection["selected_count"], "batch_count": selection["batch_count"], "evidence_mode": selection["evidence_mode"], "output": str(args.out.resolve())}
        else:
            catalog = json.loads(args.catalog.read_bytes())
            selection = json.loads(args.selection.read_bytes())
            validate_selection(catalog, selection)
            lifecycle = json.loads(args.lifecycle.read_bytes())
            evidence = json.loads(args.evidence.read_bytes()) if args.evidence else None
            patents = ready_batch(selection, args.batch, lifecycle, evidence)
            result = {"status": "validated_batch_record", "batch": args.batch,
                      "patent_ids": [x["patent_id"] for x in patents], "patents": patents,
                      "scope_language_window_and_human_origin": "verify_separately"}
    except (ValueError, OSError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "error", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
