# Structured IP review opinions and evidence records

## Three-part report

Use these three headings by default, in the requested file format or Markdown. Do not add duplicate overviews, workflow narration, dashboards or aggregate scores.

### 1. Quality overview

One sentence gives the overall judgment and decisive reason: Pass / Conditional pass / Return for revision / Unable to complete review. One sentence states necessary scope, retaining only material object/version/jurisdiction/date information and noting screening-process exclusion. Do not add a separate conclusion heading. Follow with a compact **Dimension | Judgment | Brief basis** table, one sentence per row. Unreviewed dimensions cannot pass.

### 2. Main issues

Order by impact. Merge common-root-cause errors while retaining all affected locations/conclusions; do not force together different evidence or remedies. Each short paragraph identifies the problem, actual source location and impact, optionally Major/Moderate/Advisory. Add vocabulary/query fragments only when comparison benefits. Concision cannot omit major defects, decisive evidence or reasonable disagreements.

### 3. Revision recommendations

Short action + completion-evidence list, linked to issue numbers where useful. Do not repeat issue prose. Retain evidence prerequisites for use/sign-off and human judgment items. If none, state “No revisions identified.” Never claim the author revised or IP reviewers approved.

## Overview dimensions

| Dimension | Object | Question |
|---|---|---|
| Synonym expansion | Complete concepts, aliases/abbreviations/translations/candidates | Which terms are supported, missing, too broad or semantically shifted? |
| Query reasonableness | Grouping/operators/fields/languages/boundaries | Does it express intended conditions with valid restrictions? |
| Search derivation | Features→concepts→groups→branches→merge | Why this combination; any unsupported narrowing/expansion? |
| Selected-reference applicability | Identity/version/time eligibility/geography/citation mapping | Can the references serve their assigned evidentiary role? |
| Factual foundation | Patent/product facts and original sources | Are decisive facts reliable and unknowns preserved? |
| Text comparison and conclusions | Limitation mapping, interpretation and scenario method | Do sources support novelty/inventive-step/coverage reasoning? |
| Compliance/traceability | Scope/method/source/version/limits/consistency | Are use boundaries clear and judgments reproducible? |

These expand four modules, not seven MCP scores or mandatory rows. Use Conforms / Needs revision / Pending verification; Not applicable only where genuinely inapplicable, Not reviewed for excluded/unchecked dimensions. Missing in-scope evidence is pending, not inapplicable. Keep detailed evidence in section 2.

For novelty/inventive-step reports, assess each separately, not one patentability score. FTO focuses on applicable claims/necessary limitations/boundaries; EoU binds patent/product evidence. Single-issue review shows relevant dimensions only and notes the rest unreviewed; no forced synonym calls or query creation.

## Search-specific presentation

For material terminology issues use **Concept | Report term | Action | Professional reason**. Distinguish keep/add/restrict/remove and synonym/broader/narrower/related relationships and combination constraints. Label terms extracted from queries as such, not an author's nonexistent vocabulary list. Tool candidates need not all be adopted; unused counts do not measure quality.

For query issues show:
1. Original query/fragment verbatim with location.
2. Intended vs actual complete-concept logic; reviewer-reconstructed derivation labeled.
3. Necessary changes labeled conceptual illustration or proposed Patsnap query, with syntax-check and execution states separate. No unexecuted “verified” claims.
4. Potential noise/omission/scope effect without unmeasured missed counts or accuracy claims.

Example: if hinge concept (A or B) must coexist with positioning C, `A OR (B AND C)` allows A without C; `(A OR B) AND C` matches the stated relationship. This illustrates logic, not actual missing/excludable patents or unverified precedence rules.

## Writing

Use complete formal English by default, or the explicitly requested language, identifying actual documents/features/disputed conclusions. Use the output language for headings, table labels and prose. Keep search languages independent. Preserve labeled evidence originals with translations as needed.

One issue per paragraph: judgment, basis and impact; concrete remedies go in section 3. Distinguish contradicted by source, insufficient support, not yet confirmable and reasonable interpretive disagreement. Formal tone must not soften confirmed errors into vague suggestions. Avoid colloquial verdicts and empty business jargon.

Use business dimension names and helpful issue numbers; leave internal indicator IDs/status codes/JSON/YAML/MCP fields in evidence records unless requested. Terms/queries themselves may appear as reviewed material. Use real readable citations (“D1 description [0021],” “D2 claim 1”); without numbering use title/section/exact quote. Define necessary technical terms initially. Technical similarity alone is not lack of novelty/inventive step. Recommendations must name a concrete action, not “improve further.” Do not request screening logs/exclusion reasons/full pools or repeat legal/scope warnings after every issue.

## Selected results and analysis

Check selected identities/applicability, relevance and citation mapping. Assess facts and inference separately in concrete prose, e.g. “D1's publication date and version are verified. The cited paragraph describes the structure, but the report does not explain its correspondence to the distinguishing feature, so it does not yet support the conclusion.”

Internal indicators may use Met / Partly met / Not met / Unverifiable / Not applicable. Explicit source contradiction means evidence_status=contradicted and Not met. Successful fulltext retrieval is not valid comparison.

Screening process is out of scope, not an unverifiable indicator or a score/gap/disposition factor. Final lists are normal input. Only necessary facts about selected objects may be pending. Do not calculate screening hit/overlap/AI-agreement rates or infer exhaustive coverage from reviewed examples.

## Internal evidence record

Local structure, not MCP fields; expose only for machine processing or explicit requests. Do not invent or lose its facts in external prose.

```yaml
finding_id: F-001
module: Analysis quality
indicator_id: A2
indicator_result: Not met
report_location: null
report_assertion: null
review_conclusion: null
severity: Major
evidence_status: contradicted
evidence:
  - source_tool: null
    source_path: null
    object_id: null
    source_locator: null
    excerpt: null
impact: null
recommendation: null
limitations: []
human_disposition: pending
```

This is an unfilled structure, not a completed finding. Actual records need report location/assertion/evidence/judgment/recommendation. MCP citations retain real tool/container-prefixed path/identity/quote/location; missing fields stay missing. Report/attachment contradictions use file locations directly without fake MCP provenance. These materials establish their own statements; patent-fact verification follows official Patsnap tool boundaries.

Evidence states: verified / contradicted / partially_supported / not_verifiable / not_checked. In prose explain the specific object as verified, inconsistent with source, partly supported, insufficient evidence to confirm, or not checked. human_disposition stays pending until the user adopts a view.

## Verification scope

Normally state reviewed key references and material gaps briefly, without a coverage dashboard. If requested, count supported, contradicted, partly supported, unverifiable and unchecked assertions separately. Coverage denominator is explicitly planned in-scope assertions; numerator is completed verification establishing support or contradiction. Exclude screening-process material entirely; do not rescreen/create logs to increase coverage. Coverage is not quality.

## Disposition rules

- Pass: explicitly bounded scope, no major in-scope defect and sufficient evidence for intended use; partial pass is not whole-report pass.
- Conditional pass: no established blocking error, but specified non-decisive revisions/evidence are needed before use.
- Return for revision: confirmed major defects can change core conclusions, method or use.
- Unable to complete review: missing decisive in-scope material prevents reliable opinion.

Absent excluded screening-process material never downgrades disposition. Explain recommendation/reason in full sentences. Major defects cannot be averaged away; user-requested scoring needs weights and unscorable items.

## Synthetic novelty/inventive-step example

Illustration only, not verified patent facts: section 4.2 combines D1 [0021] disclosing A and D2 [0018] disclosing B to deny novelty, without a single reference disclosing both.

> The novelty conclusion needs revision. Section 4.2 relies on D1 and D2 for separate features, but the available evidence does not establish complete disclosure in either single reference. Their combination therefore does not support the current novelty objection. Check features against individual references and analyze the combination separately for inventive step, including distinguishing features, the technical problem and a reason to combine.

This does not prove novelty/inventive step or require screening logs. For a section-4.2-only review, recommend revision within that scope, list novelty/inventive-step judgments separately and mark other dimensions unreviewed. Recommend individual-reference mapping and separate inventive-step reasoning, without penalizing missing vocabulary outside scope.
