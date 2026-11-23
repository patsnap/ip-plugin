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

The example date illustrates a user-supplied cutoff, not a default. Paginate with `limit` and `offset` under the current definition and record actual returned scope; one page is not the full set. Normally rank by relevance; switch to dates/citation counts when requested.

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
