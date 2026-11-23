# Patent Layout Data Fields

Use this reference when building patent datasets, source notes, or Excel outputs.

## Search Strategy Fields

| Field | Purpose |
| --- | --- |
| analysis_topic | User-facing technology topic |
| technology_branch | Module from the technology tree |
| keywords_cn | Chinese search terms and synonyms |
| keywords_en | English search terms and synonyms |
| classification | IPC/CPC/FI/F-term or local patent classification |
| applicants | Original applicant names supplied by user |
| applicant_aliases | Normalized aliases, subsidiaries, historical names |
| jurisdiction | CN, WO, US, EP, JP, KR, etc. |
| time_range | Filing/publication date range |
| query_formula | Search formula actually used |
| source | Database or public source |
| search_date | Date the search was run |

## Patent Record Fields

| Field | Purpose |
| --- | --- |
| publication_number | Publication number |
| application_number | Application number |
| title | Patent title |
| abstract | Abstract or condensed technical summary |
| independent_claim_summary | Brief summary of key claim scope |
| applicant_original | Applicant as retrieved |
| applicant_normalized | Cleaned applicant group |
| inventors | Inventor list |
| filing_date | Filing date |
| publication_date | Publication date |
| grant_date | Grant date if available |
| legal_status | Pending, granted, invalid, withdrawn, expired, unknown |
| simple_family_id | Family grouping key |
| family_size | Number of family members |
| jurisdictions | Family jurisdictions |
| citations_forward | Forward citation count if available |
| citations_backward | Backward citation count if available |

## Analysis Fields

| Field | Purpose |
| --- | --- |
| technology_module | Main module from clustering |
| sub_module | More detailed function or scenario |
| technical_problem | Problem addressed by patent |
| technical_solution | Claimed solution pattern |
| technical_effect | Improvement or effect |
| application_scenario | Product/process/application scenario |
| value_label | Core, important, peripheral, noise |
| trend_label | High-frequency, emerging, frontier, declining |
| risk_label | Blocker, reference, design-around, low-risk |
| opportunity_label | Protection, reserve, countermeasure, white-space |
| recommended_action | File, monitor, design around, acquire/license, no action |
| evidence_note | Short explanation tying recommendation to evidence |

## Metric Rules

- Separate raw publications from patent families.
- Use filing-year trends for innovation timing unless publication-year is explicitly better for the question.
- Normalize applicant aliases before ranking companies.
- Keep invalid/expired patents visible for technology learning, but exclude them from active blocking-risk counts.
- Do not mix China-only counts with global family counts in the same chart without a label.
