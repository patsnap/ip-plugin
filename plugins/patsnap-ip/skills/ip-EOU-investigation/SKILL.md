---
name: ip-EOU-investigation
description: "EoU Investigation helps companies identify potential patent infringement leads by matching their own patents with evidence from third-party products. It discovers relevant patents, explains key claim features, researches competing products, and maps supporting evidence into a clear comparison matrix. Findings are delivered in a standalone HTML report with traceable sources, evidence gaps, and recommended next steps to support further review."
metadata:
  version: "0.1.3"
---

# EOU Investigation

Use this workflow when a user wants to investigate a third-party product using their own patents. Establish the objective and choose how to search, read source material, trace relationships, and fill evidence gaps. Use available public web capabilities to find and read product material. Default dialogue, reports, labels, and templates to English and honor an explicit output-language request. Keep search language and jurisdiction independent of output language, and preserve original evidence with translations where needed. Explain findings in plain language and short tables. Lead with findings, evidence, and the next action, adding technical detail as needed.

Read the bundled references when their steps become relevant, and use the report template under assets. Resolve both relative to this Skill directory. Keep case records and generated files in the current task directory.

## Inputs and confirmation

The company is the minimum input required to begin. Extract it from the chat or existing case and ask only when missing. Resolve the name with `get_standard_assignee_name`, show the actual legal entity candidates and the understood constraints, and ask the user to confirm. Reuse an explicitly confirmed company unless a real ambiguity emerges. Store company and assignee identities separately. A competitor name identifies the investigation target and cannot determine or replace the user's company.

Product, technology or problem, competitor, owned patents, patent jurisdiction, and sales market are optional. State what each geographic or time constraint applies to. Use supplied information directly and distinguish suggested directions from user-specified constraints.

When the user specifies owned patents, ask whether they want additional recommendations. Reuse an existing explicit answer.

- If recommendations are wanted, include every specified patent in each portfolio. Each portfolio must contain at least two relevant patents verified as owned by the company.
- If recommendations are unnecessary, use the specified patents as the portfolio, including a single patent when applicable. Verify ownership before summarizing key claim points.
- Preserve the original input for malformed numbers, unverified ownership, or conflicts with company scope. State the specific issue and wait for the user to resolve it.

Obtain explicit confirmation separately for company scope, the selected portfolio, key claim points, and retained leads. Reuse prior answers. Interpret “yes” or “continue” at the current checkpoint without extending it to later choices the user has yet to see.

## Tools and methods

Patent and literature work uses the following nine tools. Check runtime definitions before first use and follow the actual schemas for requests and responses.

| Tool | Purpose |
| --- | --- |
| `get_standard_assignee_name` | Resolve company and standardized assignee identities |
| `get_corptree_hierarchy` | Find the immediate parent or ultimate parent as needed |
| `search_patent` | Find owned patents, relevant third-party patents, or patents by specified number |
| `fetch_patent` | Read claims and descriptions for the exact document, and retrieve family, citation, or figure information as needed |
| `fetch_patent_lifecycle` | Retrieve legal status, ownership changes, and other events |
| `field_analysis` | Explore the company's portfolio or aggregate the same query scope |
| `describe_search_capability` | Check supported fields and operators before specialized-domain searches |
| `search_literature` | Find relevant terminology, principles, and research |
| `fetch_literature` | Read the paper material actually returned |

The host constructs queries, screens results, decomposes claims, evaluates technical evidence, and prepares the report. Use each call to resolve the current question and reuse text and responses already acquired.

Check each request against confirmed user constraints and the actual schema. Use product or technology names for semantic and keyword expressions. Apply IPC, status, time, and jurisdiction filters only when explicitly specified by the user and supported by the schema. Copy internal patent and company IDs from actual responses. Use a known exact publication number directly where the interface supports it. Check the current case's material index before calling a tool to see whether existing material answers the question.

## Investigate from the current stage

### Directions and portfolios

Read [Directions and portfolios](references/portfolio-discovery.md) before recommending patents. When only the company is known, aggregate the portfolio, read representative patents, and combine those findings with public material to suggest a few concrete directions. When a product or technology is known, examine its mechanism. When a competitor is known, read its product material before searching for relevant owned patents.

Organize portfolios around products that could be investigated. For every patent, give the exact document number, title, owner, jurisdiction, status, protected subject matter, reason for recommending it, and relationship to the other members. Describe family versions separately and support complementary roles with text. Mark user-specified products and patents as “User specified.” Let relevance determine how many portfolios to present, and continue after the user confirms the selection.

Before presenting portfolios, compare their exact sets of documents. Merge identical sets and list their different uses as investigation angles. Describe supported technical roles, known citation links, and any unverified family membership separately. A limited relationship list that omits a document, different application numbers, or a citation link leaves family membership unresolved.

### Key claim points

Read [Claims and evidence](references/claims-comparison.md) and read the selected claims and dependencies in full. Summarize at least one point worth investigating per patent. Give the exact version and claim number, a plain-language explanation, supporting original wording, and conditions still to verify. Assign stable IDs and wait for written confirmation.

### Product leads

Read [Search and evidence gathering](references/product-evidence.md). Use available public web capabilities to investigate iteratively, starting from product material or patent relationships. For broad discovery, aim for ten sourced, deduplicated, specific models and report the actual number found. For a single competitor or model, investigate it in depth. Present a meaningful batch of findings before pursuing the most consequential gaps.

### Comparison and delivery

Build a matrix with one product per row and one confirmed claim point per column. Use ✓ when the material actually read supports the confirmed definition of the point and ? when confirmation is pending. Identify partially supported elements in the evidence details. Keep confirmed point definitions and checkmark criteria consistent. If a definition changes, revise it and ask for confirmation again. Classify a lead with at least one ✓ as “Evidence supported” and a lead with zero ✓ as “Pending manual review.” Record the quotation, source, location, reasoning, and uncovered conditions for each cell. Track the key point separately from all limitations of the original claim.

Use one overview row per retained product model and one column per confirmed key point. Put the product classification in the final column and element-level analysis in expandable details. Read the generated report, count its rows and claim-point columns, and check each classification against the retained list.

The user can remove leads in writing or add one with a URL alone. Read and verify a new URL before assessing it. After the user confirms which leads to retain, read [Report writing and template](references/report-writing.md) and use the [report template](assets/report-template.html) to generate a standalone HTML file. Lead with findings and the matrix, then expand on the portfolios, key points, and evidence. Explain in the report body what each patent protects and why it was recommended.

## Working across turns

When the investigation begins, read [Records and delivery](references/continuation-and-records.md). Before replying in any turn with substantive progress, confirmation, revision, or a pause, update `case.md` and read it back. Record the stage, pause status, confirmed and pending choices, exact patent and material index, and next action. Keep originals and detailed analysis in linked files and enough summary in the case record to resume across chats. Answer standalone conceptual questions directly.

When constraints change, new material arrives, or work pauses or resumes, revisit only the affected parts. On pause, save the status and handle only the user's intervening questions. When resuming in a new chat, read `case.md` and its necessary linked records before deciding whether further calls are needed.

Keep user material, product sources, original patent text, and investigation hypotheses separate. Hypotheses can guide queries and enter the evidence assessment only after obtaining direct support. Check citations, technical correspondence, and output consistency during the investigation. Keep unsupported conditions pending and specify the facts on which material findings depend.

Deliver supported results for the current stage before investigating decisive gaps. Record actual time, calls, and material reuse, and plan the next action around the requested depth and deliverable.

Use plain language in user-facing material. Keep raw JSON, internal IDs, tool names, and parameter troubleshooting in the working records.
