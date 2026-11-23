# Tool usage

Read on first use and after protocol changes. Runtime MCP is the sole source of inputs, outputs, enums, limits and response structure. This reference defines routing, evidence and handoff boundaries, not schemas.

## Calls

- Read current definitions and use declared inputs only; do not infer parameter names/defaults/limits from this Skill.
- Save complete actual requests, tool provenance, input versions and raw receipts. Reuse identical completed nodes.
- Tool success, business completion and evidence sufficiency are separate. Stop affected dependencies for errors, incomplete returns or unparseable content; failure is not zero results.

## Handoffs

- Use only transfer forms supported by both tools. Stop when lossless transfer is impossible; do not rebuild inputs from display summaries or inference.
- Use the main route’s feature extraction followed by term expansion, preferring compatible direct transfer. Do not invent types, levels, scores, classifications or facts, or substitute another expansion tool.
- Freeze original Chinese/English `patsnap-ip:expand_patent_search_terms` receipts. For confirmed other market languages, create a separate AI-localized lexicon with source term, back-translation, role and review state; adopt only reviewed terms in Boolean intent and independent semantic QuerySpecs.
- Use opaque references unchanged only through allowed protocol paths; do not parse, concatenate or present them as raw queries.
- Before Screening/CC, verify complete identity, version, source branch and actual retrieval window.
- Obtain required claims/descriptions through the full-text tool. Search snippets, screening summaries and third-party paraphrases are not originals.
- Simplified status does not replace lifecycle evidence for current claims, versions and events.

## Business completion criteria

These are business checks, not response schemas.

| Tool | Completion requires | Does not establish |
|---|---|---|
| `patsnap-ip:extract_technical_features` | Parseable nonempty features traceable to frozen facts, actual element count/evidence/gaps reconciled | Completeness from count/success; string features are not automatically compatible expansion objects |
| `patsnap-ip:expand_patent_search_terms` | Runtime-supported input or open-object lossless `element_description` mapping; source-index/text identity and actual Chinese/English terms; at least one adopted element with nonempty terms, with empty/missing fields reconciled | Success/count/permissive acceptance does not prove handoff. Unrecognized `description` can yield empty expansion; missing optional type/level/score cannot drive logic; other languages are not proven covered |
| `patsnap-ip:build_patent_boolean_query` | Opaque execution reference and human-review expression preserving frozen branches, logic, fields, languages/classes, excluding geography/status/dates | Correct intent, execution or hits from construction success |
| `patsnap-ip:search_patent` | Real receipts for strategies/all adopted pages; per-object identity, route, rank, jurisdiction/status reconciled; leaks/unknowns separated and exclusive Boolean outside formal pool | Scope effectiveness, complete windows or blocking rights from requested filters/success/hit/page counts. Never edit references or merge filter-ignored Boolean into the formal pool |
| `patsnap-ip:fetch_patent` | Adopted identity/bibliography match, required located claim originals and required descriptions obtained or explicitly missing | Complete claims from titles/abstracts/summaries/success; automatic family substitution |
| `patsnap-ip:fetch_patent_lifecycle` | Matching jurisdiction, assessment date, publication, events and located status evidence/gaps | Current validity from an event name, simplified label or absent invalidation record; claim text |
| `patsnap-ip:screen_patents_for_FTO` | Correct filtering-tool provenance, submitted/resolved/returned/unresolved/processing reconciliation and server-evidence-based mode | Inherited search filters for PN input, effective rights, actual Pro or full processing from request/success/order |
| `patsnap-ip:build_claim_chart` | Selected objects passing lifecycle/text gates; per-object completion/errors, claim coverage/evidence/gaps; product and interpretation support for inference labels; label–row–conclusion consistency | Eligibility, selection, current claims or final legal opinions from risk/status/include flags; common structure as necessary inherency, same function as coverage, or definitive summaries conflicting with unresolved rows |

## Screening handshake

- Call only `@Patsnap IP`’s `patsnap-ip:screen_patents_for_FTO`; do not choose/fall back among same-named services. Stop affected work if its protocol cannot support the case.
- Record `protocol_checked → request_accepted → mode_acknowledged → processing_reconciled`. Requesting Pro, `isError=false` or returned candidates do not acknowledge actual mode.
- Use `pro_confirmed / pro_requested_unverified / mode_mismatch`. Only server mode evidence allows confirmed. Without it, disclose unverified mode; candidates may undergo subsequent strong-evidence review. Do not silently fall back on mismatch.
- Mode and processing are independent gates. Even confirmed Pro requires submitted, resolved, explicitly processed, returned, unresolved, scoring-failed and status-unavailable reconciliation.

## Business boundaries

- AI language supplementation is not tool output or new product fact. Language, location and hits do not authorize geography.
- Recall routes run independently with identity union only. Jurisdictions/dates follow confirmed scope; pending/active grants are the default FTO status gate. Exclusive/filter-ignored Boolean is unrestricted diagnosis, outside formal pooling. Verify actual jurisdiction/status per returned object. Exclude leaks without consuming eligible windows; unknowns await checks. An entirely out-of-jurisdiction nonempty page stops route paging as `route_degraded`. Do not guess unclear enum codes; obtain lifecycle evidence before CC.
- Failed scope filtering degrades that route only. Semantic routes may continue when replacement sufficiency passes; large counts alone do not prove coverage.
- Client lists use exact OR import and identity checks, without expansion, automatic family replacement or unauthorized scope.
- Deliver a lightweight candidate catalog after Screening. Obtain CC scope and full-text choices before proceeding. Do not default all/top-N or fetch/expand unselected objects.
- Reconcile changed/nonreturned PNs with the same application or explicit relationship evidence, row by row; titles/family proximity alone are insufficient. Compensate unexplained differences at most once, preserving separate provenance/original ranks; unresolved processing remains unavailable.
- Before CC, selected objects pass lifecycle/adopted-text gates. Exclude inactive/withdrawn/abandoned/rejected/revoked/expired rights by default; unknowns block. Do not silently replace with active family members.
- Cover every frozen object with original claims, product evidence, dependencies, interpretation conditions and unknowns. Tool comparisons are not final legal risk.
- Medium/high labels or uncertain rows, unsupported equivalence or unknown product facts conflicting with a definite noncoverage summary imply `cc_conclusion_conflict`; do not adopt that summary. Retain raw results and evidenced conditional local opinions.
- Optional full-text relationship failures do not mean empty basic text. If unnecessary, preserve failure and retry once without optional expansion; maintain the gap when relationships are necessary.
