# Strong-evidence Claim Charts

Applies to all/some candidates actually adopted by the user, with no fixed total. Run serial batches ≤10 for local verification, not as an API limit. Display every adopted object under the same original-text/evidence rules regardless of tool judgment or local risk opinion. Other candidates remain “Not included in this CC.” Resolve scope/fulltext choices first; no CC with pending strategy. For fulltext, complete this batch's acquisition/analysis before official CC and evidence review. Claims mode still requires complete claims and necessary interpretive evidence.

## 1. Identify the comparison text

First pass `lifecycle_and_text_gate`: verify target-jurisdiction/date pending or active rights with `patsnap-ip:fetch_patent_lifecycle`, and adopted text with `patsnap-ip:fetch_patent`. Inactive, expired, terminated, withdrawn, abandoned, rejected or revoked/invalidated objects are excluded by default. Unknown status/text blocks CC; do not compare first and verify later. Explicit historical comparisons remain separate from current blocking-risk counts.

Bind product configuration, assessed activity, jurisdiction/date, document/claim numbers, dependencies and adopted text. Use effective granted/post-grant-amended claims for active rights and latest available published/sourced amended claims for pending applications. A publication draft alone is publication-time text and may not be current prosecution text. Check publication/grant/amended versions of the same application. Other family applications, divisionals and continuations are not one claim set. Latest returned text is not automatically applicable.

State whether the comparison baseline is original filing, published application or an amendment. Align by actual text/dependencies, allowing renumbering, splits/merges and dependent limitations incorporated into independent claims. Do not pair by identical numbers alone. Missing baseline permits bounded CC with differences pending.

Reuse confirmed case facts without per-patent questioning. Call `patsnap-ip:build_claim_chart` under the current MCP protocol and inspect actual receipts for analyzed objects, claims, limitations and evidence; do not assume all dependent claims are covered. When requested claims are not covered, perform sourced local review and list gaps. Local interpretation/jurisdiction conditions are not automatically adopted server-side. Hypothetical configurations remain conditional; plans/AI inference are not implementation evidence.

Tool `legal_status` or equivalent simplified codes do not replace jurisdiction/date lifecycle verification. `include_in_report` controls tool-report adoption, not client selection, eligibility or low risk. Tool capability to compare inactive patents does not authorize current blocking-risk CC. Reconcile every submitted object with returns; list nonreturns, unresolved identities, errors and mismatches explicitly.

## 2. Decompose originals before translating

Fixed order: **complete adopted claim original → original units/locations → corresponding translations → interpretive/product evidence → comparison opinions**. Do not draft summaries or translated features first and backfill approximate originals.

1. **Original units:** take continuous complete technical units from one adopted version in claim order. Add only row numbers, layout and highlighting; no word edits, spelling fixes, punctuation replacement, new sentence assembly or ellipses. HTML escaping/display line breaks are permitted with raw source retained. Note suspected typos separately.
   - div/seg containers, paragraphs, line breaks and array entries are transport/layout, not inherently technical units. One may hold multiple limitations; several may form one inseparable relationship.
   - Reconstruct continuous text first, then consider preamble, comprising/wherein/and/or, parallel components, relationships, steps, conditions, numbers and negations. Use FWR and necessary relations as the granularity standard; one div does not justify one row for a whole claim.
   - Returned feature quotes/locations are anchors and omission-check clues. Locate verbatim in the adopted claim or explicitly record failure. Never rewrite originals from feature summaries/translations or pair arrays to rows by position. Record many-to-one/one-to-many/cross-row associations.
   - Fill missing local units from complete originals and label “Not separately identified in official CC.” Over-split official features may map many-to-one without altering text. Container, feature and row counts need not match.
2. **Complete coverage:** represent preamble, body, connectors, numbers/units/materials, negatives, sequence, AND/OR, conditions and dependencies. Discuss whether preamble limits scope; do not delete it first. Dependent claims include inherited limitations through original rows or explicit complete row references. Analyze multiple-dependency branches separately, never synthesizing a new claim. Split meaningful clauses without breaking necessary relationships.
3. **Itemwise translation:** translate locked original units fully into output_language with matching row IDs/locations. Original precedes translation; summaries are not translations. If already in output language, label “Original (same as output language)” without duplication. AI translation is allowed when tool translation is absent, with provenance and unresolved terminology marked pending.
4. **Moderate granularity:** retain enough function/way/result and necessary relationships for judgment. No word-by-word row requirement or forced F/W/R fields per row. FWR is not a substitute for jurisdiction-specific construction/equivalence rules. Component names may be subheadings, not replacements for limitations.

Summaries belong only in labeled overviews, never original/translation cells. Partial excerpts may be delivered as “Selected limitations / partial verification,” not complete CC. Length or lack of a high-risk label does not justify retaining only decisive phrases.

## 3. Review mapping, evidence and interpretation separately

For every row ask how it technically maps, whether evidence supports/conflicts/is insufficient, and what interpretation applies. Keep local states separate from actual tool judgments/evidence; do not rewrite receipts or derive new states mechanically from scores.

### Legal structure only when relevant

Check preambles, open/closed transitions, functional limitations, Markush/Jepson, product-by-process, order and dependencies only insofar as they affect the row/jurisdiction. Do not force every category into ordinary cases or invent authorities.

- Material ambiguity: state conditional branches, e.g. correspondence under X but not Y/pending; reuse adopted interpretations. Not every structural noun is disputed.
- If US §112(f) may apply, examine corresponding structure/material/acts and authority; same function alone is insufficient. Language does not determine jurisdiction.
- Ordinary embodiments do not automatically limit claims. Explicit definitions/disclaimers, supported procedural restrictions and applicable functional construction cannot be dismissed solely because not verbatim in the claim. Missing material limits that issue, not an automatic full litigation investigation.
- Added dependent limitations need actual rows; inherited rows must be complete and readable in expanded/exported views. Separate multiple-dependency branches; an independent claim's stability opinion does not analyze dependent claims.

| Check | Rule |
|---|---|
| Silence/plans/inference | Neither absence nor implementation; insufficient evidence is pending, not exclusion. |
| Support/counterevidence | Check conflict after finding a similar quote. Preserve correspondence/difference quotes, sources and fact nature. Accurate quoting is not independent factual verification. |
| Broad/narrow concepts | A specific product species may meet a broader claim genus; the converse is not assured. Same function does not establish identical scope/mechanism. |
| Inherency | Explain necessity from established facts; common practice/possibility is insufficient. |
| Numbers/ranges/order | Partial overlap only identifies relevant operating conditions. Missing actual values/conditions remain unknown; do not invent sequence. |
| AND/OR/configurations | All necessary conditions must hold in one actual or explicit hypothetical configuration, not assembled from incompatible embodiments. |
| Equivalence | Identify concrete FWR way, differences/substitution evidence and jurisdictional limits. Same purpose is insufficient; unresolved conditions mean candidate equivalence. |
| Row/claim/conclusion | Check inheritance, decisive limitations and labels against prose. Averaged feature scores do not yield legal conclusions. |

Official call success does not pass these checks. An unknown row does not automatically make a patent low risk, nor automatically invalidate a separate decisive, evidenced nonmatch. Where another necessary limitation is decisively unmet and interpretation/equivalence questions are resolved, give a configuration-bounded conclusion while disclosing remaining unknowns.

### Stricter inference-label review

- `IMPLIED`: identify actual frozen product facts making the element logically necessary in the same configuration. Product category, common structures, intended use or “needed for the function” alone becomes product fact unknown.
- `HYPERNYM`: use only when the actual object is an evidenced species of the claim genus, with roles, connections and steps established. Capability is not actual method performance; do not transfer concept relations across components.
- `FUNCTIONAL`/equivalence: check specific way/structure, FWR and target-jurisdiction interpretation, not function/result alone. Without interpretation evidence, retain candidate correspondence rather than complete coverage.
- Numeric status codes, automatic expiry, risk levels and implementation advice are neither product facts nor lifecycle evidence. Preserve originals, but do not adopt them before lifecycle/text/row gates pass.

If a necessary limitation becomes unknown, record `cc_inference_unsupported`. Show the raw whole-claim result separately, without asserting every limitation satisfied, coverage established or definite implementation advice.

### Label–row–conclusion consistency gate

Before adopting any official summary, check whole-patent/claim risk, row statuses and summary text together.

- Medium/high risk alongside “not covered,” “no implementation obstacle” or “free to operate” is `cc_conclusion_conflict`; do not adopt the summary.
- `QUESTIONABLE_RISK`, unknown product facts, unsupported FWR/equivalence or possible/common mislabeled necessary preclude definite exclusion.
- `include_in_report=false`, `risk=false`, similarity or simplified codes cannot cure conflicts.
- An independent local exclusion is permissible only with explicit contrary product evidence for another necessary limitation, resolved construction/equivalence and failure of the complete claim in the same actual configuration. Limit it to configuration, claim and time; retain the raw tool summary unchanged.

Conflicted objects may show originals, full raw results and local issues, but remain conclusion-conflict/pending and outside confirmed-low-risk/free-to-operate counts.

Ordinary gaps/adopted conditional interpretations may remain pending rather than treated as transport failures. Decisive errors such as unknown→absent, unsupported equivalence, invented sequence or label/conclusion conflict require preserving official results, listing local issues and suspending affected conclusions/formal reports. Independent checks and partial review may continue.

Use available official material first. Ask only for customer-held decisive facts/configurations, not mandatory confirmation of every patent decomposition. User preference cannot establish legal effect; unresolved interpretation stays conditional. Gap acceptance does not validate unsupported judgments.

## 4. Four-column table and evidence

Each local row records stable ID, full-text location, complete original unit, translation/provenance, version-change evidence, interpretation/authority, product support/counterevidence/knowledge state, linked rows, opinion and unknowns. Locations may be character intervals or verifiable paragraph/page/sentence references tied to document/claim/version. Join originals/translations by identity, not array position. These are local records, not new MCP fields.

| Column | Content |
|---|---|
| Claim limitation (original/translation) | Row ID/location, complete original and complete translation, with corresponding additions/changes highlighted relative to the application baseline. |
| Description support / claim interpretation basis | Prioritize actual description/prosecution quotes, paragraph numbers, location and purpose; concise adopted conditions; local views labeled “Local interpretation.” If relying only on the claim, say so. Missing external quotes stay unavailable; model common-knowledge reasoning cannot replace original support; detailed branches may expand. |
| Customer implementation | Actual configuration's quote/image location, source and verification state. Supplier-report retellings are not original process facts. |
| Comparison opinion | Correspondence/difference and decisive basis; brief pending-evidence/interpretation/equivalence labels with reasons rather than forced low risk. Put detailed support/counterevidence/FWR/linked rows below. |

Label translation provenance accurately: returned tool machine translation, AI translation/revision, or human translation. Tool output is not certified. Locally revised tool translation gets a revised provenance label with original tool version retained. Originals/translations never overwrite each other; adopted text excludes removed historical wording. If highlighting is unavailable, use separate change notes rather than inserting fake source text.

All headers/instructions/interpretation/change notes/opinions use output_language; clearly labeled originals may differ. Keep four columns, concise opinions and expandable claims/evidence to simplify presentation. Expanded views must actually contain all units/translations/locations, not empty “see appendix” pointers. Print/export retains full content or accessible attachments.

Separate technical mapping, claim-version differences and translation. Unknowns may guide searches but cannot prove absence/coverage. Never combine products/incompatible embodiments. Disclosure/coverage/similarity judgments do not directly yield legal conclusions.

## 5. Change notes below rows

Do not add sprawling label columns or split every word into a row. Add one note per changed unit; full before/after originals/translations/procedure evidence belong in expandable details or located appendices.

| Situation | Note |
|---|---|
| Published application vs grant available | “Application publication → grant: X changed to Y.” Endpoint differences may be verified while dates/reasons remain pending. |
| Grant independent claim adds limitation | If supported: “Grant independent claim incorporates X; application dependent claim N already contained related content.” Do not call it first disclosure/new matter automatically. |
| Actual post-grant text and procedure available | Identify amendment/incorporation/deletion, process/date/source. Separate text date and effective date; retain legal-effect uncertainty. |
| One original missing / event title only | “Change unverified: missing X.” No invented highlights or “unchanged” claims. |

If post-grant procedure was not checked, say so. Verified no-change applies only to the checked unit. Text differences alone do not establish overall broadening/narrowing, rationale or estoppel. Obtain targeted reliable evidence when material rather than defaulting to complete litigation research.

## 6. Delivery checks and reuse

- **Verbatim:** removing highlights, each row matches its source exactly except display whitespace. Check all claim text/order/dependency branches, not approximate meaning.
- **Lossless reconstruction — hard gate:** concatenate original units in order; after display-whitespace normalization, match the complete adopted claim exactly, without omissions/duplicates/reordering. A single row for a multi-limitation HTML container needs a reason why it is indivisible; otherwise decomposition is incomplete.
- **Anchor coverage — hard gate:** map every actual returned quote/location, explicitly recording unresolved/cross-row/not-separately-listed cases. No positional pairing. Unexplained missing anchors allow displaying official CC but strong-evidence status remains pending/incomplete.
- **Translation:** every required unit has a complete matching translation preserving numbers/units/negation/connectors/conditions/references. Material missing/ambiguous translations remain pending.
- **Provenance/language:** originals, translations, versions and quotes are retrievable; labels/prose/opinions agree in language, with foreign text confined to labeled evidence. No reverse-translated invented originals or fabricated interpretation citations.
- Change type/stage/date/reason require evidence; identify opinion producer. Template requirements never justify fabricated material.
- Cover all necessary/inherited limitations or disclose partial scope. Product unknowns are not absence and unverified material is not established correspondence.
- Apply section 3 row checks. Evidence priority is not a certainty score; decisive contradictions suspend adoption.
- Supplement insufficient official CC using actual official text in a labeled local view. Input edits do not prove control over backend claim adoption.
- Failed checks mean incomplete with specific gaps, although verified portions may be shown. Risk labels/page-generation success do not establish complete CC.
- Track official call/business completion separately from strong-evidence review. Official success with missing applicable text/translation/product evidence stays locally pending. Save local four-column/risk views separately before reporting.
- Save the verified adopted row view for direct report reuse, including originals/translations/locations/notes/conditions/opinions. Meaning-changing corrections to configuration, interpretation, translation, text or history require affected rows, inheriting claims and summaries to be reviewed with old opinions retained. Formatting-only changes rerender.
