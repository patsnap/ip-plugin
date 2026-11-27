---
name: ip-novelty-search
description: "Use when checking whether an invention or technical proposal is new. Compare its features with the closest patents, verify the decisive evidence, and report novelty and inventive step separately in a traceable HTML report. Use for prior-art searches, novelty or inventive-step analysis, X/Y evidence audits, and continuation of an existing search. FTO, competitor analysis and portfolio planning fall outside its scope."
---

# Novelty Search

Start with complete technical relationships, find the most useful prior documents, verify differences, and then form conclusions.
Use the user's requested language for conversation and reports; default to English. Preserve evidence quotations in their original language.
This Skill provides prior-art and patentability research, without guaranteeing patentability or replacing a formal novelty-search opinion.

## Tools and materials

Use these four tools. Their current definitions govern parameters. Before calling them, read [Tool meanings and input/output patterns](references/tools.md), the explicit tool contract for this Skill.

| Tool | Purpose |
| --- | --- |
| `extract_technical_features` | Extract features and source locations from the original disclosure |
| `search_patent` | Semantic, keyword, filter, Boolean and citation retrieval |
| `fetch_patent` | Read bibliography, full text and media as needed for known patents |
| `assess_feature_disclosure` | Compare individually or in batches using the same disclosure and features |

Use materials returned by these tools for patent searches, text, drawings and PDFs. Local scripts only organize records and generate reports.
If a required tool is unavailable, identify the blocked step. Do not invent legacy tool names or switch to another patent service.

## 1. Understand the disclosure and assessment boundary

Read current and earlier messages, accessible attachments and existing task records to identify:

- Components, positions, connections and interactions, or method actions, sequence and conditions.
- The problem or technical effect; either is sufficient, without requiring quantitative experiments.
- The solution to assess, publication cutoff and explicit search scope; also record any known intended filing date or effective priority date to identify earlier-filed, later-published applications under the target jurisdiction.
- Intended filing or examination jurisdictions. Inventive-step conclusions must follow their examination framework. A technical search and comparison may proceed without a target jurisdiction, but cannot yield a definitive jurisdiction-specific inventive-step conclusion.

Extract information already supplied. Do not always display scope selectors or require internal forms.
Ask the necessary questions together and wait before dependent steps only when implementation details are missing, attachments cannot be read, or ambiguity changes the assessment subject. A name, use or expected effect alone cannot support a complete novelty search.

Check for a concrete, inevitable conflict with established natural laws. Explain and stop if one exists; if a decisive condition is missing, clarify only that condition. Incomplete parameters, missing experiments and engineering difficulty alone are not conflicts.
If no cutoff was set, state that no publication cutoff applies; do not substitute today, a filing date or a priority date. Technical retrieval and structural comparison may proceed, but documents with unresolved date eligibility cannot be treated as qualifying prior art. Mark novelty and inventive-step conclusions as provisional and distinguish publication dates from prior-art eligibility. If inventive step is requested without a target jurisdiction, clarify jurisdiction and assessment cutoff together. If the user permits a test first, identify its test jurisdiction without assuming a universal worldwide standard.
For insufficient input or multiple solutions, read [Intake and assessment subjects](references/intake.md).

## 2. Organize technical features

When extraction is needed, call `extract_technical_features` with the original disclosure and actual drawings. Read the complete structured result and address clarification questions. An existing valid feature list may be reused.

- Treat the extraction receipt’s complete relationships as `source_features`, preserving text and order exactly. Do not merge, rewrite, delete or split the original receipt. Save raw source features and their evidence in the feature plan.
- After preserving the source relationships, a host-owned `comparison_units` list must split a relationship when a document could expressly disclose one independently judgeable limitation without disclosing another; retain an indivisible relationship as one unit. Every unit remains a complete local relationship with objects, connection/action and condition; never use isolated parts, effect words or disconnected phrases.
- Each unit maps to exactly one `source_feature_number` and quotes the actual original disclosure sentence for that source. Do not recombine relationships across sources. Every source relationship has at least one unit.
- Derive formal `features` verbatim from `comparison_units[].feature`; this is the sole feature list passed to every formal comparison. `groups` aggregate units by source relationship without overriding unit facts.
- Update extracted features only when a user correction, scope change or a tool clarification changes the assessment subject. Re-extract and retain the new receipt instead of silently editing the old one.
- Separate the primary solution, optional improvements and alternative implementations; assess products and methods separately.
- Check for omitted necessary limitations, optional conditions mixed in, or requirements absent from the disclosure.
- Use the same list throughout retrieval, comparison, verification and reporting; revise only when understanding or scope changes.

Do not require itemwise confirmation of an unambiguous list. Save the original disclosure, features, sources and solution scope for later checks.

## 3. Search and select

Read [Search methods](references/search.md) before retrieval. Organize queries around decisive relationships and uncertainties that could change the judgment, without fixed rounds, tool ratios or candidate counts.

- Discover candidates with `search_patent`; semantic queries express complete technical intent and keywords preserve complete concepts.
- Default to mixed semantic and keyword recall in the same request using `semantic` and `keyword`. Semantic input carries complete intent, relationships and the problem; keywords carry precise structures, industry terminology and multilingual variants. The two inputs complement each other instead of repeating the same string.
- Mixed recall is not a mandatory AND. Merge by exact publication identity and family; retain semantic, keyword or dual-channel provenance. Channel matches determine reading priority, not disclosure facts.
- Before each discovery query, set a target number of distinct technical groups to review. Group publication aliases, known families and exact normalized titles in the reading queue. If the first page falls short, keep the request fixed and advance only `offset` until the target is met, results are exhausted, or a tool window, budget or error ends the search. Record the stopping reason and preserve every publication in the ledger, including members of provisional title groups.
- Search the complete primary combination first, then decisive differences or unresolved relationships. Targeted rounds still pair natural-language relationships with grouped concepts rather than broad OR lists of isolated parts.
- After filling the queue and before deciding to stop, review the search routes. Check whether queries repeat one causal relationship, leading results echo the name or intended effect, one family or mechanism dominates, or a decisive relationship lacks an independent route based on structure, position, movement, sequence or conditions. Record the sample evidence and decision in the ledger. When results stay concentrated, expand the family, rewrite terms, reconstruct the route or request missing disclosure details as appropriate. Follow the decision rules in [Search methods](references/search.md).
- For each `relation` query, record a testable proposition linking a subject, action or interaction, and object or condition. Preserve decisive limits such as position, sequence, state changes, quantity, size or clearance. Cite the original disclosure, a user clarification or saved candidate full text. Scoring references, hidden ground truth and answers learned later cannot supply the proposition.
- Derive each `synonym` route from a recorded `relation` query. Expand the subject, relationship, object or condition, and constraints separately, then compose complete phrases that preserve their connections. Record `derived_from_query_id` and `relation_synonym_expansion`. Use the composed phrases verbatim and in order as `keywords`.
- Apply user-specified scope and dates in actual requests; reference fields or IPC codes do not automatically become hard filters.
- For strong candidates, use `fetch_patent` to verify text, exact publication number, application date and publication date; request `media` only when visual evidence is needed.
- Extend citations through `search_patent`: `B_CITES:(publication number)` for backward citations and `F_CITES:(publication number)` for forward citations.
- Retain complementary strong candidates based on evidence actually read; explain relevance, key differences and reading depth.
- Select closest art by the complete relationships, modification starting point and technical purpose, rather than keyword counts, raw ranking or isolated-feature coverage. A document clearly closer to the complete primary combination must enter formal comparison or receive a reasoned exclusion.
- Group families, corresponding national applications and equivalent core-claim routes. Preserve national publication identities, but do not count them as independent technical evidence. A later-published member may assist reading without acquiring prior-art eligibility.

One successful call, an absent word in an abstract, or repeated old candidates does not establish completion. Converge when remaining uncertainties are unlikely to change the main judgment; retain decisive counterexamples.
Normally select no more than 10 documents for formal comparison, without filling a quota. Explain and batch any justified larger set.
Briefly state each round's verification objective, findings and next action. Save actual requests and receipts; tool failures are not zero hits.

Maintain the [candidate ledger](references/candidate-ledger.md) throughout the search. Use ledger version 2 for new tasks. Enter every exact publication number or within-result alias group from every retained receipt, with its query, original rank, channel, family, actual publication date, jurisdiction and stage. Reconcile candidates before full-text retrieval, before formal comparison and before final reporting. Advance in-scope candidates that have high priority or are clearly close to the primary combination, or record a specific exclusion with evidence. Account for user-supplied candidates as well. The validator calculates `unexplained_drop_count` from unrecorded result groups and candidates without a terminal disposition. The count must be zero before proceeding.

Keep two views. The ledger preserves every publication’s date and jurisdiction. The reading queue groups families and provisional exact-title matches to cover distinct technical routes. Fill the queue by paging the original query before reviewing the routes. Mark retrieval as weak if one family still accounts for more than half of the leading sample, one core mechanism exceeds 60%, several routes echo the same effect, or fewer than 60% of the manually reviewed results retain the target chain of technical objects. Use the route review to choose the next action. Raw hit counts cannot justify stopping.

## 4. Formal comparison

First read [Disclosure judgments and fact verification](references/comparison.md).
Call `assess_feature_disclosure` with the original disclosure and the same features. Reuse actual text/drawings already obtained; otherwise provide a patent ID or complete publication number as the tool defines.
Batch 1–10 documents, associate requests/results by original index, retain successful items and recover only failures.
Before a formal call, verify both levels: `source_features` must match the valid extraction receipt in content and order, and request `features` must exactly match validated `comparison_units[].feature`. Stop comparison if either check fails.

Check each relationship's status, reason, quotation, figure number, reading scope and overall arrangement. Distinguish explicit disclosure, necessary inherency, explicit differences and silence in the material read; keep evidence gaps unresolved. Show both comparison-unit statuses and source-relationship aggregates. A group’s incomplete disclosure must not override its disclosed units. Retrieval-stage relevance analysis is not complete comparison. Do not repeat the whole comparison without cause after formal results are available.

### Return from step 4 to step 3

Formal comparison feeds retrieval. Create a concrete feedback item and return to targeted retrieval when:

- Every decisive relationship in the strongest candidate is `not_mentioned`, possibly because terminology, synonyms or classification routes were missed.
- Full text reveals new industry terminology, alternative structures, citation seeds or earlier family publications.
- A difference intended to support novelty has not undergone counterexample retrieval, or a proposed Y combination lacks a secondary document providing the decisive bridge.
- New candidates or facts may change closest art, difference groups, complete single-document disclosure or combination paths.

Each item records at least `feedback_id`, source publication number, affected features, triggering fact, verification question, new relationship proposition, `semantic_query`, `keywords`, and retained dates/scope. For relationships learned from a candidate, cite the actual full-text receipt and source publication number. Reserve scoring references for separately labeled diagnostics. On returning to step 3:

1. Run mixed semantic/keyword retrieval only for the feedback item, preserving previous receipts.
2. Fetch new candidates first, then compare only new documents or affected features.
3. Update candidates, differences and conclusions while retaining the pre-feedback judgment.
4. Converge when new retrieval no longer yields documents or relationships likely to change the principal judgment.

Do not return directly to retrieval for missing text/figures: obtain them through `fetch_patent` first. Recover only failed items for retryable comparison errors. Reuse an already executed query when there are no new terms, scope or seeds; do not loop.

## 5. Verify decisive facts and form conclusions

Separately verify “not mentioned” findings decisive to a positive novelty conclusion and “necessarily inherent” findings decisive to a negative one.
The Agent actually rereads originals/drawings or recalculates derivations. Save the original judgment, material, rationale and outcome with `method: agent`. Obtain more material, run targeted retrieval or call the existing comparison tool again as needed; this is not an independent review tool.
When facts or evidence change, update affected differences, overall arrangements and conclusions, preserving the original record.

Read [Analysis and reporting requirements](references/report.md) before concluding:

- For inventive step, also read [Target-jurisdiction practice and X/Y evidence audit](references/jurisdiction-practice.md); determine jurisdiction before assigning evidence roles and combination paths.
- For novelty, check whether one date-eligible document completely corresponds to the solution in one arrangement; do not combine documents.
- For inventive step, analyze closest art, actual differences, effects, the objective problem and a complete modification or combination path.
- Ease of modification is not disclosure; a partial teaching does not make the complete solution obvious.
- Label every inventive-step difference as document teaching, evidence-supported common knowledge or engineering inference. Unverified assertions of routine practice/common knowledge cannot provide a decisive bridge to a definite lack-of-inventive-step conclusion.
- A set of documents separately containing parts is not Y evidence. Each numbered Y group identifies primary/secondary documents, differences addressed, jurisdiction-specific teaching/motivation, reasonable expectation of success and obstacles. Incomplete groups remain Y candidates.
- Keep novelty research separate from FTO: date-eligible disclosure affects patentability; claim coverage, validity, jurisdiction and implementation barriers are FTO matters. Unless also requested, record only risk leads without infringement conclusions.
- If decisive evidence remains unresolved, state that assessment of the solution is incomplete. Hit ratios or missing material cannot replace judgment.

## 6. Generate the report and continue existing work

Read [Report data and commands](references/report-data.md) and use the existing template to generate a standalone HTML report. Set `report_data_version: 2` for new reports and reference the candidate ledger. The renderer reconciles it at the final gate. If validation fails, keep the report `partial`. Do not manually reconstruct the final candidate list from the documents fetched.
Retain the complete matrix, originals, actual drawings, Agent checks and search appendices. User templates must retain the same evidence and judgments.
The report scripts require Python 3, `markdown-it-py` and `Pillow`; check dependencies first.

Open the finished report and check conclusions, dates, counts, evidence navigation, images and unresolved issues. Deliver an accessible report file. Briefly state the principal conclusions and decisive evidence in conversation rather than pasting the HTML.

For continuation, first read saved disclosure, features, requests, receipts, checks and reports. Reuse unchanged evidence; update only parts affected by changed input, scope, material or judgment. Distinguish reused work from new work. A previous check cannot be reused when it no longer matches current facts.
