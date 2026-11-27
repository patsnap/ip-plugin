---
name: competitive-patent-analysis
description: "Use when analyzing one company's strongest technology directions and representative patents. Confirm the company and its subsidiaries, verify patent families where data permits, explain each selected patent, and deliver an HTML report. Does not replace FTO research."
---

# Competitive Patent Analysis

Turn company and technology clues into a shareable technology/patent assessment. Follow the six-step workflow and its gates for technical-area confirmation and counting checks.

## Applicability

**Objective:** Research one company or group’s existing technical strengths, technology routes and portfolio evolution, explaining links between platforms, product improvements and representative patents. Input may be a company name with optional product/technology clues; display and confirm the specific areas at Gate A.

**Deliverables:** Representative patents organized by area, individual interpretations and an integrated HTML assessment. The user need not explicitly request HTML.

**Exclusions:** Tasks primarily planning our future filing portfolio or designing new technical proposals, novelty/patentability judgments, FTO infringement analysis, office-action responses and multi-company patent-metric comparisons.

Decide by the actual research objective when users mention “our R&D” or “portfolio”; researching one company’s existing technologies remains in scope. Separately address additional purchase-value, training or product-benchmarking requests using evidence, without changing the main deliverable or its confirmation requirements.

## Tools and language

Choose and connect tools by the steps below; runtime definitions govern full parameters and response structures. Verify company, product, industry and standards information using user material and available web search/read capabilities. Disclose capability/evidence limits; do not fabricate data or treat abstracts, samples or links as full evidence.

Default to English for dialogue, reports, templates and labels; honor an explicit requested output language. Preserve original evidence with translations as needed. Search language is independent of output language; keep useful Chinese/original-language search terms. Set HTML `lang` to the actual output language.

## Gates

### Gate A — Confirm technical strengths (blocking)

After identifying candidate areas, show the list and obtain confirmation before any patent search:

```text
Based on your input and public information, I propose these N technical strengths:
1. {Area} ({one-sentence technical core}) — strategic role: {physical foundation / licensing barrier / commercial moat}
2. ...
{Where evidence for a layer is insufficient: name the gap and the second area from another layer used instead.}
Shall I search patents for this list? You can add, remove or adjust areas.
```

Do not call patent search before confirmation. If the initial prompt names areas A/B/C, present those as the candidate list for confirmation; do not omit the display.

### Gate B — Integrity of counting conventions (blocking)

- Technology areas use independent Boolean queries whose result sets may overlap.
- Never sum area `matched_total` values or turn them into pies, stacked charts, shares or a “technology distribution.”
- Distribution charts may use only IPC/CPC facets over the same result set, or deduplicated manually classified results; state the convention in the caption.
- For trends, rankings or classification aggregation use `field_analysis`. Pass the already executed, scope-verified Boolean expression in `source.query`, retaining `ALL_AN`; opaque builder references are not aggregation inputs. Combine required supported dimensions in one `dimensions` request for the same dataset, rather than calling separately for each dimension. Present returned `display_rows` before interpretation. Check `source_resolution.query`, hit scope and `warnings`, disclose truncation/classification overlap, and do not sum buckets as a deduplicated total. Explain unsupported dimensions rather than guessing fields. Internal tool labels in responses are not new callable names.
- End with “Search notes” explaining independent overlapping queries, `matched_total` as hits within that query's scope rather than deduplicated classes, and technical descriptions as assessments rather than claim construction.

### Gate C — Delivery completeness

Do not claim completion without a company introduction, a technical card and patent table for each area, a technical description per patent, a comparative assessment table and search notes. Every representative table must retain “Assessed value” and “Jurisdictional coverage,” with `matched_total`, `returned_count`, `independent_family_count`, `eligible_family_count` and `listed_count` disclosed below it.

## Step 1 — Research the company and technical domain

1. Read supplied background/product/technical material first. If identity is unresolved, use `get_standard_assignee_name(query=company_name)`; use `get_corptree_hierarchy(company_id=confirmed_id)` only when parent/root relationships are needed. Actual responses support names, aliases and directly linked assignees, not a complete company profile, product specifications, certifications or full group membership. Extract founding year, headquarters, technology origins, models, milestones and specifications from materials with provenance/verification status. Check official/authoritative web sources when available, recording dates; otherwise mark not independently verified.
2. Use the user's product names and technical clues as search anchors; do not replace them with guesses.
3. Prepare 6–8 company `profile-grid` key/value facts. Retain company and product/milestone fields; missing data is “To be verified” with source limits, never invented to fill cards. User material is evidence of its statements, not independent patent-tool verification.
4. If only a company name is available and no areas can be supported, ask for product/technology clues or necessary material while continuing identity checks. Do not infer strengths from the name or bypass Gate A through patent search, aggregation or FTO tools.

Check company and assignee match states separately and retain evidence. `resolved` identifies the first match and may still include alternatives; `ambiguous` does not authorize selecting the first. Use `company_id` for corporate relationships and confirmed `ans_id`/directly linked `ans_ids` to verify assignee identity; do not interchange them or automatically include group assignees. Build the search restriction with verified assignee names in `ALL_AN`, following Step 3. Relationship-tool `patent_signal.patent_count` is not the search baseline.

Before company analysis, establish whether the subject is a single company or a group. Reuse explicit scope; confirm ambiguity together with Gate A. List actually included standardized assignee names and entities, checking user-named subsidiaries. Relationship tools do not return a complete subsidiary list; roots/directly linked assignees are not the whole group. Disclose covered entities and gaps when incomplete, without calling a single-company search a group total.

## Step 2 — Identify technical strengths

1. Default to three areas, or the user's requested count. Each must map to concrete engineering, be searchable by patent keywords, and differ in mechanism or product role.
2. Default narrative uses one area from each strategic layer:
   - Physical/manufacturing foundation: the structure/process enabling the product.
   - Regulatory licensing/certification barrier: differentiated conditions for lawful commercial use. In less-regulated sectors, standards, compulsory certification, market-entry qualifications or customer certification may apply, with evidence.
   - Commercial moat: product families, application coupling and system integration.
   Mark unsupported layers “Not applicable” or “Insufficient evidence,” replacing them with another area from a supported layer and labeling that layer. Do not invent barriers/moats to fill the structure. Classify user-specified areas by evidence without changing them.
3. For each area, state technical core, product role, candidate evidence and strength assessment. Identify whether it came from the user, public evidence or this analysis. Support strength with technical differences, product role or sustained investment. Representative patents alone establish relevance, not leadership, licensing barriers or moats.
4. Proceed to Gate A.

## Step 3 — Search patents by area

Run an independent search for each confirmed area:

1. Use Boolean search for baseline, area and expansion queries: `search_patent` with `search_strategy=["boolean"]`, `boolean_query` and explicit `ALL_AN` assignee scope. Do not mix strategies or supply `semantic_query`, `keywords`, `filters`, `domain_filters`, or a non-general domain. Execute existing executable queries directly. For construction, term expansion or translation, send complete natural-language intent to `build_patent_boolean_query`, specifying `ALL_AN` and confirmed scope. Check fields, phrases and logic in `data.reference_query`; pass the returned opaque `data.boolean_query` unchanged to search. Save both, without decoding, concatenating or editing the reference. Correct mismatched intent and regenerate; the builder is not a validator for existing queries. Do not add unconfirmed dates, jurisdictions or statuses; implement explicit restrictions in the Boolean.
2. First obtain a baseline for the confirmed entity scope as the first “Search baseline” row. Use `ALL_AN:("Verified assignee name A" OR "Verified assignee name B")` (illustrative; substitute actual names within the confirmed scope). Do not substitute company names in technical keywords or put internal company/assignee IDs in place of names. Retain the executed query and identity evidence; keep the same `ALL_AN` scope across the baseline, area queries and expansions. Similar names alone do not justify including another company. Confirm only actual identity ambiguity, not merely because a parameter needs an explicit value.
   `ALL_AN` covers current, original and historical assignee fields; hits do not establish current ownership or complete group coverage. Label the baseline as hits within that assignee-query scope. For representatives, reuse current/original assignees from `fetch_patent` to verify association; resolve differences rather than excluding solely because search summaries show a different current assignee. For current holding, transfers or legal-status conclusions, supplement with `fetch_patent_lifecycle` as needed and disclose unverified gaps.
3. Query structure: `ALL_AN:(confirmed assignee name group) AND area keyword group` (OR-expanded Chinese/English terms, abbreviations and synonyms), covering components, mechanisms, industry abbreviations and upstream/downstream processes. Technical fields and the complete expression must follow runtime Boolean syntax. Preserve the original `ALL_AN` restriction when expanding technical terms.
4. Retrieve the pool within runtime pagination limits with explicit `collapse_family=false`; search folding is not verified simple-family deduplication. Check `status`, errors and notices before reading documents, `data.total_hits` and `data.returned_count`; failure is not zero hits. Merge pages by exact document identity and record actual windows. If limits prevent complete retrieval, label family counts “independent families within the returned sample,” never full-query family totals. Ten is a listing cap per area; see `references/report-spec.md`.
5. **Deduplicate simple families before representative selection.** Search currently has no directly usable simple-family identifier. For missing relationship evidence call `fetch_patent(patent_id=returned_id, include=["relations"], format="json")` individually; it accepts one patent per call, not an ID array. Group actual members from `response.relations.simple_family`, retaining one representative, preferably granted with broad jurisdictional coverage. Save document-to-family evidence and reuse bibliography, claims and descriptions returned together. Empty relationship arrays or arrays without declared completeness do not establish singleton families. Do not request members again when existing evidence suffices. On relationship failure/authentication requirements retain retrieved documents/errors and stop family-dependent complete counts/final selection. Ordinary full text may be read independently but cannot replace relationships. Mark unverified identities pending and deliver interim results only; titles, equal valuations and shared assignees do not establish families.
6. Review relevance within independent families, then select up to ten eligible representatives under the count tiers in `references/report-spec.md`. Never borrow across areas, relax assignees, lower relevance or add family siblings to meet a count.
7. Distinguish all five counts. Read `matched_total` from that area query’s `data.total_hits`, meaning query hits only. Report `returned_count` as that query’s actually retrieved, document-deduplicated pool, retaining each page’s `data.returned_count`. The last three counts are local calculations from actual records. After expansion retain hits/provenance per query; for a unified hit total execute a scope-consistent merged Boolean. Do not mix one round’s total with a multi-round union or sum page/expansion totals. Missing values are `—`.
8. Preserve raw `independent_family_count`, relevance-qualified `eligible_family_count` and actual `listed_count`. Unknown/weak relevance is not eligible; raw hits/families cannot force table filling. Follow the reference for zero results.
9. Collect value and jurisdiction data before writing tables:
   - `search_patent` and `fetch_patent` do not return monetary valuations. If another discovered, available valuation tool exists, first verify its definition, exact identity, units and valuation scope before using it as a supplementary source; another connection does not prove this plugin has bound that capability. Without an actual source use `—` and disclose the gap, never zero or an inferred amount.
   - Reuse actual `response.relations.simple_family` members from `fetch_patent`. Inspect actual member structures/completeness rather than assuming fields. Count genuine jurisdictions/publication prefixes; simple families only. Extended families and member counts cannot substitute for jurisdiction counts. Label EP/WO as regional/international offices.
   - Disclose partial/missing membership; unverifiable coverage is `—`. If deduplication cannot be completed, mark counts unverified and deliver a bounded interim report, without complete-count formulas, false zeroes or completion claims.
   - If valuations exist, verify units and document/family scope; do not assume batch capability or five-dimensional scores.

## Step 4 — Write individual technical descriptions

Reuse bibliography, claims and descriptions obtained in Step 3 first. Record actual source locations for each description and assessment. Check relevant claims/descriptions for protected objects, component relationships and mechanisms; limit statements and disclose gaps when evidence is insufficient. `technical_problem`, `technical_solution` and `technical_effect` are analytical aids, not source quotations. Abstracts/summaries are not claim-scope interpretation.

Below every title, add one italic technical sentence, normally 20–50 English words or 12–60 Chinese characters (use comparable information density for other requested languages). Never omit it or use generic filler. It must include:

1. Protected object: specific structure, mechanism or system level.
2. Technical feature: concrete operating principle/construction, e.g. gravity, density difference, membrane separation or grid topology.
3. Technical relevance: role in the area's strength, commercialization scenario or certification step.

Read `references/description-writing.md` before drafting for templates, layer-specific examples and prohibited claims.

## Step 5 — Comparative assessment

1. Compare: Technology area | Strategic role | Core representative families | Patent date span.
2. Create evidence-based conclusion cards, e.g. most active area over the last three application years, competitive benchmarks from highly cited foundational patents, and product-family signals from families directly linked to models.
3. Anchor every conclusion in specific patent numbers or family names; avoid generalities.
4. Explain each area’s technical implementation and significance from obtained patent evidence. The integrated assessment explains observed portfolio characteristics or changes, rather than only charts or one or two generic sentences. Disclose insufficient evidence instead of inventing causes to add length.

## Step 6 — Generate HTML

1. Read/reuse `assets/report_template.html`. Materialize it into the task's `reports/` folder if supported, otherwise copy/edit it with available tools.
2. Fill its structure using native patch or incremental writing tools. Localize fixed labels for the requested output language while preserving sections, columns and styles. Do not create a temporary Python/JavaScript program embedding the entire HTML merely to generate the report. Verify all placeholders are replaced and each patent row matches its header cell count.
3. Save `reports/{company_slug}_patent_report.html`, unless the task specifies another output directory.
4. Fixed order: header → company introduction → search baseline → confirmed number of technology sections → comparative assessment → search notes → footer.
5. Deliver a host-supported clickable file link or actual returned artifact handle plus a section-structure table; never invent a handle.
6. Check entity names, count labels and source navigation. Use readable company/assignee names rather than internal IDs. State whether counts represent publications, simple families or representative patents, and identify sample scope separately. Provide actual source links for company, patent, search-result or SaaS destination pages when available; otherwise disclose absence rather than constructing URLs. See `references/report-spec.md`.

## Guardrails

- Query hits and aggregation counts come from actual receipts; document deduplication, simple/eligible-family and listing counts are local calculations over sourced records. Preserve calculation evidence; never estimate or add cross-query hit totals.
- Copy publication numbers, publication dates and legal status from responses; missing values are `—`, never blank/guessed. Citation counts are not default table fields unless requested.
- Use complete traceable URLs returned by tools, never constructed links. Without a URL, show the number and “Details link unavailable.”
- State that technical descriptions are assessments, not conclusions about claim scope.
- Company certifications/milestones/specifications need sources and dates. Label unverified user assertions “According to user materials; not independently verified.” Patent disclosure does not prove product launch/certification.
- Preserve the user's removal of any chart/section across revisions.
- Use “simple-family deduplication” in reports; do not use the label `INPADOC`.
- Ten representatives is a cap, not a completion threshold. If fewer eligible families remain after expansion, list the actual number, even one. Never lower relevance, borrow across areas, broaden assignees, list siblings or hide an area to pad results.
- For 0–4 eligible families, perform the three expansion tiers, then report honestly without returning to Gate A merely because the count is low. Retain zero-result sections and explain evidence gaps; return to Gate A only to change confirmed areas/scope.
- Retain value and coverage columns even if entirely missing. Missing tools/data mean `—` with reasons; PCT-stage records are not zero-valued.
- Label values as simple-family level only when the actual source confirms that scope. Equal values do not prove family identity.
- Never rank/select solely by valuation. Family size may inflate market-related value without technical influence. Relevance is the entry criterion; use available citations, rights status, family coverage and text for disclosed qualitative value assessment when monetary data is absent. Do not convert these to money or invented scores.
- Below each table disclose all five counts, marking unknowns `—` with reasons. Limit family counts to retrieved samples unless all results were fetched; disclose expansion and outcomes when fewer than ten are eligible.
