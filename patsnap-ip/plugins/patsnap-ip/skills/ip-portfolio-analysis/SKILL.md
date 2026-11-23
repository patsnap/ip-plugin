---
name: ip-portfolio-analysis
description: "Use when planning patent protection for a defined project. Analyze portfolios, competitors and technical spaces using explicit dates and jurisdictions; produce a layout matrix and evidence-backed recommendations. Proposed workflow; apply the local MC/Skill/ip-portfolio-analysis execution contract. Runtime binding and channel availability remain unverified."
---

# Patent Portfolio Analysis

## Overview, tools and language

A complete SOP, quality gates, error prevention and output contract for HTML portfolio reports suitable for technical review. Four methods are provided by references within this directory. Use available patent/literature tools and disclose missing capabilities. Read [tool usage](references/tool-usage.md) for handoffs/counting/evidence; runtime schemas govern parameters/results. Verify company/product/industry/standards facts from user/available web material, not invented data, abstracts-as-fulltext, samples-as-populations or unread links.

## Applicability

**Objective:** Plan future portfolios for a target company or R&D project, using own coverage, competitive and industry evidence to determine technical gaps to strengthen, patent combinations, filing priorities and target countries, and deliver portfolio analysis with HTML.

**Scenarios:** New R&D or annual portfolio planning; competitive landscape, threat and own-portfolio health analysis for portfolio decisions; invention mining, design-around, matrices and cluster design within that planning; and technical-review material based on these analyses.

**Exclusions:** Only interpreting one competitor’s existing technology or producing standalone new technical proposals. Competitive research, mining and design-around serve portfolio decisions within this workflow and do not change its main deliverable.

| Input | Requirement/default |
|---|---|
| Technical topic | Required; ask once if absent. |
| Target company | Required; ask once if absent. |
| Competitors | Recommended; otherwise identify relevant direct competitors, key suppliers and other supply-chain roles for the industry. |
| Objective | Portfolio advice + technical-review report. |
| Time | All available data, emphasis on the last ten years. |
| Geography | Global totals + detailed China analysis. |

Once the technical topic and target company are known, organize requirements and technical boundaries. Do not require users to supply their own patent inventory, technical tree or portfolio matrix. Confirm scope and strategy at P2 before search; record extra monitoring or validation plans separately.

**Confirmation rules:** Confirm P2 boundaries, decomposition, elements, noise, strategy and queries stage by stage under the built-in search method and report template. Apply the built-in mining method to P7 CP-0 and deep-mode key choices. A generic analysis/report request does not confirm these specific contents. Reuse explicit confirmations and applicable continuous authorization with their scope recorded; self-checks do not replace user confirmation, and pending contents are not approved execution inputs.

Default all authored dialogue, reports, templates, headings and chart labels to English; honor explicit output-language requests. Preserve source originals and verbatim user requirements with labeled translations where needed. Search languages, country scope and source identifiers remain independent; English localization does not change China/global scope. Set HTML lang accordingly.

## Principles

1. Trace every count to query/unit. Disclose population statistics, individual checks and deep-reading coverage separately. Estimates need sources/formula/assumptions; missing is unavailable, not fabricated precision.
2. Lock conventions under references/layout-report-method.md. Every table states publication/application unit; comparisons share units/scope. Application deduplication is not family deduplication.
3. Keep IPC/CPC codes out of business prose, trees and matrices; allow them only in the search appendix with meanings.
4. Use built-in search-strategy-method, mining-method, design-around-method and layout-report-method, supported by ppt-output-spec/data-fields.
5. Final HTML has no unresolved placeholders, example content or “to fill” text; genuine evidence gaps must be explicit findings, not unfilled templates.

## Ten-stage SOP

P1–P10 always mean execution phases; Chapters 01–13 mean report sections. Never interchange them. Details: references/sop-phases.md.

| Phase | Work | Output / method |
|---|---|---|
| P1 | Boundaries/decomposition | Tree, keywords, exclusions; layout-report-method |
| P2 | Search strategy | S0/S1/S2/S3, NOISE and expanded FINAL; search-strategy-method |
| P3 | Comprehensive patent search | Publication-level data and competitor counts; search_patent/field_analysis |
| P4 | Competitive landscape | Trends, assignee ranks, focus; field_analysis |
| P5 | Own portfolio | Individual module/status checks; fetch_patent/lifecycle |
| P6 | Industry/nonpatent evidence | Policies/standards and article influence; literature tools/available sources |
| P7 | Invention mining | CP-0, Blocks 1–3, innovation list; mining-method |
| P8 | Design-around | Four strategies for high-risk patents; design-around-method |
| P9 | Matrix/clusters | Existing coverage, plans and evidence separate; layout-report-method/cluster-spec |
| P10 | HTML and iteration | Traceable, code-free business prose, no placeholders; html-spec/quality-gates |

## Required 13 chapters

1. Cover and 3–5 key conclusions.
2. Technical decomposition: tree/keywords.
3. Industry developments/nonpatent literature.
4. Comprehensive competitor landscape: trends/ranks/focus.
5. Key suppliers/supply-chain roles chosen by relevance; explain inapplicability.
6. Own portfolio: individually verified modules/status.
7. Deep analysis of 3–5 key frontier/high-value patents where evidenced.
8. All five technical spaces.
9. High-risk design-around: four strategies.
10. Complete innovation list: three-dimensional assessment, TRIZ and dispositions.
11. Portfolio matrix: eight columns for category/direction, patent type, existing coverage, future action, evidence status, strategy, verified existing-rights regions and proposed filing regions.
12. Existing/proposed clusters with original abstract drawings or labeled SVG illustrations.
13. Appendix: complete executable queries.

Prohibited: unsourced numbers, estimates-as-measurements, unknown-as-zero, IPC/CPC outside appendix, family counts replacing publication/application units, unresolved S1/N1 query shorthand, unsolicited action-plan/filing-cadence chapters (dispositions required; roadmap only on request), and inconsistent cover/conclusion/chart/detail numbers.

## Common errors

See quality-gates.md. Prevent inconsistent repeated numbers; expired/unread media URLs; IPC in trees; zero pie slices; unsorted bars (sort ascending); mixed global/CN/application units; missing relevant supply-chain roles; omitted intersection/competitor-expansion spaces; unused CSS; broken navigation anchors. Verify actual media identity/readability and use labeled analytical SVG when originals are unavailable.

## Data and degradation

P3: search_patent details + field_analysis totals. P4: field_analysis trends/ranks/geography/technology. P5: search/fetch/lifecycle for individual originals/status. P6: literature tools and available web material. Page samples are not full datasets and aggregate totals are not individual verification. Article id becomes paper_id; abstracts are not fulltext.

| Missing capability | Bounded fallback | Disclosure |
|---|---|---|
| Patent search/details | Analyze existing receipts/user material in affected P3/P5; verify supplemental identities/versions/coverage or retain gaps. | Cover and Chapters 04/06: no full patent source connected, counts are sample-level, not exhaustive; list missing fields. |
| field_analysis/dimension | Aggregate actually acquired P3 records locally; without full retrieval, only sample statistics/ranks. | Chapter 04/charts: missing capability, actual scope and whether exhaustive; never extrapolate. |
| Literature search/details/fields | Use existing/verifiable supplemental evidence; retain unavailable citation analysis. | Chapter 03: sources, missing fields and coverage. |

Degradation narrows disclosed scope; it never licenses invented estimates.

## Built-in methods and reading priorities

- search-strategy-method: seven-step strategy, S0–S4, multidimensional terms, proximity, noise and recall/precision gates.
- mining-method: nine scenarios/seven bottlenecks, CP-0, four blocks/ten steps, technical/legal/market evaluation and five dispositions.
- design-around-method: risk matrix, removal/substitution/combination/decomposition, five surrounding directions, three-dimensional extension, five R&D dimensions, TRIZ/patent maps.
- layout-report-method: nine intermediate assets, ten actions, five technical spaces, canonical matrix and five strategies.

Read the phase's primary entry first, not every reference:

| Phase | Required | As needed |
|---|---|---|
| P1 | layout-report-method.md | tech-decomposition-method.md |
| P2 | search-strategy-method.md | patsnap-query-rules.md for syntax, searchable-fields.md for codes, tech-decomposition-method.md for routing, search-report-template.md for delivery, search-validation-checklist.md for actual result validation |
| P3–P6 | Corresponding sop-phases.md sections | data-fields.md |
| P7 | mining-method.md | — |
| P8 | design-around-method.md | — |
| P9 | layout-report-method.md + cluster-spec.md | — |
| P10 | html-spec.md + quality-gates.md | ppt-output-spec.md |

The six P2 support files are large; do not load all at startup. Field references govern syntax guidance, not output language or proof that a query executed. All report-language rules in this release follow the English-default policy above.
