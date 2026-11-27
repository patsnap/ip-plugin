# Search methods

## Organize queries and converge

Investigate decisive structures, connections, positions, action conditions and process relationships of the complete solution. Consider the primary combination, independent methods and valuable alternatives separately; verify disclosure assertions about existing art. Local queries may be compressed but do not represent the whole disclosure.

Select semantic discovery, exact terms, field filters, Boolean queries, further original reading or citation expansion according to uncertainties, without fixed three-round or Top5 rules. If a leading conclusion depends on another document lacking a relationship, seek the counterexample most likely to change it. Do not add fixed recheck rounds once evidence is sufficient.

Retrieval and reading are not limited to five documents. Rank strong candidates by decisive-relationship coverage, evidence adequacy, complementary differences and independent-method value; this order is not the service's original ranking. Check other strong candidates after identifying a source family. Converge when remaining uncertainties are unlikely to change the main judgment, without filling a quota.

Choose closest art as the most reasonable starting point for a complete modification, rather than the largest number of matching features. Compare documents with different purpose, overall layout or interfaces against candidates closer to the primary combination even if their local match counts are higher.

Group families and corresponding applications as one technical evidence group while retaining each jurisdiction’s exact publication identity. Count candidates separately from independent technical routes. Check core documents in a supplied prior report/list against the current pool; retrieve missing documents or give an evidenced exclusion reason instead of copying conclusions.

Inventive-step supplementation seeks a complete Y-role teaching, rather than a missing part alone: a reason, functional link or problem-based teaching to adopt the difference under the target jurisdiction, compatible with the primary document’s structure and operating conditions. Search unresolved difference groups separately. Disconnected parts without combination teaching remain A background or Y candidates rather than accumulating document counts.

## Mixed semantic and keyword retrieval

Use mixed retrieval to cover alternative expressions while retaining complete technical relationships; the channels are not a Boolean AND. A single request can enable `semantic` and `keyword`. Deduplicate exact publications and families while retaining channel provenance.

| Input | Content | Avoid |
| --- | --- | --- |
| `semantic_query` | Technical object, complete component/step relationships, position/order, problem and overall function in natural language | Synonym piles, field codes, applicant/date/IPC conditions |
| `keywords` | Complete precise mechanisms, material/parameter concepts, customary industry names, abbreviations and equivalent Chinese/English/Japanese relationship phrases | Independent generic words such as laser, lens or control |
| `filters` | Confirmed dates, jurisdictions, assignees and statuses | Treating the assessment jurisdiction as an automatic national-only retrieval restriction |

The inputs must complement each other. Semantic input is normally a coherent paragraph; keywords normally comprise 3–8 complete concepts or relationship phrases. Multilingual terms cover real expression differences rather than translating generic words to fill a quota. Dual-channel hits may receive reading priority, but do not establish disclosure or X/Y/A roles.

### Relationship propositions and their sources

Express each decisive technical relationship as a testable proposition. Record:

- `subject` — the component or step that acts or participates.
- `relation` — the action, connection, position, transmission, trigger or interaction.
- `object_or_condition` — the object, state or condition to which the relationship applies.
- `constraints` — the disclosed position, sequence, direction, quantity, size, clearance or state change. An empty array is valid when the disclosure supplies none.

For example, a detector and two gratings name three parts. A testable relationship specifies that detecting removal or installation of the detector or either grating triggers preliminary irradiation to detect a relative position error. Express the complete proposition and technical purpose in `semantic_query`. Use industry phrases that bind the parts and actions in `keywords`.

Store a `relation_proposition` with each `relation` query:

```json
{
  "subject": "blade guard",
  "relation": "slides lengthwise along the handle guide",
  "object_or_condition": "extended to cover the blade and retracted to expose the blade",
  "constraints": ["the guard is detachable from the knife body"],
  "source": "disclosure",
  "source_refs": ["feature-plan.json#comparison_units/2"]
}
```

Use only `disclosure`, `user_clarification` or `candidate_feedback` as the source. For `candidate_feedback`, record `source_publication_number` and point `source_refs` to a saved full-text receipt and a specific passage. Keep scoring references, hidden ground truth, answer keys and target abstracts seen after unblinding out of formal queries. If used for diagnostics, label the experiment as having exposed the reference answers. Its results cannot establish a blind-retrieval improvement.

To expand a relationship with synonyms:

1. Identify one parent `relation` query in `derived_from_query_id`. Inherit its exact `comparison_unit_numbers` and relationship source.
2. Expand `subject_variants`, `relation_variants` and `object_or_condition_variants` separately. Add one `constraint_variant_groups` entry per original constraint, linking it with `source_constraint` and retaining the original and equivalent expressions in `variants`. Preserve the technical meaning.
3. Recombine the slots in `composed_phrases`. Record the complete `text`, its `language`, the chosen slot variants and one expression from each constraint group. Avoid mechanically generating every combination of variants, which can produce unnatural phrases, omit constraints or misstate the technical relationship.
4. Use `composed_phrases[].text` as the actual `keywords` in the same order. Run mixed retrieval with a `semantic_query` that preserves the complete relationship.

```json
{
  "query_id": "Q3",
  "route": "synonym",
  "derived_from_query_id": "Q2",
  "comparison_unit_numbers": [2],
  "semantic_query": "A removable blade guard moves along a longitudinal guide to cover or expose the blade.",
  "keywords": [
    "可从刀体分离的刀具护罩沿手柄导槽滑动并覆盖或露出刀刃",
    "removable blade guard sliding in a longitudinal handle guide to cover or expose the blade"
  ],
  "relation_synonym_expansion": {
    "subject_variants": ["刀具护罩", "blade guard"],
    "relation_variants": ["slides lengthwise along the handle guide", "沿手柄导槽滑动", "sliding in a longitudinal handle guide"],
    "object_or_condition_variants": [
      "伸出时覆盖刀刃、缩回时露出刀刃",
      "extended to cover the blade and retracted to expose the blade"
    ],
    "constraint_variant_groups": [{
      "source_constraint": "the guard is detachable from the knife body",
      "variants": ["the guard is detachable from the knife body", "可从刀体分离", "removable from the knife body"]
    }],
    "composed_phrases": [{
      "text": "可从刀体分离的刀具护罩沿手柄导槽滑动并覆盖或露出刀刃",
      "language": "zh-CN",
      "subject_variant": "刀具护罩",
      "relation_variant": "沿手柄导槽滑动",
      "object_or_condition_variant": "伸出时覆盖刀刃、缩回时露出刀刃",
      "constraint_variants": ["可从刀体分离"]
    }, {
      "text": "removable blade guard sliding in a longitudinal handle guide to cover or expose the blade",
      "language": "en-US",
      "subject_variant": "blade guard",
      "relation_variant": "sliding in a longitudinal handle guide",
      "object_or_condition_variant": "extended to cover the blade and retracted to expose the blade",
      "constraint_variants": ["removable from the knife body"]
    }]
  }
}
```

For weak retrieval, list every comparison unit that could still change the conclusion in `retrieval_assessment.decisive_comparison_unit_numbers`. Cover each with at least one `relation` query before ending retrieval.

### Retrieval levels

Choose levels by actual uncertainty, without fixed rounds:

1. **Complete primary combination:** express overall structure and purpose semantically, with 2–5 discriminating relationship groups as keywords to discover overall closest art.
2. **Key subcombinations:** search independently expressible optical paths, mechanisms, control chains or method steps while retaining connections/order.
3. **Decisive uncertainties:** pair function/problem semantics with precise structural keywords to seek counterexamples and secondary documents for differences affecting conclusions.
4. **Terms and citations:** update keywords using actual strong-candidate terminology and extend citations when useful; citation counts do not establish relevance.

Iterate when strong candidates come only from one channel and the other channel’s terms are clearly mismatched, abstracts reveal missing synonyms, decisive relationships remain merely “not mentioned,” or new structures may change conclusions. Low counts, repeated candidates or an unmet round quota alone do not require further retrieval.

Basic request shape:

```json
{
  "search_strategy": ["semantic", "keyword", "filter"],
  "semantic_query": "Complete technical intent, component relationships and problem",
  "keywords": ["Complete concept in Chinese", "English technical relationship", "Equivalent Japanese technical relationship"],
  "filters": {"date_type": "publication", "date_to": 20201231},
  "limit": 20,
  "offset": 0,
  "collapse_family": false
}
```

If the date is unknown, omit `filter` and `filters`; do not substitute the test or search date.

### Fill the reading queue after deduplication

Set `target_unique_groups` before the first call on each discovery route. For a recall-sensitive Top 100 evaluation, target 100 distinct technical groups. For client work, use the planned review capacity. Keep the target fixed regardless of which documents appear.

Build two views from the first and subsequent pages:

1. **Publication ledger.** Treat the publication aliases in one result, including its `pn` array, as one identity. Keep distinct publications separately with their original rank, page and query ID.
2. **Reading queue.** Group by a tool-supplied family ID or a verified family. When family information is missing, provisionally group only exact normalized title matches. Otherwise use the publication identity. Start with the highest-ranked representative of each group.

An exact-title group suppresses duplicate reading only. Preserve every publication, its date and jurisdiction. Update groups as family evidence becomes available and split same-title groups when the technical content differs.

While `unique_group_count < target_unique_groups`, change only `offset`. Keep semantics, keywords, filters, sort order, language and family-collapse settings fixed. Save each original receipt and append its results to the publication ledger. Stop when:

- The number of distinct technical groups reaches the target.
- The current page returns fewer results than the requested `limit` or the reported total is reached.
- The tool’s pagination window is exhausted.
- The user’s stated time or budget limit is reached.
- The tool fails and recovery with the original request also fails.

If the target is not met, record the actual stopping reason. Disclose any shortfall caused by budget limits or tool errors in the report limitations. Such a shortfall cannot support a claim that retrieval was sufficient. Use `scripts/dedup_fill_results.py` to summarize consecutive pages and read `status` and `next_offset`.

```sh
python3 scripts/dedup_fill_results.py calls/Q1-page-*.json --target 100 --page-size 100 --output calls/Q1-dedup-fill.json
```

The script’s `exact_title_provisional` label applies only to the reading queue. Preserve all exact publication identities in `candidate-ledger.json`.

### Review and reconstruct search routes

After filling the queue, review at least 20 distinct technical groups from the combined leading results before rewriting the queries or deciding to stop. Record verifiable observations and the decision in a route review entry:

- Participating query IDs and sample receipts.
- Number of distinct families or provisional groups, and number of results sharing the dominant mechanism.
- Decisive relationship coverage as `covered`, `partial` or `missing`.
- Whether the leading results echo the name, use or effects such as “improve,” “allocate” or “control” while missing the disclosed structure or action.
- Missing dimensions of implementation, such as structure, position, connection, motion, sequence, condition, control, material, path, interface or mechanism.
- Decision and follow-up query IDs.

Change course if one core mechanism accounts for at least 60% of the sample and decisive coverage is partial or missing, or if `effect_term_echo=true` and results miss the decisive structural relationship. Also change course if several routes repeat the same subject–action–object relationship without adding an implementation dimension, or if the same verified family dominates across languages and titles despite exact-title deduplication. Continuing the same pagination or concluding the search would leave the issue unresolved.

Choose one primary action:

- `family_expand` — the technical family is established. Read its members and identify the publications eligible by date and jurisdiction.
- `term_rewrite` — the structure is the same but the field uses different terminology. Rewrite using expressions found in candidate full text.
- `route_reconstruct` — search a different dimension supported by the disclosure, such as position, movement, control dependencies or step order. Temporarily remove a frequent effect term if it anchors the results to one mechanism.
- `request_input` — ask for specific structural detail when the disclosure does not support an alternative route.
- `converge` — stop only when the decisive relationship is covered, one mechanism no longer unduly constrains the results, and further routes are unlikely to change the principal finding.

For `route_reconstruct` or `term_rewrite`, identify the new query and retain its complete proposition and source. Use the original disclosure, user clarification or a retrieved candidate’s full text. Exclude scoring references, hidden ground truth and target abstracts seen after unblinding from both review evidence and query sources.

For example, three searches for “heat transfer efficiency” might all return one mechanism that repeats those words. If the disclosure specifies coolant splitting across staggered microchannels and rejoining in a manifold, choose `route_reconstruct` and search the channel positions, branching and rejoining without the effect term. If the disclosure gives only a name, choose `request_input` and ask for the missing structure.

### Channel records

Record each candidate’s `semantic_hit`, `keyword_hit`, query IDs, original ranking, family group and formal reading status. A dual-channel hit is not “disclosed”; a decisive counterexample found by one channel must remain included.

## Key `search_patent` bindings

| Value in `search_strategy` | Required parameter |
| --- | --- |
| `semantic` | `semantic_query` |
| `keyword` | `keywords` |
| `filter` | `filters` with at least one actual field, or supported `domain_filters` |
| `boolean` | `boolean_query`, with strategy exactly `["boolean"]` |

Do not pass parameters for unselected strategies. Boolean mode must not mix semantic, keyword, filter or domain parameters.
For ordinary technical topics prefer semantic plus keyword retrieval: preserve complete intent in semantic text and complete concepts/necessary limitations in each keyword, rather than broad component words that retrieve independently. Without language restrictions, supply core-concept equivalents in Chinese, English and Japanese as the tool requires.

Semantic and keyword routes may retrieve independently; one is not a hard constraint on the other. Put metadata restrictions in actual `filters`; assignee/date/IPC prose in semantic text is not a filter.

```json
{
  "search_strategy": ["semantic", "keyword", "filter"],
  "semantic_query": "Brackets on the left and right sides of a tray jointly support an open lid to prevent it from sagging",
  "keywords": ["托架承托开启盖板", "brackets supporting an open lid", "開いた蓋を支持するブラケット"],
  "filters": {"date_type": "publication", "date_to": 20201231},
  "limit": 20,
  "offset": 0,
  "collapse_family": false
}
```

The example date illustrates a user-supplied cutoff, not a default. Paginate with `limit` and `offset` under the current definition and record actual returned scope; continue paging the fixed query if deduplication leaves the queue below target. Normally rank by relevance; switch to dates/citation counts when requested.

## Fields and Boolean queries

Construct executable Patsnap expressions using current field documentation, without requiring another query-builder tool. Use verified fields/syntax only; preserve user-provided executable queries. Pass pregenerated opaque references completely unchanged, without parsing or concatenation.

- Use publication dates through `filters.date_type=publication` or Boolean `PBD`; filing/priority dates do not replace publication eligibility.
- For unresolved names use supported name fields; do not invent `assignee_ids` or company trees.
- `ANC` is current-assignee name; `ANCS` and `ANCS_ID` require resolved identities. Use supported `TREE@` only for confirmed group scope.
- IPC and CPC differ. Use only allowed classification restrictions; do not narrow all retrieval independently.
- For zero hits, first check terminology, entity scope and fields; do not silently drop hard restrictions.
- If the current tool requires describing domain capabilities first but the target MCP exposes no corresponding tool, do not construct `domain_filters`. Use supported ordinary retrieval and disclose specialized-filter coverage limits.

## Backward and forward citations

Use `search_patent` directly, with direction relative to the seed:

```json
{"search_strategy":["boolean"],"boolean_query":"B_CITES:(US6394621B1)","limit":20,"offset":0,"collapse_family":false}
```

`B_CITES` returns documents cited by the seed; `F_CITES` returns documents citing the seed. Put publication cutoffs in the same Boolean, e.g. `B_CITES:(US6394621B1) AND PBD:[* TO 20000101]`. Keep `*` unrestricted below, without inventing a lower date boundary.

Save seed, direction, expression, date handling and pagination. Later forward citations are leads, not automatically prior evidence. Read candidates with `fetch_patent`; citation-count thresholds, topical similarity or shared assignees do not establish citation relationships. There is no need to obtain citation lists through `fetch_patent.relations`.

Field directions: [Patsnap Types of Citation](https://help.patsnap.com/hc/en-us/articles/12479407137949-Types-of-Citation).

## Reading and process records

`fetch_patent` returns text/bibliography by default; include `media` only for original images/PDFs. Media URLs are source leads; obtain, read and save actual material before using it as visual evidence. Technical summaries are not originals; do not measure ratios from undimensioned schematic drawings.

Each round states “verification objective → actual retrieval/reading → findings and next step.” Preserve real requests, complete structured receipts and failures. Count total hits, current-page returns, deduplicated candidates and formal comparisons separately. Failure is not zero hits; unknown counts remain unknown.

If the assessment date is unknown, publication dates can be recorded and sorted, but prior-art eligibility remains unresolved. Publication before the search date does not replace eligibility relative to intended filing or priority.

## Candidate retention and follow-up for weak retrieval

Append each round to `candidate-ledger.json` as results arrive. Keep leading hits, in-scope and user-supplied candidates, and candidates close to the overall relationship traceable as new documents appear. See [Candidate ledger and stage checks](candidate-ledger.md) for the fields, stage transitions and validation command.

If leading results fail to cover decisive relationships, or no query expresses a necessary comparison unit as a complete relationship, record why retrieval is weak. Run at least one query preserving subject, action or interaction, and object or condition, plus an independent synonym or alternative-structure, classification or citation route. Keep each technical relationship intact during follow-up.

For each round, retain the publication ledger from `collapse_family: false`, including dates, jurisdictions and original ranks. Use the tool’s family-collapsed view or group uncollapsed receipts locally by known family or provisional exact title for the reading queue. Prioritize distinct groups and fill the queue by paging the original request. Keep the uncollapsed ledger throughout.

Review at least ten leading results. Record the number of distinct families, the largest family’s share and how many results preserve the target chain of technical objects. If one family exceeds half the sample, mark retrieval as weak, read across grouped families and add an independent relationship route. If fewer than 60% retain the target object chain, mark retrieval as weak and restore the domain objects to the semantic query and keyword phrases. Apply these checks regardless of total hits.
