# Standard fields

This guide describes the roles of common report-review fields and how values pass between tools. Read the runtime schema before calling a tool. If fields, types or allowed values differ, follow the runtime schema and record the discrepancy.

## Term expansion and search

### `expand_patent_search_terms`

| Direction | Field | Use |
|---|---|---|
| Input | `technical_proposal` | The complete technical proposal from the report or commission materials. A title or isolated keywords are insufficient. |
| Input | `search_elements` | An array of traceable search elements. Prefer the report’s existing structure. |
| Input | `search_elements[].element_description` | Carries one element’s original text when an open object must be passed through without loss. Do not invent types, scores or facts. |
| Input | `input_lang` | The language of the input proposal. Use only values allowed at runtime. |
| Input | `region` | The context or regional preference for term expansion. It does not filter search jurisdictions. |
| Input | `task_id` | An optional tracking identifier with no bearing on the technical facts. |
| Output | `search_elements[]` | Expansion results by element. Match each result to the original input text. |
| Output | `element_description` | Identifies the returned element so the reviewer can check whether its identity was preserved. |
| Output | `chinese_keywords` / `english_keywords` | The element’s base keywords. Review them before using them as search terms. |
| Output | `chinese_synonyms` / `english_synonyms` | Candidate expressions associated with each base keyword. Distinguish synonyms, broader and narrower terms, related terms and ambiguous terms. |
| Output | `classifications` | Candidate classification leads. They do not automatically represent IPC codes or independently establish a technical classification. |

Parse expansion containers such as `expanded_keywords` and `expanded_keywords_data` as they appear in the actual response. Review and select expressions, then recombine them into complete phrases preserving the subject, relationship, object or condition, and qualifiers.

### `search_patent`

| Field | Use |
|---|---|
| `search_strategy` | Declares semantic, keyword, filter or Boolean strategies. Use the Boolean strategy on its own. |
| `semantic_query` | The complete technical intent and relationships. Use only with the semantic strategy. |
| `keywords` | An array of reviewed phrases that preserve the technical relationships. Keep this search parameter distinct from the name of the expansion tool. |
| `filters` | Structured limits. Common fields include `pn`, `apno`, `assignees`, `assignee_ids`, `jurisdiction`, `date_type`, `date_from`, `date_to` and `legal_status`. |
| `boolean_query` | An executable Patsnap Boolean query or an opaque reference from the builder. Pass it through without decoding, rebuilding or manual edits. |
| `collapse_family` | Controls patent family collapsing. Keep this setting fixed in A/B checks. |
| `limit` / `offset` / `sort` | Pagination and sort settings. Keep them identical in A/B checks. |
| `data.docs` | Documents returned on the current page. |
| `data.returned_count` | Number of documents returned on the current page. |
| `data.total_hits` | Total hits when available. This count alone cannot establish search effectiveness. |

## Building a Boolean query

### `build_patent_boolean_query`

| Direction | Field | Use |
|---|---|---|
| Input | `text` | The complete natural-language search intent. Do not submit an executable field query for validation or rewriting. |
| Output | `data.reference_query` | A reference expression for human review of concept groups and logic. |
| Output | `data.boolean_query` | An executable query or opaque reference to pass unchanged to `search_patent.boolean_query`. |

## Patent originals and evidence

### `fetch_patent`

| Direction | Field | Use |
|---|---|---|
| Input | `patent_id` | A patent ID or publication number whose identity has been verified. |
| Input | `format` | Use `json` for structured checks. For `markdown`, parse the Markdown actually returned. |
| Input | `language` | Preference for original text or a translation. Identify translations as such. |
| Input | `include` | Request `relations` or `media` only when needed. Omit full text from this field. |
| Output | `response.bibliography` | Bibliographic details, dates, parties and simple status. |
| Output | `response.claims` | Original claims. Preserve dependencies and required limitations. |
| Output | `response.description` | Original description. Claims determine the claim boundaries. |
| Output | `response.relations` | Family, citation and similarity relationships to check as needed. |
| Output | `response.media` | Leads to original PDFs or drawings. A link alone does not establish that the material was read. |

Use `fetch_patent_lifecycle` for legal events and status at a specific date. Simple status cannot substitute for the full event record.

## Entities and nonpatent literature

- For `get_standard_assignee_name`, read `company.candidates[].company_id` and `company.candidates[].ans_ids` for company candidates, and `assignee.candidates[].ans_id` for assignee candidates.
- For `get_corptree_hierarchy`, supply the confirmed `company_id` and check `direct_ans_ids` as needed. Keep company IDs and assignee ANS IDs distinct.
- For `search_literature` / `fetch_literature`, use the literature ID from `data.docs[].id` as the latter tool’s `paper_id`.
