# Report data and commands

## Contents

- Save inputs and receipts
- Solutions and features
- Report draft
- Agent verification
- Inventive step and supplementary evidence
- Generate and validate

## Save inputs and receipts

Reuse the task directory and save original disclosure, feature plan, every actual request and complete receipt, original images and report draft. Suggested paths are `calls/unique-id/request.json` and `response.json`. Requests contain actual business parameters; record full tool name/provenance separately. Existing task organization is acceptable without a host-specific protocol.

The renderer accepts direct structured results, MCP receipts with `structuredContent`, and JSON-RPC results, without modifying originals. A plain-text summary cannot replace complete results. Disclose missing, failed or oversized/incompletely retrieved receipts; do not fabricate successful results.

Actually read media links. Tool image inputs use the current schema's `ref: image:<file SHA256>`, `mime_type`, `data_base64`, `label`, and available `pdf_page`/`text_locations`. Local reports may reference saved originals through `host_file`. The renderer can also associate `material.assets` with `material.patent_images` by `ref`, validate complete Base64 images and save them under task-local `evidence/`. This does not establish that images were read.

All referenced files must be inside the task directory, with paths relative to the draft. Preserve quotations verbatim; summaries and tool-generated technical overviews are not original text.

## Solutions and features

Minimum `feature-plan.json`:

```json
{
  "feature_plan_version": 3,
  "disclosure_sha256": "SHA256 of original disclosure.txt",
  "feature_source": {
    "type": "extract_technical_features",
    "response_file": "calls/extract_features_response.json"
  },
  "source_features": [
    "Source relationship 1",
    "Source relationship 2"
  ],
  "source_feature_evidence": [
    {
      "feature": "Source relationship 1",
      "source_quote": "Original sentence supporting 1A and 1B",
      "image_labels": []
    },
    {
      "feature": "Source relationship 2",
      "source_quote": "Original sentence 2",
      "image_labels": []
    }
  ],
  "comparison_units": [
    {
      "feature": "Independently judgeable complete relationship 1A",
      "source_feature_number": 1,
      "source_quote": "supporting 1A",
      "image_labels": []
    },
    {
      "feature": "Independently judgeable complete relationship 1B",
      "source_feature_number": 1,
      "source_quote": "and 1B",
      "image_labels": []
    },
    {
      "feature": "Indivisible complete relationship 2",
      "source_feature_number": 2,
      "source_quote": "Original sentence 2",
      "image_labels": []
    }
  ],
  "features": [
    "Independently judgeable complete relationship 1A",
    "Independently judgeable complete relationship 1B",
    "Indivisible complete relationship 2"
  ],
  "feature_evidence": [
    {
      "feature": "Independently judgeable complete relationship 1A",
      "source_quote": "supporting 1A",
      "image_labels": []
    },
    {
      "feature": "Independently judgeable complete relationship 1B",
      "source_quote": "and 1B",
      "image_labels": []
    },
    {
      "feature": "Indivisible complete relationship 2",
      "source_quote": "Original sentence 2",
      "image_labels": []
    }
  ],
  "solutions": [
    {
      "name": "Primary solution",
      "kind": "product",
      "description": "Complete combination supported by the disclosure",
      "feature_numbers": [
        1,
        2,
        3
      ]
    }
  ],
  "groups": [
    {
      "title": "Source relationship 1",
      "source_feature_number": 1,
      "feature_numbers": [
        1,
        2
      ]
    },
    {
      "title": "Source relationship 2",
      "source_feature_number": 2,
      "feature_numbers": [
        3
      ]
    }
  ],
  "coverage": [
    {
      "quote": "Complete continuous original disclosure text",
      "treatment": "evaluated",
      "feature_numbers": [
        1,
        2,
        3
      ],
      "reason": "Included in the primary solution"
    }
  ]
}
```

New tasks use `feature_plan_version: 3`. For tool extraction, `feature_source.type` is `extract_technical_features` and points to the actual complete receipt. `source_features` and `source_feature_evidence` must match its content and order exactly. For an already determined user-provided list, use `{"type":"provided","reason":"Source and applicable scope"}` and also preserve that list in `source_features`.

Split `comparison_units` only within one source relationship at a judgeable granularity. Each unit maps to exactly one `source_feature_number`; its `source_quote` is continuous original text from that source’s evidence. Do not recombine sources or reduce relationships to component/effect words. Every source needs at least one unit.

`features` must equal ordered `comparison_units[].feature` and every formal comparison request. Generate `feature_evidence` verbatim from each unit’s `feature/source_quote/image_labels`. Each `groups` entry corresponds to one source and its `feature_numbers` exactly covers that source’s units. `solutions` and `coverage` use 1-based comparison-unit numbers.

The renderer validates version-3 source receipts, unit mappings, original quotations and complete groups. Receipt/source mismatches, cross-source units or mismatched requests fail validation. Versions 1 and 2 support historical reports only; upgrade to version 3 when continuing and regenerating a report.

`coverage` accounts for disclosure passages using `evaluated`, `optional` or `background`, with reasons. Do not hide necessary relationships as optional; resolve decisive ambiguities first. A complete report requires coverage of the original disclosure. Save UTF-8 `disclosure.txt`; `disclosure_sha256` must be its actual SHA256.

## Report draft

`report-draft.json`:

```json
{
  "title": "Technical Solution Novelty Report",
  "language": "en-US",
  "report": {
    "feature_plan_file": "feature-plan.json",
    "primary_solution": "Primary solution",
    "status": "partial",
    "headline": "Principal conclusion and stage status",
    "findings": [{
      "solution": "Primary solution",
      "novelty": {"status": "pending", "reason": "Established facts, decisive documents and relationships still requiring verification"},
      "inventiveness": {"status": "pending", "reason": "Paths actually investigated and unresolved issues"},
      "recommendation": "Next action tied to actual risks and gaps"
    }],
    "documents": [{
      "label": "D1",
      "request_file": "calls/comparison/request.json",
      "comparison_file": "calls/comparison/response.json",
      "metadata_file": "calls/fulltext/response.json",
      "reason": "Reason for including this document",
      "reviews": [{"request_file": "checks/item/request.json", "response_file": "checks/item/result.json"}]
    }],
    "searches": [{
      "tool": "search_patent",
      "purpose": "Actual verification objective",
      "request_file": "calls/search/request.json",
      "response_file": "calls/search/response.json"
    }],
    "search_summary": "Actual search approach, convergence rationale and reuse",
    "limitations": ["Specific gap and affected scope"]
  }
}
```

Example paths represent genuinely saved task files. Omit `reviews` if no verification was performed. Omit `metadata_file` when identifier-based comparison already returns identity. For supplied-material comparisons, supplement title, filing date and publication date from an exact-publication-matched raw `fetch_patent` receipt, reading `response.bibliography`. Mark missing filing/publication dates in formal comparison documents as awaiting verification rather than silently omitting them. Text and images must reflect material actually used in comparison; later retrieval does not mean that text was compared.

Batch documents share the complete request/receipt and each adds `document_index` using the original zero-based `index`. Include successful items only in the formal table. Identify failures from original batch records and show them in the appendix; remaining failures mean `partial`. After recovery of the same document, cite new results without renumbering the original batch.

The search appendix reads actual `search_strategy`, parameters, `data.docs`, `total_hits` and `returned_count`. Accumulate actual documents, deduplicate exact publication numbers, and retain page size/offset/family-collapse scope. Unknown totals are not zero. Detect citation directions from actual `B_CITES`/`F_CITES` expressions.

`publication_date` is an inclusive ISO publication cutoff, supplied only when set by the user. A known intended filing date or effective priority date may be recorded separately as `target_filing_date` for jurisdiction-specific earlier-application audits; it does not replace publication-date filtering. Conclusion statuses are `supported`, `not_supported`, `pending` or `not_assessed`; exactly one finding per solution. Overall status is `complete` only when all required assessments, disclosure coverage and decisive checks are finished; otherwise `partial`.

For negative novelty fill `novelty.whole_disclosure` with the decisive publication number and explain the common arrangement in `arrangement_reason`. Inherency requires valid verification. Positive novelty needs a valid difference against each document; unverified decisive silence is insufficient.

Top-level `parts` can configure six categories: `overview`, `novelty`, `inventiveness`, `recommendations`, `comparison`, `search`. Each uses either `content` or task-local Markdown `content_file`, not both. Omit `parts` for default sections. Prose cannot replace the matrix, change facts or override conclusions.

Optional presentation fields: `recommendation_detail` separates `risk/direction/value`; top-level feature-plan `feature_labels` and `feature_summaries` provide equal-length short descriptions. `report.technical_overview` may contain `title/technical_problem/technical_solution/technical_effect`; omit unsupported effects. The default template already supports these fields, without style rewrites.

## Agent verification

These are local records written after actual Agent verification, not MCP tool responses. Save the original comparison's disclosure, shared features, patent text/images and original `comparison` in the request:

```json
{
  "disclosure_text": "Original disclosure",
  "features": ["The same complete feature list"],
  "publication_number": "Exact publication number",
  "patent_text": "Actual full text identical to the original comparison material",
  "patent_images": [],
  "comparison": {"feature": "Feature to verify", "judgment": "not_mentioned", "disclosure_type": null, "evidence": [], "reason": "Original rationale"}
}
```

Result file:

```json
{
  "method": "agent",
  "status": "upheld",
  "checked_scope": "Sections, paragraphs, figure pages actually reread or calculations actually checked",
  "reason": "Actual verification method, findings and rationale",
  "original_comparison": {"original comparison": "Replace with the actual complete original object"},
  "reviewed_comparison": {"current comparison": "Replace with the complete valid current object"}
}
```

Replace both placeholder comparison objects with actual complete objects; do not submit them unchanged. `upheld` agrees with the original judgment; `overturned` requires a real change; `material_insufficient` is not a passed check and may have a null `reviewed_comparison`. Mismatched original text/images/features/judgments make the record stale and unusable for conclusions. Scripts verify associations and quotation presence, not whether professional reading actually occurred.

If verification changes facts/evidence used to negate novelty, use the same comparison tool, image/text material and every feature of the solution to recheck overall arrangement. Save actual `request_file/response_file` in `novelty.arrangement_check`; itemwise changes alone do not establish whole disclosure.

## Inventive step and supplementary evidence

For a definite inventive-step conclusion fill the solution's `inventiveness.analysis`:

```json
{
  "closest_publication_number": "Compared and date-eligible publication number",
  "difference_feature_numbers": [2],
  "technical_effect": "Effect of the actual difference",
  "objective_problem": "Actual problem without the target solution embedded",
  "routes": [{
    "title": "Concrete modification or combination path",
    "scope": "whole_solution",
    "result": "unresolved",
    "feature_numbers": [2],
    "teaching": "Original starting point and teaching",
    "motivation": "Reason to adopt it",
    "obstacles": "Necessary interactions, obstacles and their resolution",
    "reason": "Actual judgment",
    "evidence_refs": [{"publication_number": "Actual publication number", "feature_number": 2, "evidence_number": 1}]
  }],
  "overall_reason": "Whether the changes can jointly work in the complete solution"
}
```

`scope` is `local` or `whole_solution`; `result` is `established`, `not_established` or `unresolved`. Differences match current facts; a complete path covers all differences. Evidence numbers are 1-based and refer to real evidence in the current valid comparison. Unresolved paths do not support definite inventive-step conclusions.

With actual common-knowledge sources, use `report.common_knowledge[]`: `publication_number`, 1-based `feature_number`, current complete `comparison`, applicability `reason`, and `source` fields `file/title/date/locator/quote`. Sources must be date-eligible, verifiable task-local originals. Routine labels neither replace common-knowledge evidence nor change original disclosure facts.

## Generate and validate

Requires Python 3, `markdown-it-py` and `Pillow`. Install missing dependencies in an isolated Python environment:

```sh
python3 -m pip install markdown-it-py Pillow
python3 scripts/render_report_html.py --input /task/report-draft.json --validate-only
python3 scripts/render_report_html.py --input /task/report-draft.json --output /task/report.html
```

Run from the Skill root. `--data-output` exports validated structured data; `--parts-dir` exports complete sections and the resource manifest. User templates must preserve the same facts and gaps. No task-panel startup or Skill-version reporting is required.

Open the result and inspect originals/drawings, check provenance, solution switching, complete matrix, search records, narrow-screen and print views. `scripts/preview_report.py --file /task/report.html` previews only that file. Deliver the actual file link.
