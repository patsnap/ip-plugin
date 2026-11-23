# Tool meanings and input/output patterns

## Contents

- General rules
- `extract_technical_features`
- `search_patent`
- `fetch_patent`
- `assess_feature_disclosure`

## General rules

This is the explicit contract used by this Skill. Current runtime schemas govern changes; update this reference accordingly. Use tool-returned patent search results, text, figures and PDFs. Local scripts organize records and generate reports only.

Identify the blocked step when a required tool is unavailable; do not invent legacy names or switch patent services. Tool failure is not zero hits; missing material is not nondisclosure.

## `extract_technical_features`

Purpose: extract the solution, complete technical relationships and sources from the disclosure for shared retrieval/comparison use. It does not search patents or decide novelty/inventive step.

Input:

```json
{
  "disclosure_text": "Complete original user disclosure",
  "language": "en-US",
  "disclosure_images": [{
    "label": "Figure 1",
    "mime_type": "image/png",
    "data_base64": "Base64 of complete image bytes",
    "ref": "Image reference identifier",
    "pdf_page": 1,
    "text_locations": ["Disclosure page 3"]
  }]
}
```

`disclosure_images` may be omitted. Read output as follows:

```json
{
  "status": "complete",
  "technical_solution": "Solution overview",
  "features": ["Complete feature relationship 1"],
  "feature_evidence": [
    {"feature": "Complete feature relationship 1", "source_quote": "Original disclosure sentence", "image_labels": []}
  ],
  "questions": [],
  "language": "en-US",
  "audit": []
}
```

Handle unresolved `questions` that change the assessment subject under entry step 1. Do not replace the original disclosure with a summary or silently rewrite `features` locally.

## `search_patent`

Purpose: discover candidate patents and bibliography through semantic, keyword, structured-filter and Boolean retrieval. Abstracts/snippets do not replace full text for comparison.

Mixed semantic/keyword input:

```json
{
  "search_strategy": ["semantic", "keyword", "filter"],
  "semantic_query": "Complete technical intent, relationships and problem",
  "keywords": ["Complete Chinese relationship phrase", "English technical relationship"],
  "filters": {"date_type": "publication", "date_to": 20201231},
  "limit": 20,
  "offset": 0,
  "collapse_family": false,
  "sort": "relevance"
}
```

Remove `filter` and `filters` when dates are unresolved. Available filters include `pn`, `apno`, `assignees`, `assignee_ids`, `inventors`, `ipc`, `jurisdiction`, `legal_status`, `date_type`, `date_from`, `date_to` and `cited_min`; use only user-confirmed or workflow-verified conditions.

Boolean input is mutually exclusive with other strategies:

```json
{
  "search_strategy": ["boolean"],
  "boolean_query": "B_CITES:(US6394621B1) AND PBD:[* TO 20000101]",
  "limit": 20,
  "offset": 0,
  "collapse_family": false
}
```

Read output:

```json
{
  "status": "success",
  "data": {
    "total_hits": 100,
    "returned_count": 20,
    "docs": [{
      "id": "patent_id",
      "patent_number": "US...A1",
      "pn": ["US...A1"],
      "title": "Title",
      "text": "Abstract or relevant snippet",
      "publication_date": 20200101,
      "priority_date": [20190101],
      "application_date": 20190101,
      "jurisdiction": "US",
      "legal_status": "pending",
      "ipc": "B23K...",
      "assignees": [],
      "inventors": [],
      "url": "Source page",
      "view_url": "View link"
    }]
  }
}
```

Record `total_hits`, returned page count, unique candidates and formal comparison count separately. `status=error` and tool failure are not zero hits.

## `fetch_patent`

Purpose: read the exact publication version, bibliography, claims and description of a known patent, with families, citation relationships or actual media when needed.

Input:

```json
{
  "patent_id": "id returned by search_patent",
  "language": "en-US",
  "format": "json",
  "include": ["relations", "media"]
}
```

`include` may be omitted; request `relations` or `media` only for needed families, citations or visual evidence. Output for `format=json`:

```json
{
  "tool": "fetch_patent",
  "input": {},
  "response": {
    "bibliography": {
      "publication_number": "US...A1",
      "publication_date": "2020-01-01",
      "priority_dates": ["2019-01-01"],
      "title": "Title"
    },
    "claims": "Complete claims",
    "description": "Complete description",
    "technical_problem": "Optional high-value field",
    "technical_solution": "Optional high-value field",
    "technical_effect": "Optional high-value field",
    "relations": {"simple_family": [], "cited_patents": [], "citing_patents": []},
    "media": {"figures": [], "pdf": []}
  },
  "executed_at": "Timestamp"
}
```

For `format=markdown`, read `response.markdown`. Media links become visual evidence only after the material is actually obtained and read.

## `assess_feature_disclosure`

Purpose: verify disclosure facts per patent using the same original disclosure and feature list. It returns feature judgments, quotations, reading scope and common technical arrangement, without replacing final legal conclusions.

Single-document input:

```json
{
  "disclosure_text": "Complete original disclosure",
  "features": ["Complete feature relationship 1", "Complete feature relationship 2"],
  "language": "en-US",
  "publication_number": "US...A1",
  "patent_text": "Actually obtained complete claims and description"
}
```

Without existing text, choose `publication_number` or `patent_id` for tool retrieval. With supplied text/images, use a publication number as label. Batch input uses `patents`, 1–10 documents per batch, mutually exclusive with top-level single-document fields:

```json
{
  "disclosure_text": "Complete original disclosure",
  "features": ["Complete feature relationship 1"],
  "language": "en-US",
  "patents": [
    {"publication_number": "US...A1"},
    {"publication_number": "CN...A", "patent_text": "Complete text"}
  ]
}
```

Read single-document output:

```json
{
  "status": "complete",
  "comparisons": [{
    "feature": "Complete feature relationship 1",
    "judgment": "disclosed | not_disclosed | not_mentioned | null",
    "disclosure_type": "explicit | implicit | combined | null",
    "evidence": [{"location": "[0020]", "quote": "Original text"}],
    "reason": "Complete rationale"
  }],
  "coverage": {"text_scope": "Actual reading scope", "images_read": [], "limitations": []},
  "arrangement": {
    "basis": "single_embodiment | linked_combination | incompatible_pieces | not_applicable",
    "reason": "Common-arrangement rationale"
  },
  "language": "en-US",
  "audit": []
}
```

For batches, read `status`, `total`, `succeeded`, `failed` and input-ordered `results[]`. Each item preserves its original `index`, publication number and `status`, with success in `result` and failure in `error`. Retry only failed items marked `retryable=true` or recoverable by supplying material. Do not discard successes and rerun the whole batch.
