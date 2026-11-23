# Writing the report and filling the template

Before delivering HTML, read all of `assets/report-template.html`. Preserve its structure, styles, navigation, matrix skeleton, and reading scripts. If the file is truncated, continue to the end. Populate it with current case data and verify the actual output.

Escape plain text fields, use actual source addresses, and handle layout HTML separately from original evidence. Use the host's available file processing capabilities to populate the template in bulk if useful. Reuse confirmed portfolios, key points, matrix entries, and material records, then verify the generated file.

## Reading order

Start with two or three sentences covering what was found, how far the evidence supports it, and the most important gap. Follow with scope and the product matrix, then patents, key points, and evidence. Default to plain English and honor explicit output-language requests. Keep original titles and foreign-language evidence in the details. If the report language changes, localize template labels and set the HTML language accordingly, preserving original quotations.

For each patent, state in the body what it protects, why it was recommended, and how it relates to other portfolio members. Explain the specific mechanism and confirmation status of each key point. Replace placeholder instructions with case content. Use expandable details for original text, long element tables, and supporting detail.

## Header fields

- Fill `report_title`, `report_subtitle`, `report_date`, and `report_status` with the actual title, brief description, date, and confirmation status.
- Use the current deduplicated retained product count for `lead_count`. Compute `supported_count` and `pending_count` from the matrix rows. Their sum equals `lead_count`.
- Deduplicate the exact selected patent documents for `patent_count` and check against the portfolio, key points, and matrix.
- Use `findings_summary` for findings and decisive gaps, and `priority_next_step` for the single highest-priority item to obtain or action to take.
- Fill `confirmed_scope` with `div > dt + dd` for company, product, technology, competitor, user-specified patents, patent jurisdictions and statuses, product markets, and time constraints. Use “Unrestricted” for absent optional conditions and `div.full` for long descriptions.
- Use `coverage_summary` to show what was read, assessed, and outside coverage. Mark a draft and specify gaps when confirmation is pending or material conflicts.

## Matrix and IDs

Keep `table#lead-matrix`. Use one row per model, one column per confirmed key point, and a final classification column. In `core_point_headers`, use `th.core-col` with a stable point ID and short title linking to the point's explanation.

In `product_rows`, use `th.product-cell[scope=row]` for the company, exact model, and source entry. Use `td.match-cell` for each comparison. Use `a.mark` for ? and `a.mark.supported` for ✓ and link each to an existing evidence detail. Keep cells brief and put extended reasoning, quotations, and uncovered conditions in the details.

Use `li` entries in `core_point_legend` to map each column ID to the exact publication number, claim, and plain-language mechanism. Use unique, consistent point IDs across the report, matrix, and evidence. List complete claim elements separately with element IDs.

For a product with at least one ✓, label the final cell “Evidence supported” using `span.badge.supported`. Use “Pending manual review” and `span.badge.pending` for all other products. Follow the confirmed point definitions and criteria. Put partial element support in the details. Keep ? when evidence is insufficient and verify the mechanism even when sources describe the same effect.

## Portfolios, key points, and evidence

Use `div.group` for portfolios and `article.patent` for members in `portfolio_overview`. Use `div.item-heading`, `p.patent-id`, `div.tags`, and `dl.reading-notes` as needed for exact version, owner, status, protected subject matter, recommendation rationale, and relationships. Apply “User specified” where the inputs warrant it.

Use `article.core-point` for each entry in `confirmed_core_points`, with the same ID as its header link. Explain the mechanism, exact document and claim, necessary dependencies, and confirmation status. Use `details.evidence-detail` for the full claim and original-language element mappings.

Group `evidence_details` by product in `article.lead`. Match every `details.evidence-detail` ID to its matrix link. In `div.evidence-body`, give the reasoning, original product quotation, source and location, scope supported, missing conditions, and priority evidence. Specify the exact boundary of partial support.

Use `ol.sources` and `ol.next-actions` for deduplicated sources and concrete follow-up actions in `sources_and_next_steps`. Cite original text on the mechanism for technical judgments and use quotes limited to number, owner, or status for their respective metadata. Keep original quotations separate from explanations. Use actual web URLs. For local-only evidence give the filename and location, and use relative links when the files are packaged with the report.

Cite user material as a factual source within the verified scope. Verify companies, products, numbers, and technical judgments from reference reports before adopting them. Retain unresolved family status and explain supported technical roles and citations independently. State the subject and date of historical litigation or prior case conclusions. Compare current models using material applicable to those models.

## Verify delivery

Read the populated HTML, remove all placeholders, and verify the current confirmed list, counts, matrix rows and columns, fixed labels, unique IDs, and anchors. If versions or members conflict between the portfolios, key points, and matrix, resolve them in the case record. Verify evidence for each product and model.

Check that each patent and key point has a readable explanation, long original passages are expandable, and missing evidence and pending items are marked accurately. Default to A4 portrait printing. For many claim points, switch to A4 landscape if needed and recheck widths. Where the host allows, check desktop and narrow layouts, expanding details, horizontal scrolling, and printing. Record the checks actually completed.
