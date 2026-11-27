#!/usr/bin/env python3
"""Build a deduplicated reading queue and decide whether the same query needs another page."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


def _norm_pn(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    value = re.sub(r"[^A-Z0-9]", "", value.upper())
    return value or None


def _norm_title(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    value = "".join(char.casefold() for char in value if char.isalnum())
    return value or None


def _data(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        return {}
    if isinstance(payload.get("structuredContent"), dict):
        payload = payload["structuredContent"]
    data = payload.get("data")
    return data if isinstance(data, dict) else {}


def _identities(doc: dict[str, Any]) -> set[str]:
    values = [doc.get("patent_number"), doc.get("publication_number")]
    pn = doc.get("pn")
    values.extend(pn if isinstance(pn, list) else [pn])
    return {item for value in values if (item := _norm_pn(value))}


def _family(doc: dict[str, Any]) -> str | None:
    for key in ("family_id", "simple_family_id", "familyId", "simpleFamilyId"):
        value = doc.get(key)
        if value not in (None, ""):
            return str(value)
    return None


def build_summary(payloads: list[Any], target: int, page_size: int,
                  max_window: int) -> dict[str, Any]:
    identity_owner: dict[str, int] = {}
    identity_docs: list[dict[str, Any]] = []
    pages: list[dict[str, Any]] = []
    total_hits: int | None = None

    for page_index, payload in enumerate(payloads):
        data = _data(payload)
        docs = data.get("docs") if isinstance(data.get("docs"), list) else []
        if isinstance(data.get("total_hits"), int):
            total_hits = data["total_hits"]
        pages.append({
            "offset": page_index * page_size,
            "returned_count": len(docs),
        })
        for raw_rank, doc in enumerate(docs, start=page_index * page_size + 1):
            if not isinstance(doc, dict):
                continue
            identities = _identities(doc)
            owners = {identity_owner[item] for item in identities if item in identity_owner}
            if owners:
                owner = min(owners)
                identity_docs[owner]["identities"].update(identities)
                for item in identities:
                    identity_owner[item] = owner
                continue
            owner = len(identity_docs)
            for item in identities:
                identity_owner[item] = owner
            identity_docs.append({
                "doc": doc,
                "identities": set(identities),
                "raw_rank": raw_rank,
            })

    queue: list[dict[str, Any]] = []
    group_owner: dict[tuple[str, str], int] = {}
    for item in identity_docs:
        doc = item["doc"]
        family = _family(doc)
        title = _norm_title(doc.get("title"))
        identities = sorted(item["identities"])
        if family:
            key = ("family", family)
        elif title:
            key = ("exact_title_provisional", title)
        else:
            stable = identities[0] if identities else str(doc.get("id") or item["raw_rank"])
            key = ("identity", stable)
        representative = {
            "cluster_basis": key[0],
            "cluster_key": key[1],
            "raw_rank": item["raw_rank"],
            "publication_number": doc.get("patent_number") or doc.get("publication_number"),
            "identities": identities,
            "title": doc.get("title"),
            "members": 1,
        }
        if key in group_owner:
            queue[group_owner[key]]["members"] += 1
        else:
            group_owner[key] = len(queue)
            queue.append(representative)

    raw_count = sum(page["returned_count"] for page in pages)
    unique_groups = len(queue)
    last_returned = pages[-1]["returned_count"] if pages else 0
    next_offset = len(pages) * page_size
    if unique_groups >= target:
        status = "target_met"
        next_offset_value = None
    elif not pages or last_returned < page_size or (total_hits is not None and raw_count >= total_hits):
        status = "results_exhausted"
        next_offset_value = None
    elif next_offset + page_size > max_window:
        status = "tool_limit"
        next_offset_value = None
    else:
        status = "needs_more"
        next_offset_value = next_offset

    return {
        "target_unique_groups": target,
        "page_size": page_size,
        "max_window": max_window,
        "pages": pages,
        "raw_result_count": raw_count,
        "unique_identity_count": len(identity_docs),
        "unique_group_count": unique_groups,
        "status": status,
        "next_offset": next_offset_value,
        "queue": queue[:target],
        "note": (
            "exact_title_provisional suppresses queue duplicates only; all exact publication identities "
            "must remain in the candidate ledger"
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("responses", nargs="+", type=Path)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-window", type=int, default=1000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.target < 1 or args.page_size < 1 or args.max_window < args.page_size:
        parser.error("target, page-size and max-window must be positive and consistent")
    payloads = [json.loads(path.read_text(encoding="utf-8")) for path in args.responses]
    summary = build_summary(payloads, args.target, args.page_size, args.max_window)
    text = json.dumps(summary, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
