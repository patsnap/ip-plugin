# FTO report structure and formatting

Read when generating, redesigning or reviewing final reports. These delivery/layout rules do not change retrieval, Screening, Claim Chart or legal assessment, or duplicate MCP protocols.

## 1. Document structure

Use this order. Omit optional statistics without data; retain required unexecuted sections with their actual status.

1. Cover;
2. Contents (required for more than 10 body pages);
3. Executive summary and fact basis;
4. Retrieval and candidate-screening scope;
5. Results overview;
6. Per-patent, itemwise assessment of possible claim coverage;
7. Conclusions and unresolved matters;
8. Appendix A: keywords and classifications;
9. Appendix B: search strategies and queries;
10. Appendix C: evidence, adopted versions and current rights;
11. Appendix D: completeness and delivery verification;
12. Disclaimer.

Partial tasks retain this hierarchy but name their actual scope, such as partial analysis, report review or specified-patent comparison, on the cover/summary. Do not imply complete FTO.

### 1.2. General readers

Apply the main Skill’s plain-language rules throughout. Explain scope, findings, unknowns and decisions first, then technical terminology, queries and evidence. Explain FTO/Boolean/Screening/Claim Chart on first use; keep internal codes in parentheses/appendices. Preserve full originals/claims and layer important evidence as original, complete translation and plain explanation, without treating explanations as originals/legal conclusions.

### 1.5. HTML preview and final-format choice

Generate a self-contained preview before final delivery for content review and format selection. Use chapter navigation, conclusions first, evidence anchors and expandable details, with FTO structure:

1. Summary, scope and decisive unknowns;
2. Product solution and evidence;
3. Logic, keywords/synonyms/classes, Boolean/broad semantic recall and convergence within a frozen semantic pool;
4. Retrieval, Screening, selection and completeness reconciliation;
5. Selected identities, lifecycle and itemwise CC;
6. Conditional conclusions, evidence gaps, completeness and disclaimer.

Navigation targets section anchors; evidence links target actual limitations/appendices. External original links use only tool-returned/verified official URLs with `target="_blank" rel="noopener noreferrer"`. Do not build URLs from PNs. Mark missing links without deleting documents.

Default status is customer preview, with unresolved items and HTML/Word/PDF/Markdown/explicit-combination choices at the top. Record actual client confirmation/choice provenance. Confirmed HTML can be final; do not generate all formats automatically.

Do not embed complete raw Screening receipts, unselected full texts or duplicate claims. Retain locations/completeness. Selected CC must be complete when expanded and printed; folding cannot hide gaps. No external CSS/JavaScript dependencies; color alone cannot carry conclusions.

Show actual semantic sentences, relationship phrases by language, input-pool count/version, scope, method and retention rules directly in the body. Long PN/ID lists may use downloads/appendices; hashes/references or “converged” alone are insufficient. Separate convergence from new whole-database supplementary recall.

## 2. Page system

- Word/PDF: A4. Portrait body/appendices with left/right 3.18 cm and top/bottom 2.54 cm margins.
- Per-patent CC: landscape with left/right 2.54 cm and top/bottom 3.18 cm; restore portrait through a new section afterward.
- Keep patents in one document. Start each with a level-2 heading/identity band, paging as needed without near-empty title-only pages.
- Repeat table headers across pages. Allow natural row continuation; avoid fixed heights clipping text. Keep short limitation rows together where possible.
- Header: case name/report version. Footer: confidentiality if supplied, page X of Y. No cover header; numbering starts at contents/body.
- Long queries/originals may span pages. Do not shrink to unreadable sizes or force entire-page cells.

## 3. Cover and contents

Cover includes product name, freedom-to-operate report/actual task type, version, delivery/assessment dates, markets/activity countries, sourced client/preparer identities and one scope-summary sentence. State actual route counts, Screening returns, selected/completed/incomplete CC and decisive unknowns, with sourced counts rather than cross-stage inference. Avoid long risk prose or “not found” equated with clearance.

Use real heading hierarchy/page numbers for contents. Patents appear at level 2; individual limitations do not.

## 4. Summary and results

Answer object, countries/activities/date, work actually completed, findings and gaps. Present solution and features separately so readers need not reconstruct product facts from queries.

Use two overview tables:

1. Process counts: database returns, retrieved/identity-verified, submitted, returned candidates, selected, successful reviews, failures, unresolved and pending counts/sources.
2. Candidate overview: original screening order, PN, title, applicant/owner, authority, adopted claims, pending/active status, comparison result, local review and main gaps.

Add an applicant/owner × high/medium/low/pending matrix only with verified identities and decision value. List PNs and use the same completed-analysis denominator. Screening order is not legal risk; nonreturns are not low risk.

## 5. Solution and features

Explain purpose, components/relationships, operation/conditions, problem/effect and unknowns in coherent prose, separating configurations without inventing a combined product. Feature table: `ID | actual type | technical feature | source location | search purpose/status`. Use actual extraction categories/traceable sources. Put keywords/synonyms/classes and queries in appendices A/B rather than crowding this table.

## 6. Per-patent Claim Chart

Repeat these components:

1. Level-2 heading: sequence, PN, title;
2. Identity: publication/adopted version, applicant/current owner, jurisdiction, filing/priority dates, legal/procedural status, evidenced expected expiry and evidence date; unavailable stays pending without calculation;
3. Scope: claims/dependencies, product configuration, full-description strategy and evidence state;
4. Separate raw tool and local-review conclusions, with decisive limitations/unknowns before conditional findings;
5. Four-column strong-evidence table: claim limitation, description support/interpretation, product facts, comparison opinion.

Keep the strong-evidence contract rather than an ordinary feature/similar-text/relevance table. Suggested landscape widths: 34%/20%/26%/20%, adjustable for language/evidence without losing originals, translations, sources, knowledge states or unknowns.

- Column 1: row/claim/dependency identity, complete original unit, complete translation/provenance and version changes.
- Column 2: prioritize original description/prosecution quotes, paragraph numbers and conditions/status. State claim-only reliance or unavailable originals. Embodiments do not automatically limit scope; model reasoning is not description support.
- Column 3: product-element IDs, actual quotes/figure locations, sources and present/absent/unknown states.
- Column 4: raw label alongside local correspondence/difference/pending-evidence/interpretation opinion and decisive reason; preserve conflicts.

Use one limitation per row, not one vertically merged claim cell across many pages. Repeat claim IDs or “continued” and page headers. Preserve frozen candidate order rather than resorting by final risk.

## 7. Appendices

### A. Keywords and classifications

One retrieval unit per row: unit ID, feature, Chinese terms, target-language terms, classification, adoption/rejection reason. Expanded terms remain separate from product facts.

### B. Strategies and queries

First list route ID, strategy/language, search intent, countries/status/dates, actual viewed window, database-return/retrieved counts and receipt locations. Then reproduce complete queries in monospaced naturally wrapping text. Separate Boolean, semantic and keyword routes; do not sum overlapping counts as unique totals.

### C. Evidence, versions and lifecycle

List complete claims, dependency sources, procedural records, description evidence, product materials and locations by evidence ID. Body citations resolve to those IDs; mark missing material individually.

### D. Completeness and delivery

Record stages, object coverage, failures/unresolved identities, version consistency, count reconciliation, page rendering, removed placeholders and professional-review gaps as passed/failed/not verified. File generation does not establish content completeness.

## 8. Visual standards

- Black headings, body and headers/footers. Use stable sans-serif fonts with available language fallbacks; body 10.5–11 pt, tables 9–10.5 pt, footnotes/sources at least 9 pt.
- Real Word heading styles: level 1 16 pt, level 2 13–14 pt, level 3 11–12 pt, supporting contents generation.
- `#D9D9D9` table borders, consistent pale-blue header fill, black text. Status colors supplement text.
- Center numbers/dates/short statuses; left-align long text with vertical centering and consistent cell padding.
- Use hierarchy, whitespace and grouped tables, without decorative rules, textbox conclusion cards or large dark fills.

## 9. Generation and acceptance

Fill the unified template, generate the customer HTML preview, then confirmed final formats. Verify navigation, evidence anchors, evidenced original URLs, logic/terms/queries, expandable evidence and printing. Remove inaccessible external links and mark unavailable.

For Word, update contents/page numbers and render every page, checking cover, contents, section orientations, all multipage headers and CC pages. Check missing glyphs, font replacement, clipping, overlap, broken tables, abnormal blank pages, orphan headings, fixed-height truncation and placeholders.

Long reports may use main report plus evidence attachments, but the main report still lists every adopted object, completion state and conclusion basis. Splitting cannot omit failed, unknown or low-risk objects.
