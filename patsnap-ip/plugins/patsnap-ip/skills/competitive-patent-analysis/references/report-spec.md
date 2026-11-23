# Report layout and representative-patent selection

## 1. Fixed section order

Header → company introduction → search baseline → confirmed number of technology sections → comparative assessment → search notes → footer.

The company introduction precedes all technical sections. Include three paragraphs: origins/technology path, product line/evidenced milestones, and competitive logic; add 6–8 `profile-grid` facts. Founding dates, certifications, orders and specifications need user material, actual responses or verifiable web evidence with dates. Mark facts not independently checked “Unverified.” Retain missing fields as “To be verified” and state verification scope.

Default authored content and template labels to English, honoring explicit output-language requests. Preserve original evidence with translations as needed. Set HTML `lang` accordingly.

## 2. Search baseline

First row: hits for confirmed names in `ALL_AN`, identifying single-company or verified group scope. The field includes current, original and historical assignees, so this is not a current-ownership total. Following rows show five counts per technology area using these labels and units. Explain below that independent result sets may overlap and cannot be added into a company total.

| Internal field | User-facing label and unit |
|---|---|
| `matched_total` | Query hits: N publications |
| `returned_count` | Actually retrieved: N publications |
| `independent_family_count` | Simple-family deduplication: N families |
| `eligible_family_count` | Relevance-qualified: N families |
| `listed_count` | Listed here: N representative patents |

Without complete retrieval, label family counts “within the retrieved sample,” not vague “database-folded results.”

Put the actually executed `ALL_AN` Boolean in `BASELINE_QUERY`, in collapsed search-note details. Preserve direct queries unchanged; for builder execution display the same response's `reference_query`, labeling it the reference expression corresponding to the execution reference. Save the actual `boolean_query` reference in work records rather than displaying it as a readable query. `BASELINE_SCOPE_NOTE` explains confirmed entities and assignee scope. Use readable company/standardized-assignee names in prose and charts; internal IDs belong in actual query records only. Match real tool/field execution; a single-company baseline is not a complete group total.

Company, patent-details, search-result and SaaS destination links must come from actual responses or verified sources and match their objects. Fill `SOURCE_LINKS_OR_NOTE` with real links/readable names, or disclose absence. Do not substitute a homepage for an object-specific link or construct URLs.

Never sum area hits or depict them as pies, stacked charts or shares.

## 3. Mandatory simple-family deduplication

Search returns publications, not independent inventions. Multiple publications, jurisdictions and related filings can create false diversity if counted directly.

Keep this order:

1. Retrieve the pool with publication-level counts following [Step 3](../SKILL.md#step-3--search-patents-by-area). Respect runtime pagination limits and record actual coverage.
2. Verify simple-family memberships individually through `fetch_patent` relations (search currently lacks `simple_family_id`). Reuse evidence and text obtained together; do not pass an array to the single-patent interface. Retain one representative per family, prioritizing granted over pending, broader over single-jurisdiction coverage, then newer publication date. Missing/empty/failed relationship evidence does not establish a singleton. List unknown membership separately and keep complete family counts pending.
3. Compute raw `independent_family_count`, which is not the relevance-qualified count.
4. Rank by relevance/value and select only within this deduplicated set.

Without valuations use `—`. Actual tool definitions determine document/family valuation scope; equal values are not family evidence. Unverifiable membership means unverified counts and limited delivery, not complete-count formulas.

## 4. Selection after deduplication

Use technical relevance as an entry criterion and patent value for ranking. High value cannot compensate for low relevance. If monetary valuation is unavailable, assess qualitative value from actual citations, rights status, coverage and text with reasons; keep the monetary column `—`, without simulated amounts/scores.

When results suffice, aim for a balanced selection within the overall cap:

- 3–4 core-family representatives directly matching the technical core.
- 2–3 highly cited/valuable foundational records indicating technical origins.
- 1–2 multi-jurisdiction examples with verified family links.
- 2–3 recent records from the past three years indicating evolution.

## 5. Mandatory count tiers

Relevance precedes quantity; ten is the cap. Record raw family count, then assess relevance to derive `eligible_family_count`. Default `listed_count = min(eligible_family_count, 10)`; honor a smaller user cap and disclose it. Unknown relevance stays on a pending list, outside eligible counts. Four raw but ineligible families mean raw = 4, eligible = 0, listed = 0.

| Eligible families | Action |
|---|---|
| ≥10 | Select ten using section 4. |
| 5–9 | List all; state “All N relevance-qualified families in this area are included.” |
| 1–4 | Perform the three expansion tiers, then list actual eligible results with hits and evidence-supported reasons. Low counts alone do not return to Gate A. |
| 0 | Perform all expansion tiers. If still zero, retain the area and search scope, distinguishing no hits, irrelevant samples and unverified evidence. State supported reasons/next steps, not that the company has no such patents. Low counts alone do not return to Gate A. |

### Three expansion tiers (0–4 eligible families, lowest cost first)

1. Expand synonyms: industry abbreviations, upstream/downstream process terms, parent-company terminology and original-language terms.
2. Check constraints: remove only restrictions added by the analyst. Preserve user-defined jurisdictions, dates and identities; obtain authorization before changing scope.
3. Check name variants and `ALL_AN`: add only identity-supported names belonging to the same confirmed entity and save before/after queries. Technical expansion preserves the entity restriction, without switching assignee fields or structured filters. New entities such as affiliates require consent when they expand scope. `ALL_AN` already includes original/historical assignees; its hits do not authorize expanding entity scope.

If still 0–4, present actual results. State only evidenced causes; otherwise give next verification steps. Possible explanations require specific evidence: trade-secret/data-based protection documented publicly; relevant patents held by an evidenced parent/affiliate; an early technology whose public timeline falls outside the available publication window; or terminology gaps demonstrated by new relevant expanded-search results. Do not present these hypotheses as established reasons.

Never borrow patents across areas, loosen assignees to add other entities, count simple-family siblings as independent representatives, hide sparse areas or lower relevance to fill tables.

## 6. Required patent table

Fixed order: No. | Patent number (link) | Publication/grant date | Jurisdiction | Title | Legal status | **Assessed value** | **Jurisdictional coverage**.

Add a citation-count column only on explicit request, using returned values or `—` if unavailable. Missing required facts use `—`, never blanks, zeroes or guesses. Retain value/coverage columns even if entirely missing, explaining why in search notes. Every title requires an italic technical sentence with a fine left border; see [writing rules](description-writing.md).

| Column | Source | Missing handling |
|---|---|---|
| No. | Local sequence | — |
| Patent number/link | Complete URL from search response | Number only if URL unavailable; never fabricate links. |
| Publication/grant date | Search and verified fetch_patent bibliography for the same publication version | `—` |
| Jurisdiction | Search and verified bibliography | `—` |
| Title | Search and verified bibliography | Do not leave blank; use `—` if unavailable. |
| Legal status | Search/details simple status; lifecycle evidence for specific legal events as needed | `—` |
| Assessed value | Actual valuation source and units, if available | `—`; never zero for PCT-stage records. |
| Jurisdictional coverage | Actual `response.relations.simple_family` members from `fetch_patent`; verified jurisdiction/publication codes | `—`; disclose partial membership. |

Value requirements:
- Without valuation capability, show `—` and explain; with values, show actual units.
- One representative per simple family; show geographical breadth in coverage rather than extra sibling rows.
- Label simple-family values only if the source establishes family-level scope; do not assume it for missing data.

Coverage requirements:
- Use `fetch_patent(include=["relations"], format="json")` and actual simple-family members only; never extended families.
- This plugin uses `fetch_patent` relations and does not assume an independently bound family service. Missing/authentication-required relationships mean `—`; partial returns state member scope without inferred complete coverage. Successful ordinary full-text retrieval does not establish successful relationship retrieval.
- Prefer jurisdiction count (e.g. “4 jurisdictions”); for small families (≤6 members), codes such as US/EP/KR/WO may be listed directly. EP/WO are regional/international offices.
- Member count differs from jurisdiction count: 23 members all in KR represent one jurisdiction, not 23.

## 7. Mandatory search notes

Explain independent overlapping queries, `matched_total`, simple-family deduplication (do not use `INPADOC` in reports), missing fields, and that technical sentences are assessments rather than claim construction. Disclose family scope for actual family-level valuations.

## Five-count disclosure under every area table

Read/calculate counts under [Step 3](../SKILL.md#step-3--search-patents-by-area). Missing is `—` with reasons; incomplete deduplication permits interim delivery only.

```text
This area's query matched {matched_total} publications; {returned_count} were retrieved.
Simple-family deduplication identified {independent_family_count} raw families,
of which {eligible_family_count} passed relevance review. This table lists
{listed_count} representatives, capped at ten by default without padding.
```

When `returned_count < matched_total`, label independent families as “within the returned sample.” Only complete pagination supports a full-query family count. If fewer than ten are eligible, disclose actual expansion steps/results under the tiers. Raw, eligible and listed counts are limited to the material retrieved and verified at each respective stage.

Prohibited mistakes: using hits/publications as representative counts; selecting ten before deduplication; showing repeated sibling valuations as distinct valuable assets; or padding/hiding an area because fewer than ten families remain.
