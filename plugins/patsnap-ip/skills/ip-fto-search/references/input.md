# Input and intent: a correctable case card

## 1. Ask only questions that change the route

Read existing material first. Use short prompts such as “I understand the main objective is …; is A or B closer?” Allow uncertainty/free text without steering users to a predetermined answer.

| Topic | Clarify | Execution impact |
|---|---|---|
| Decision | R&D exploration, design freeze, launch/export, old-report review | Exploration, formal scope or review |
| Object/scope | Product/module/configuration, manufacturing/sales/use countries, dates, and whether to include a separate design-right track | Separate cases, search scope, applicable claims and comparison tracks |
| Existing assets | Proposal, query, patent list, CC, report; column meanings, original order and changes this time | Entry/list-import gate/reuse |
| Tradeoffs | Unsettled technology, required objects, deadline/budget, first deliverable | Evidence gaps and batches |

Usually 3–5 exchanges suffice; combine topics and reuse known answers. Wait only for ambiguity affecting current correctness; mark other items pending. Without jurisdictions, unrestricted technical exploration is possible but is not country-specific FTO. Chinese input does not imply CN.

### Scope card before the first formal call

Show and save plain-language `product/configuration | manufacturing countries | import countries | sales countries | use countries | search authorities | assessment date | evidence cutoff | unresolved items`.

- **Assessment date:** when rights must be pending/active and conclusions apply. If absent, propose the current date explicitly and obtain confirmation; do not silently insert it.
- **Evidence cutoff:** last relevant collection date for searches/lifecycle/other evidence. Update with evidence; it is not automatically the assessment date.
- **Patent-date filters:** filing/publication/priority/grant restrictions need a client request or evidenced case rule. Neither assessment nor evidence cutoff is an automatic filing/publication lower bound.

Unconfirmed items permit only clearly labeled technical exploration. Missing activity countries, actual European countries or assessment date must be resolved before formal jurisdiction retrieval, Screening or CC. Pure report review still discloses whether the original report’s countries and dates are known.

After scope confirmation record `execution_mode=continuous_ai` or `execution_mode=stage_confirm`.

- Continuous AI execution optimizes and advances within confirmed scope, pausing for mandatory client decisions, scope changes, decisive missing facts or result conflicts. It does not authorize new countries, rewritten facts, expanded client lists, skipped lifecycle checks or AI-selected CC scope.
- Stage confirmation shows adopted input, changes, reasons, expected effects and gaps before the next major stage and waits for confirmation. Pagination, reading, formatting and one bounded retry within a stage do not need repeated confirmation unless scope, cost or result meaning changes.

Do not begin the first formal business call before the execution-mode choice. Show the choice once, separately from later mandatory decisions. Switch at safe points and record time/effective stage.

Distinguish priority competitors from exclusive assignee scope. Industry/group inference is not a hard filter. Reuse explicit assignee/classification/country/status/date conditions; clarify only unresolved hard-limit/priority and AND/OR logic, without a forced extra question. Separate products/mutually exclusive implementations.

## 2. Minimum card

- **Requirements:** decision/stage, configuration/module boundary, manufacturing/import/sales/use activities and respective jurisdictions, search authorities, assessment date, evidence cutoff, execution mode, assets, priority/exclusive scope, deadline/budget and first result.
- **Evidence:** technical quote/faithful excerpt + location + nature (actual assertion/plan/customer uncertainty/AI inference) + verification state (not independently checked/verified/conflicting).
- **Process:** simplified/full/partial route, T/input version, query/list, client-list import disclosure, steps 1–8, 5.5 rule version and original/new pools, 6.5 awaiting/confirmed/not analyzing, all/partial conditions/list, full-description option and acquisition/analysis state, interpretation sources, changes/next step.

For client lists, identify publication numbers, application numbers, patent records or other fields and fix the objective: Screening, direct comparison, original-text retrieval or a combination. Preserve original rows, blanks, duplicates and display formats; normalization creates a mapping rather than overwriting the client file. Number lists enter Boolean construction/search through the main list-import gate; N received rows are not N imported patents.

Also freeze one summary line: **actual manufacturing/sales/use countries, search authorities and unresolved regions; complete coverage or adopted window; post-Screening all/partial CC and actual count; full-text option; receipts and strategy references**. For “Europe/EU/EP/EPO” without actual countries, distinguish EP-document retrieval from FTO for specific European markets. The latter requires target countries and EP plus necessary national routes under the screening rules. Until clarified, only unrestricted technical exploration is allowed, without a “European FTO” conclusion. “Worldwide sales” does not remove unresolved overseas scope; workload does not authorize taking only the first ten.

All three sections may share `case.md`; retain originals/receipts separately. Confirmed plans remain plans; report assertions retain report provenance. Preserve old/new values when users change facts and update affected work without overwriting originals with summaries.

Record prefilters as `field/value and AND-OR logic | hard limit or priority group | requirement basis | unknown/remainder handling | adopted version`. Apply explicit jurisdiction, legal-status and date conditions through current structured search scope in Step 4 and reuse them after Step 5.5 checks. Do not put them into the technical Boolean or append them twice. Prefilter-only changes reuse technical input and restart affected retrieval/screening, not polishing. “All CC” after prefilter still means all subsequent Screening candidates.

Before CC, organize product evidence as `element ID | product element | present/absent/unknown | quote/image and location | version/configuration | nature and verification`. Only explicit counterevidence supports absent; silence means unknown. Plans, hypotheses and measurements differ. Preserve originals and reference this record by element ID in CC.

Reuse this card at CC; ask only new material ambiguities. Record disputed legal interpretations as adopted conditions with authority; user preference is not legal authority. Analyze fixed hypothetical configurations separately with conditional conclusions.

## Language and jurisdiction are independent

These are orchestration records, not new API parameters:

| Axis | Record/use | Must not imply |
|---|---|---|
| `input_language` | User's main language; preserve original technical input | Chinese input means China-only search |
| `output_language` | English by default for this release, or explicit user choice; UI/report agree | Search-term/source-evidence language |
| `search_languages` | Chinese/English/other terms and field/index coverage by jurisdiction | An official parameter or guaranteed semantic coverage |
| Countries/authorities | Actual `target_markets`, `search_authorities` C, pending regions | EP documents prove national effect or authority filters prove full market coverage |

Record actual `tool_language` separately: prod_us generates English, other environments Chinese. Local keyword-region preferences are not API fields. Generation language or Chinese proposals cannot reduce C to CN.

- Identify input language from the task instruction or standalone proposal. Foreign patents, attachments and tool returns do not switch it. If genuinely ambiguous mixed input matters, ask once. Explicit language requests update the card; do not repeatedly reconfirm.
- All visible explanations, stage results, headers, legends, notes, comparison opinions and local reports use `output_language`. Template English is default copy, not a prohibition on requested languages.
- Preserve labeled evidence originals, document numbers, source titles, code and queries. When evidence differs from output language, CC requires complete itemwise translations alongside originals. Never delete originals for consistency or let foreign evidence switch narrative language. Localize displayed enum labels while preserving original enums in receipts/annotations.
- Each tool’s language capabilities and invocation follow the runtime MCP protocol. Construction/search tools do not automatically change scope with delivery language. Preserve raw receipts and localize presentation to output_language with translation provenance. Delivery language does not change source evidence, search languages or jurisdictions.
- Translate locally from actual originals, retaining complete mappings and labeling AI/human translation/review provenance. If a tool returns the wrong language, preserve its response and correct presentation; do not call machine translation original or officially certified text.

### Implement search-language coverage

1. Check Chinese/English terms in Step 3 by adopted authorities, query fields and verified index/translation capabilities. Overseas searches from Chinese input need equivalent English technical terms; non-English jurisdictions need local-language routes or verified cross-language indexing. English does not automatically cover Japanese/German documents. In Step 3 perform one targeted translation/synonym check for each adopted priority language, once per language rather than country. Reuse established language plans.
2. Do not replace original P with a full translation. Keep `original concept | search expressions by language | source/nature | adopted query location/coverage basis`. Preserve structure, action, quantities, negatives and relations. New mechanisms/uses/materials/effects remain inference. Synonyms are not CC product facts.
3. Check K in 3 and actual Q before adoption in 4/5. Language equivalents are usually OR branches, not Chinese AND English forcing bilingual matches. Classifications/other verified routes may supplement coverage; English characters or one English term do not establish core-concept coverage.
4. Repair necessary terms under the same P or use available official searches for terminology. Locally edit Q under Step 4 scope/execution checks with provenance/change records; do not restart the entire workflow for translation. Keep feature receipts unchanged and K separate, without invented fields. Recheck language/scope after execution too.
5. For auxiliary multilingual semantic exploration, preserve each expression/language/receipt, merge by ID with provenance and use Step 6 PN entry as needed. Do not assert automatic multilingual coverage from the model alone. Disclose specific gaps; resolve requested scope rather than silently reverting to Chinese-only search.

Example for an English-release task submitted in Chinese: `input zh | output en unless explicitly changed | search zh+en (other languages verified by jurisdiction) | C=authorities derived from adopted countries`. If overseas patents are absent, check whether authority scope was incorrectly reduced to CN; if terms are Chinese-only, inspect K/Q. Adding English terms does not remove existing CN structured scope.

One clarification suffices: “Is this EP-document retrieval only, or FTO for specific European markets? For the latter, please confirm countries.” Reuse explicit countries or EP-only instructions. Label EP-document scope as document retrieval, not European-market scope. GB/FR/DE markets might use `target_markets=[GB,FR,DE]`, `search_authorities=[EP,GB,FR,DE]`, `search_languages=[en,fr,de]`; this example is not a user choice. National effect, unitary effect and UPC checks remain separate from search scope.

After Screening, independently resolve `CC all/some (conditions/list)` and `advance full-description analysis yes/no`. Both all+fulltext and partial+claims are supported. Ask only missing choices; fulltext does not automatically expand selection.

Use one combined prompt from the main Skill’s customer-prompts reference when needed. Reuse existing answers rather than asking to demonstrate the process. Customer-facing text follows the plain-language reference; template language does not fix delivery language.

## 3. Technical clarification: six optional angles

Understand who does what to whom, under which conditions and by which means. Check **objects/components, actions/connections, materials/processes, control/timing, application boundaries, problems/effects**.

Company domain, supply chain and system context may reveal missing questions. TRIZ only guides questions; do not force power/transmission components into every proposal. Unstated materials/mechanisms/effects are AI inference or pending confirmation. Add only search/comparison-relevant information.

If input is insufficient, official semantic search may supply sourced terminology/problem/effect clues for key questions. Inventors need not confirm every synonym; new technical meaning that changes understanding does require confirmation.

## 4. Keep the adopted solution concise

Order: **purpose/object → components/relationships → operation/conditions → problem/effect → unknowns**. Preserve necessary quantities, units, negatives, sequence and materials. Do not remove ordinary components as “non-inventive.”

- Search: facts plus clearly labeled exploratory concepts; unknowns may aid retrieval and alternatives remain distinct.
- Screening/CC: actual configuration, provenance/nature and key unknowns; exploration is not implementation and silence is not absence. Hypotheses need separate conditional analysis.

Keep fact/plan/unknown/search-only sections within one adopted P rather than freely rewriting it between stages. Version proposal changes and revisit affected downstream work. Save sent-version/original mappings. Clear simplified input may bypass Step 1; full mode/difficult text/images use local preparation and verify no lost conditions. Preserve images; unread images remain pending. Submit text and attachments under the extraction tool’s current protocol, preserving their correspondence; image interpretation is not verbatim evidence.

Do not insert jurisdiction, interpretive preferences or custom CC prompts into P and claim they override backend rules. Call `patsnap-ip:build_claim_chart` under the current protocol with frozen solution and selected patent identities clearly distinguished. Verify jurisdiction, interpretation and dependent claims against actual claims/lifecycle evidence; do not claim local opinions were written back to the tool.
