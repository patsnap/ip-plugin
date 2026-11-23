# Target-jurisdiction practice and X/Y evidence audit

Use this reference for inventive-step analysis; it does not replace current local law, examination guidelines or case law. Record the target jurisdiction and official rule version at the outset; verify current official-office texts when rules may have changed.

## Shared X/Y roles

X/Y/A are search-evidence roles relative to the current solution and evidence path, rather than permanent document attributes.

1. Verify dates first. Ineligible documents remain technical leads or later-published explanatory material.
2. Explain why an `X` document is sufficient alone; do not silently add cross-document knowledge.
3. Each `Y` belongs to a numbered group, such as `Y1 = P1 + S1`. Identify primary P, secondary S, differences covered, teaching, compatibility, expectation of success and contrary teaching.
4. Separate documents containing individual parts support `Y-candidate` only; use `Y-confirmed` after the complete group passes the jurisdiction’s standard.
5. Treat families, corresponding applications and substantially identical disclosures as one technical evidence source; do not combine them with each other in a Y group.

## CN: China

Apply the current Patent Examination Guidelines’ three-step approach and requirements for combination inventions and common knowledge:

1. Choose closest art by technical field, problem, effect/use and necessary features as a reasonable modification starting point, without mechanically counting features.
2. Identify differences and the actual technical problem objectively from their effects, without embedding the difference or answer in the problem.
3. Determine whether prior art as a whole provides technical teaching. Secondary means must perform the same function there, or common knowledge must be supported by verifiable evidence. Check structural conflicts, changed use, contrary teaching and unpredictable effects.

A CN-Y group records at least primary document, difference group, actual problem, secondary means and function, why a skilled person would adopt them, and whether the modified arrangement works. Three or more documents are not automatically forbidden, but more sources, distant fields and interface changes require a stronger independent, coherent teaching rather than hindsight assembly.

Prefer textbooks, technical dictionaries, manuals and standards for decisive common knowledge. An analyst’s unsupported “routine design” remains unverified. Asserted unexpected effects must be comparable with closest art and supported by the disclosure.

## EP: European Patent Office

Use the Problem-Solution Approach: choose realistic closest prior art/most promising starting points, determine differences and the objective technical problem, and apply the could-would approach. Ask whether a skilled person would, rather than merely could, adopt secondary teaching to solve the problem. Address multiple reasonable starting points and partial problems when appropriate, without embedding the invention in the problem. Mere combinability cannot establish `Y-confirmed`; give the would rationale and reasonable expectation of success.

## US: United States

Use the Graham factors and KSR framework: prior-art scope, claim differences, ordinary skill and objective evidence. Articulate combination reasons, such as known methods improving similar devices, predictable combinations, design needs or market pressure. Check analogous art, reasonable expectation of success, teaching away and secondary considerations. Conclusory common sense is insufficient.

## JP: Japan

Starting from differences against the primary reference, examine combination motivation from technical field, problem, action/function or teaching, with obstacles and advantageous effects. Similar components alone do not establish motivation. Evaluate remarkably advantageous, unexpected effects separately.

## KR: Korea

Assess closest art, differences, problem and ease of combination, checking relationships in field, purpose and function/action, combination suggestions, technical obstacles and unexpected effects. Use verified current KIPO terminology; without a verified rule version, retain Y-candidate status.

## PCT/ISA or no specified country

Provide X/Y/A candidates by international-search-report relevance roles without extending them to a national final inventive-step conclusion. Y means particular relevance in combination with one or more other documents; specify actual groups rather than an isolated Y letter.

## Output table

Each Y group contains at least:

| Field | Content |
| --- | --- |
| `path_id` | Y1, Y2, … |
| `jurisdiction` | CN, EP, US, JP, KR or PCT/ISA |
| `primary` | Primary document and date eligibility |
| `differences` | Complete difference group against the primary |
| `secondary` | Secondary documents and differences addressed, excluding family duplicates |
| `teaching_or_motivation` | Jurisdiction-specific teaching/motivation with source locations |
| `same_function` | Whether secondary means serve the same function in the source and target combination |
| `compatibility` | Optical, mechanical, electrical, control, material or step interfaces |
| `expectation` | Reasonable expectation of success |
| `counter_indications` | Contrary teaching, changed use, structural conflicts, unexpected effects |
| `role` | Y-candidate or Y-confirmed |
| `conclusion` | Effect on inventive step and unresolved issues |
