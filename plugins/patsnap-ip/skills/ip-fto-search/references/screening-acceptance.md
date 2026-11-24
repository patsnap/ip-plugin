# Screening binding and ranked-list acceptance

## When to run

Run only after Skill installation, `patsnap-ip:screen_patents_for_FTO` protocol/service changes or suspected binding/ranking faults. This controlled acceptance does not replace production cases or repeat on every FTO task.

## 1. Binding

- The actual call must use `@Patsnap IP Plugin`’s `patsnap-ip:screen_patents_for_FTO`. Narrative claims or another provider’s same-named tool do not prove binding.
- Save complete request, call provenance, case/batch identities and raw receipt. `isError=false` proves no reported call error only.
- When Pro is required, explicitly request `mode=pro`. Without server `effective_mode=pro` or equivalent evidence, retain `pro_requested_unverified`.

## 2. Frozen five-patent ranking list

Use this solution, order and relevance grades without relabeling after observing results:

> A magnetic mobile-phone holder detachably connects to the phone’s back using magnets. The phone contains a metal coil. The holder’s front has a cosmetic case containing cosmetics or a mirror.

Grades apply only to this test: 3 highly relevant; 2 relevant but missing one core relationship; 1 local terminology overlap only; 0 unrelated-field noise.

| Input order | PN | Grade | Frozen rationale |
|---:|---|---:|---|
| 1 | `CN113614954A` | 0 | Lithium-battery cathode material, unrelated-field noise |
| 2 | `US8833379B1` | 2 | Phone-back cosmetics container/mirror using adhesion rather than magnetism |
| 3 | `CN219535032U` | 1 | Magnetic connector without phone-holder/cosmetic-case/mirror combination |
| 4 | `US11284525B2` | 2 | Attachable storage accessory for mobile electronics, connectable to stand/ring accessories |
| 5 | `US9537992B2` | 3 | Phone-holder, mirror and magnetic-field components; closest overall test combination |

Use invalid number `ZZ0000000000A1` separately as a parsing control. It must appear as unresolved, never a ranked patent.

## 3. Pass criteria

| Check | Requirement |
|---|---|
| Binding | Actual `@Patsnap IP Plugin` `patsnap-ip:screen_patents_for_FTO` call |
| Identity set | All five valid inputs returned by original PN or verified version mapping; list missing/out-of-input objects separately |
| Relevant first | Grade 3 before all 2/1/0; every grade ≥2 in top three |
| Noise last | Grade 0 last; grade 1 below every grade ≥2 |
| Pairwise order | Higher grade precedes lower grade; no required order within a grade |
| Invalid number | Unresolved set only |
| Version mapping | Per-row input/returned PN, same application or explicit relationship evidence, adopted version/source; titles/family proximity alone do not suffice |
| Pro | Server `effective_mode=pro` or equivalent; otherwise independently unconfirmed without negating observed ranking |
| Processing evidence | If scores/reasons are absent, state “ranking observable; scoring basis not returned” |

Do not require every noise item to disappear. Returning all five does not fail a ranking tool; frozen relative order is decisive. Passing proves only this small-list reranking, not large-pool stability, recall completeness, per-patent claim coverage or legal risk.

For replaced grant/application versions without server mapping reasons, record a local `identity_remap` only after full-text or verified identity materials establish the same application, noting “server reason not returned.” Unproven substitutions remain out-of-input results plus original inputs with unknown processing status; do not force count reconciliation.

## 4. Record boundaries

Keep actual run dates, requests, receipts, metrics and large-pool observations in repository test records, not installation content. Judge each run against these frozen inputs/criteria and record current evidence locations. Historical passing does not replace retesting after changes.

Large-pool counts, mappings and ranks depend on actual receipts, without permanent tool limits, global stable risk rankings or proof all inputs processed. Do not complete production pools through repeated identical-request unions or choose the most favorable ranking.
