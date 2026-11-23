# Ten-stage execution SOP

P1–P10 are workflow phases; Chapters 01–13 are report sections. Keep numbering distinct. Sequence: boundaries → strategy → retrieval → competitors → own portfolio → industry/literature → mining → design-around → matrix/clusters → HTML.

## P1 — Boundaries and decomposition

Retain the request verbatim. Define topic with broader/narrower concepts, evidenced application exclusions, target/confirmed affiliate names and relevant competitors/supply-chain roles. Build a topic-specific tree and Chinese/English/abbreviation/trade-name vocabulary. Use object, structure/material, mechanism, control, integration and validation only where relevant; no mandatory six modules, energy or drivetrain branches. Each node maps to a user objective/evidence.

Gate: engineering names without IPC; justified exclusions rather than count control; all known in-scope aliases; relevant roles/inapplicability explained; vocabulary coverage including broader/narrower terms. Avoid class codes as tree labels and missed confirmed subsidiaries/institutes, without claiming a complete group tree.

## P2 — Strategy

Read search-strategy-method.md. Build nine concept blocks with Chinese/English/abbreviation/trade terms and class anchors confined to query material. Identify at least five noise categories where supported, each with terms/treatment/N query; do not invent exclusions solely to fill categories. Construct S0 seed terminology checks (200–500 is an indicative planning range, not invented results), S1 direct-topic, S2 device/function and S3 class-anchor routes. Deliver FINAL_BALANCED_EXPANDED, NOISE_TOTAL_EXPANDED and FINAL_PRECISION_EXPANDED, with all concepts expanded and actual supported syntax.

Illustrative structure only, requiring real terms and syntax checks:

```text
(topic_terms AND function_terms)
OR (device_terms AND function_terms)
OR ((IPC_LOW:verified_code_1 OR IPC_LOW:verified_code_2) AND constrained_terms)
```

Gate: object/function/mechanism/application/product/class dimensions covered; noise categories justified; no unresolved S1/N1/term placeholders in executable delivery; proximity such as $W/$SEN where needed, not flat AND; IPC_LOW for subgroup-inclusive intent. Do not label shorthand/pseudocode executable or omit the required expanded noise expression.

## P3 — Comprehensive retrieval

Use search_patent for details and field_analysis for population totals under the canonical scope. Execute balanced query/global baseline, each adopted competitor/supplier assignee route, and target plus only confirmed affiliates. Save date/database version.

Every table identifies publication/application unit; family relationships do not change counts. Separate global/CN. Note recent-two-year publication lag and possible incompleteness. Gate: date, adopted identities/affiliate gaps, geography and applicable roles recorded; partial-role rankings disclose included/excluded roles. Never call selected-company ranks industry-wide or compare mismatched geographies.

## P4 — Competitive landscape

Use field_analysis supported dimensions for trends/ranks/distributions; search/fetch representative records. Apply missing-capability rules. Produce project-scope filing trends (filing/grant dates distinct), Top 10–15 assignee bars sorted ascending programmatically, annual competitor comparison, per-company focus with representatives, and module comparison tied to the tree. Insufficient data means no density map.

Identify direct competitors, suppliers, technology providers and relevant roles by evidence, not fixed OEM/Tier-1 quotas. Automotive may use those roles; other sectors use their own. Missing/inapplicable roles are disclosed, not fabricated.

Gate: ascending bars, relevant supply-chain coverage, representative identities/status/evidence without padding. No recent records means “No recent filings found within this scope,” not business exit; consider publication lag/entity coverage. Activity needs comparable trends and is not automatically threat. Include evidenced early pioneers even when many older rights expired.

## P5 — Own portfolio

Search target/confirmed affiliates, then individually verify current status via fetch and relevant lifecycle events for changes/fees/lapse reasons; never estimate. Classify by adopted tree. Highlight active key patents with application/date/technical point and important inactive patents with evidenced reasons (fees/rejection/abandonment, otherwise unknown).

Status interpretation uses actual current definitions: active/granted with applicable term, pending/examination, inactive/expired/abandoned. Resolve contradictions with events/date; filing age or long examination does not prove withdrawal.

Gate: chosen unit, same-application-only publication merging, individual status verification, no zero pie slices, active/total rate reconciled, supported lapse reasons. CN/WO/US publications are three publications, not automatically three independent technical inventions.

## P6 — Industry and literature

Aim for at least four relevant policy/regulatory items and two applicable standards (ISO/GB/SAE as relevant), each with portfolio implications. Actual evidence controls counts; retain gaps rather than padding. Without original/version, mark standards unverified; article mentions do not prove currency.

Aim for six relevant articles through actual search_literature/fetch_literature; inspect schemas, no patent Boolean strategy. Actual data.docs[].id becomes paper_id. Use returned/verified title/year/authors/affiliations/journal/citations only; missing fields do not authorize invented tools/statistics. Each article gives title/year/core point/innovation implications, including existing public knowledge. Produce a known-directions list to prevent recommending already-known concepts as new.

Gate: policy/standard impacts, actual article sources and known directions, with count/data gaps explicit.

## P7 — Four-block/ten-step mining

Read mining-method.md. Show CP-0 type/mode/entity/bottlenecks/technical lines, reusing P1–P6 scope and continuous authorization; wait only for decisive missing choices. Blocks: decomposition (scan/decompose), concepts (prioritized problems/solutions), evaluation (prior art/differentiation/conditional risk/design-around/refinement), dispositions (roadmap only requested).

Evaluate technical differentiation/overlap, legal scope/stability and market value/barriers. Dispositions: prepare filing only with reproducible design, prior-art comparison, evidenced differences/effects and no decisive gap; refine; incubate; trade secret; abandon. No grant guarantees.

For P0, identify improving/worsening parameters among TRIZ's 39, consult the contradiction matrix, identify principles and convert to concrete domain solutions. Gate: CP-0 scope/authorization, no IPC in business prose, all P0 TRIZ work, every disposition, and nonpatent as well as patent evidence.

## P8 — High-risk design-around

Read design-around-method.md. For each evidence-confirmed blocker examine applicability of all four strategies: substitution (different implementation), combination (integrate features), decomposition (cooperating subfeatures), removal (transfer function elsewhere). Mark inapplicable strategies with reasons.

Output patent/application/title/assignee/status, independent-claim core limitations, strategy alternatives/recommendation, original→new feature, expected effects and evidenced new-patent opportunity. State configuration/claims/effect-cost validation/unknowns. Without comparison/validation, say candidate design-around, not successfully avoided or superior.

Gate: four applicability checks per blocker, evidence for new opportunities without quotas, and permission to recommend redesign without filing, further evidence or abandonment based on performance/cost.

## P9 — Matrix and clusters

Use the single matrix definition in layout-report-method.md: technical category/direction, type, existing coverage, future actions, evidence status, strategy, verified existing and proposed filing regions. Symbols describe existing coverage only. Present all five spaces in order; unsupported spaces remain pending.

Clusters follow cluster-spec.md: overall three-box/arrow overview distinguished by color; existing/proposed status tree; detailed patent cards with application/3–4 technical features/abstract drawing or labeled SVG. Adapt actual clusters to evidence rather than inventing them to fit layout.

Gate: all five spaces, separate geographic columns, counts consistent with cover/conclusions, feature descriptions and appropriate figures; distinguish proposed/verified items.

## P10 — HTML and iteration

Follow html-spec.md. Mandatory checks:
1. Reconcile every repeated number across cover cards, conclusions, charts and detail tables.
2. Every sidebar href has an actual section ID.
3. IPC/CPC codes occur only in the search appendix.
4. Fetch media clues, actually read/check image/document identity; use labeled analytical SVG if originals are unavailable, never a fake original.
5. Trace every number/unit; estimates retain source/formula/assumptions/uncertainty. Unsupported numbers are removed or unavailable, not replaced with spurious precision. Verify statistics/individual/deep-reading coverage under layout-report-method.md; complete chapters are not complete work.

Check used CSS and initial scroll-spy activation (`cur = sections[0]`). Render/inspect relevant layouts and iterate on actual defects.
