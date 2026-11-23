# Exploring directions and owned patent portfolios

## Company and constraints

Check company and assignee match status separately. Use the actual `company_id` for corporate relationships and verified standardized assignee IDs for patent filters. Record the ultimate parent, selected company, and directly associated assignees separately. State the actual coverage of returned relationships. Fix the company scope after confirmation.

Use the product, technology, problem, and competitor to interpret one another while preserving the original inputs. Organize names, components, connections, motion or data flow, triggers, values, negation, and alternative implementations. Keep source statements separate from deductions. Respect exclusions in the search and treat user conjectures about competitor internals as facts to verify.

Organize the description into explicit constraints, components, relationships, and direct functions, preserving the user's original wording and source. Use deductions for open questions or query hypotheses. If the connection is unspecified, flag it for verification and look for a diagram or manual.

## Search based on the information available

- With only a company, use `field_analysis` to examine the same company's technology, time, or status distribution, then use `search_patent` to find and read representative patents. Combine the classifications with company product material to propose several distinct technical directions.
- With a product or technology, build complementary expressions around components, mechanisms, problems, industry terminology, and language variants. Start with a reasonable route and add others in response to specific gaps. Record the queries and the basis for combining their results.
- With a competitor, use available public web capabilities to read its product material. Anchor the search in actual mechanisms and treat competitor patents as third-party leads.
- With specified patents, verify the exact documents and ownership first, then follow the user's choice about recommendations. Keep every specified number in each recommended portfolio.

Match `search_patent` strategies to their parameters. Combine ordinary semantic, keyword, and filter strategies as the schema allows. Use the Boolean strategy alone with an executable field expression. Keep company and user constraints in every OR branch. Use `describe_search_capability` before specialized field searches. Start with a small result set for inspection, then page or expand based on relevance and new information.

Set filters against the user's wording and confirmed scope. Translate the user's technical direction into semantic, keyword, or technical text expressions. Treat inferred IPC, legal status, dates, or jurisdictions as possible suggestions. For fields the schema requires the user to specify, obtain that condition before use. Apply the same rule to equivalent Boolean filters. For a confirmed company, restrict the search using standardized identities from the resolution response.

For an exact known publication number, retrieve the document directly with an identifier supported by `fetch_patent`. Search when the number or identity requires resolution. Copy internal IDs exactly from saved responses. On failure, check the number and identity mapping, then retry with the actual number or verified ID. Save the mapping between exact publication number, returned ID, and raw response file.

## Read the patents before forming portfolios

Use abstracts for initial screening. Base recommendations and technical relationships on claims, relevant description passages, and actual product material. Follow the schema for `fetch_patent` defaults and `include` values. Retrieve relationships or figures only when needed. Use `fetch_patent_lifecycle` to check status, assignments, and similar events.

Check the material index and what has already been read. If you have the original text but need family data, make one targeted relationship request. If the response also returns the full text, record the new relationship data and reuse what was already read. Read sections using the actual character length and reach the relationship fields of each document being compared. Record counts, truncation, pagination, and unknown completeness.

Explain at least three things for each portfolio:

1. Which product or technical problem the investigation addresses.
2. What distinct part each patent protects and where the original text supports it.
3. Why they should be investigated together and what still requires product-specific verification.

Distinguish versions of the same invention, complementary technologies, and merely similar subjects. Verify simple family membership using actual relationships. Read applicable claims separately for original applications, divisionals, and continuations. Show versions side by side for jurisdictional and textual differences. Complementary members must cover genuinely different subject matter.

Track technical roles, citations in either direction, application chains, and family membership separately. Cite actual citation responses. Absence from a limited family list, different application numbers, or a citation alone leaves family membership unresolved. If priority fields are missing, pagination is incomplete, or relationship coverage is unknown, state that no match was found in the relationships read and that full family membership remains unverified. When determining membership, retain its source, family type, and the scope read.

Prioritize fit with the direction, the relationship between claim mechanisms and possible product functions, applicable jurisdictions and status, and the likelihood of observing the mechanism in public evidence. Use sourced citation, family, and time information as supporting reasons. List unknowns explicitly and avoid speculative scores.

## Present recommendations

Lead with the portfolios available for selection. Use a short table to show product direction, members, what each protects, recommendation reasons, and sources. Quote text supporting each patent's actual role. Show current ownership and when it was verified. Distinguish facts from investigation suggestions. Keep long claims and document-level checks in the case record. If there are too few members, report the actual result and possible next searches, then let the user decide.

Compare portfolios by their exact document membership. Reordering documents or changing the rationale leaves the set identical. Merge identical sets and list their different product uses. Sets can share members when each additional member has an explained role. List family versions separately in member descriptions and explain differences between portfolios in terms of protection.

Track `total_hits`, returned page counts, local deduplicated counts, and family counts separately. Independent searches may overlap. Deduplicate combined results by exact document identity and explain counting rules alongside the table.
