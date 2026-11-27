# Scenario review rubrics

## Four common modules

### Search strategy

Use three evidence-based checks, never word counts, tool scores or hits as substitutes:

| Check | Professional assessment | Typical correction |
|---|---|---|
| Synonyms | Preserve full concepts/qualifiers/languages; aliases, abbreviations and translations must be equivalent in context and enter appropriate branches. | Identify omissions/drift; distinguish synonyms from related/broader/narrower terms. Restrict broad terms or use supplemental branches, not indiscriminate synonym ORs. |
| Query | Check applicable syntax/fields, intra-group alternatives, inter-group relationships, parentheses, phrase/proximity/truncation, date types and geography/status/class restrictions. | Keep originals/proposals and validation states separate; unverified database syntax is conceptual logic, not a fabricated executable query. |
| Derivation | Features/problems→concepts, necessary conditions, alternatives, branches/merge; no unsupported scope shifts. | Explain concrete paths/counterexamples; without measurement, only potential misses/noise, not counts/recall. |

Start with the report’s complete technical concepts. Compare them with its vocabulary or the terms extracted from its queries, then check the Boolean relationships. If the report provides both a complete technical proposal and traceable search elements, you may use `expand_patent_search_terms` to generate candidates for review. Check that each element was passed through and returned nonempty expressions. Use the technical context to decide which expressions to adopt and recombine them into complete relationship phrases. If a Boolean reference expression is needed, pass the reviewed concepts and combination logic to the builder. Do not send it an existing executable query for rewriting or validation. Base adoption on technical context, established meaning or relevant usage in original text. Tool output alone cannot establish equivalence. The report need not include every candidate, and list overlap is not a score. Check languages according to the report’s purpose.

Normally OR equivalent expressions and AND concepts that must co-occur, subject to actual relationships. Do not AND incompatible alternatives or turn supplemental class routes into unsupported global conditions. Preserve dependencies when splitting compounds; broad words are not unconstrained replacements for complete concepts. For example, flattening flexible-hinge terms to `flexible OR elastic OR hinge OR joint` admits joint-only documents. Preserve the full term or constrained combinations. This is conceptual, not verified Patsnap syntax.

Search logic differs from legal analysis: single-document novelty and all-elements FTO do not require ANDing every feature/product detail during retrieval. Search identifies relevant claims/disclosures; legal sufficiency belongs to analysis. Reconstruct missing derivation as reviewer interpretation without penalizing absent process narrative. Ask only genuine concept/objective ambiguities. Selected-results/analysis-only work does not trigger this module.

### Selected-reference results

Review final selected/actually cited documents only, excluding criteria/reasons/disposition/handoffs even if supplied. No exclusion-log requests.

| Check | Object | Reportable issue |
|---|---|---|
| Identity/applicability | Final documents, dates, versions and evidentiary eligibility | Wrong number, ineligible date under adopted rules, inapplicable claim version. |
| Relevance | Link to report topic/features/use | Unrelated content used as evidence; insufficient abstracts require targeted originals during analysis. |
| Citation mapping | Final list, comparisons and prose | D1 content attributed to D2, mixed family text, duplicated independent evidence. |

Assess whether selected documents can support the report, not why authors chose/excluded them. Do not infer screening misses or compute screening hit/completeness rates. Final-list-only input is normal; absent exclusion material is not an issue, gap, unverifiable fraction or disposition factor. Missing necessary evidence for an actual selected object must still be identified precisely and distinguished from excluded process material.

### Analysis quality

Separately assess A1/A2 internally as Met/Partly met/Not met/Unverifiable/Not applicable with reasons. Prose gives concrete judgments, not mechanical IDs. Unverifiable is not scored as Not met.

| Track | Check | Acceptance |
|---|---|---|
| A1 facts | Applicable object | Patent/family member/claim version matches jurisdiction/date; product models/versions not mixed. |
| A1 facts | Sources | Decisive patent/product facts have located sources; dates/status checked to required depth. |
| A1 facts | Nature | Originals, translations, facts, assumptions, unknowns and AI inference differ; silence is not absence. |
| A2 comparison | Faithful quotation | Conditions/parameters/relationships/negatives retained; dependent claims include inherited limitations. |
| A2 comparison | Supported mapping | Original elements map to report/product features with reasons; beyond-literal interpretation has support. |
| A2 comparison | Proportionate inference | Scenario method applies; evidence supports conclusion strength and addresses counterevidence/unknowns. |

Check facts, quotations and reasoning separately. Reasonable professional disagreement is not automatically error; state issues, competing bases and effects for human disposition. Missing decisive facts mean inadequate factual foundation and unverifiable dependent comparisons, not a new CC run whose AI agreement fills the gap.

Negative findings also need evidence: a reliably unmet necessary element may defeat literal coverage of that claim, not every claim/family/equivalence question. “Not in the manual” is insufficient proof of absence.

### Compliance/traceability

Check commission, scope, date, sources, methods, limitations, human judgment and versions; reconcile numbers/tables/prose/attachments.

## Patent search reports

Prioritize reproducibility and result applicability, without forcing infringement/novelty/validity conclusions. Queries/databases/dates/languages/classes/merge rules must be reviewable. Assess missed-hit risk, bias and boundaries rather than hits alone. Target final selected/cited documents without regenerating pools or reviewing exclusions. “Comprehensive/no relevant patents” claims need stronger scope/limitation disclosure.

## Novelty and patentability reports

Distinguish scientific novelty review from patent novelty/inventive-step judgments; apply patentability rules only to corresponding conclusions. Verify critical date and public availability. Novelty normally needs one reference disclosing all relevant features; do not mosaic multiple references into single-document disclosure. Check decisive original passages, not abstracts alone. Inventive-step/combinations need distinguishing features, technical problem, motivation/teaching and jurisdiction-appropriate method; similarity is not automatically obviousness. Nonpatent evidence needs verifiable source/date/content.

Check selected records' actual evidentiary use/time/relevance; expired patents may still be prior art. A1 verifies date/version; A2 checks limitations, combination and same embodiment, avoiding incompatible embodiments assembled as one disclosure. A failed novelty combination may still matter to inventive step; assess each separately.

## FTO reports

Establish configuration, activities, jurisdictions and date. Search targets potentially covering claims, not generic similarity. Verify applicable active/pending claims, family members and versions; simple status cannot support complex time-specific conclusions. Compare claim elements with implementation; abstracts/descriptions do not replace claim boundaries. Description may explain terms but cannot silently expand/narrow scope. “No risk found” means no blocking object identified within searched scope/date, not legal clearance. A1 checks applicable claims/real product facts; A2 preserves all necessary limitations without importing an embodiment restriction without basis.

## EoU reports

Separate patent/product evidence. Verify applicable claims/version/needed legal context. Product evidence may be actual webpage text, manuals, images, tests, purchase/use records from user/available sources. Patent records do not prove implementation; URLs are not read text. Each claim element needs product evidence or an explicit gap, not overall similarity. Patent evidence alone leaves product side not_verifiable, not implemented/not implemented. Bind selected sources to product identity/time; similar marketing/function language does not prove claimed structure, relationships or values.

## Invalidity searches and other reports

Establish grounds, critical date, claims and evidence eligibility. Separately check date qualification, single-document disclosure, combination logic, authenticity and versions. Lifecycle clues to review/invalidation decisions are not complete decisions/reasoning. For other reports choose the closest rubric, stating inapplicable rules without changing the original purpose.

## Severity

**Major:** can change core conclusions, use or sign-off, e.g. wrong jurisdiction/date/version, unsupported infringement/novelty, material numerical inconsistency or unverified→absent. Explain impact before tags.

**Moderate:** weakens in-scope reliability/traceability without immediately overturning conclusions, e.g. synonym gaps, incomplete secondary citations or insufficient limitations. Screening process/exclusion reasons are not defects.

**Advisory:** presentation/format/minor improvements without conclusion impact. Reasonable disagreement is not automatically major.
