# Step 5 — Query iteration

Read only when enabled; default simplified mode skips this step. Use `patsnap-ip:search_patent`/`patsnap-ip:fetch_patent` for evidence; fixed sampling, coverage and missed-hit diagnosis are local, not returned tool fields.

Step 4 feature grouping, plan/expression checks, initial execution and bounded corrections remain mandatory where applicable even when this optional step is skipped. Freeze query-plan and branch provenance so local corrections preserve other adopted risk directions.

Reuse T/L/P/C/LS. Q0 is the adopted starting technical Boolean; Q=Q0. Save jurisdiction, legal-status and date scope separately as frozen `SEARCH_FILTERS`. Keep candidates separate from adopted queries.

All following Boolean + `SEARCH_FILTERS` steps require explicit runtime support for their combination and receipts proving filters effective. If Boolean is exclusive, filters are ignored or the result is an uneditable opaque reference, record `blocked_boolean_scope_unsupported`; do not run 5.1–5.7 and fabricate same-scope metrics. Retain unrestricted Boolean diagnosis separately from scoped semantic/keyword quality checks; they do not share S/U/H metrics. Sample initialization is also blocked if Boolean cannot execute within the same scope. Never edit opaque references to add scope.

## 5.0 Initialize one fixed sample

Under current search definitions, create one independent semantic sample from P with the same `SEARCH_FILTERS` as Q0, no family collapse, at most 200 publications under actual pagination capability. Scope includes all adopted authorities/statuses/dates; do not omit unsupported conditions. If structured filters cannot express equivalent scope, stop with the specific gap rather than evaluating against a broader sample.

Save requests/receipts, exact ID-to-PN mapping, order, time and scope. S is this fixed publication set; never resample to improve metrics. Unresolved identities, partial paging failure, inconsistent counts or fewer than ten samples stop optimization. Users may choose repair or explicitly skip and retain Q0. This is a semantic-search window, not a human-labeled relevance gold standard.

## 5.1 Initial metrics (round 0)

Construct a sample restriction using verified publication-number Boolean fields with full country/kind codes. Pass frozen `SEARCH_FILTERS` for every Boolean evaluation and execute:

- `SEARCH_FILTERS` intersected with sample restriction → reachable set U.
- Complete Q intersected with sample restriction → hit set H.
- Complete Q alone → available total N.

Sample restrictions are for evaluation only, never final Q or `SEARCH_FILTERS`. Do not concatenate opaque builder handles. If valid sample restrictions cannot be constructed, stop. Retrieve complete intersections within runtime query-length/page limits; if needed, split into disjoint PN batches, verify identities and merge all batches. Sample-query totals are not N.

Compute `coverage=100×|H|/|U|`, misses `U−H` locally. Require H⊆U⊆S, all batches complete and nonempty U. Partial failures/unresolved identities invalidate the metric. Retry a side-effect-free read once, then stop; failed batches do not supply zeroes.

Save sets, formula, provenance and calculation time. Label “fixed semantic-sample coverage,” not true database recall or legal-risk coverage. Assess query breadth locally from actual technical conditions and N, with reasons; do not invent a tool breadth label.

## 5.2 Convergence and stopping

Stop the main loop after a valid evaluation meets any condition:

- Coverage ≥85% and evidence-based local checks find no overly narrow query.
- Two consecutive valid rounds show no increase.
- Five main query-change attempts are reached.

85 is a working sample threshold, not proof of full recall. Every edit, syntax correction and rejected candidate counts toward five; read retries cannot become unlimited optimization. Partial failures are not valid rounds and cannot justify further changes. Window/workload checks remain independent even after coverage passes.

If the target is unmet, show actual metrics/gaps and let the user accept the current state or revise input. Do not assume remaining misses are legitimate exclusions. Finalization uses only the last adopted, validly evaluated query.

## 5.3 Diagnose misses

Use `patsnap-ip:fetch_patent` on at most ten valid misses to check actual titles, abstracts, classifications and necessary text. Diagnose terminology/fields/relationships/omissions locally. Test supported clauses only within the same `SEARCH_FILTERS` and missed set, recording actual queries/hits.

`SEARCH_FILTERS` cannot be relaxed as technical conditions. A blocking clause is a diagnostic clue, not proof that the patent should be retrieved. Without misses/evidence, do not invent edits; missing fields are unknown.

## 5.4 Candidate rewrite

Change one supported clause/variable; field edits and synonyms take separate rounds. Preserve `SEARCH_FILTERS`; scope changes are not technical Boolean optimization. Where domain terms are mandatory, check relevant classification OR fallbacks. Do not promote product names, active ingredients or exploratory alternatives to mandatory AND conditions without basis.

Save complete before/after queries and rationale; Qcandidate does not overwrite Q. Do not reverse-engineer evaluation queries from answer keys or known missed titles; label such runs diagnostic experiments, not independent validation.

## 5.5 Execute and check fixed scope

Under main Step 4, locally verify parentheses, language and technical logic, then execute Qcandidate with Boolean and the same `SEARCH_FILTERS` through `patsnap-ip:search_patent`. Only successful, scope-preserving candidates proceed to evaluation. Do not invent auto-repair/validity fields. Preserve errors; failed candidates do not replace adopted Q. Syntax fixes still consume attempts.

## 5.6 Evaluate and adopt

Repeat 5.1 with identical S/`SEARCH_FILTERS` and the candidate. Unexpected U changes require reachability checks, not a new denominator to fake improvement. Stop if comparability cannot be restored. Once valid, record query/sets/N/reasons and decide adoption; do not automatically adopt lower coverage or distorted scope. Update Q/N/metrics only when adopted, then return to 5.2. Failures preserve valid records.

## 5.7 Final recall expansion (once at most)

If valid misses remain, retrieve actual details for at most 15 and identify supported terminology gaps from titles/abstracts/classifications/necessary text. No evidence means no expansion.

With a clear blind spot, create one supplementary candidate using technical `B OR supplementary_technical_conditions` and execute with the same `SEARCH_FILTERS`. Do not put scope fields into the Boolean or relax adopted scope.

Apply 5.5/5.6 again. Failure does not replace adopted Q; disclose the gap and stop without a new loop.

## Deliverables

Show rounds, complete-query references, edit reasons, actual total hits, local sample coverage, validity and adoption. Include S/U/H sizes/provenance, final Q/N, stop reason and unresolved gaps. If the target is unmet and no acceptance is recorded, do not automatically start Screening.

Attach final executable query, real search receipts and local iteration history; local history is not a tool-returned field.
