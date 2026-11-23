# Scope, Screening and CC strategy

Read before Steps 4–6.5. Connect user scope, official Screening receipts, user decisions and the current CC list. All record formats and strategy interaction are local orchestration, not new MCP parameters/tools.

## 1. Confirm jurisdictions while preparing technical input

Map manufacturing/import/sales/use to `activity | requested scope | adopted authorities/regions | pending regions | source/adoption decision | status`.

- China manufacturing plus worldwide sales are two scope requirements. Unresolved global scope is not agreement to CN-only first; do not complete CN CC before asking about overseas coverage.
- Execute all-authority search only if explicitly supported and verifiable, with database limits recorded. Otherwise resolve markets or explicit interim scope before Step 4. Do not invent global-scope values or assume omitted geography necessarily means worldwide coverage.
- US/EP/JP/KR are discussion examples, not global coverage. EP search differs from national effects/unitary protection; WO/PCT is not a globally enforceable right.
- Whenever EP appears, check country clarification. Ask before search if actual countries are unknown, or confirm EP-documents-only intent. Reuse explicit answers. Europe/EU/EPC are not the same scope.
- For adopted GB/FR/DE markets, authorities will typically include EP/GB/FR/DE. Add only adopted countries, not all Europe. Verify national effect/applicable claims separately in CC. Respect explicit EP-only scope and disclose absent national routes.
- Added countries create a scope version: retain old Q/C, choice and additions; reuse technical expressions. Establish the authorized new Q0 before Step 4 checks. Do not reject authorized expansion against stale EP-only baselines or silently remove scope protection. Recheck all OR branches/new C and invalidate affected candidate/Screening/selection versions.
- While global scope is pending, continue technical preparation in 1–3. An explicit first-branch instruction permits bounded work with gaps recorded. Do not re-ask settled scope.
- Keyword-region hints do not alter C. Check actual query/provenance in 4/5/6; multi-country scope must not collapse to one country.
- A verified combined query may cover multiple authorities. Keep separate receipts for branches. C listing several countries does not prove the retrieved window contains them: inspect candidate origins. If one authority fills the window, retrieve/screen adopted markets through appropriate branches and merge, without arbitrary equal quotas. Blocked branches remain gaps, not removed scope. CC follows actual all/partial choice, with no total cap of ten.

Pending applications and active grants are the default FTO scope, without requiring a separate client narrowing instruction. Search status is a candidate gate; lifecycle evidence is the separate pre-CC gate. Verify current status-code meanings for pending/active; retaining codes is not semantic verification. Record assessment date/source update time; execution date is not legal-event effective date.

For every search page record `requested_statuses`, `raw_returned_count`, `eligible_returned_count`, `status_filter_leak_count` and `status_unknown_count`. A requested filter does not prove execution. Move inactive/withdrawn leaks to exclusions; hold unknowns before formal pooling/Screening. Continue paging to fill the frozen eligible window when leaks consume slots; disclose incomplete windows at runtime boundaries without substituting raw counts for eligible counts.

## 2. Three query checks

1. **Scope:** use confirmed, actually effective structured scope only where the route protocol supports it. Exclusive/filter-ignored Boolean remains unrestricted diagnosis outside the formal jurisdiction pool. Unions contain verified-scope objects only; syntax success does not prove intent.
2. **Key concepts:** reference Step 2–4 retrieval units/query-plan and record `element | expression/query location | omission reason`. Routes may be terms, synonyms, classifications, supplementary retrieval or explicit Screening deferral; not every feature is ANDed together. Verify AND within a unit, OR across independent risk directions and classifications not accidentally becoming global gates. Repair unintended omissions locally and check syntax; recall priority does not waive checks and no dedicated clause does not prove zero coverage.
3. **Actual languages:** check concepts in Q or evidenced index/alternate coverage, not only K. Equivalent Chinese/English terms normally use OR. Tool output language does not constrain search terms/jurisdictions. Recheck adopted queries: complete vocabulary with CN-only structured geography is still CN-only search.

Ordinary gaps do not automatically enable Step 5. If sample diagnosis is needed, record why and the five-round limit. Passing sample coverage does not resolve Step 6 windows; overly broad queries with one retrieved window remain incomplete.

<a id="field-prefilter"></a>
## 2.5. Step 5.5 — Field prefilter before official Screening

Applicable to queries from 4/5, official auxiliary search candidates or supplied PN lists without requiring 5. Reuse upstream conditions; additional client-field filters may be skipped when absent, but the pending/active status gate remains mandatory. This selects objects **sent to Screening**; 6.5 selects objects **sent from Screening to CC**. Archive separately.

| Field | Official route | Boundary |
|---|---|---|
| Assignee/standard assignee | Available official entity disambiguation, then current search protocol | Different entity identifiers are not interchangeable; applicant field is not necessarily current owner. |
| Group/company tree | `patsnap-ip:get_corptree_hierarchy` for selected/direct-parent/root mappings | Not a full subsidiary list; use verified identities within requested scope and retain group gaps. |
| IPC | Current supported classification capability or verified Boolean class expression | Adopted user limits are allowed; AI predictions/vocabulary classes are clues. Main IPC does not exclude other classes. |
| Authority | Current supported structured geography | Reuse C and EP/country rules; grouping cannot delete other adopted markets. |
| Legal status | Current supported structured legal-status scope | Default all FTO recall routes to pending/active grants under current definitions. Unknown status awaits verification rather than being treated as active; search filters and lifecycle evidence remain distinct. |
| Dates | Current supported structured date scope | Distinguish filing/publication/priority/grant and boundaries; “last 20 years” does not replace validity checks. |
| Publication/application numbers | Current supported exact-number capability or verified list | Preserve full identities; family/A-B deduplication cannot erase relevant countries/claim versions. |

Use current MCP-declared capabilities only. Verify patent-type/other conditions against the official protocol or Boolean guide before use; do not add undeclared conditions. Preserve sources for identity, code tables, language and filter rules.

- **Hard limits:** explicit exclusive requirements/adopted rules may narrow the pool. Reuse known conditions. “Prioritize/first look at” is not exclusive. Out of scope is not no risk.
- **Priority groups:** process priority companies/classes first while retaining remainder/unknown groups within the plan and official within-group order. Overlapping queries may be used with an original-scope remainder route, or group a fully retrieved set. Uncovered remainder prevents complete Screening claims; priority is not a new official global risk ranking.
- **Clues/unknowns:** uncertain structures, AI inference, similarity thresholds and predicted classes cannot directly exclude. “95% similar to prior art” does not remove an infringement candidate here.

Ask only unresolved scope-changing priority/exclusive, identity or logical questions. Preserve AND/OR/negation: “company A or class B” is not their intersection. Prefiltering is optional.

PN-list Screening does not inherit search jurisdiction/status/date filters. Reconcile and remove ineligible objects before submission, rather than expecting Screening to remove them. Controlled mixed-status probes are not production batches. If runtime cannot express pending/active status reliably, mark the gate not pushed down and verify lifecycle before formal submission; do not guess codes.

When designs appear, suffix/title alone is not complete rights-type evidence. Resolve a separate design-risk track via customer prompts if scope is unclear. Technical claim charts and design comparison remain separate; disclose omitted tracks.

### Two routes

1. **Executable query → candidate list:** preserve original Q/N, technical Boolean and multilingual expressions; update only confirmed structured scope. Check runtime strategy support before scoped execution/paging into Step 6. With exclusive Boolean lacking scope support, retain diagnostic receipts only and build formal candidates using supported routes. Record old/new scope baselines and user basis; never reuse old N.
2. **Structured/mixed search/client number list → candidate list:** pass client publication/application numbers through the main list-import gate: `patsnap-ip:build_patent_boolean_query` creates exact OR, then `patsnap-ip:search_patent` retrieves and verifies real identities. Apply confirmed structured scope where present. Disclose original rows, duplicates, anomalies, unresolved identities, version mappings and actual windows. Submit verified objects to `patsnap-ip:screen_patents_for_FTO`, without presenting opaque Boolean references as other screening content. Existing lists stay within their original set unless expansion is requested.

If conditions cannot be expressed or semantics/logic are unverified, preserve original input and resolve the specific gap; do not guess parameters or switch to freeform summary screening. Push negative conditions only with verified Boolean/missing-value semantics, or filter a fully retrieved set locally from evidence.

**Two layers of missingness:** retrieved lists record matches/evidenced nonmatches/unknowns, retaining unknowns for screening/review without invented values. Database filtering may omit missing-metadata documents before retrieval; do not claim those unknowns were retained. If required, keep a supplementary route without that condition under the window plan; otherwise disclose the field-defined coverage limit. Not returned may mean missing metadata, window truncation or call failure, not proven noncompliance.

### Records and rollback

Reference local `prefilter.json` from case.md: original Q/list and version; fields/values/logic/purpose/user basis; requests/adopted Q/N or PNs/unknowns/exclusions; pagination/window/receipts/version/affected nodes. If the full pool was never saved, retain query/receipts/window, not a fabricated pool.

Show original hits, conditions/purpose, filtered hits or retrieved PN count, uncovered/unknowns and actual Screening entry. Use matching response counts; count lists only when obtained. Do not subtract overlapping/time-varying counts to infer exclusions. Deduplicate grouped unions by identity with provenance; do not sum group counts. Failures are not zeroes.

Relaxed/revoked rules restore the saved original query/pool, reuse unchanged technical input/valid receipts and redo affected retrieval/Screening/catalogue/strategy checks, not Step 1 by default. Reuse Screening only with identical technical/scope/query-list/mode-window input. New candidates do not inherit old itemwise choices. CC-list/evidence-depth changes alone do not rerun prefilters.

Old sample metrics belong only to their query/sample. New diagnosis needs an explicit evaluation version, not automatic five-round optimization. Reducing N below W does not establish original-scope completeness. Official Screening or valid reuse is still required.

## 3. Window strategy before Screening

W is the local retrieval window determined by current MCP, case budget and coverage objectives; N is the actual corresponding search total. Retrieve with `patsnap-ip:search_patent`, then submit actually obtained, identity-verified candidates to `patsnap-ip:screen_patents_for_FTO`. Planned window, retrieved count, submitted count and processed count differ. Judge candidates, unresolved objects and completeness only from real receipts; do not assume itemwise exclusion evidence exists for every input.

| Condition | Action |
|---|---|
| Known N≤W | No known window overflow; still check errors/receipts/visible coverage before claiming complete processing. |
| N>W | Adopt explicit limited-window review or a verified, workload-bounded sharding/retrieval plan before CC. |
| Unknown N | Obtain available counts/window evidence; if still unknown, treat scope as unresolved, not fully screened. |

Reuse explicit quick-review/window-sampling decisions. Do not downgrade requested full scope without a choice. Prepare coverage first, not 150 CC analyses followed by a truncation disclaimer.

Use connected official capabilities only:
- Shard executable queries by supported authorities/dates with verified union coverage and boundary/missing-value treatment. Overlap is allowed with deduplication/provenance. IPC is multivalued, not inherently disjoint; a few classes cannot silently omit the remainder.
- Retrieve candidates through semantic, keyword, Boolean and structured scope under current MCP pagination/reachable depth. Keep Boolean separate from semantic/keyword routes reusing confirmed structured scope only when explicitly supported. Exclusive Boolean is unrestricted diagnosis only. Record actual retrieval boundaries; beyond reachable windows use verifiable authorized shards or a disclosed limited window, never a full list.
- Submit actually retrieved and verified candidates to `patsnap-ip:screen_patents_for_FTO` under runtime entry limits. When batching, preserve actual requests, receipts, unresolved objects and original order. Explicit lists cannot recover unsearched objects; nonreturned objects are not evidenced exclusions.
- Estimate shard count, reachable bounds and budget first. Resolve a feasible plan before large work with unknown budget; do not recursively exhaust data or add unsupported technical exclusions merely to fit a window.

All hits from one query still do not prove 100% true recall; this addresses known-result window coverage only.

## 4. Preserve official Screening evidence

New search paths require actual `patsnap-ip:screen_patents_for_FTO` or valid previous receipts for the same solution/scope/query/mode. Save tool name, complete credential-free request, input version, raw receipt, business status, query/window, actual returned list, unresolved and nonreturned objects. For each object check adopted version, claim basis, missing product facts, rationale stability and processing completeness. Unavailable content is “Not returned by tool,” without local fabrication. Completion prose or search/semantic ranking cannot replace receipts.

Use only Screening entry paths declared by runtime MCP. Do not invent parameters or present opaque Boolean references as other business content. Apply custom criteria in retrieval/local records without claiming tool adoption. If itemwise reasons are absent, do not invent exclusion evidence. Adjust saved actual inputs explicitly for rescreening and create request versions.

User-directed company/module/experience rules may guide rescreening with old/new pools and rationale. Field prefilters follow section 2.5 and never replace Screening. Preserve remainder for priority groups and record hard-scope exclusions separately. IPC, semantic scores, industry context and unknown facts alone cannot justify exclusion.

For explicit direct comparison, first verify identities through the main list-import gate and obtain adopted originals with `patsnap-ip:fetch_patent`, then enter 7 with “Screening not executed: specified-object comparison.” Generic lists/search results/supplier reports do not automatically qualify. Pure review of existing CC may reuse old results.

Keep hits, requested window, returned candidates, selected count and actual CC count distinct. If receipts omit processed counts/exclusion reasons, state “Not returned by tool”; submitted minus returned does not prove exclusions. Returned candidates do not prove only those deserve attention.

Keep identity matching, request submission, successful batches, obtained claims, explicitly processed objects and returned candidates separate. A candidate-only receipt cannot prove full processing. Reconcile PN changes with same-application numbers or explicit relation evidence in a rowwise table, not titles/family proximity alone. Record input PN, returned PN, relationship, adopted version and source; missing server reasons remain unavailable. Do not resubmit evidenced mappings. Compensate unexplained differences once with the same solution/mode/version; label recovered objects `reconciliation` without changing original ranks. Remaining differences retain unknown processing status.

Repeat identical production requests neither to accumulate candidates nor choose favorable ranks. On controlled/fault reruns compare sets/order/mappings; record `screening_rank_unstable`, preserve receipts and avoid certain global risk rankings. Count identity matches, submissions, batches, explicitly processed objects, returned candidates, processing unknowns, selected objects and actual CCs separately. All batches successful never means all inputs processed.

## 5. Step 6.5 — Independent strategy interaction

State chain: `Screening success → lightweight catalog → awaiting_user_strategy → user_confirmed → lifecycle_and_text_gate → optional full-text review → batched CC`. All/some applies to returned Screening objects, not the earlier search pool. No fixed total; ≤10 per batch is local verification, not an API limit.

Two independent choices may be answered together:
- CC scope: all current catalogue, or some by assignee/status/authority/manual selection/explicit combination.
- Evidence depth: full-description acquisition/analysis before CC, or no advance full-description analysis while retaining complete claims and necessary interpretive evidence.

Fulltext works with either scope. Wait for missing choices; default neither to all nor a top-N subset. Explicit “all candidates, no advance fulltext” needs no itemwise re-confirmation.

Keep full raw Screening evidence in case files, without repeating it in dialogue, selection pages or report body. Deliver the lightweight catalog with mode/completeness notes first; only adopted objects receive lifecycle/text verification and, after passing, optional full-text enhancement and CC. This local traffic/status gate does not change the service protocol.

### Lightweight catalogue and partial selection

- Make every returned candidate selectable through a downloadable/paginated page, without pasting all detailed reasons into dialogue. Retain actual source order/provenance. Group order is not global risk rank. Deduplicate cross-group IDs while preserving locations; do not merge distinct national family rights. Do not force new Screening merely for selection UI.
- Keep stable ID, PN, title, assignee, jurisdiction/status, original rank/group, brief selection reason and completeness only. Link detailed reasons to raw receipts. Reuse search/Screening metadata without batch full-text calls to fill the catalog; unavailable remains marked. Do not confuse applicant/current owner, standardized names, group scope or status source/date.

- Clarify AND/OR and assignee matching. Current UI uses OR within a field, AND across fields; text search changes display only. UI supports assignee/status/authority/manual choices; other rules can be recorded in dialogue as reviewable IDs.
- Unknown/unverified metadata does not automatically fail filters. Preview conservatively retains potentially matching unknowns for review; users may explicitly include/exclude them. Unselected means not in this CC, not no risk.
- Before confirmation show total/selected count and list, conditions/unknowns, batches ≤10 and evidence option. Resolve actual budget/workload conflicts without invented prices/times or automatic truncation.
- Resolve one-authority-dominated multi-market windows first under sections 1–3. Selecting all cannot recover unsearched countries/window-external objects.

### Local helper (not MCP)

Requires Python 3 standard library only. Ten per batch is a local verification/current-adapter ceiling, not a permanent MCP claim; obey stricter runtime limits.

Read complete `patsnap-ip:screen_patents_for_FTO` receipts and reconcile submitted, returned, unresolved and nonreturned sets before saving local `step6-final.json`. This is selection-script input, not an MCP response schema:

```json
{
  "schema_version": "fto-screening-evidence-2",
  "results_complete": true,
  "sources": [{"path": "/absolute/path/fto-screening-result.json", "sha256": "actual-file-sha256"}],
  "submitted_pns": ["Actual submitted publication number"],
  "identity_remaps": [{"input_pn": "Application-publication PN", "returned_pn": "Returned grant PN", "reason": "Verified same-application version relationship"}],
  "unresolved_pns": [],
  "nonreturned_pns": ["Input PN absent from returns without an explanation"],
  "records": [{
    "patent_id": "actual-internal-id",
    "pn": "Returned and verified PN",
    "evidence_refs": [{"source_index": 1, "pointer": "/actual/result/path"}]
  }]
}
```

Sources contain genuine Screening receipts; pointers locate actual returned-candidate JSON objects. `records` contains service-returned candidates only, without invented keep/exclude labels. Record identity remaps only after `patsnap-ip:fetch_patent`/`patsnap-ip:fetch_patent_lifecycle` verification; same-application A/B deduplication also needs explicit mapping. Submitted PNs, mappings, unresolved and nonreturned PNs disclose input coverage together. Nonreturned objects are neither low risk nor evidenced exclusions. Set `results_complete=true` only after all planned batches have been obtained and parsed; this means local planned receipts are complete, not that the service processed every input or should return every input.

`prepare` creates the complete catalog and an unselected strategy page:
```bash
python3 scripts/select_cc.py prepare --screening /absolute/path/step6-final.json --case-id case-id --input-version v1 --scope 'Actual countries, authorities, window and gaps' --language en --out /absolute/path/cc-catalog.json --html /absolute/path/cc-select.html
```

The operator must verify that each catalog object came from actual Screening returns. The script validates source files, identities and pointers, not model reasoning. List unresolved/nonreturned PNs separately in scope notes, without presenting them as candidates or evidenced exclusions. Optional metadata: `{by_patent_id:{ID:{title,assignees,jurisdiction,legal_status,screening_reason,completeness,url,source_ref}}}` via --metadata. `screening_reason` is one short selection reason; `completeness` records receipt completeness. Do not embed abstracts, claims or full descriptions. Repeat --screening for multiple normalized records with their own provenance, not a fabricated merged official receipt. Pass `--language zh` or `--language en` explicitly to match the adopted output language. For another requested language, localize the full selector while preserving its catalogue, selection logic and source evidence.

After actual user reply or submitted UI JSON:

```bash
python3 scripts/select_cc.py confirm --catalog /absolute/path/cc-catalog.json --choice /absolute/path/user-choice.json --user-action /absolute/path/actual-user-reply.txt --out /absolute/path/cc-selection.json
python3 scripts/select_cc.py validate --catalog /absolute/path/cc-catalog.json --selection /absolute/path/cc-selection.json --lifecycle /absolute/path/lifecycle-gate.json --batch 1
```

Choice schema `fto-cc-choice-3`: catalogue hash, strategy=all/subset, selected_patent_ids, evidence_mode=claims/fulltext; subsets also retain subset_method=manual/filters and conditions. All must equal the whole catalogue. Missing either choice prevents runnable batches. Ordered batches contain ≤10. Every validation requires `--lifecycle`; fulltext also requires `--evidence` under the full-text reference.

The script validates format, all submitted identities, source/result hashes, pointers and selection sets. It cannot authenticate humans, full server-result reading, exclusions, market coverage or legal opinions. Never fabricate actual replies. Reuse real choices and ask only missing fulltext decisions; automated picks are not user choices.

### Lifecycle and adopted-text gate before CC

After client selection, obtain `patsnap-ip:fetch_patent_lifecycle` per selected object for the target jurisdiction/date and `patsnap-ip:fetch_patent` for the actual adopted text. Save local `lifecycle-gate.json` (not MCP response structure):

```json
{
  "schema_version": "fto-lifecycle-gate-1",
  "selection_sha256": "Canonical JSON SHA-256 of cc-selection.json",
  "assessment_date": "Assessment date",
  "reviews": [{
    "patent_id": "Selected PID",
    "eligibility": "active_grant | pending_application | ineligible | unknown",
    "adopted_pn": "Actual adopted CC publication",
    "text_basis": "current_grant_claims | current_post_grant_claims | current_pending_claims | published_pending_claims | unavailable",
    "status_label": "Actual tool status and short rationale",
    "lifecycle_record": {"path": "/absolute/path/lifecycle-receipt.json", "sha256": "Actual file SHA-256"},
    "text_record": {"path": "/absolute/path/adopted-text-receipt.json", "sha256": "Actual file SHA-256"}
  }]
}
```

- `active_grant`: potentially subsisting rights in the jurisdiction at the assessment date, using grant or evidenced corrected/limited/reexamined claims.
- `pending_application`: still pending; prefer sourced latest amended claims. Published-only claims use `published_pending_claims` and disclose that they may not be current prosecution text.
- `ineligible`: inactive, expired, terminated, withdrawn, abandoned, rejected or revoked/invalidated rights outside current blocking scope; retain exclusion evidence and omit CC by default.
- `unknown`: unresolved lifecycle, national effect or text; hold without treating as active.

Invalidation, reexamination, limitation or correction event names/numbers/dates without decisions, maintained scope and effective text require unknown eligibility/unavailable text and `current_claims_unverified`. Active database labels alone cannot establish `active_grant`.

Same-application A/B mapping needs identity/lifecycle evidence. Other applications, divisionals, continuations and national EP rights require separate verification; an active family member cannot revive an inactive object.

Before each batch:

```bash
python3 scripts/select_cc.py validate --catalog /absolute/path/cc-catalog.json --selection /absolute/path/cc-selection.json --lifecycle /absolute/path/lifecycle-gate.json --batch 1
```

Every object must be an active grant/pending application with traceable adopted PN/text. Ineligible, unknown or unavailable objects fail the batch. Separate excluded/pending objects from runnable batches and disclose counts/evidence; a validation failure is not low risk.

Catalogue/proposal/scope changes create versions and require affected strategy review. Criteria may be reused, but new candidates do not inherit itemwise authorization. Evidence-depth-only changes do not rerun search/Screening. Reuse completed official CC; new description evidence changing interpretation requires row review and opinion history. New solution facts require verification and a new solution version. Interpretive opinions and dependent-claim review remain local; do not claim tool writeback, and rerunning alone does not prove evidence adoption.

## 6. Handoff and delivery

Before 7 show countries/search languages/gaps, prefilter scope if any, N/W, returned M, all/partial/count, fulltext/readiness, batch plan and actual user decision. Do not re-ask settled matters. Pending strategy permits candidates/questions, not CC/report completion.

Every selected object gets the required original/translation/evidence CC regardless of local risk opinion. Retain unselected lists labeled “Not included in this CC”; selected unfinished objects need concrete reasons, never low-risk placeholders.

Step 8 uses ID-matched official results for the adopted list with original fields unchanged; store full-text/local review separately. Denominators are adopted objects. CC completion on returned candidates is not completion of all hits or markets.
