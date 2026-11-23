# Investigation records, resumption, and reporting

Use the current task directory. At the start, save `case.md` with the user's company, objective, specified inputs, geographic and time constraints, current step, confirmed choices, open questions, and next action. Link confirmations to the actual user message or a traceable location and keep the model's analysis separate.

Update the case record and read it back before the end of each substantive turn, especially after confirmation of scope, portfolio selection or key points, or a pause or change in constraints. Verify the actual file and its current status and additions. If writing fails, retain the pending content and explain what was actually saved.

Keep the case record concise and link to complete originals and detailed analysis. Cite existing text and analysis by file path and precise location. Change only what is affected by new confirmation or evidence. Keep at least the following:

- Current status, including active investigation, the confirmation awaited, or pause, plus the user's latest decision and the next action.
- Legal company name, confirmed scope, verified assignee mappings, and the confirmation message.
- User-specified products, patents, competitors, patent jurisdictions, product markets, and time constraints, with individual confirmation status.
- Candidate and selected portfolios, exact versions, each patent's role and supporting text, and selection status.
- Stable IDs for confirmed key points, their meanings, claims, exact text locations, and uncovered conditions.
- Retained products and models, key point mappings, classifications, evidence, and gaps. Link a large matrix separately if useful.
- Material index with the object requested, actual publication numbers and IDs, file paths, what was read, failures, and truncation.

A new chat should be able to recover the confirmed scope and stage from the case files. Chat history can supplement a self-contained case record. Answer standalone conceptual questions directly.

Save original tool requests and complete responses where available, or record an accessible location for the host's original execution record. For long responses, prefer the host's save, export, or file handling capability. Cite original material and keep quotations, interpretations, and hypotheses separate. If the host supplies only partial text or excerpts, save the range actually obtained, mark it “Excerpt read,” and note any gap in preserving the response. For web pages, files, and patent text, keep the source, object, retrieval time, range actually read, and any truncation or failures.

Reuse material before refreshing it for current legal status or updated product documents. Before requesting the same object again, check whether the prior scope and date still apply. Map patent or product IDs to source text and provenance, and keep raw responses intact.

## Changes and pauses

When a market, jurisdiction, or exclusion changes, identify affected queries and leads, keep the prior version, and reassess the affected results. When patents or key points change, review related matrix columns and reuse material that still applies.

For an added link, first read it and verify the model, then update relevant cells. For a removed lead, record the user's choice and the original row. Build the final report from the current retained list. On pause, save progress and stop investigating. Answer intervening questions, then resume at the current step when the user asks to continue.

When resuming across tasks, read the case record and files it relies on, then state where work resumes. If the case is unclear, ask only for information needed to locate it. If the environment cannot retain files, give a portable text summary and state what was actually saved.

## HTML delivery

After the user confirms the retained leads, read [Report writing and template](report-writing.md) and use `assets/report-template.html`. Populate the findings, counts, scope, portfolio, key points, matrix, evidence, and next steps with current confirmed data, using the actual counts available. Default to plain English, honor the requested language, and preserve original evidence with necessary translations.

Keep the `lead-matrix` table. Add one column per confirmed point and one row per retained model. Put ✓ or ? in each cell, link to its evidence, and show the row classification in the final column. Place long element-by-element tables in the evidence details. Verify row and point-column counts against the confirmed lists and recalculate every row label.

Use the current company, patent versions, key points, and retained products. Each matrix cell should expand to its reasoning and gaps. Link to actual URLs or local evidence files. Use patent links from tool responses when available, otherwise give the exact number and original-text location.

Deliver standalone HTML with inline styles, horizontally scrollable wide tables, and native expandable details. Keep internal IDs and long JSON in the working material. Save raw responses separately and show readers the quotations, locations, and sources they need.

Read the generated file and verify placeholders, columns, citations, matrix classifications, selected counts, and links. Provide the actual file link, completed scope, key findings, and material still needed. Record only checks actually completed and expand the details as requested.
