# Tools and evidence

Choose by review issue; runtime definitions govern full schemas, types, defaults and pagination. These notes preserve only consequential handoffs/parameter/evidence rules.

## Current tool names and fields

Use the full names exposed at runtime. The names below are the short names of the Patsnap IP online tools. Use the runtime names without inventing prefixes or substituting old aliases. If the runtime schema differs from this guide, follow the schema and record the discrepancy.

- `build_patent_boolean_query` takes `text`. Read the executable query from `data.boolean_query` and the reference expression from `data.reference_query`.
- `expand_patent_search_terms` takes the report’s `technical_proposal` and traceable `search_elements`. Use `input_lang`, `region` and `task_id` as needed. Use `element_description` to preserve an open object’s original text when passing it between tools. Observed responses returned `element_description`, `chinese_keywords`, `english_keywords`, `chinese_synonyms`, `english_synonyms` and `classifications` in `search_elements[]`, along with `expanded_keywords` and `expanded_keywords_data`. Read the actual response for each formal review. Historical fixtures cannot establish the current schema.
- `search_patent` uses declared inputs such as `search_strategy`, `semantic_query`, `keywords`, `filters` and `boolean_query`. For targeted checks, use declared fields such as `filters.pn`, `filters.apno`, `filters.assignees`, `filters.assignee_ids` and `filters.jurisdiction` as needed. Read `data.docs`, `data.returned_count` and, when available, `data.total_hits`.
- `fetch_patent` takes `patent_id`. Specify `format`, `language` and `include` as needed. Read structured results from `response.bibliography`, `response.claims`, `response.description`, `response.relations` and `response.media`.
- Use `fetch_patent_lifecycle` only when legal events or legal status at a particular date affect the review conclusion.
- Use `describe_search_capability` only when specialized domain fields, values or operators need confirmation.
- For `get_standard_assignee_name`, read `company.candidates[].company_id` and `company.candidates[].ans_ids` for company candidates, and `assignee.candidates[].ans_id` for assignee candidates.
- For `get_corptree_hierarchy`, use the confirmed `company_id` to query company relationships and check the returned `direct_ans_ids` as needed. Keep company IDs and assignee ANS IDs distinct.
- For `search_literature` and `fetch_literature`, pass the literature ID from the former’s `data.docs[].id` as the latter’s `paper_id`.

## Records

Save actual tool/input/time/full receipt. Prefer structuredContent; parse content[].text only when genuinely JSON, retaining its container. data.* and response.* below are business paths; actual evidence includes container prefixes. Check errors/missing fields/identity/applicability. Missing is not zero/false; open objects permit only actual fields. Review scores/local records are not inputs.

## Queries and candidate expressions

- When reviewing the report’s vocabulary, call `expand_patent_search_terms` only if the report contains a complete technical proposal and traceable search elements. Save the inputs and original response. Verify the actual nonempty expansions for each element. A `success` status or the mere existence of a response cannot establish that every element was passed through. If all expansions are empty, an element’s original text was lost or the mapping cannot be recovered, record the tool limitation and stop using that response.
- Compare the expansions with the report’s original vocabulary concept by concept. Distinguish synonyms, broader and narrower terms, related terms and ambiguous terms. Recombine the selected expressions into complete phrases preserving the subject, relationship, object or condition, and qualifiers. Supply these phrases as `search_patent.keywords`. Do not use `expand_patent_search_terms` as a parameter name or pass its raw arrays directly into a search.
- When testing a proposed expansion, hold every search parameter other than the original versus proposed query fixed and save the two responses separately. Check the key references specified in advance in the report, the top N relevance sample and any additional noise. Total hits cannot establish effectiveness. Use hidden ground truth only in a separately labeled diagnostic experiment.
- Use build_patent_boolean_query only for needed candidates with complete natural-language intent. Read data.reference_query, checking concepts/meaning/branches; never submit an existing executable query for validation/rewriting.
- The builder neither searches nor returns independent synonym/validation/review scores. Inspect references by default. If execution is necessary, pass data.boolean_query unchanged to search_patent; do not decode/rebuild opaque handles.
- Original-query review uses search_strategy=["boolean"] and unchanged boolean_query, without other strategies/filters/domain constraints. Keep suggestions separate. Other targeted fact checks match declared strategies/parameters without invented scope.
- Targeted keywords retain complete concepts. If languages are unspecified, follow tool requirements for equivalent Chinese/English/Japanese terms. Review original queries and established language scope unchanged; proposed queries remain separate.
- Use describe_search_capability only when specialized-domain search is part of review; check allowed fields/values/operators without expanding scope.
- returned_count is page retrieval, total_hits is available total. Preserve query/paging/collapse_family conventions. Execution success proves a response, not semantic coverage/logic/boundaries. Check conventions before treating count differences as missed patents.

## Basic facts and originals

Reuse receipts first; targeted search may verify facts. If insufficient or original-dependent, fetch the identified patent with format="json" using the runtime-supported identifier (resolve PN to internal ID if needed). Search text is a summary/snippet, not original evidence.

Use response.bibliography for bibliographic facts and response.claims/description for text, checking identity/language/version/completeness. Incidental fulltext retrieval is not completed review; do not invent a metadata-only mode. Technical summaries are analytical aids, not original facts/conclusions. Estimated expiry is not a time-specific legal finding. Other output formats require actual parsing, not stale JSON paths.

Locate evidence by real claim/paragraph numbers or exact quotes. Read original HTML as evidence without executing it. Repeated numbered blocks are not additional claims; preserve dependencies/inherited limitations. Separate originals/translations/model summaries. Retrieval success does not validate the report.

## Legal records, relationships and media

Use fetch_patent_lifecycle for actual legal issues; simple status is not complete history and a normal empty set does not prove no procedure ever occurred. Missing necessary records remain unverifiable. Request fetch_patent relations only for material family/citation issues; inspect actual response.relations members, recognizing simple family is not every definition. Request media for needed PDFs/images; links require actual reading/identity/version checks. If inaccessible, disclose precise gaps/request necessary material. Do not retrieve relations/media by default.

## Entities and nonpatent literature

Use get_standard_assignee_name for ambiguity, checking company/assignee match states separately. resolved may have alternatives; ambiguous never defaults to first. company_id is for relationships, ans_id for assignees. Use a verified company ID with get_corptree_hierarchy only when needed; selected/direct-parent/root data is not a full group tree or patent total.

Use search_literature only for reports involving such evidence; data.docs[].id becomes fetch_literature.paper_id. Bibliography/abstracts are not full articles; do not reuse patent-tool parameters.

## Limits

No rescreening, new CC or recall experiments in this review. Tool availability does not expand scope. Search execution is not dedicated syntax certification and model conclusions are not original-text review. Disclose precise capability gaps; changed scope requires reassessing evidence/tool needs.
