# Complete Search Report Template

Use every section for a Patsnap technology-topic search report unless the user explicitly requests a formula-only answer. Default to English; preserve the original request and executable multilingual query terms.

## 0. Execution and confirmation gates

`Pending user confirmation` is a workflow gate. Proceed after an explicit confirmation or confirmation-button action. Reuse authorization already provided in the session. A requested complete draft may include every section with unapproved gates marked pending; drafting does not itself authorize execution.

| Gate | Deliverable | Confirmation | Next step |
| --- | --- | --- | --- |
| 1 | Original requirements and technical scope | Scope is correct | Technology decomposition |
| 2 | Technology decomposition table | Decomposition is correct | Technical elements |
| 3 | Technical and noise elements | Elements are correct | Search strategies |
| 4 | Strategies, classifications and proximity | Strategies are correct | Individual queries |
| 5 | Individual, noise and combined queries | Queries are correct | Patsnap execution and logging |
| 6 | Results and recall/precision validation methods | Whether to start independent validation | Validation or finalization |

## 1. Technology topic

- Original user request (preserve verbatim):
- Technology topic:
- Search purpose:
- Search type: Technology topic / Problem-oriented topic / Applicant / Mixed
- Application and industry scope:
- Database:
- Countries/regions:
- Date range:
- Legal status:
- Patent types:
- Deduplication basis:
- Search date:
- User-provided seed evidence:
- Requirement status: Confirmed / Pending user confirmation / Revised following feedback

### Understanding and execution assumptions

| Item | Current understanding | Source | Confirmation status |
| --- | --- | --- | --- |
| Topic | | User wording / Agent inference | Pending |
| Application | | User wording / Agent inference | Pending |
| Search objective | | User wording / Agent inference | Pending |
| Data scope | | User wording / Default assumption | Pending |
| Deliverables | | User wording / Default complete report | Pending |

## 1.1 Topic definition

Before setting boundaries, explain the topic, core technical features, included concepts, and easily confused concepts outside the core scope.

Confirmation status: Pending user confirmation

## 2. Technical scope

### Included scope

| Item | Description | Source | Confirmation status |
| --- | --- | --- | --- |
| | | User wording / Agent inference / Example method | Pending |

### Excluded scope

| Exclusion | Reason | Could it cause missed results? | Confirmation status |
| --- | --- | --- | --- |
| | | Yes / No / To assess | Pending |

Explain boundary decisions. Ask whether inclusions/exclusions match the objective and whether any technology, product, company or date range must be added before execution.

## 3. Technology decomposition

| Level 1 topic | Level 2 technology/module | Level 3 technology/element | Description | Search purpose | Strategy ID | Confirmation status |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | Pending |

Confirm whether the hierarchy is too broad, too detailed or missing branches, and whether each branch should enter the query or only later tagging/analysis.

## 4. Technical elements

| Element ID | Name | Chinese keywords | English keywords | Abbreviations/trade names/aliases | Classifications | Suggested fields | Notes | Confirmation status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | | | | | | | | Pending |

### Multidimensional expansion checklist

| Dimension | Expansion | Evidence | Include in query? | Confirmation status |
| --- | --- | --- | --- | --- |
| Direct terms/synonyms | | User wording / Keyword assistant / Sample patents | Yes / No / To validate | Pending |
| Broader/narrower concepts | | Background research / Classifications / Expertise | Yes / No / To validate | Pending |
| Objects/materials/components | | Definitions / Sample patents | Yes / No / To validate | Pending |
| Functions/effects | | Problems / Effect wording | Yes / No / To validate | Pending |
| Mechanisms/processes/methods | | Process chain / Description wording | Yes / No / To validate | Pending |
| Applications/product modules | | User scope / Industry scenarios | Yes / No / To validate | Pending |
| Trade names/commercial wording | | Product materials / Sample patents | Yes / No / To validate | Pending |
| Abbreviations/formulas/short names | | Industry wording / Sample patents | Yes / No / To validate | Pending |
| Classifications | | IPC/CPC assistant / Classification browser | Yes / No / To validate | Pending |
| Foreign-language variants | | Translation fields / Family members | Yes / No / To validate | Pending |
| Seed patent terms | | Seed records | Yes / No / To validate | Pending |
| Applicant terminology | | Key applicant samples | Yes / No / To validate | Pending |

For problem-oriented searches, add:

| Problem element | Wording | Suggested fields | Notes | Confirmation status |
| --- | --- | --- | --- | --- |
| Technical problem/effect | | | | Pending |
| Solution method | | | | Pending |
| Related module | | | | Pending |
| Application/background | | | | Pending |
| Applicant | | | | Pending |

Confirm missing or unsuitable keywords, synonyms, English terms, abbreviations and trade names; exact classification constraints versus descendant recall; known seeds, applicants and required terminology.

## 5. Noise elements

| Noise ID | Type | Keywords/classifications/fields | Cause | Removal method | Include in final query? | Confirmation status |
| --- | --- | --- | --- | --- | --- | --- |
| N1 | | | | | To validate / Yes / No | Pending |

### Noise feedback log

Identify technical, keyword, field, parenthesis or classification causes; do not merely list applicants.

| Feedback batch | Sample characteristics | Representative applicants/classes | Cause | Revision | General rule? |
| --- | --- | --- | --- | --- | --- |
| | | | Stable industry noise / Parenthesis issue / Broad synonym / Broad field | Add noise block / Tighten positive block / Fix parentheses | Yes / No / Topic-specific |

Confirm that the proposed noise can be excluded and identify apparently noisy records that the business still requires.

## 6. Classification scope

| Classification | Meaning | Purpose | Field | Scope | Confirmation status |
| --- | --- | --- | --- | --- | --- |
| | | Recall / Precise constraint / Noise removal | `IPC` / `IPC_LOW` / `CPC` / `CPC_LOW` | Exact code / Include descendants | Pending |

Use `IPC_LOW`/`CPC_LOW` for all descendants, e.g. `IPC_LOW:C22B3/00`.

## 7. Proximity strategy

Explain where proximity replaces flat Boolean logic.

| Relationship | Risk of AND/OR alone | Proximity expression | Initial window | Adjustment evidence | Confirmation status |
| --- | --- | --- | --- | --- | --- |
| Object + action | | | `$W5-$W9` | | Pending |
| Element/material system | | | `$W3-$W5` | | Pending |
| Method + equipment | | | `$W5` or `$SEN` | | Pending |
| Effect + application | | | `$W5` or `$SEN` | | Pending |

## 8. Search strategies

| Strategy ID | Name | Logic | Elements | Fields | Expected role | Risk/noise | Include in combined query? | Confirmation status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S0 | Narrow seed query | | | | Collect highly relevant samples | | No / Yes | Pending |
| S1 | Core query | | | | | | Yes | Pending |
| S2 | Recall expansion | | | | | | Yes | Pending |
| S3 | Classification assistance | | | | | | Yes | Pending |
| S_LANGUAGE_RECALL | Non-English/machine-translation recall | | | `TACD`, strict positive constraints | Recover language variants | Higher noise; sample separately | Subject to sample validation | Pending |
| N1 | Noise query | | | | Remove noise | | Subject to validation | Pending |
| N_STABLE_INDUSTRY_NOISE | Stable industry noise | Classification + keyword | | | Remove stable cross-domain noise | Excluding adjacent applications | Subject to sample validation | Pending |

Confirm fit to the objective, inclusion versus validation-only strategies, whether to execute balanced recall first, and whether feedback creates a general rule, a topic-specific rule or a disputed boundary case.

## 9. Individual strategy queries

Provide a purpose and complete query for every strategy in the table. Add/remove sections as needed.

```text
S0 =
S1 =
S2 =
S3 =
S_LANGUAGE_RECALL =
```

Use language recall when missed relevant samples show systematic non-English or machine-translation variants. Constrain this branch tightly; never use broad translation terms alone.

## 10. Noise queries

State the target of each noise block. Include every used/proposed query and explain any exclusion from the final expression.

```text
N1 =
N2 =
N_STABLE_INDUSTRY_NOISE =
NOISE_TOTAL =
NOISE_TOTAL_EXPANDED =
```

Stable industry noise must be supported by hit review, preferably using classification plus keywords/context. The expanded noise formula is mandatory and must contain no unresolved N1/N2 placeholders, even when shorthand is also shown.

## 11. Combined queries

### Directly executable Patsnap expressions (show first)

Provide complete expanded formulas before execution notes. Never deliver only `S1 OR S2 OR S3` shorthand.

```text
FINAL_BALANCED_EXPANDED =
(
  [S1 full formula body]
)
OR
(
  [S2 full formula body]
)

NOISE_TOTAL_EXPANDED =
(
  [N1 full formula body]
)
OR
(
  [N2 full formula body]
)

FINAL_PRECISION_EXPANDED =
(
  [FINAL_BALANCED expanded full formula body]
)
NOT
(
  [NOISE_TOTAL expanded full formula body]
)
```

### Explanatory shorthand

```text
FINAL_BALANCED =
FINAL_PRECISION =
```

Confirmation status for each: Pending user confirmation

If too long to maintain safely, provide the entire expanded query in an appendix/attachment and additionally suggest saving individual strategies in Expert Search before combining them.

### Expansion checks

- Balanced query contains no unresolved S1/S2/S3 placeholders.
- Noise query contains no unresolved N1/N2/N3 placeholders.
- Precision query contains actual expanded positive and noise blocks, not references to their variable names.
- Expanded formulas are visible beside the combined-query section, not hidden only after notes.
- Check status:

## 12. Execution log

Fill after Patsnap execution; otherwise mark `Pending user execution in Patsnap`.

| Query | Hits | Deduplication basis | Execution date | Notes |
| --- | ---: | --- | --- | --- |
| S0 | | | | |
| S1 | | | | |
| FINAL_BALANCED | | | | |

## 13. Recall and precision validation guidance

Provide methods only unless executed result sets, labeled samples and independent recall samples are available.

### Precision

1. Execute the balanced or individual queries.
2. Stratify samples by strategy, year, applicant, classification and frequent keywords.
3. Manually label Relevant / Borderline / Irrelevant.
4. Count noise sources.
5. Decide whether to add noise blocks or tighten fields/proximity windows.

`Precision = relevant samples / all sampled records`

| Sample scope | Sample count | Relevant | Borderline | Irrelevant | Precision | Main noise | Adjustment |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
| | | | | | | | |

### Recall

Hits alone cannot establish recall. Build independent relevant samples from user seeds, manually screened full portfolios of key applicants, competitor/product/standard/paper reverse searches, broad/classification searches, and trade-name/material/process-route reverse searches.

`Recall against the independent sample = retrieved independent relevant samples / all independent relevant samples`

| Independent sample source | Sample count | Hits | Recall | Why missed | Revision |
| --- | ---: | ---: | ---: | --- | --- |
| | | | | | |

### Proximity adjustment

| Concept block | Current operator/window | Observed problem | Adjustment |
| --- | --- | --- | --- |
| | | Too noisy / Missed seed / Good balance | |

## 14. Iteration log

| Version | Change | Hit-count change | Recall effect | Precision effect | Decision |
| --- | --- | ---: | --- | --- | --- |
| S0 | | | | | |

### Noise/missed-result feedback

| Feedback | Sample source | Observation | General issue? | Current revision | Suggested skill revision |
| --- | --- | --- | --- | --- | --- |
| Noise | | | Yes / No / To assess | | |
| Missed result | | | Yes / No / To assess | | |

## 15. Limitations and pending items

- Fields/syntax to verify in Patsnap:
- Classifications to review:
- Insufficient seed samples:
- Noise removal awaiting sample validation:
- Date/country/legal-status scope:
- Recommended next steps:

## 16. Confirmation checklist

| Gate | Checkpoint | Status | User action | Feedback/revision | Next step |
| --- | --- | --- | --- | --- | --- |
| 1 | Requirements and scope | Pending user confirmation | Confirm | | Decomposition |
| 2 | Decomposition | Pending user confirmation | Confirm | | Technical elements |
| 3 | Technical and noise elements | Pending user confirmation | Confirm | | Strategies |
| 4 | Classification, proximity and strategies | Pending user confirmation | Confirm | | Individual queries |
| 5 | Individual, noise and combined queries | Pending user confirmation | Confirm | | Patsnap execution |
| 6 | Validation methods / Independent validation | Pending user confirmation | Confirm | | Validation or finalization |
