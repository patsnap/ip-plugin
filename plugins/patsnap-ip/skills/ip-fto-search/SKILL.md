---
name: ip-fto-search
description: "Use for freedom-to-operate research on a confirmed product and its target countries. Screen candidate patents, let the user choose which ones go into claim analysis, build claim charts, and produce a risk report with sources and coverage gaps. Does not guarantee non-infringement."
metadata:
  version: "2.0.0"
---

# FTO Search

## MCP protocol boundary

The runtime MCP protocol is the sole source of truth for inputs, outputs, enums, limits and response structure. This Skill defines business orchestration, decision rules, evidence boundaries and each tool’s indispensable business inputs and handoff sources. It does not duplicate complete schemas, list optional parameters, assume response paths or turn current limits into permanent rules.

Read the current protocol before each call and use only declared inputs. Save complete raw receipts and verify completion, object coverage and evidence identity against the actual response structure. Follow runtime changes; parameter changes alone do not require rewriting the Skill unless business semantics also change.

The target server is `patsnap-ip`. Claude uses fully qualified `patsnap-ip:tool_name`; Codex uses the exposed equivalent `mcp__patsnap_ip__tool_name`. Tables below use Claude notation. Do not call same-named tools on other servers.

## Tool routing

| Stage | A1 tool | Responsibility |
|---|---|---|
| Technical features | `patsnap-ip:extract_technical_features` | Extract traceable technical features |
| Keyword expansion | `patsnap-ip:expand_patent_search_terms` | Expand Chinese/English keywords, synonyms, related terms and broader terms |
| Boolean construction | `patsnap-ip:build_patent_boolean_query` | Convert frozen concepts and combination logic into a patent query |
| Patent retrieval | `patsnap-ip:search_patent` | Execute Boolean, semantic, keyword and structured-scope searches |
| Patent full text | `patsnap-ip:fetch_patent` | Obtain originals, bibliography and relationship evidence |
| Lifecycle | `patsnap-ip:fetch_patent_lifecycle` | Verify current claim versions, legal events and ownership records |
| Screening | `patsnap-ip:screen_patents_for_FTO` | Use the filtering tool for batch screening by technical relevance and possible claim coverage |
| Claim Chart | `patsnap-ip:build_claim_chart` | Compare claim limitations with target-solution facts item by item |

When a required tool is absent or its protocol cannot support a step, record the specific gap and stop the affected dependency chain. Do not guess or fabricate results with another tool. See [Tool usage](references/tool-usage.md).

## Required business inputs

These are indispensable business materials, not a schema. Read the current protocol before calling; map renamed fields to the same materials without inventing undeclared parameters.

| Tool | Required input | Source and non-substitution rule |
|---|---|---|
| `patsnap-ip:extract_technical_features` | Complete solution and traceable attachment facts | The input card’s frozen single product/configuration; not an abstract, keywords or query |
| `patsnap-ip:expand_patent_search_terms` | Same solution and verified original features | Prefer a runtime-compatible direct handoff, preserving one-to-one identity, order and evidence; invent no types, levels, scores or facts. Stop if lossless transfer is impossible |
| `patsnap-ip:build_patent_boolean_query` | Complete natural-language search intent | Define concept groups, intra/intergroup logic, text fields, languages and classification systems; not an executable field query or jurisdiction/status/date conditions |
| `patsnap-ip:search_patent` | Defined strategy, corresponding query and frozen scope | Supply only the strategy’s inputs. Pass the builder’s original opaque Boolean reference without adding countries/statuses |
| `patsnap-ip:fetch_patent` | One identity-verified patent | From real search/Screening receipts with version verification; not a title, snippet or local index |
| `patsnap-ip:fetch_patent_lifecycle` | Verified identity matching the adopted publication | Not a simplified status, applicant name or another family member |
| `patsnap-ip:screen_patents_for_FTO` | Frozen solution, actual candidate entry and screening mode | Only retrieved, identity-verified candidates passing the status gate; no fabricated references, hit counts or unretrieved patents |
| `patsnap-ip:build_claim_chart` | Frozen solution and patents passing client selection, lifecycle and adopted-text gates | Batch in frozen order. No unselected, inactive, withdrawn, status-unknown or text-missing objects; preserve the case chain across batches |

Parameter acceptance, tool success and business-stage completion are distinct. See [Tool usage](references/tool-usage.md) for completion criteria and facts each tool cannot replace.

## Scope and entry points

Default path: **input card → features/retrieval units → Chinese/English keyword groups → target-market language supplementation → independent Boolean and semantic recall → keyword convergence within the semantic pool → candidate union → FTO Screening → client chooses CC scope/full-text strategy → Claim Chart → local report.**

| Existing material / objective | Entry |
|---|---|
| Technical solution | Feature extraction and search planning |
| Executable query | Verify technical logic/scope, then execute and retrieve |
| Client patent/application-number list | Exact OR query from original numbers, then identity verification; fetch originals when requested, or enter Screening for FTO |
| Direct comparison of specified patents | Verify identities/originals, then Claim Chart; disclose Screening was not run |
| Existing CC | Verify solution, identities, versions and evidence; redo missing/changed objects only |
| Existing FTO report | List assertions and evidence first; review alone does not authorize a fresh search |

Preserve client-list rows, column names, order and file version. OR numbers without keyword expansion, default family substitution or unauthorized jurisdiction/status/date/assignee/technical restrictions. Count only actually returned, identity-verified objects as imported. Separately disclose blanks, malformed entries, duplicates, unresolved identities, version mappings and out-of-input objects. Original-text delivery comes from the full-text tool, not search abstracts/snippets.

## Stage 0: Input card and scope

Read the [input card](references/input.md). Fix one product/configuration, assessed activities, manufacturing/sales/use countries, search authorities, assessment date, input/output/search languages, existing assets, CC scope and full-text strategy status.

Before the first formal business tool call, show a plain-language scope card with product/configuration, manufacturing/import/sales/use activities and respective countries, search authorities, assessment date, evidence cutoff and unresolved items. Reuse supplied answers. Ask one combined question from [Customer prompts](references/customer-prompts.md) for missing items affecting jurisdiction or current rights. The assessment date determines pending/active rights; the evidence cutoff states how current retrieval/evidence is. Do not confuse these dates or automatically use the evidence cutoff as a filing/publication-date filter. Unconfirmed scope permits explicitly labeled geographically unrestricted technical exploration only, without formal jurisdiction searches, Screening or Claim Chart.

For referenced attachments, verify actual readability, page/figure locations and consistency with the input card before the first business call. A filename/path/list is not proof of reading. Name missing, undecodable or unmounted attachments and stop dependent feature extraction/formal retrieval. Do not invent attachment facts from summaries or general knowledge. Continue independent work with explicit limited scope.

After scope confirmation and before the first formal business call, ask the client to choose **continuous AI execution** or **stage-by-stage confirmation**. Continuous execution advances autonomously within frozen scope, pausing at mandatory gates, scope/product changes, consequential gaps, and client-owned CC-list/full-text decisions. Stage confirmation presents adopted input, adjustment reasons, expected effects and unresolved items before each major next stage: features/units → keywords/plan → retrieval/pool → Screening → CC scope/full-text strategy → Claim Chart → HTML preview. Await actual confirmation; do not create repeated gates for pagination, harmless reads or same-stage protocol retries. Record the mode in the input card. A later switch changes subsequent orchestration without rewriting frozen receipts/evidence.

Ask only at decisions affecting later execution and reuse answers. Rewrite all customer questions, updates, technical/search explanations, candidate reasons, itemwise opinions, conclusions, headers, captions and page text under [Plain language](references/plain-language.md), ahead of internal template terminology. Explain the business meaning in the adopted language first; introduce technical terms parenthetically when needed. [Customer prompts](references/customer-prompts.md) covers scope, technical gaps, degraded routes, rights types, missing screening objects, CC scope and final format.

For “Europe/EU/EP/EPO,” distinguish operating countries from document authorities. EP-only retrieval does not cover every European market or replace national-route, unitary-effect or UPC checks. Input language, user location, earlier cases and initial hits do not default scope to CN.

Create a local case ID and associate complete requests, receipts, input versions and identities. It is for audit, not automatically an MCP input.

## Rules throughout

- Version solution, query, scope, candidate window and selections; downstream uses frozen versions only.
- Separate language from geography; synonym regional preferences do not define patent scope.
- Execute Boolean, semantic and keyword routes according to their meanings, without score fusion. Use current structured jurisdiction/status/date capabilities outside technical Boolean. Exclusive Boolean that ignores filters is unrestricted technical diagnosis only, excluded from the formal jurisdiction pool; do not edit opaque references to add scope.
- Default FTO candidates are pending applications and active grants at the assessment date. Expired, terminated, withdrawn, abandoned, rejected, revoked/invalidated rights enter a status-exclusion list, not blocking Claim Charts. Verify unknown status first.
- Search status filtering reduces noise; it does not replace lifecycle review. Before CC, every selected object requires `patsnap-ip:fetch_patent_lifecycle` for current status and `patsnap-ip:fetch_patent` for adopted text.
- Establish units/logic before new queries; do not AND every product feature or flatten distinct concepts into OR.
- Count search hits, retrieved patents, Screening returns and CC selections separately.
- Identity matched, request submitted, batch success, claims obtained per object, screening processed per object and candidate returned are six distinct states. Successful batches do not prove every input was screened when receipts list candidates only.
- Nonreturned, unresolved, failed or unselected objects are not low risk.
- CC covers every client-adopted object. Local verification batches do not authorize a top-N cutoff.
- Tool judgments are not final legal opinions; verify claims, product facts, versions and lifecycle.
- Stop affected dependencies for errors, business failures, partial returns or unparseable structures; failure is not an empty result.

## Step 1: Organize the solution (local, as needed)

For difficult materials, images or multiple configurations, organize “use/object—components/relationships—operation/conditions—problem/effect—unknowns/alternatives.” Preserve originals, locations and fact nature. Image interpretation is not verbatim evidence. Use clear text directly without a polishing tool.

## Step 2: Extract features

Call `patsnap-ip:extract_technical_features`. Check objects, actions/relationships, conditions, configurations, structures, algorithms, materials, processes and applications against the original. Every adopted feature traces to text or attachment locations. Resolve gaps without inventing features.

Do not repeat ordinary cases to obtain identical wording. For release acceptance, regression testing or omission of explicit source facts, rerun exactly the same input at most once and retain both receipts. Select by source-fact coverage, evidence locations and complete entity relationships, not feature count; do not merge strings into fabricated tool output. If no single receipt covers decisive facts, stop and disclose instability.

Maintain `unit ID | source location | feature pointer | object/relationship/condition | domain/core/implementation/support | linked units/incompatible configurations | retrieval purpose`. Independently protectable components, relationships, methods, materials and algorithms are independent risk directions; scores do not determine globally mandatory features.

## Step 3: Expand keywords

Call `patsnap-ip:expand_patent_search_terms`. Prefer direct, runtime-compatible transfer of actual extracted elements. If upstream returns strings and downstream declares open objects without internal required fields, use a **lossless handoff mapping**: put each original feature in the service-verifiable minimal key `element_description`, preserving one-to-one identity, order and source evidence. Save mapping separately from both raw receipts. Do not guess a generic `description` key or invent element types, keyword levels, relevance, classes or technical facts. Future explicit runtime fields govern; stop if no field can carry original text.

Verify each input yields nonempty keywords/synonyms aligned to its original index. `success=true` with entirely empty expansion or lost element descriptions is `keyword_handoff_failed`, not completion. Retry the same lossless mapping at most once. Missing optional element/keyword types or relevance are “not provided”; do not use them to delete, weight or construct queries. Their absence alone does not fail an otherwise complete original-text/term handoff.

Check meanings, roles and provenance. Expanded terms do not become product facts. OR synonyms inside one concept, AND distinct concepts necessary to a retrieval unit, and normally OR independent risk directions. Do not combine independent roots into invented exact long phrases.

## Step 3.5: Target-market language supplementation (local)

After freezing the expansion receipt, localize adopted roots, synonyms, broader terms, decisive objects/actions/relationships and semantic centers only for confirmed markets and search languages. EP routes prioritize English/German/French; supplement actual countries using local languages and verified index coverage. Do not infer geography or generate regional language sets before confirmation.

Save translations separately as `source_element | source_term | source_language | target_language | translated_term | back_translation | technical_role | review_status`; do not overwrite receipts/product facts. Check back-translation, roles, inflections, patent usage and ambiguity. Unchecked literal translations, transliterations or ambiguous terms cannot enter formal queries. OR multilingual variants within a concept; AND distinct relationship concepts.

Freeze the adopted translated lexicon, include it in the Boolean builder’s natural-language intent and create independent target-language semantic QuerySpecs from the same facts. Record languages actually executed; a report-only translated list is insufficient. See [Query construction](references/query-construction.md).

## Step 4: Boolean and semantic retrieval

Freeze a search plan. Technical baseline:

```text
K = K1 OR K2 OR ... (independent risk directions)
Q_tech = (D AND K) OR (C_cls AND (D OR K))
SCOPE = confirmed jurisdictions/dates + default pending/active-grant rights
```

With unconfirmed scope, run technical exploration only; do not default to CN or replace “global” with a finite country list. Classification is a technically constrained supplementary branch, not a global AND gate or bare classification route.

Send frozen terms, intra/intergroup logic, text fields and classification systems to `patsnap-ip:build_patent_boolean_query`, excluding jurisdictions/statuses/dates from technical Boolean. Verify generated logic, phrases, classifications and languages. Correct drift through natural-language intent, without editing opaque references.

Read strategy binding before `patsnap-ip:search_patent`. Submit confirmed authorities and pending/active-grant scope with Boolean only if runtime supports that combination. If Boolean is exclusive, filters are ignored or receipts do not prove filtering, execute the technical reference unchanged and mark `boolean_scope_unsupported`. Use it for expression diagnosis/terms only; unrestricted results cannot enter the formal jurisdiction pool. Never append authority/status/date fields to `BOOLEAN_QUERY_ID` or infer scope from `success`. Build the formal pool through routes actually supporting structured scope; enable combined Boolean/scope only after verifiable runtime support returns.

For scoped routes, verify actual `jurisdiction` and `legal_status` for every returned object on every page. A requested filter alone proves nothing. Exclude `jurisdiction_filter_leak` and `status_filter_leak`; missing/unknown fields await verification.

Leaks do not consume the frozen eligible-candidate window. Continue paging until exhaustion, runtime boundary or the frozen eligible count. If any nonempty page consists entirely of out-of-jurisdiction objects, mark `route_degraded`, save the page and stop blind expansion; enlarging windows cannot mask systematic leaks. Disclose an incomplete eligible window at the boundary. Unsupported filters, unclear enums or missing scope fields permit technical exploration only; mark candidates “scope unverified” and exclude them from formal recall/Screening until verified. Distinguish zero hits, syntax errors and failures; do not remove scope or OR everything to force hits. Deduplicate identities across branches, preserving sources, ranks and actual windows; overlapping counts are not additive union totals.

Use [Semantic retrieval](references/semantic-retrieval.md) for independent single-center natural-language routes. Union with Boolean by identity only. Generate from product facts, features and receipted public-patent probes, never GT, missed titles, target patent numbers or client conclusions. Runtime governs windows/paging.

Only after broad semantic recall and pool freezing, softly converge inside that fixed pool using object + decisive relationship + context phrases. New whole-database `semantic+keyword` hits are not convergence. Use `patsnap-ip:search_patent` for reranking only when PN/ID constraints verifiably restrict the original pool; otherwise locally tier traceable titles/abstracts/claim snippets. Missing words mean unknown/lower priority, not deletion based on abstract silence. Preserve original per-route ranks, resulting tiers and unsubmitted remainder. For resource-limited screening, use frozen tiers and round-robin routes within tiers.

Before convergence, show actual broad semantic sentences, relationship phrases by language, pool count/version, scope, convergence method and retention rules. Hashes/opaque references alone are insufficient. Provide a downloadable long PN/ID list with count/version/link. This is reviewable disclosure, without a repeated confirmation gate when scope is already decided.

Boolean, semantic and independent keyword searches are recall routes; within-pool keyword convergence is fixed-pool reranking. Routes need not all succeed. Degrade routes with failed jurisdiction/status filtering, zero eligible objects or service errors and exclude their ineligible results completely. Continue to pooling/Screening only if semantic routes pass the [replacement-sufficiency gate](references/semantic-retrieval.md), disclosing the missing route without claiming equivalent Boolean coverage from semantic counts. If the gate fails and continuation materially narrows scope, ask the client via [Customer prompts](references/customer-prompts.md) to continue limited routes or wait.

Read [Query iteration](references/query-iteration.md) only when optimization is requested. Fixed-sample metrics are local diagnostics, not database recall.

## Step 5.5: Status gate and other field filters

Before Screening, reconcile requested status-filter count / raw returned count / pending-or-active passes / `status_filter_leak` / status-unknown count. Move evidenced expired, withdrawn, abandoned, rejected, revoked/invalidated objects to status exclusions. Unknowns await verification and do not enter formal Screening or become low risk. Other assignee/classification/authority/date conditions follow confirmed client scope only. Distinguish hard restrictions from priority groups; retain the remainder and do not treat missing metadata/inference as nonqualification. Use current supported structured capabilities. See [Scope and selection](references/screening-selection.md).

## Step 6: FTO Screening

Submit retrieved, identity-verified, status-gate-passing search/list candidates to `patsnap-ip:screen_patents_for_FTO` under current runtime protocol. This workflow uses that filtering tool, without switching to other same-named services or substituting `field_analysis`, search ranks or local relevance scores. PN-list inputs do not inherit previous country/status/date filters; exclude inactive objects beforehand. Do not pass builder references as raw screening queries or fabricate absent fields.

After Skill/tool/service changes, run controlled [Screening acceptance](references/screening-acceptance.md). Correct binding alone does not verify useful ranking: a frozen graded list must show relevant items before noise, with invalid numbers, version mappings, mode confirmation and processing evidence checked separately. Small-list ordering does not establish production recall or legal risk.

### Fixed endpoint and mode handshake

On first use/protocol change, record protocol confirmation, request acceptance, server mode evidence and processing reconciliation under [Tool usage](references/tool-usage.md), then controlled acceptance. Acceptance is not actual-mode confirmation. Without server evidence, mark mode unconfirmed; an explicit mismatch stops the dependent chain. Timing, count and shape cannot establish mode.

Separate batch-call status from object-processing completeness. Reconcile submitted, explicitly processed, returned, unresolved, nonreturned, out-of-input, substituted and many-input-collapsed objects. Only explicit per-object statuses or verifiable equivalent details prove processing. If only candidates are returned, the input-minus-returned difference is “processing status not obtained,” not unavailable patent, screened out, irrelevant or low risk.

For changed returned PNs or unexplained nonreturns in list mode, produce rowwise identity reconciliation. A/B version folding requires the same application number or verified relationship evidence for the same application text; titles, family proximity and rank alone do not suffice. Record input PN, returned PN, application/relationship evidence, adopted version and source. Missing server reasons remain “not returned.” Do not resubmit evidenced mappings. For unexplained differences, run at most one compensating subbatch with the same solution/mode/input version. Add recovered objects with `reconciliation` provenance without altering original ranks. Remaining nonreturns stay “processing status not obtained.” Ask continue/wait only if this gap changes the client’s next scope; no endless retries.

For each candidate verify adopted version, claim basis, missing product facts, rationale stability and processing completeness. Missing tool content remains unavailable. Even all-success batches mean “all batch receipts obtained,” not every input processed.

Screening order is this receipt’s candidate priority, not a stable risk score. Do not repeat production inputs to cherry-pick more candidates. Acceptance/fault reruns compare identity sets, order and version mappings; record changes as `screening_rank_unstable` and preserve all receipts. Do not present one chosen order as certain global risk ranking or a random multi-run union as one complete Pro result.

## Step 6.5: Client selects CC scope and full-text strategy

Once receipts are parseable, handshake state is disclosed and the full catalog is frozen, obtain two independent choices. With `pro_requested_unverified`, label mode unconfirmed; with `mode_mismatch`, remain blocked. No server echo means no “Pro confirmed” claim.

Keep full requests/raw receipts as audit evidence, without dumping them in conversation/report body. Deliver a lightweight selectable catalog first. Fetch full text/lifecycle and run CC only for adopted objects. Unselected objects retain identity, original rank and receipt location without automatic detailed treatment. Label order “this Screening order,” not infringement risk. Show observed same-input ranking instability.

1. All candidates or a conditionally/manually selected subset for CC;
2. Whether to obtain and analyze complete descriptions before CC.

Without the client decision, do not call Claim Chart or automatically fetch candidate full text. No default all/top-N, silence or timeout. `scripts/select_cc.py` freezes catalogs/selections/batches and validates local records; it does not define MCP or authenticate real human approval.

If design rights appear and inclusion is unresolved, ask for technical invention/utility-model claims only or a separate design-right track. Do not mix designs into ordinary technical Claim Charts or silently delete them for lacking technical claims.

Selection is a scope decision, not status verification. Obtain lifecycle and full-text receipts per selected object before final batches. Move inactive/withdrawn selections to evidenced exclusions; unknown status or missing text blocks CC. A target-jurisdiction pending/active family/application alternative requires verified new identity, without silent substitution.

Lifecycle event names/numbers for invalidation, reexamination, limitation, correction or litigation without decisions, maintained scope and effective claims imply `current_claims_unverified`. An Active label cannot resolve this. Do not use original grant claims in blocking CC without evidence of claims effective at assessment time.

## Step 7: Claim Chart

Call `patsnap-ip:build_claim_chart` only on the frozen list passing current-status/adopted-text gates. Active grants use effective granted/corrected/reexamined/limited claims. Pending applications use latest available published or sourced amended claims, disclosing potential changes. If only a publication draft is available without proof it is current, make a bounded pending comparison without calling it current claims. Simplified status, risk or `include_in_report` fields cannot replace lifecycle eligibility, selection or adopted text.

Save each raw batch receipt and verify results/errors for every object. Partial returns, timeouts and mismatched identities stop dependent batches; IDs/download links do not prove analysis completion. For full-text enhancement first read [Full-text review](references/fulltext-review.md). Follow [Strong-evidence CC](references/claim-chart.md) for original claims, dependencies, complete translations, product evidence, interpretation conditions, unknowns and local opinions. Separate tool results from local legal/technical review.

Before report adoption, apply the label–row–conclusion consistency gate and inference-label review in [Strong-evidence CC](references/claim-chart.md). Unknown product facts, unsupported equivalence or unresolved interpretation preclude definite exclusion. Risk labels/numeric codes do not replace lifecycle checks.

## Step 8: HTML preview and final delivery

Organize the [unified report](assets/report-template.md) and first generate a self-contained customer HTML preview with [HTML preview template](assets/html-report-preview.html). Apply [Plain language](references/plain-language.md) to headings, notes, headers, statuses, conclusions and questions, understandable on first reading. Explain internal codes/acronyms at first use, then use plain terms. Include scope/facts, features, retrieval units/logic, keywords/synonyms/classes, Boolean/semantic routes and scopes, retrieval/screening count reconciliation, selections, itemwise CCs, conclusions and evidence gaps. Reference full receipts by location without repeating them.

Create “View original” patent links only from accessible URLs actually returned by search/full-text tools or verified official evidence. Do not construct URLs from PNs. Otherwise show “Original link not obtained,” keeping local evidence anchors/source locations.

Deliver HTML as a content-review draft and ask the client to confirm content and choose HTML, Word, PDF, Markdown or an explicit combination. Without confirmation label it preview, not final. Changes to facts, jurisdictions, queries, selections or evidence strategy restart affected nodes and produce a new preview. Layout/format changes alone do not rerun tools.

Before final generation read [Report structure and formatting](references/report-format.md) for cover, portrait/landscape sections, overview, per-patent CC, appendices and pagination. Render and inspect every Word page with available document capabilities; verify print layout for PDF. Cite solution, final queries/scope, actual windows, complete screening receipts, choices, all CC batches, full-text and lifecycle evidence.

Identify unsearched, unretrieved, nonreturned, unselected, CC-failed and evidence-pending objects. Selected CC completion is not worldwide/product clearance or completion of all search hits.

## Failure and recovery

- Record absent tools/unsupported protocol and stop affected chains without cross-stage substitution.
- Retry harmless reads once. For unknown Screening/CC state, inspect saved receipts before resubmitting.
- Fetch only basic full text needed for the step by default. If optional relationships fail authentication/permission and are unnecessary, retain the failure and retry once with the same identity excluding optional relations. Do not call it empty full text. Necessary relationship evidence cannot be silently dropped.
- Reuse completed identical nodes; redo affected downstream work only after solution, jurisdiction, query or candidate-version changes.
- Mark stages complete, reused, not run, awaiting selection or blocked. Technical analysis is not a final legal opinion.
