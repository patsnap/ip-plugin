"""Read current MCP receipts without changing the saved source files."""

import json
import re


def payload(value):
    """Accept structured content, MCP envelopes and JSON-RPC call results."""
    if not isinstance(value, dict):
        return value
    if "jsonrpc" in value:
        if "error" in value:
            return {"isError": True, "error": value["error"]}
        value = value.get("result", value)
    if isinstance(value.get("structuredContent"), dict):
        return {**value["structuredContent"], **({"isError": True} if value.get("isError") else {})}
    if isinstance(value.get("content"), list):
        for block in value["content"]:
            if block.get("type") != "text":
                continue
            try:
                decoded = json.loads(block.get("text", ""))
            except (ValueError, TypeError):
                continue
            if isinstance(decoded, dict) and "skill_upgrade" not in decoded:
                return {**decoded, **({"isError": True} if value.get("isError") else {})}
    return value


def bibliography(receipt):
    value = payload(receipt)
    # Older saved reports can still supply their original metadata file.
    return value.get("response", {}).get("bibliography") or value.get("patent")


def search_result(receipt):
    value = payload(receipt)
    data = value.get("data") or {}
    docs = data.get("docs", value.get("patents", [])) or []
    patents = []
    for doc in docs:
        numbers = doc.get("pn") or []
        number = doc.get("patent_number") or doc.get("publication_number") or (numbers[0] if numbers else None)
        patents.append({**doc, "publication_number": number})
    return {
        "patents": patents,
        "total": data.get("total_hits", value.get("total", value.get("count"))),
        "failed": bool(value.get("isError") or value.get("error") or value.get("status") in {"failed", "error"}),
        "partial": value.get("status") == "partial",
    }


def search_query(request):
    parts = [request.get("boolean_query"), request.get("semantic_query")]
    if request.get("keywords"):
        parts.append("\n".join(request["keywords"]))
    return "\n".join(x for x in parts if x) or request.get("query") or request.get("text") or json.dumps(request.get("filters", {}), ensure_ascii=False)


def search_routes(request):
    strategy = request.get("search_strategy", [])
    query = request.get("boolean_query", "")
    if "boolean" in strategy and re.search(r"\b(?:B_CITES|F_CITES|BF_CITES)\s*:", query):
        return ["citations"]
    if (strategy == ["filter"] and (request.get("filters", {}).get("pn") or request.get("filters", {}).get("apno"))) or re.match(r"\s*PN\s*:", query):
        return ["publication"]
    return strategy or ["boolean"]
