# Patent Layout PPT Output Spec

Use this reference when creating or reviewing a patent layout PPT report.

## Default Deck Structure

| Page | Title | Required Content |
| --- | --- | --- |
| 1 | Scope and key conclusions | Topic, companies, time range, geography, data sources, 3-5 key conclusions |
| 2 | Technical decomposition | Technology tree with modules, submodules, keywords, and application scenarios |
| 3 | Industry and frontier developments | Public industry trend, policy/standard/market signals, why the topic matters |
| 4 | Search and counting conventions | Search scope, formulas or formula summary, deduplication rules, dataset size |
| 5 | Competitive patent landscape | Company trend, portfolio size, technology distribution, top applicants |
| 6 | Frontier patent technologies | Representative high-value patents with technical problem, solution, effect |
| 7 | Five technical spaces | Enterprise existing, competitor existing, overlap, competitor extension, enterprise extension |
| 8 | Portfolio matrix | Modules mapped to protection, reserve, countermeasure, design-around, no-layout |
| 9 | Patent cluster design | Core/peripheral/improvement/application/defensive patent clusters |
| 10 | Action plan (only when requested) | Filing quantity, priority, patent type, timeline, owner, next-step materials |

Page 10 is optional unless the user requests an action plan; dispositions remain required. If the requested deck is shorter, preserve pages 1, 2, 5, 7 and 8, plus 10 when requested. If the deck is longer, expand pages 5-9 by technology module.

## Slide-Level Rules

### Scope and key conclusions

State the exact boundary. Do not bury the conclusion behind method language.

Must include:
- Technology topic
- Target companies
- Time range and geography
- Data source and search date
- Key conclusion bullets

### Technical decomposition

Show a business-readable technology tree. Each branch should become a search and analysis dimension.

Good branches are functions, components, algorithms, data flows, deployment locations, or application scenarios. Avoid vague labels such as "AI technology" or "platform capability".

### Competitive patent landscape

Use normalized applicant groups. Use the canonical publication/application unit; family relationships remain separate.

Useful views:
- Filing trend by year
- Company ranking
- Module distribution
- Recent growth modules
- High-value patent examples

### Five technical spaces

This is the bridge from intelligence analysis to layout strategy.

Use five buckets:
- Company existing technology
- Competitor existing technology
- Shared technology
- Competitor expansion
- Company feasible/proposed expansion

For each bucket, provide evidence and action implication.

### Portfolio matrix

Rows should be technology modules. Columns should be strategy types.

Use:
- Protective strategy: already or soon-to-be productized by enterprise
- Reserve strategy: future roadmap or emerging opportunity
- Counter-positioning: competitor-heavy control point
- Design-around/alternatives: high infringement or blocking risk
- Defer: low business relevance or weak evidence

### Patent cluster design

Show how individual filings work together. A cluster is not just a list.

Common cluster types:
- Combination: several complementary patents protect one complete solution
- Dense coverage: dense coverage around variants and implementation details
- Surrounding: peripheral alternatives around competitor core patents
- Layered progression: basic, improvement, application, and manufacturing/process layers

## Quality Gate

Before delivery, check:

- No `XXX`, `XXXX`, "example content", or unfilled placeholders remain.
- Every patent number and claim summary can be traced to a source.
- Search scope and data date are stated.
- Counts follow the canonical publication/application unit with family links separate.
- Applicant aliases are normalized.
- Recommendations map to evidence, not only intuition.
- Sensitive internal information is masked if requested.
