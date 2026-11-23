# Tool usage

Runtime definitions govern full parameters, types, defaults, pagination and response structures. These notes retain consequential handoffs, parameter rules and evidence meanings.

## Search and evidence

Keep complete technical concepts/qualifiers in keywords, not broad independent component terms. Semantic and keyword routes are independent; semantic_query does not necessarily constrain keyword hits. Without explicit language scope, prepare equivalent Chinese/English/Japanese expressions as current tool requirements indicate. Honor established languages and disclose gaps. Use supported semantic/keyword routes for ordinary topics, verified Boolean grouping for strict intersections.

- search_patent searches patents; use build_patent_boolean_query only to construct from natural-language intent. Existing executable queries go directly to search. data.reference_query is readable; pass data.boolean_query unchanged without decoding/rebuilding references.
- Boolean uses search_strategy=["boolean"] and boolean_query exclusively, without other strategies/filters/domains. Other strategies bind their declared parameters. Literature does not use patent Boolean parameters. Verify specialized fields through describe_search_capability first.
- search_patent data.docs[].id can feed fetch_patent. Request relations/media only for needed family/citation/image evidence. Search text is a snippet/abstract; actual claims/descriptions support verification. Technical summaries are not originals and media links are not read images.
- search_literature data.docs[].id becomes fetch_literature.paper_id. Bibliography/abstract is not full article text.
- fetch_patent_lifecycle supplies legal records. Simple status/empty results cannot establish time-specific legal conclusions or absence of all past events. Verify actual records; missing stays pending.
- Disambiguate with get_standard_assignee_name; use get_corptree_hierarchy only for needed relationships. Check company/assignee matches separately. resolved may include alternatives; ambiguous never defaults to first. company_id is for relationships, confirmed ans_id/direct ans_ids for patent-assignee filters. Do not interchange IDs. Relationships are not a full group tree, do not automatically expand identity scope, and patent_signal is not search total.

## Scope and counts

- data.total_hits is query hits; data.returned_count is page count; matched_total is a local report mapping. Do not sum hits across queries/pages. Deduplicate merged details by real document identity and disclose paging-limited samples.
- Publication-level counts explicitly use collapse_family=false. Folding changes both details/totals and is not automatically application-number or simple-family deduplication. Application deduplication requires actual application numbers; simple families require actual fetch_patent relations.simple_family membership with coverage limits.
- Confirm IPC/date/jurisdiction/company scope under business rules; candidate conditions are not user choices. Field references help construct queries but do not prove tool acceptance; retain execution results/errors.
- Use actual returned links tied to document identity. Otherwise show the number and “Link unavailable.” Do not claim online verification without reading content.

## Population statistics and charts

- Use field_analysis for totals/trends/rankings/distributions. Combine requested dimensions for one dataset within runtime group limits; when splitting, preserve query/counting conventions. Use country for geography and authorize_year for grant year.
- source.query takes confirmed natural-language scope or an executable query, not opaque builder references. Check source_resolution.query. Never guess Workspace sources without valid space/directory IDs.
- Read total from source_resolution.matched_count and distribution from response.results[].display_rows or actual buckets; inspect warnings/errors/truncation. Bucket counts/sums are not deduplicated patent totals.
- Multiple classes/assignees overlap; do not present them as mutually exclusive shares. Technical themes differ from effects/custom branches. If a dimension is unsupported, retain the report section with a limitation or classify retrieved records locally as a sample. For 20-year trends verify actual years/date bounds; missing years are not automatically zero.

## Missing capabilities/evidence

These patent tools do not supply market size, policy/standards originals or monetary valuations. Use user material/available web sources with source/version/date; otherwise mark unavailable. Qualitative technical/legal/market assessment may use existing evidence, but no invented dollar values, five-axis scores, TRL evidence or current standard clauses. General industry knowledge supports general principles, not current company facts or document existence.

Prefer local HTML resources for offline sharing. If original figures are unavailable, create SVG only from read text, labeled “Analytical illustration, not an original patent drawing.” Links do not verify image content. Tool availability does not expand tasks; risk/design-around/innovation require concrete evidence and relevant user decisions, not additional analyses as substitutes. Continue bounded analysis with existing material when tools are unavailable; samples/frameworks/pending evidence are not completed exhaustive searches.
