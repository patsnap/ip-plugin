# Candidate ledger and stage checks

## Contents

- Purpose and scope
- Ledger data
- Stage checks
- Weak retrieval and scope drift
- Validation

## Purpose and scope

Record what each search returned and the evidence for advancing or excluding each candidate. Use every retained `search_patent` receipt, user-supplied candidate and core publication in a previous report. Raw rank cannot replace technical judgment. Unknown scoring reference patents must not be used as search targets.

Track each exact publication number. Group family members for technical reading while retaining their jurisdiction and publication-stage identities.

## Ledger data

Save `candidate-ledger.json` in the task directory. The minimum structure is shown below.

```json
{
  "ledger_version": 2,
  "dedup_fill_policy": "required",
  "route_reflection_policy": "required",
  "scope": {
    "publication_date": "2018-12-03",
    "publication_date_inclusive": false,
    "required_publication_jurisdictions": ["CN"]
  },
  "search_response_files": [
    "calls/Q1-page-0.json", "calls/Q1-page-100.json",
    "calls/Q2-page-0.json", "calls/Q3-page-0.json", "calls/Q4-page-0.json"
  ],
  "queries": [{
    "query_id": "Q1",
    "route": "complete_combination",
    "comparison_unit_numbers": [1, 2, 3],
    "dedup_fill": {
      "query_signature": "sha256-of-request-excluding-offset",
      "target_unique_groups": 100,
      "pages": [
        {"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q1-page-0.json"},
        {"offset": 100, "limit": 100, "returned_count": 100, "response_file": "calls/Q1-page-100.json"}
      ],
      "raw_result_count": 200,
      "unique_identity_count": 132,
      "unique_group_count": 100,
      "status": "target_met"
    }
  }, {
    "query_id": "Q2",
    "route": "relation",
    "comparison_unit_numbers": [2],
    "semantic_query": "A blade guard slides lengthwise along the handle guide, covering the blade when extended and exposing it when retracted.",
    "keywords": ["刀具护罩纵向导槽滑动", "blade guard sliding in longitudinal guide"],
    "relation_proposition": {
      "subject": "blade guard",
      "relation": "slides lengthwise along the handle guide",
      "object_or_condition": "extended to cover the blade and retracted to expose the blade",
      "constraints": ["the guard is detachable from the knife body"],
      "source": "disclosure",
      "source_refs": ["feature-plan.json#comparison_units/2"]
    },
    "dedup_fill": {
      "query_signature": "sha256-Q2-excluding-offset",
      "target_unique_groups": 20,
      "pages": [{"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q2-page-0.json"}],
      "raw_result_count": 100,
      "unique_identity_count": 78,
      "unique_group_count": 20,
      "status": "target_met"
    }
  }, {
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
    },
    "dedup_fill": {
      "query_signature": "sha256-Q3-excluding-offset",
      "target_unique_groups": 20,
      "pages": [{"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q3-page-0.json"}],
      "raw_result_count": 100,
      "unique_identity_count": 74,
      "unique_group_count": 20,
      "status": "target_met"
    }
  }, {
    "query_id": "Q4",
    "route": "relation",
    "reconstructed_from_reflection_id": "R1",
    "comparison_unit_numbers": [2],
    "semantic_query": "A guard flange engages a longitudinal slot in the handle. The slot walls constrain its motion as it translates between two stops.",
    "keywords": ["护罩凸缘嵌入纵向槽并在止挡位置之间平移", "guard flange captured in a longitudinal slot and translating between stops"],
    "relation_proposition": {
      "subject": "guard flange",
      "relation": "engages and translates along a longitudinal slot in the handle",
      "object_or_condition": "guided by the slot walls and located at two stop positions",
      "constraints": ["the guard is detachable from the knife body"],
      "source": "disclosure",
      "source_refs": ["feature-plan.json#comparison_units/2"]
    },
    "dedup_fill": {
      "query_signature": "sha256-Q4-excluding-offset",
      "target_unique_groups": 20,
      "pages": [{"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q4-page-0.json"}],
      "raw_result_count": 100,
      "unique_identity_count": 82,
      "unique_group_count": 20,
      "status": "target_met"
    }
  }],
  "retrieval_assessment": {
    "strength": "weak",
    "reason": "Leading candidates still lack the decisive relationship",
    "family_diversity": {"top_k": 20, "unique_families": 7, "dominant_family_count": 11},
    "object_precision_sample": {"reviewed": 10, "on_object": 5},
    "decisive_comparison_unit_numbers": [2],
    "feedback_query_ids": ["Q2", "Q3"]
  },
  "route_reflections": [{
    "reflection_id": "R1",
    "query_ids": ["Q1", "Q2", "Q3"],
    "sample_size": 20,
    "unique_families_or_provisional_groups": 8,
    "dominant_mechanism_count": 13,
    "decisive_relation_coverage": "partial",
    "effect_term_echo": true,
    "missing_dimensions": ["position", "kinematics"],
    "evidence_basis": "retrieval_sample",
    "evidence_refs": ["calls/Q1-page-0.json", "calls/Q2-page-0.json", "calls/Q3-page-0.json"],
    "decision": "route_reconstruct",
    "decision_reason": "One mechanism dominates the leading results and echoes the stated effect. Position and motion have yet to be searched independently",
    "followup_query_ids": ["Q4"]
  }],
  "candidates": [{
    "publication_number": "CN1234567A",
    "aliases": ["CN1234567"],
    "family_id": "optional-family-id",
    "publication_date": "2018-11-16",
    "jurisdiction": "CN",
    "discoveries": [{"query_id": "Q1", "rank": 2, "channels": ["semantic"]}],
    "eligibility": {"jurisdiction": "eligible", "date": "eligible"},
    "priority": "high",
    "stage": "compared",
    "decision": "advance",
    "reason": "The overall structure is close to the primary combination",
    "evidence_refs": ["calls/fetch-CN1234567A/response.json"]
  }],
  "jurisdiction_reconciliation": {
    "CN": {"status": "represented", "reason": "The in-scope high-priority candidate has been compared", "evidence_refs": ["calls/compare/response.json"]}
  },
  "unexplained_drop_count": 0
}
```

Use `ledger_version: 2` for new tasks. Version 1 supports continuation of historical ledgers. Use these values:

| Field | Values |
| --- | --- |
| `route` | `complete_combination`, `relation`, `synonym`, `classification`, `citation`, `user_candidate` |
| `stage` | `searched`, `shortlisted`, `fetched`, `compared`, `final`, `excluded` |
| `priority` | `high`, `normal`, `background` |

For new tasks set `dedup_fill_policy: "required"`. Every query except `user_candidate` records its `dedup_fill` target, a signature of the fixed request excluding `offset`, consecutive pages and receipts, raw result count, exact identity count, distinct technical group count and stopping status. Use `target_met`, `results_exhausted`, `tool_limit`, `budget_limit` or `tool_error`. Include a `limitation` for the last two. Identical normalized titles may provisionally share a reading group. Keep all member publications in `candidates` and reconcile them against the original receipts.

Set `route_reflection_policy: "required"` and save at least one entry in `route_reflections` after filling the reading queue. Allowed values for `evidence_basis` are `disclosure`, `user_clarification`, `candidate_feedback` and `retrieval_sample`. Exclude scoring references and hidden ground truth. For `route_reconstruct` and `term_rewrite`, list the follow-up query IDs and link each new query back with `reconstructed_from_reflection_id`. When one mechanism accounts for at least 60% of the sample and decisive coverage is incomplete, reconstruct the route or request more disclosure. If results merely echo the stated effect and coverage is incomplete, reconstruct the route or request input. You may choose `family_expand` when family crowding is the only issue and the decisive relationship is covered.

In version 2, each `relation` query records its actual `semantic_query`, nonempty `keywords` and complete `relation_proposition`. Its source must be `disclosure`, `user_clarification` or `candidate_feedback`. For candidate feedback, record `source_publication_number` as well. Exclude scoring references and hidden ground truth from formal queries. For weak retrieval, list `decisive_comparison_unit_numbers` and cover each number with at least one relationship query.

Each version 2 `synonym` query references a relationship query in `derived_from_query_id`, inherits its comparison units, and saves `relation_synonym_expansion`. Tie each complete phrase to declared subject, relationship, object or condition, and constraint variants. The actual `keywords` must exactly match `composed_phrases[].text` in content and order.

Treat the `pn` array within a single returned document as one alias group. Choose a canonical `publication_number`, store the remaining values in `aliases` and assign each alias to only one candidate. Normalize commas, spaces, hyphens and slashes for identity checks, so `US3,457,643` matches `US3457643`. Preserve the correct display format in the report.

For each exclusion, set `decision: "exclude"`, give a verifiable `reason` and cite actual `evidence_refs`. Identify the specific mismatch in object, relationship, purpose, date, scope or family evidence. A low rank or a bare statement of low relevance leaves the exclusion unexplained.

## Stage checks

1. **Before full-text retrieval.** Review leading hits from each round, in-scope and user-supplied candidates, and those close to the primary combination. Fetch high-priority candidates or document their exclusion using available abstract, bibliographic or scope evidence.
2. **Before formal comparison.** Compare each high-priority candidate whose text was obtained, or record an exclusion based on that text.
3. **Before reporting.** Assign every candidate a terminal stage of `final` or `excluded`. Cite evidence for exclusions, including user-supplied candidates, high-priority candidates and leading in-scope hits. Generate the final list from the reconciled ledger.

When grouping family members, the main evidence text can reach `final`. Keep an `excluded` record for each other member, identifying the family relationship, representative publication number and how its date and jurisdiction were accounted for.

## Weak retrieval and scope drift

Set `retrieval_assessment.strength` to `weak` and run supplementary searches if any of the following applies:

- Leading hits match only isolated parts and miss decisive relationships.
- No query expresses a necessary comparison unit as a complete relationship.
- One term, classification or mechanism dominates results.
- All decisive relationships in the strongest candidate are `not_mentioned`, or the candidate clearly provides a different starting point for modifying the overall design.
- One family occupies more than 50% of the leading sample.
- Fewer than 60% of at least ten manually reviewed leading results preserve the target chain of technical objects.

Run at least one `relation` query linking subject, action or interaction, and object or condition. Also run an independent `synonym`, `classification` or `citation` route. Apply classification codes within their own search route.

When the user explicitly restricts publication jurisdictions, account for all in-scope candidates. If all were excluded, cite the evidence for each exclusion in `jurisdiction_reconciliation` and disclose that no in-scope document remained for formal comparison. A target examination jurisdiction alone does not impose this publication restriction.

With `scope.publication_date`, specify `publication_date_inclusive`. “Before” normally means `false`. “Through” or “no later than” normally means `true`. Record the actual `publication_date` for each version 2 candidate. The validator computes eligibility from the date and checks `eligibility.date`. Later publications and unverified dates can support leads or reading only.

For an explicit publication jurisdiction restriction, record each version 2 candidate’s actual `jurisdiction`. The validator checks `eligibility.jurisdiction` and reconciles `represented` against that field. A publication-number prefix cannot supply the jurisdiction.

## Validation

```sh
python3 scripts/validate_candidate_ledger.py --ledger /task/candidate-ledger.json --root /task --phase final
```

Use `--phase fetch`, `compare` and `final` for the respective stages. The validator checks query references, stages, high-priority dispositions, weak-retrieval follow-up and explicitly required jurisdictions. At the final stage it recomputes unexplained losses from receipt alias groups and candidate dispositions. An exclusion evidence file must contain the publication number or one of its aliases. Human review determines whether the cited material supports the technical reason for exclusion.
