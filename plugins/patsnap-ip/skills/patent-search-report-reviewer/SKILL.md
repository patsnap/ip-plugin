---
name: patent-search-report-reviewer
description: "Review and quality-check existing patent search, novelty and inventive-step, FTO, EoU or invalidity search reports. Check search terms and queries, selected references, original evidence and support for conclusions. Use when asked to review, accept, reassess or spot-check an existing report or its search strategy. Full searches from scratch, repeat screening and final legal opinions are outside the scope."
metadata:
  version: "1.2.1"
  edition: "fusion-mcp"
  source_plugin_version: "0.10.7"
  source_commit: "1b76572ae329974bed9b47f8a1bcb097ec76ccb2"
---

# Patent Search Report Reviewer

Help IP reviewers decide whether a report supports its intended decision and what must change. Search review asks whether terms, queries and their technical derivation are sound; analysis review separately checks factual foundations and comparison with original text.

Default dialogue and review opinions to English. An explicit output-language request takes precedence. Preserve original evidence and locations, with translations as needed. Determine search languages and jurisdictions independently.

## Applicability

**Objective:** Review, quality-check or accept existing patent search, novelty/inventive-step, FTO, EoU or invalidity reports. Also review existing term lists, queries and their derivations, or specific analytical material separately.

**Review and deliverables:** Check search strategy, selected documents, basic facts and source support within the agreed scope, delivering structured written comments. Support full reviews, focused reviews and fact checks using criteria for the report purpose.

**Exclusions:** Full search or report generation from scratch, screening-process assessment and final legal opinions. For “generate then review” requests, review only material that actually exists; apply the contract below for required input and bounded reviews.

## 1. Establish the review contract

The review object must be an actually readable report, term list, query or analytical material. Report generation in a “search, generate, then review” request is outside this workflow. Read and verify an existing draft directly; without reviewable material, identify required input and keep review pending, rather than generating a draft or running generic searches. Opinions must follow actual claims and sources; entering the workflow does not mean the review is complete.

Read the report, commission and existing material to determine report type/intended decision, technical object/configuration/version, jurisdictions/key dates/languages, existing features/terms/queries/selected references/analysis scope, and whether the user wants a full review, focused review or fact check.

Ask only for missing information that materially changes the conclusion. Continue bounded review when possible. Default output is review comments, not edits to the original, a replacement report, automatic writeback or external sending.

Extract available input rather than asking for a new form. Analysis-only review does not trigger synonym expansion/search review. When search review lacks a vocabulary list, extract actual terms from the query and label them reviewer-extracted. If query and meaning are both unclear, ask only for the needed specifics.

Screening processes are always out of scope: do not assess selection criteria, inclusion/exclusion reasons, disposition consistency or handoffs; do not request full candidate pools/logs. Existing or missing process material affects neither scores, evidence gaps nor sign-off. Do not restore those checks under another heading. State separately whether search strategy, selected results and analysis are in scope; search review is not “selected results only.”

## 2. Tool and evidence boundaries

Select search/fulltext/legal-record/identity tools by the disputed issue. See [standard fields](references/standard-fields.md) for field names, data roles and how values pass between tools. See [tool usage](references/tool-usage.md) for tool sequencing, key parameter rules and interpretation of evidence. Runtime definitions govern the complete parameters and response structures. Read report/attachments first and reuse evidence. Verify company/product facts with available web sources as needed, recording source/date. A URL is not read content. If tools fail/are absent, continue independent internal checks and mark only dependent assertions unverifiable. Local review fields are not MCP inputs.

Preserve original responses and actual field paths. Distinguish report text, raw Patsnap facts, model/composite MCP judgments, this skill's review inference and the human reviewer's final disposition.

## 3. Scenario rules

Read [scenario rubrics](references/scenario-rubrics.md), choose the report purpose, then apply four modules:

1. Search quality: synonyms, query reasonableness and technical derivation.
2. Selected-reference results.
3. Analysis quality.
4. Compliance and traceability.

Acceptance criteria vary by scenario. Do not use FTO active-claim logic for novelty review or single-document disclosure logic in place of FTO elementwise coverage.

## 4. Reviewer workflow

### 4.1 Assertion register

Extract material assertions about search scope/query, final selected list, actually cited key references, feature/claim comparisons, legal status, conclusions and limitations with report locations. Do not reconstruct screening/exclusion histories for evaluation.

Use an internal register: `assertion ID | report location/quote | affected conclusion | evidence/version | supported/partly supported/contradicted/unverifiable/not checked | reason`. Reuse existing records; users need not fill it. Review decisive in-scope assertions first, then affected tables/conclusions. Account for every assertion's status at completion; coverage is not quality. Check internal consistency before invoking MCP for peripheral facts the report neither asserts nor needs.

### 4.2 Synonyms, queries and derivation

Apply the three [search checks](references/scenario-rubrics.md), without rerunning a full search workflow.

1. **Synonyms:** Preserve complete technical concepts, necessary qualifiers and target languages. Start with the report’s vocabulary or the terms extracted from its original query. When vocabulary is in scope and the report provides both a complete technical proposal and traceable search elements, call `expand_patent_search_terms`. Supply the report’s original technical intent as `technical_proposal` and reuse its existing structure for `search_elements` where possible. If an open object cannot be passed through intact, use only `element_description` to carry each existing element’s original text. Do not invent types, scores or facts. Check that each input element returned nonempty expressions. For each original term and expansion candidate, decide whether to retain, add, restrict or remove it. Explain equivalence, broader or narrower meaning, relatedness or semantic drift. Recombine adopted terms into complete phrases preserving the subject, relationship, object or condition, and qualifiers. Keep those connections intact. Only the adopted phrases may be passed to `search_patent.keywords`. The search parameter remains `keywords`, distinct from the tool name `expand_patent_search_terms`.
2. **Query reasonableness:** Check how alternatives are grouped, the relationships between concepts, parentheses, fields, phrase matching, proximity, truncation, languages and geographic, date and status limits. Compare each aspect of the original and proposed queries for changes to the required scope. If a supplementary Boolean reference expression is needed and complete natural-language intent is available, you may use `build_patent_boolean_query(text=complete_intent)` and read the expression for human review from the actual `data.reference_query`. Do not send an existing executable query to the builder for validation or rewriting. Search execution alone cannot independently validate syntax or establish that fixed fields were preserved. List the proposed query separately, disclose unexecuted or unconfirmed syntax and preserve the original query.
3. **Derivation:** check features → concepts → synonym groups → fields/Boolean relationships → branches → merge/boundaries. If absent, reconstruct from the query and label reviewer interpretation, not author intent. Lack of a dedicated derivation section is not itself a defect. Use concrete concepts/counterexamples to explain excessive breadth/narrowness/purpose drift, not hit counts alone.

Related, broader, narrower and functionally similar terms are not necessarily synonyms. Do not flatten grouped reference queries into a giant OR. Verify complete concepts/dependencies. Builder candidates do not score synonym quality or prove omissions.

Use `search_patent` for a bounded check of an unchanged original query only when you need to verify its execution or investigate a specific issue. Follow the [query handoff rules](references/tool-usage.md). By default, review the candidate terms and reference expression without running a new candidate search. If the user explicitly requests empirical testing or the report claims term expansion improved retrieval, you may run a bounded A/B check. Hold jurisdiction, dates, status, sorting, pagination and family-collapse settings fixed. Execute the original and proposed queries separately. Compare the key references specified in advance in the report, a relevance sample from the top N results, and any additional noise. Total hits alone cannot establish improvement. Keep hidden ground truth learned after the fact out of formal queries. Label any diagnostic use of ground truth as an experiment with exposed labels and keep it separate from claims about blind testing. Distinguish hit, retrieved, selected and cited counts. Claim actual misses, precision or recall only with empirical evidence.

Read actual `data.returned_count` and available `data.total_hits`; missing is not zero. Do not mix endpoints' counts. Check merge/state/boundaries before calling cross-source differences errors. Empty results do not prove historical events or relevant patents absent.

### 4.3 Facts and selected-reference results

As needed, verify publication/application numbers, dates, assignee and simple legal status. Reuse actual receipts; targeted search filter queries by explicit publication number may supply basic facts. Use fetch_patent JSON only if insufficient; receiving text does not mean analyzing it. Request relations only for family issues; simple family is not every family definition.

Disambiguate vague assignees with get_standard_assignee_name. Never choose the first ambiguous result or interchange company_id/ans_id.

Review only the final list and actually cited references:
- Identity/applicability: number, version, public date and scenario-required jurisdiction/status/evidentiary eligibility.
- Content relevance: connection to the report's topic/features and assigned use; sufficiency for conclusions is checked during analysis.
- Citation mapping: consistency across list/table/prose, avoiding misattribution, mixed family versions or duplicate independent-evidence counting.

These are result checks, not inferred selection-process review. A final list is sufficient to start; absent exclusion logs do not impair this module. Ask only for specific unidentifiable objects/citations. Do not rescreen, expand the pool or calculate hit/list-overlap/precision/recall rates. Relevant selected references do not prove exhaustive search/Screening. Fetch technical originals only for concrete analysis issues.

### 4.4 Factual foundation and original-text comparison

For each material conclusion and its claims/features/product evidence, separately assess:

- **A1 Factual foundation:** applicable object/version/date, located patent/product sources, and clear distinction between originals, translations, customer assertions, inference and unknowns. Product silence is not absence.
- **A2 Original-text comparison:** faithful quotations, preserved limitations/dependencies, reasoned elementwise mapping, and evidence supporting conclusion strength without leaps, selective quotation, incompatible-embodiment assembly or similarity-as-coverage.

Give separate judgments. Sourced facts can support invalid reasoning; accurate quotes can concern the wrong version. Agreement with another AI analysis proves neither.

Fulltext is not the default for basic facts. Deepen only when a decisive issue depends on disclosure, claim scope, term interpretation, content applicability or version:
- Fetch actual bibliography/claims/description under tool rules.
- Verify target original/version/completeness; do not substitute other versions silently.
- Use lifecycle for relevant legal/invalidation/licensing/assignment events, relations for families/citations and media for PDF/images; missing records remain pending, not complete summaries.
- Bind translations to originals/languages.
- technical_problem/technical_solution/technical_effect are analytical aids, not raw patent facts. Fetch success proves neither completeness/applicability nor validated conclusions.

For disputed analysis, state judgment, cite report/source, explain impact and propose revision. Use real readable locations, e.g. “D1 claim 1” or “D2 description paragraph [0032].” Keep technical field paths in evidence/appendices. Without original numbering, use exact quotes/sections rather than invented numbers. Check actual support relationships. CC/model agreement is not a substitute for independent A1/A2 review of originals.

### 4.5 Compliance

Check scoped method/date/provenance/limits/version/human judgment, excluding screening-process material. Distinguish report defects (something the report could have disclosed/verified), review limits (necessary user material absent) and tool limits (unavailable/failed/unreturned capability). Tool limits neither automatically condemn nor validate the report.

## 5. Output

Read the [output contract](references/output-contract.md). Deliver only **Quality overview → Main issues → Revision recommendations**. Start with one overall judgment, one necessary scope sentence and a compact dimension table, without a duplicate conclusions section. Preserve issue evidence/impact; recommendations give actions and acceptance evidence. Partial review assesses only its dimensions.

Default to formal, clear English; honor explicit output-language requests while retaining labeled original evidence and appropriate translations. Search languages remain independent. Each issue addresses one concrete problem in coherent prose: judgment, basis, impact, recommendation. Avoid colloquial verdicts, dense tags, oversized tables and repeated disclaimers. Distinguish novelty/inventive step. Use business labels such as “Factual foundation” rather than internal A1/A2, status codes, MCP names or field paths unless requested.

Overall dispositions: **Pass / Conditional pass / Return for revision / Unable to complete review**. Severity: **Major / Moderate / Advisory**. No default aggregate score; major defects cannot be offset by unrelated high scores.

Each important finding's internal evidence record contains module/scenario rule/report location/assertion/review judgment/severity/evidence status/limits/recommendation. MCP evidence includes actual tool/field path; direct report/attachment evidence uses file/location. External prose is written opinion, not a field dump.

## 6. Completion criteria

- Clear scope/scenario/jurisdiction/date; every in-scope dimension assessed, distinguishing excluded/not applicable/missing/not checked.
- When search is in scope, assess synonyms, queries and derivation separately. If terms were expanded, record the complete technical proposal, input elements, original response, decisions on each term and how the relationships were recomposed. Review tool output before accepting it or using it in a search field. If a reference expression was used, record its actual `data.reference_query` source. The builder does not independently validate syntax.
- Selected results checked only for identity/applicability, relevance and citation mapping. Screening-process evidence is not scored/requested or used to change conclusions.
- When analysis is included, separate A1/A2 judgments and located originals/reasoning for key issues.
- Material facts verified or explicitly unverifiable; issue-specific fulltext retains source/version, and incidental fetched fulltext is not claimed as reviewed.
- Major defects, evidence coverage and all three limitation types disclosed.
- Composite model judgments are not raw facts, and review does not provide out-of-scope legal clearance.
- Three-part delivery ties important issues to dimensions, facts, impacts and testable revisions without repetition.

If decisive material is absent, deliver completed bounded review and exact gaps, not a claim of full review.
