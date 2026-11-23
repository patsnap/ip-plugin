# Recall and Precision Validation

Use this reference before claiming a search strategy is reliable.

## Recall Checks

Run at least three recall checks when evidence is available:

1. **Seed coverage**
   - Build a seed set from user-provided patents, known competitors, papers, standards, or expert examples.
   - Check whether each seed patent is retrieved by the formula.
   - For each miss, record the missing term, field problem, date/scope problem, or true out-of-scope reason.

2. **Classification cross-check**
   - Compare top IPC/CPC groups in results with expected technology classes.
   - Run a classification-only or classification-plus-light-keyword query for a small sample.
   - Identify relevant patents outside the keyword formula and feed terms back into the matrix.

3. **Citation/family expansion**
   - Inspect cited/citing/simple-family neighbors of high-confidence seed patents.
   - Add recurring technical terms, applicants, and classifications only when they generalize beyond a single record.

Optional checks:

- applicant benchmark: known active companies should appear unless the scope excludes them;
- time trend sanity: result peaks should match known technology cycles or reporting windows;
- language check: English-only or Chinese-only formulas should be tested for misses in the other language.

## Missed-Record Feedback Loop

Use this loop when the user provides known relevant patents that were missed, a supplemental-search document, or borderline relevant examples:

| Missed record | Why relevant | Miss reason | Candidate added terms | Field location | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  | missing object/effect/application/classification/noise over-exclusion |  | title/abstract/claims/description | add / reject / monitor |

Rules:

- Treat missed records as learning signals, not automatic positives.
- Add terms only when they generalize beyond one record or are important customer vocabulary.
- Record whether the miss came from missing keywords, overly narrow fields, missing classification, language variants, or an over-aggressive exclusion.
- Re-run precision sampling after adding broad effect terms or description/full-text fields.
- Preserve relevance tiers when newly retrieved records include medium- or low-relevance examples.

## Precision Checks

Use sampling rather than intuition:

- Sample at least 20 records when result count is small, or 30-50 records for broad landscapes.
- Stratify by top applicants, years, IPC/CPC groups, and high-frequency keyword clusters when the result set is diverse.
- Mark each sampled record as relevant, borderline, or irrelevant.
- Record the reason for each irrelevant record and decide whether to add a positive constraint or exclusion.

Suggested precision bands:

| Purpose | Precision expectation |
| --- | --- |
| Broad landscape | 60-75% may be acceptable if recall is explicitly prioritized |
| Balanced technology report | 75-90% target |
| Monitoring/update feed | 85%+ target |
| Evidence/FTO pre-screen | Prefer high precision, but disclose recall limitations |

Do not use these bands as absolute pass/fail rules; user requirements and technical ambiguity override defaults.

For general intelligence-search tasks, use 80%+ sample precision as a common working target when the user has not specified a stricter threshold.

## Iteration Log

Every final package should include a concise log:

| Version | Change | Result count | Recall effect | Precision effect | Decision |
| --- | --- | ---: | --- | --- | --- |
| S0 | Seed terms only |  |  |  |  |
| S1 | Add synonyms |  |  |  |  |
| S2 | Add IPC/CPC |  |  |  |  |
| S3 | Add exclusions |  |  |  |  |

## Final Validation Statement

State quality honestly:

- "Seed coverage validated" only when seed patents are checked.
- "Sample precision validated" only when sample review is documented.
- "Query suitable for preliminary analysis" when validation is partial.
- "User must verify syntax/fields in Patsnap" when exact Patsnap syntax was not executed.
