# From features to FTO queries

Read during Steps 2–4 for new queries or user-requested logic reconstruction. These are Skill orchestration rules from features/expanded terms to technical Boolean and structured scope, not additional tools.

## Contents

- 1. Features to retrieval units
- 2. Expanded terms to unit expressions
- 3. Unit expressions to the combined query
- 4. Builder requests and result checks
- 5. Execution, diagnosis and candidate handoff
- 6. Magnetic charging dock example

## 1. Features to retrieval units

FTO seeks claims potentially covering product components, relationships, methods or materials. Patents need not describe all additional product features; complete-product feature coverage cannot be a universal retrieval admission rule.

Preserve raw feature-tool receipts. Maintain a separate local mapping; these are audit fields, not MCP inputs/outputs:

| Field | Purpose |
|---|---|
| unit_id, source_quote/location, feature_pointer | Map original product text to actual returned elements; use local IDs and array pointers when tool IDs are absent |
| entity, relation/action, condition | Preserve entity roles, connections, direction, quantity and triggers, rather than a subjectless word bag |
| source_type, dimension, configuration | Preserve original categories; check structure, algorithm, material, process and application dimensions; separate incompatible configurations |
| linked_units, retrieval_role, reason | Mark domain background, independent risk direction, related implementation, supplementary retrieval or later verification with reasons |
| keyword_pointer, groups, classifications | Link expansion provenance, root groups and IPC/CPC schemes; record gaps explicitly |

Normally form Ki from core features, also checking whether key implementations/support technologies contain independent protection directions, especially cross-domain materials, algorithms and processes. Do not drop dimensions by relevance thresholds or mechanically create a route for every trivial detail. Related implementations may complete one Ki's object/action/condition, preserving merged provenance.

Retain numbers, sequence and entity roles in product records and Screening/CC inputs. Whether they become retrieval conditions depends on discrimination and indexed expression; neither discard all nor AND all. Unknown facts are not present elements; alternatives are not ANDed together. Correct missing dimensions against originals and re-extract.

## 2. Expanded terms to unit expressions

Step 3 prioritizes direct runtime-compatible transfer of actual extracted elements. For string features and open downstream objects without internal required fields, preserve each original in the service-verifiable `element_description`, one-to-one in order, with mapping and both raw receipts saved separately. Do not guess `description` or invent types, levels, scores, classifications or facts. Stop if lossless transfer is impossible. Verify actual nonempty expansion by source index/text; success with all-empty terms or lost originals is `keyword_handoff_failed`, with at most one identical-map retry. Missing optional types/levels/scores remain unavailable and cannot drive logic. Read complete receipts rather than assuming old field names.

1. A root term, synonyms and language equivalents form OR group Gi. Preserve language/provenance relationships; actual Q must cover adopted languages.
2. AND distinct concepts needed for one unit, such as “conductive contact object AND floating/tilting relationship.” They are not synonyms to flatten into OR.
3. OR alternative implementations/equivalent expressions within a unit; separately OR independent risk units Ki. Domain is not the sum of every component, action and effect.
4. Established terms such as `pogo pin` may be phrases. Do not combine roots into a nonexistent exact long phrase; retain “floating AND probe holder,” without forcing “floating probe holder.”
5. Effects such as error compensation/stability usually supplement expression or verification, without another mandatory effect gate. Trade names, narrow uses and AI-inferred terms are not automatic global constraints. Preserve explicit genuine material/object restrictions.
6. Check meaning and entity roles. Broad terms such as “restoration,” “adsorption” or “base” cannot form isolated routes without unit context.
7. After freezing the expansion receipt, perform Step 3.5 local translation using confirmed `target_markets/search_languages`. Save source element/term/language, target language, translation, back-translation, role and review state. Adopt only reviewed terms. Check roots, synonyms, broader terms and decisive relationships in each priority language, without context-free literal translation. OR language equivalents within concepts; do not require bilingual documents. For EP prioritize English/German/French, supplementing actual countries by local language and verified index coverage. Adopted translations must actually enter Boolean intent or independent target-language QuerySpecs, not only a report list.

For duplicates, blanks, nested results or multiple expression forms, map by element descriptions, technical meaning and originals rather than assumed array positions. An empty display layer does not delete a unit. Explain adopted paths for conflicting forms; record gaps or rerun expansion when unrecoverable. Local additions require sources and remain separate from raw receipts.

Keep classification `code/scheme/associated unit/source/verification status`. A flat list without a declared scheme must not automatically be put into IPC. First check the returned scheme and current field capabilities. Related classes can guide supplementary retrieval; predicted classes are neither product facts nor exclusion rules.

## 3. Unit expressions to the combined query

First form local D (domain text), Ki (risk-unit text) and Ci (relevant classification expressions), retaining sources. Keep jurisdiction, legal status and dates separately in `SEARCH_FILTERS`; not every Ci needs a value. An abstract structure is `((S1 AND (S3 OR S5)) OR ((S2 OR S4 OR S6) AND (S1 OR S3 OR S5)))`, where S1 is domain terminology, S3/S5 core-feature terms and S2/S4/S6 related classifications. The default baseline is:

```text
D = domain background concepts (OR equivalents within groups, AND required concepts)
Ki = one independent risk unit (AND necessary concepts, OR alternative implementations)
K = K1 OR K2 OR ...
C_cls = verified relevant classifications, with IPC/CPC distinguished
B_text = D AND K
B_class = C_cls AND (D OR K)
Q_tech = B_text OR B_class
SEARCH_FILTERS = confirmed jurisdiction/date + default pending/active-rights structured scope
```

This is an evidenced baseline, not a fixed recipe or backend format. Independent implementation/support risks may join Ki or a separate contextual supplementary route. For multidimensional solutions, OR separate `Dj/Kj/Cj` routes rather than requiring hardware, algorithms and materials simultaneously. Reuse the same `SEARCH_FILTERS` only where runtime support and receipts permit verification; exclusive Boolean cannot be represented as scoped.

- **Domain fallback:** B_class admits relevant patents lacking a narrow product name through classifications and technical units. Do not AND D outside the entire query and defeat this branch.
- **Classification is not a global gate:** OR related classifications and combine them with meaningful technical expressions. Do not AND C_cls to the whole Q or add a bare C_cls OR branch retrieving an entire class. For explicit classification-only scope, prefer supported structured classification capabilities, otherwise a verified technical classification expression.
- **Do not AND everything:** `D AND K1 AND K2 AND implementation AND support AND classification` can be an explicit precision route, not the default sole route. A precision branch contained in a broad branch adds no union recall; do not claim new hits.
- **No reliable classification:** mark classification supplementation not run. If D is too narrow, add a route grounded in original generic component/relationship context and explain differences. Do not invent classes or claim equivalent restoration of the missing route.
- **No clear D:** use traceable components/technical context and record why. Clarify only gaps affecting direction; do not default to trade names or invention titles.
- **Scope preserved:** set countries/dates from authorization; default FTO status is pending/active grants at the assessment date, using verified runtime enums and supported `SEARCH_FILTERS`. CN/patent-type defaults from examples or previous cases are not general defaults.
- **No geography:** omit unconfirmed jurisdiction/authority/date restrictions but retain pending/active status gating where supported. Unsupported status permits technical exploration with status-unverified candidates and later verification. Input/output language, location, past queries, GT origin and initial-hit countries are not scope sources. Do not enumerate “global” as an unconfirmed finite country set.
- **Europe:** Europe/EU/EP/EPO is not one executable market. For market FTO confirm actual countries, then plan EP and necessary national routes. Explicit EP-document-only requests remain document scope, without European-country clearance conclusions.

Account for each adopted feature through a query unit, supplementary retrieval, Screening verification or explicit gap. Broad retrieval still requires the complete adopted P for Screening and CC.

## 4. Builder requests and result checks

Local `query-plan.json` records at least solution/feature/expansion versions and receipt locations, Step 3.5 translated-lexicon version/review status, feature mappings, term/classification groups, `SEARCH_FILTERS` and sources, unit/combined logic, adopted/pending units, query version and execution/retrieval plan. Freeze before construction and record reasons for later changes.

Send the complete natural-language plan to `patsnap-ip:build_patent_boolean_query` under the current protocol. Logical group names may explain structure, but define every group in the same intent rather than saying “refer to the previous message.” Example:

```text
Build the technical Boolean for candidate retrieval. Jurisdiction, legal status and dates
will be handled separately through structured search scope; add none to the Boolean.
D: both [object group] and [application group], with alternatives within each group.
K1: both [entity group] and [relationship group], synonyms as alternatives.
K2: both [entity group] and [action group], synonyms as alternatives.
C: any code in [verified IPC list] or [verified CPC list].
Branch 1: D, and at least one of K1/K2.
Branch 2: C, and at least one of D/K1/K2.
Union the branches. Match text in titles, abstracts or claims; listed languages are alternatives; market-language terms come from the frozen, back-translation-reviewed local lexicon.
Preserve this logic; do not require both K1 and K2, add classifications/product details,
or join independent terms into long exact phrases.
```

Check actual Boolean semantics through reviewable runtime content rather than formatting/string identity. Equivalent expansion is acceptable. At minimum:

| Scenario | Expected baseline |
|---|---|
| D true, only K1 true, no classification | Text branch may admit |
| D true, only K2 true, no classification | Text branch may admit |
| D false, C true, K1 true | Classification branch may admit |
| Only C true; D and K false | Classification alone cannot admit |
| K1 has “floating” without required contact object; D/C/K2 false | Isolated action cannot admit |

Also verify root phrases, languages, IPC/CPC fields, unauthorized geography/status/dates and missing dimensions. Adopted translated terms must actually occur in the correct concepts in the review expression; missing, role-shifted or explanation-only terms are drift. Reject intent drift, retain receipts and resubmit once with the complete plan and specific corrections. If still drifting, build frozen independent branches separately, completely defining each and using the same `SEARCH_FILTERS`; do not drop a route. Report remaining invalid branches without unlimited retries.

Check structured scope separately: omit geographical filters when unconfirmed. Any unauthorized country in builder output is intent drift. Expansion regional preferences do not authorize geography.

Use opaque execution references unchanged only through current-protocol paths, without editing, decoding or concatenation. Never append geography/status/date or other fields to `BOOLEAN_QUERY_ID`. If runtime makes Boolean exclusive and ignores filters, the reference executes unrestricted technical diagnosis only. Use supported semantic/keyword/filter routes for formal scope and record `boolean_scope_unsupported`. Execute existing executable queries directly; make a new plan/baseline only when reconstruction is requested.

## 5. Execution, diagnosis and candidate handoff

After combined-query checks, run a small-window execution check, then retrieve within actual capability. To compare breadth or diagnose zero hits, construct complete relevant unit/branch queries, reuse identical scope only when supported. Exclusive Boolean counts are unrestricted diagnostics, neither directly comparable with scoped routes nor merged into formal candidates. Record counts separately. Untested clauses are “not measured,” not zero.

Local record: `sequence | unit/combined/precision | source unit | complete intent | actual executable reference | real hit count | status | adoption reason`. These records are not tool receipts.

- Business-successful zero hits are normal. Check intent drift, then necessary branch counts to locate restrictions; without clause experiments, do not attribute zero solely to AND. Initially allow at most two evidenced semantic corrections per affected branch, one issue at a time with scope unchanged. Explicit deep optimization enters Step 5.
- Call/business errors or missing counts are errors/unknown, not zero; follow main failure rules.
- Nonzero but broad: inspect a few titles/abstracts and record noise sources. More hits do not prove better quality. Related precision routes may prioritize processing, while retaining broad results and unretrieved windows.
- Oversized union: use adopted branch/shard/window or bounded-test plans, not all-feature AND to force counts within the window.
- Separately executed branches deduplicate by actual PN/ID, retaining source, rank, page and unretrieved window. Merge identical PNs, not publication/grant versions or families automatically. Overlapping totals cannot be summed; union N requires actual combined-query returns or a complete result set.

Disclose retrieved, submitted, returned and CC counts separately. Screening uses actual PNs with identity reconciliation. Plan checks, initial execution and bounded correction are default Step 4; fixed samples and five-round coverage diagnostics remain optional Step 5.

## 6. Magnetic charging dock example

- D: magnetic/magnet AND charging dock/charging-connection context, expanding each concept separately.
- K1: contact bracket/probe holder AND floating/tilting; combine core and related implementation descriptions of the same object with provenance.
- K2: conductive probe/pogo pin AND axial compression/extension.
- Elastic connection/reset of the bracket: implementation linked to K1. Angular-error compensation is an effect for verification, not another global mandatory AND.
- C_cls: verified connector, resilient-contact, self-alignment and charging classes in their actual IPC/CPC systems.

Combine under section 3. “Magnetic AND probe” alone does not validate the complete plan. Invented long exact phrases cannot be sole expressions. This synthetic solution tests construction handoffs; it has no GT, so hit counts cannot prove improved recall.
