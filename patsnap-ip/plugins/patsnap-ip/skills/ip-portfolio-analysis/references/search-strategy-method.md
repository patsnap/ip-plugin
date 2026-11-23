# Built-in technical-topic search strategy — P2

Build an auditable, defensible Patsnap strategy: why terms enter, which fields are searched, how recall/precision can be checked and remaining limits. User-supplied syntax/screenshots/examples/history govern the supplied context; verify actual execution against current capabilities. If exact syntax is unknown, use clearly labeled draft field placeholders and state validation is required before production; do not call that draft executable.

## Seven steps

### 1. Clarify only material gaps

Preserve the original request verbatim before interpretation. Establish topic/boundaries, countries/types/status/date/languages, purpose (landscape/monitoring/invalidity/FTO/competition/report), precision/recall expectations, known seed patents/articles/products/standards/companies and whether queries, methodology report or both are required.

### 2. Decompose the topic

Give a concise concept definition and establish shared understanding before formal boundaries. Decompose object/material/component, function/effect/problem, mechanism/process/method, application/product and exclusions. Boundaries require confirmation before execution; a requested complete draft labels every unconfirmed item “Pending user confirmation.” General routing: tech-decomposition-method.md.

### 3. Term matrix before queries

Include Chinese/English, abbreviations, spelling variants, chemical/trade names, broader/narrower and adjacent concepts. Read patsnap-query-rules.md as needed. Expand multidimensionally across object/material, function/effect, mechanism/process, application, product/module, upstream/downstream terms, classes, trade names, abbreviations, foreign variants, seeds and known assignees—not literal synonyms alone.

For chemistry, add representative members, salts/derivatives, structural/process-state terms and structure-related anchors. Broad noisy members require constrained branches. Every major decomposition/search/noise element records confirmation; unconfirmed elements are not final execution scope. Use searchable-fields.md for exact fields.

Model compounds with appropriate proximity/order/sentence/paragraph relations ($Wn/$PREn/$SEN/$PARA), not default flat Boolean lists. Use IPC_LOW/CPC_LOW for subgroup-inclusive parent classes, exact fields only for exact-code intent. Identify cross-domain noise early; verified stable clusters use named class+keyword blocks, not assignee exclusions alone. If misses show systematic translation variants, create a separate strongly constrained language-recall branch; broad “extraction/material” terms cannot stand alone.

### 4. Layered queries

Route as topic, problem-led, assignee or hybrid search. Layers: S0 narrow seed/terminology validation; S1 core title/abstract/claim concepts; S2 recall extensions (synonyms/species/classes/assignees/inventors/citations/seed-derived terms); S3 precision constraints/exclusions/proximity/field choice; S4 final balanced production query with explanation. The SOP's named direct-topic/device-function/class-anchor branches are local branch names; preserve each branch's stated purpose rather than relying on labels alone.

### 5. Execute or prepare

Use search_patent for patent records, search_literature for articles and field_analysis for population statistics under main tool/degradation rules. If only drafting is possible, provide the user's execution checklist and clearly mark unexecuted status; do not simulate real hits.

### 6. Recall/precision guidance

Do not claim validated recall/precision without executed results, labeled samples and independent recall evidence. With supplied misses/samples, use search-validation-checklist.md. Before finalization, classify feedback as stable noise, grouping/logic error, field-scope issue, translation/language gap, classification gap or boundary disagreement; update decomposition/elements/noise/strategy tables and complete queries together.

### 7. Complete search report

Use search-report-template.md: topic, decomposition, search elements, noise elements, strategy table, dedicated query per strategy/noise block, total noise, final combination and expanded executable queries, post-search validation guidance and limitations.

Deliver FINAL_BALANCED_EXPANDED and NOISE_TOTAL_EXPANDED plus FINAL_PRECISION_EXPANDED when exclusions are proposed. Expand every block; `S1 OR S2 OR S3` alone is not executable. Put copy-ready expanded expressions immediately before/after shorthand, not hidden beyond appendices. Only label copy-ready after syntax is established; placeholders remain drafts.

Confirmation checkpoints: original requirement, boundaries, decomposition, elements, noise, strategy, final query. Where execution depends on user approval, stop at the gate until confirmed. “Pending user confirmation” is actionable, not decorative. Explicit complete-draft requests permit all-draft delivery with every unresolved checkpoint labeled, not unapproved execution. Reuse applicable explicit user authorization rather than mechanically re-asking settled choices.

## Principles and final gates

Prefer inspectable concept/proximity blocks over long flat lists. Core expansion must be multidimensional/auditable unless the user explicitly wants narrow quick search. Start high-signal fields and widen when recall evidence warrants. Combine terms/classes/seeds; emerging/cross-domain topics cannot rely solely on IPC/CPC. Assignee clues/filters cannot replace topic search unless competitor-specific scope is explicit.

Preserve false-positive analysis and why exclusions exist. Maintain separate landscape/monitoring/evidence queries when one cannot satisfy all objectives. Name feedback branches such as S_LANGUAGE_RECALL and N_STABLE_INDUSTRY_NOISE. Record exact date/database/unit/manual exclusions.

Before finalization verify:
- Known seeds have a planned/actually evidenced coverage check; no premature coverage claim.
- Expansion dimensions used/skipped are documented.
- Precision sampling method is provided; no rate before labeling.
- Assignees/classes/terms/year patterns are plausible for the topic.
- Frequent noise is addressed or consciously accepted; verified noise uses terms+classes where possible, with assignee exclusions supplemental.
- Misses map to missing concept blocks before adding terms; broad translations stay constrained.
- Final logic can be explained in ordinary language; compounds/relationships use appropriate proximity or an explicit reason not to.
- Parent-class retrieval uses _LOW fields, exact codes use exact intent.
- Full report, not just one query; expanded blocks contain no unresolved S1/S2/N1 symbols.
- Original requirements remain verbatim; confirmed scope differs from inference/pending assumptions.
- Boundary→decomposition→elements→strategy→execution gates are respected under actual authorization; draft permission is not execution permission.
- Language/database/syntax/emerging-terminology limits are explicit.

Supporting files: patsnap-query-rules.md (syntax), searchable-fields.md (field codes/types/examples), tech-decomposition-method.md (routing), search-report-template.md (delivery), search-validation-checklist.md (sample/iteration checks).
