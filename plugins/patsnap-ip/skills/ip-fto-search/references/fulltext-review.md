# Optional description review before CC

Run only for `evidence_mode=fulltext`. Retrieval here means obtaining selected patents' full descriptions, not new patents or a broader pool. Both all/partial strategies may use it. `claims` skips advance per-patent description review but still requires complete claims, itemwise translation and necessary interpretive evidence.

## Acquisition and limits

Follow the main Skill's A1 routing and current MCP protocol, reusing identical-identity/version receipts first. For numbers alone, verify complete publication identity through search, then obtain text through the full-text tool's supported identity route. Do not infer required identifiers/content options from the Skill. Check complete claims/descriptions and retain document, original language, version, complete receipt and provenance. No silent family substitution or summary-as-fulltext. Translate locally with provenance without overwriting originals.

For client number lists requesting import and originals, first pass the list-import gate through Boolean construction/search, then call `patsnap-ip:fetch_patent` for every verified object. Disclose complete, partial, failed and unresolved objects individually. Original-text-only delivery does not require Screening first.

Call `patsnap-ip:build_claim_chart` under the current protocol, keeping the frozen solution separate from patent identity. Do not mix patent text into product facts or present local text as the tool's own original source. Full-text enhancement first acquires, reads and records descriptions locally. Uncovered dependent claims and interpretation opinions remain separate local reviews, without claimed tool writeback. Verify actual evidence on both sides and claim coverage.

## Minimum per-patent analysis

1. Acquisition: PN/PID, claim version, source and original availability. Empty/abstract-only/error/truncated content is not acquired fulltext. Long texts may be read in segments with coverage intervals/locations; unread parts are not analyzed.
2. Interpretation clues: locate definitions, components/relationships, optional/required configurations, structures/steps supporting functional language, parameters/conditions and explicit exclusions/distinctions. Record exact quote/location and applicable claim/row.
3. Support/conflict: preserve both. Ordinary embodiments do not automatically narrow claims; description disclosure is not a claim limitation or customer product fact. Explain changes to interpretation; unknown remains unknown.
4. Handoff: separate raw text files from concise interpretation tables. Claims still decompose from originals; put description evidence in the CC interpretation column and details below/appendix, not a fulltext dump in the main table.

Acquire/analyze the current batch, then official CC and review; do not wait for all 150 before batch 1. Missing selected fulltext keeps that batch pending with specific objects. Continue independent preparation, not false fulltext completion. Users may wait, explicitly switch to claims mode or accept bounded local delivery. Mode changes create versions; gap acceptance is not acquisition.

## Verifiable local record

`fulltext-review.json` is local, not an MCP result:

```json
{
  "schema_version": "fto-fulltext-review-1",
  "selection_sha256": "canonical-selection-object-sha256",
  "reviews": [{
    "patent_id": "selected-PID", "status": "complete",
    "source_record": {"path": "/absolute/path/official-fulltext.json", "sha256": "actual-file-sha256"},
    "analysis_record": {"path": "/absolute/path/fulltext-analysis.md", "sha256": "actual-file-sha256"}
  }]
}
```

Complete requires actual acquisition and finished analysis, not successful calls alone. Missing/partial/failed states include reasons and do not validate as complete. Hash with the script's `sha(canonical(selection))`: UTF-8 JSON, sorted keys, compact separators, Unicode unescaped.

```bash
python3 scripts/select_cc.py validate --catalog /absolute/path/cc-catalog.json --selection /absolute/path/cc-selection.json --lifecycle /absolute/path/lifecycle-gate.json --batch 1 --evidence /absolute/path/fulltext-review.json
```

The script checks batch IDs, record versions, source/analysis hashes and completion, not authenticity/fulltext completeness/interpretation correctness. Other incomplete batches do not block a ready batch's validation; skipped failures cannot be called whole-case completion.

Report description acquired/analyzed/missing separately with objects, sources and effects on opinions. Use the shared local report template and distinguish official results from local evidence/interpretation/review. Fulltext may strengthen interpretation; do not promise a predetermined accuracy gain.

In the four-column table, use “Description support / claim interpretation basis,” prioritizing original description/prosecution quotations and paragraph numbers.
