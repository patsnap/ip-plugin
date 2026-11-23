# Portfolio report quality gates

These checks supplement substantive completion in layout-report-method.md. Interim work may be submitted as interim, never complete merely because the file has all sections.

## Numbers

Reconcile cover, conclusions, charts and detail tables after every change. A cover count of 18 against a cluster total of 15 fails. Module summaries should derive from the same data rather than stale hardcoded counts. Status changes update main table→summary→cover→conclusions; equal grand totals do not excuse different active/inactive splits. Every named cluster/count in conclusions must exist in the cluster design.

## Images

Signed media URLs may expire; do not assume a fixed 24-hour lifetime. Obtain actual media clues from fetch_patent, record expiry only if supplied, and actually check image/document identity using available reading tools. Embed already acquired permitted originals with provenance. Without a local original, use labeled analytical SVG, never pretend it is an original drawing.

## IPC/CPC placement

Keep technical trees and business charts physically separate from search strategy. Move all class codes to the appendix; use engineering descriptions in nodes/focus labels. Do not hide codes inside parenthetical business labels.

## Charts and counting

Sort ranking data ascending with a sorting function, not handwritten order. Remove zero pie slices or use bars/text. Captions state included/excluded industry roles; selected-company or OEM-only samples are not industry-wide rankings.

Use common geography/unit across comparisons; if heterogeneous facts must be shown, label each explicitly rather than treating them as directly comparable. Keep global/CN distinct. Publication/application counts follow the canonical scope; family links do not become interchangeable units. Never replace unknowns with zero or estimates with false precision; every number needs source/unit and every estimate formula/assumptions.

## Navigation and styles

After section changes check every href against an existing ID. Activate the first section on load (`cur=sections[0]`) and verify initial state. Status changes update badge class, border/tree classes and tag text together. Define every used class and remove unused classes after refactors.

## Required chapters

P1–P10 are workflow phases, Chapters 01–13 report sections; never interchange them. Verify:

1. Cover/key conclusions.
2. Technical tree/keywords.
3. Industry/nonpatent evidence.
4. Competitor landscape.
5. Relevant suppliers/supply chain.
6. Individually checked own portfolio.
7. Frontier/high-value patent deep analysis.
8. All five technical spaces.
9. High-risk design-around.
10. Innovations with three dimensions/TRIZ/dispositions.
11. Portfolio matrix.
12. Clusters.
13. Complete executable queries.

Do not let an optional slide-deck condensation remove HTML chapters. Five spaces always appear in order: own existing, competitor existing, intersection, competitor expansion, own expansion. Unsupported/inapplicable sections state their status/reasons rather than fabricated content.

Chapter 07 deeply analyzes solutions/independent claims/design-around; Chapter 08 references those conclusions in its five-space comparison without duplicating full analyses.

## Queries

Shorthand such as `S1=TAC:(A_CORE) AND TAC:(C_FUNC)` is design notation, not executable delivery. Provide expanded FINAL_BALANCED_EXPANDED, NOISE_TOTAL_EXPANDED and FINAL_PRECISION_EXPANDED without unresolved S#/N# placeholders. Syntax uncertainty is explicitly unverified, not a falsely executable expression.

## Acceptance checklist

- Repeated numbers agree across all four locations; cluster proposed/total counts differ correctly.
- All 13 sections and five spaces are accounted for, with substantive states/gaps.
- Rankings sorted, no zero pie slices, geographic/counting conventions explicit.
- No dead anchors, initial navigation active, no undefined/unused CSS.
- No IPC/CPC in business prose; no unfilled placeholders/example data.
- Numbers/estimates traceable; final expressions fully expanded.
- Individual-verification list, denominator and unreviewed objects are retrievable; samples labeled.
- Image availability/identity checked; originals vs analytical diagrams clear.
- Legal-status text, badges and colors agree.
- English narrative/UI/figures are consistent unless another language is explicitly requested; source originals and multilingual query examples remain labeled exceptions.
