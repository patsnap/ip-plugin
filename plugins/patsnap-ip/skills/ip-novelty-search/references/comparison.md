# Disclosure judgments and fact verification

## Comparison entry

Pass original `disclosure_text`, shared `features` and actual disclosure images to `assess_feature_disclosure`. With existing patent materials, provide `patent_text` and `patent_images`, using the publication number as a label. For identifier-based retrieval choose either a patent ID or a complete publication number.

Single-patent fields and the `patents` batch field are mutually exclusive. Each batch contains 1–10 documents and may mix identifier retrieval with supplied material. Align by the returned original `index`; do not renumber after dropping failures. Save successes and recover only failed items.

Use one relationship list throughout. Check statuses, reasons, evidence, `coverage` and document-level `arrangement`; the tool does not redefine scope or decide final conclusions.

## Establish document facts first

| `judgment` | Meaning |
| --- | --- |
| `disclosed` | Explicitly stated or necessarily determined by the same document's context; `disclosure_type` distinguishes explicit, inherent or combined disclosure |
| `not_disclosed` | An actually different structure, parameter or implementation is used; cite that fact |
| `not_mentioned` | The relevant material read does not state it; this does not establish actual absence |
| `null` | Insufficient material; describe the gap rather than relabeling it “not mentioned” |

An absent abstract term, zero text matches, unread text or unseen figures cannot establish nondisclosure. Missing figures do not invalidate facts established by text; limit conclusions only when missing figures affect decisive relationships. When text refers to table/figure parameters, inspect actual PDF pages rather than treating extraction omissions as source omissions.

Every limitation in a complete feature must be satisfied. Separate disclosure of components is not disclosure of their combination. Matching numbers/materials cannot conceal unmatched position, connection or sequence.

## Comparison units and source-relationship aggregation

Preserve original extraction entries as source relationships instead of compressing a whole row into a negative finding because of one local difference. When a source relationship contains independently disclosable limitations, compare traceable units before aggregation:

- A unit status records disclosure of that complete local relationship. Retain disclosed units even when another unit in the group differs.
- For novelty, aggregate a source relationship as fully disclosed only when one date-eligible document discloses every necessary unit in one technical arrangement. Otherwise show partial disclosure and the actual differences.
- For inventive step, an auxiliary document’s explicit disclosure of a difference unit is a local technical teaching. Separately audit combination motivation, structural compatibility, reasonable expectation of success and obstacles; local disclosure alone does not establish overall obviousness.
- Preserve a single-source mapping and original disclosure quotation for every unit. Do not recombine source relationships to increase matching.

A genus covers only species it explicitly encompasses; a species cannot supply an unstated specific use or structure for a broader target object. Similar names, a shared industry or possible use do not add specific equipment, workpieces or process limitations to the solution. State the direction of the concept relationship explicitly.

## Necessary inherency, use and numbers

Inherency requires necessity from conditions disclosed in the same document, without selection, modification or another document. Retain input quotations and explain definitions, units, assumptions, calculations, precision and results. A derivation is not a source quotation.

A usual configuration, possible adoption or an available choice is not necessary inherency. Necessity is possible only when the expressly disclosed arrangement could not be implemented without the feature; otherwise retain `not_mentioned` or `null`. Do not import FTO function–way–result equivalence to fill novelty limitations, or relabel an obvious substitution as disclosure.

Separate inherent structural capability from actual steps. A product's ability does not automatically disclose a method performed in a particular order. Different use names alone are not differences; verify any structure genuinely required by the use without adding models/dimensions absent from the target limitations.

Normalize dimensions, test conditions and endpoints first. A point/narrow range may satisfy a containing broad limitation; assess overlap/shared included endpoints for that limitation. A broad range does not automatically disclose a strictly internal point/subrange. A species may meet its genus; a genus does not automatically disclose a species, nor does one sibling species disclose another. Multiple parameters must belong to an evidenced common arrangement, not an arbitrary combination of alternatives.

## One technical arrangement

Verify complete interaction even within one embodiment; different embodiments are not automatically incompatible. Use source links between parts and conflicts in structure, parameters, states or step conditions.

- `single_embodiment`: actual interaction within one implementation.
- `linked_combination`: continuous source quotations linking the parts; possible coexistence does not prove an actual combination.
- `incompatible_pieces`: at least two source locations and the concrete incompatible conditions, not just different embodiment numbers.
- Neither a link nor incompatibility established: remain unconfirmed, without asserting impossibility of combination.

Express a missing feature through its itemwise status, not as incompatibility. Do not combine documents or incompatible arrangements to negate novelty.

## Agent verification

Actually verify decisive cases: a date-eligible document's remaining difference is only “not mentioned,” intended to support novelty; or a document may disclose the whole solution with an inherent derivation intended to negate novelty.

The Agent rereads text/figure pages most likely to contain omissions, seeks counterexamples or independently recalculates. Record `method: agent`, the original judgment/disclosure, shared features, the same document material, verification scope, rationale and current outcome. The report-data reference linked from the main Skill defines the format.

Outcomes are upheld, changed or insufficient material; incomplete execution is not upheld. Changed facts/evidence invalidate old checks. Save new facts before updating differences, arrangements and conclusions; do not overwrite raw receipts. Visual evidence must refer to actual original figures read.

Use `fetch_patent`, `search_patent` or the existing comparison tool again for specific gaps. Repeated calls are not independent review. Unverified decisive silence cannot support novelty; an unverified derivation cannot negate it. Do not hide potential counterexamples to support a positive conclusion.

## Routine modification and direct substitution

`routine` explains the document starting point, modification of differences, independent motivation, compatibility and expected effects. It does not change disclosure status or alone decide overall inventive step. Address every remaining difference in that relationship; label counts have no evaluative meaning.

For conventional direct substitution, identify the original and target means, evidence of conventional alternatives at the assessment date, equivalent function/effect and why other necessary relationships need essentially no change. Preserve actual differences instead of claiming explicit disclosure. New structures, unstated steps and cross-document additions are not substitutions. “Routine,” “easy to modify” or a passed check does not replace reasoning.
