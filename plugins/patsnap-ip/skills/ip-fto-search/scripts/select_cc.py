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
        raise ValueError("The screening receipt contains a failure flag; a submittable CC list cannot be generated.")


def evidence_value(document, pointer):
    """Resolve a JSON Pointer without assuming a service output schema."""
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError("Evidence must reference a non-root JSON Pointer in the actual result.")
    value = document
    for token in pointer[1:].split("/"):
        if any(i + 1 == len(token) or token[i + 1] not in "01" for i, char in enumerate(token) if char == "~"):
            raise ValueError("Invalid JSON Pointer escape.")
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            if not token.isdigit() or str(int(token)) != token:
                raise ValueError("Invalid JSON Pointer array index.")
            index = int(token)
            if index >= len(value):
                raise ValueError("Evidence location is outside the result bounds.")
            value = value[index]
        elif isinstance(value, dict) and token in value:
            value = value[token]
        else:
            raise ValueError("Evidence location does not exist.")
    if value is None or value == "" or value == [] or value == {}:
        raise ValueError("Evidence location points to empty content.")
    return value


def screening_items(receipt):
    """Read a local, source-linked FTO Screening record without guessing service fields."""
    check_failure(receipt)
    if not isinstance(receipt, dict) or receipt.get("schema_version") != "fto-screening-evidence-2":
        raise ValueError("Verify complete screen_patents_for_FTO receipts and create local screening records first.")
    if receipt.get("results_complete") is not True:
        raise ValueError("Task or result pagination is incomplete; the candidate catalog cannot be frozen.")
    sources = receipt.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValueError("Original result sources are missing.")
    documents, paths = [], set()
    for source in sources:
        if not isinstance(source, dict) or not isinstance(source.get("path"), str):
            raise ValueError("Result sources require actual files and hashes.")
        actual, raw = file_record(source["path"])
        if source != actual or actual["path"] in paths:
            raise ValueError("Result sources have changed, do not match the record, or are duplicated.")
        paths.add(actual["path"])
        value = json.loads(raw)
        check_failure(value)
        documents.append(value)
    submitted = receipt.get("submitted_pns")
    remaps = receipt.get("identity_remaps")
    unresolved = receipt.get("unresolved_pns")
    nonreturned = receipt.get("nonreturned_pns")
    for label, values in [("Submitted PNs", submitted), ("Unresolved PNs", unresolved), ("Nonreturned PNs", nonreturned)]:
        if not isinstance(values, list) or not all(isinstance(x, str) and x.strip() for x in values) or len(set(values)) != len(values):
            raise ValueError(f"{label} must be a unique list of actual publication numbers.")
    if set(unresolved).intersection(nonreturned):
        raise ValueError("A PN cannot be both unresolved and nonreturned.")
    if not isinstance(remaps, list):
        raise ValueError("identity_remaps must be an array, which may be empty.")
    remap_inputs, remap_outputs = set(), set()
    for item in remaps:
        if not isinstance(item, dict):
            raise ValueError("Each identity_remaps entry must be an object.")
        input_pn, returned_pn, reason = item.get("input_pn"), item.get("returned_pn"), item.get("reason")
        if not all(isinstance(x, str) and x.strip() for x in [input_pn, returned_pn, reason]):
            raise ValueError("Identity mappings require nonempty input_pn, returned_pn and a verification reason.")
        if input_pn in remap_inputs or input_pn not in submitted:
            raise ValueError("A mapped input PN is duplicated or outside the submitted set.")
        remap_inputs.add(input_pn)
        remap_outputs.add(returned_pn)
    if remap_inputs.intersection(unresolved) or remap_inputs.intersection(nonreturned):
        raise ValueError("Mapped input PNs cannot also be unresolved or nonreturned.")
    records = receipt.get("records")
    if not isinstance(records, list):
        raise ValueError("Per-item screening records are missing.")
    seen, selected = set(), []
    for position, item in enumerate(records, 1):
        if not isinstance(item, dict):
            raise ValueError("A screening record must be an object.")
        pid = item.get("patent_id")
        if not isinstance(pid, str) or not pid.strip() or pid in seen:
            raise ValueError("A screening identity is missing or duplicated.")
        seen.add(pid)
        if not isinstance(item.get("pn"), str):
            raise ValueError("PN must be a verified string; an empty string is allowed.")
        refs = item.get("evidence_refs")
        if not isinstance(refs, list) or not refs:
            raise ValueError("Each judgment requires a location in the actual results.")
        for ref in refs:
            if not isinstance(ref, dict) or type(ref.get("source_index")) is not int or not 1 <= ref["source_index"] <= len(documents):
                raise ValueError("Invalid evidence source index.")
            evidence_value(documents[ref["source_index"] - 1], ref.get("pointer"))
        selected.append({"patent_id": pid, "pn": item["pn"], "screening_decision": "returned_candidate", "source_position": position})
    returned_pns = {x["pn"] for x in selected}
    if "" in returned_pns or returned_pns.intersection(unresolved) or returned_pns.intersection(nonreturned):
        raise ValueError("Returned candidate PNs conflict with unresolved/nonreturned sets.")
    unexpected = returned_pns - set(submitted)
    if unexpected - remap_outputs:
        raise ValueError("An out-of-input returned PN lacks a verified mapping.")
    represented_inputs = (returned_pns & set(submitted)) | remap_inputs
    if represented_inputs | set(unresolved) | set(nonreturned) != set(submitted):
        raise ValueError("Submitted PNs are not fully mapped to returned, unresolved or nonreturned sets.")
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
            raise ValueError("The same screening file cannot serve as two groups.")
        items = screening_items(json.loads(raw))
        sources.append({**source, "returned_count": len(items)})
        for item in items:
            pid, pn = item["patent_id"], item["pn"]
            origin = {"source_index": group, "screening_position": item["source_position"]}
            if pid in by_id:
                row = by_id[pid]
                if row["pn"] != pn:
                    raise ValueError("The same ID has inconsistent PNs across receipts; verify identity first.")
                row["origins"].append(origin)
            else:
                row = {"row_id": f"S{len(candidates) + 1:03d}", "patent_id": pid,
                       "pn": pn, "screening_decision": item["screening_decision"], "origins": [origin]}
                candidates.append(row)
                by_id[pid] = row
    return sources, candidates


def prepare_catalog(paths, case_id, input_version, scope, language="en", metadata=None):
    if language not in {"zh", "en"}:
        raise ValueError("The page supports zh/en only; fully localize it before delivering in another language.")
    if not all(isinstance(x, str) and x.strip() for x in [case_id, input_version, scope]):
        raise ValueError("Case, input version and scope must be nonempty.")
    sources, candidates = collect_candidates(paths)
    if not sources:
        raise ValueError("Provide local screening records backed by actual result sources.")
    if metadata is not None:
        display = metadata.get("by_patent_id") if isinstance(metadata, dict) else None
        if not isinstance(display, dict):
            raise ValueError("metadata must contain a by_patent_id object.")
        allowed = {"title", "assignees", "jurisdiction", "legal_status", "screening_reason", "completeness", "url", "source_ref"}
        for row in candidates:
            data = display.get(row["patent_id"], {})
            if not isinstance(data, dict):
                raise ValueError("metadata entries must be objects.")
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
        raise ValueError("This is not a current-version candidate catalog.")
    unhashed = {k: v for k, v in catalog.items() if k != "catalog_sha256"}
    if sha(canonical(unhashed)) != catalog.get("catalog_sha256"):
        raise ValueError("The catalog has changed; old selections cannot be reused.")
    sources, rows = collect_candidates([x["path"] for x in catalog["sources"]])
    if sources != catalog["sources"]:
        raise ValueError("Source receipts have changed; rebuild the catalog and obtain a new user selection.")
    identities = [{k: v for k, v in x.items() if k != "display"} for x in catalog["candidates"]]
    if rows != identities or catalog["candidate_count"] != len(rows):
        raise ValueError("The catalog does not match the source-backed screening records.")
    if catalog.get("batch_limit") != 10:
        raise ValueError("The local verification batch size is 10.")
    expected = "awaiting_user_strategy" if rows else "no_candidates"
    if catalog.get("status") != expected:
        raise ValueError("Invalid catalog status.")


def filtered_candidates(catalog, criteria):
    """Exact metadata matching; unknowns remain eligible until explicitly reviewed."""
    allowed = {"assignees", "legal_status", "jurisdiction"}
    if not isinstance(criteria, dict) or not criteria or not set(criteria) <= allowed:
        raise ValueError("Filters must be a nonempty object containing supported fields.")
    for values in criteria.values():
        if not isinstance(values, list) or not values or not all(isinstance(x, str) and x.strip() for x in values) or len(values) != len(set(values)):
            raise ValueError("Each filter field requires a nonempty list of unique strings.")
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
        raise ValueError("The selection record must use a valid structure and specify all/subset scope and full-text strategy.")
    if choice.get("catalog_sha256") != catalog["catalog_sha256"]:
        raise ValueError("The user selection belongs to another catalog or version.")
    ids = choice.get("selected_patent_ids")
    if not isinstance(ids, list) or not all(isinstance(x, str) and x.strip() for x in ids):
        raise ValueError("The user selection must be a valid ID array.")
    if not ids:
        raise ValueError("No items selected; submittable CC batches cannot be generated.")
    if len(set(ids)) != len(ids):
        raise ValueError("The selection contains duplicate IDs.")
    known = {x["patent_id"] for x in catalog["candidates"]}
    if not set(ids) <= known:
        raise ValueError("The selection contains items outside the final screening catalog.")
    strategy, evidence_mode = choice.get("strategy"), choice.get("evidence_mode")
    if strategy not in {"all", "subset"} or evidence_mode not in {"claims", "fulltext"}:
        raise ValueError("All/subset scope and description full-text options must be explicit and independent; no defaults are allowed.")
    method, criteria, unknown = None, {}, []
    if strategy == "all":
        if set(ids) != known:
            raise ValueError("The all-items strategy must include the complete catalog, not a search/filter view subset.")
        if choice.get("filters") or choice.get("subset_method"):
            raise ValueError("The all-items strategy cannot include subset filters.")
    else:
        method = choice.get("subset_method")
        if method not in {"manual", "filters"}:
            raise ValueError("A subset strategy must specify manual selection or field filtering.")
        criteria = choice.get("filters", {})
        if criteria or method == "filters":
            eligible, unknown = filtered_candidates(catalog, criteria)
            if method == "filters" and set(ids) != set(eligible):
                raise ValueError("Field-filter results do not match the IDs; never silently remove unknown items. Mark manual adjustments as manual.")
    action_record, action_raw = file_record(user_action_path)
    if not action_raw.strip():
        raise ValueError("The actual user reply/action record must be nonempty; this script cannot authenticate human origin.")
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
        raise ValueError("No current-version user-confirmed list exists; CC cannot be called.")
    expected = confirm_selection(catalog, selection["choice_record"]["path"], selection["user_action_record"]["path"])
    if selection != expected:
        raise ValueError("The frozen list or user selection has changed; verify versions first.")
    return selection["patent_ids"]


def lifecycle_ready(selection, lifecycle, ids):
    if not isinstance(lifecycle, dict) or lifecycle.get("schema_version") != "fto-lifecycle-gate-1":
        raise ValueError("Lifecycle and adopted-text gate records are required before CC.")
    if lifecycle.get("selection_sha256") != sha(canonical(selection)):
        raise ValueError("Lifecycle gate records do not match the current client selection version.")
    if not isinstance(lifecycle.get("assessment_date"), str) or not lifecycle["assessment_date"].strip():
        raise ValueError("The lifecycle gate requires an assessment date.")
    reviews = lifecycle.get("reviews")
    if not isinstance(reviews, list) or not all(isinstance(r, dict) and isinstance(r.get("patent_id"), str) for r in reviews):
        raise ValueError("Invalid per-patent lifecycle gate records.")
    indexed = {r["patent_id"]: r for r in reviews}
    if len(indexed) != len(reviews) or not set(indexed) <= set(selection["patent_ids"]):
        raise ValueError("The lifecycle gate contains duplicate patents or patents outside the selection.")
    allowed_text = {
        "active_grant": {"current_grant_claims", "current_post_grant_claims"},
        "pending_application": {"current_pending_claims", "published_pending_claims"},
    }
    ready = []
    for pid in ids:
        review = indexed.get(pid)
        if not review:
            raise ValueError(f"Missing lifecycle and adopted-text verification for this batch: {pid}")
        eligibility = review.get("eligibility")
        if eligibility not in allowed_text:
            label = review.get("status_label") or eligibility or "unknown"
            raise ValueError(f"This batch patent cannot enter CC; exclude it or complete verification first: {pid} ({label})")
        if review.get("text_basis") not in allowed_text[eligibility]:
            raise ValueError(f"Adopted text does not match the current rights status: {pid}")
        if not isinstance(review.get("adopted_pn"), str) or not review["adopted_pn"].strip():
            raise ValueError(f"Missing adopted CC publication number: {pid}")
        if not isinstance(review.get("status_label"), str) or not review["status_label"].strip():
            raise ValueError(f"Missing a source-backed status description: {pid}")
        for field in ["lifecycle_record", "text_record"]:
            record = review.get(field)
            if not isinstance(record, dict) or not record.get("path"):
                raise ValueError(f"Missing {field}: {pid}")
            actual, raw = file_record(record["path"])
            if not raw.strip() or actual != record:
                raise ValueError(f"Lifecycle or adopted-text source is empty or has changed: {pid}")
        ready.append({"patent_id": pid, "adopted_pn": review["adopted_pn"],
                      "eligibility": eligibility, "text_basis": review["text_basis"]})
    return ready


def ready_batch(selection, batch_number, lifecycle=None, evidence=None):
    if type(batch_number) is not int or not 1 <= batch_number <= len(selection["batches"]):
        raise ValueError("Batch does not exist.")
    ids = selection["batches"][batch_number - 1]["patent_ids"]
    if not 0 < len(ids) <= 10:
        raise ValueError("Each local verification batch must contain 1–10 patents.")
    ready = lifecycle_ready(selection, lifecycle, ids)
    if selection["evidence_mode"] == "fulltext":
        if not isinstance(evidence, dict) or evidence.get("schema_version") != "fto-fulltext-review-1" or evidence.get("selection_sha256") != sha(canonical(selection)):
            raise ValueError("Full-text mode requires evidence/analysis records matching this selection version.")
        reviews = evidence.get("reviews")
        if not isinstance(reviews, list) or not all(isinstance(r, dict) and isinstance(r.get("patent_id"), str) for r in reviews):
            raise ValueError("Invalid full-text analysis record structure.")
        indexed = {r["patent_id"]: r for r in reviews}
        if len(indexed) != len(reviews) or not set(indexed) <= set(selection["patent_ids"]):
            raise ValueError("Full-text analysis contains duplicate or out-of-list items.")
        for pid in ids:
            review = indexed.get(pid, {})
            if review.get("status") != "complete":
                raise ValueError(f"Full-text retrieval/analysis is incomplete for this batch: {pid}")
            for field in ["source_record", "analysis_record"]:
                record = review.get(field)
                if not isinstance(record, dict) or not record.get("path"):
                    raise ValueError(f"Missing {field}: {pid}")
                actual, raw = file_record(record["path"])
                if not raw.strip() or actual != record:
                    raise ValueError(f"Full-text source or analysis file is empty or has changed: {pid}")
    return ready


def save_new(path, content):
    path = Path(path)
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise ValueError(f"Output already exists with different content; create a new version: {path}")
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
    prep.add_argument("--language", choices=["zh", "en"], default="en")
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
