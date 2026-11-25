# Patent Layout PPT Output Spec

Use this reference when creating or reviewing a patent layout PPT report.

## Default Deck Structure

| Page | Title | Required Content |
| --- | --- | --- |
| 1 | 课题范围与核心结论 | Topic, companies, time range, geography, data sources, 3-5 key conclusions |
| 2 | 技术主题拆解 | Technology tree with modules, submodules, keywords, and application scenarios |
| 3 | 行业与前沿动态 | Public industry trend, policy/standard/market signals, why the topic matters |
| 4 | 专利检索与数据口径 | Search scope, formulas or formula summary, deduplication rules, dataset size |
| 5 | 竞对专利态势 | Company trend, portfolio size, technology distribution, top applicants |
| 6 | 前沿专利技术 | Representative high-value patents with technical problem, solution, effect |
| 7 | 五类技术空间 | Enterprise existing, competitor existing, overlap, competitor extension, enterprise extension |
| 8 | 专利布局矩阵 | Modules mapped to protection, reserve, countermeasure, design-around, no-layout |
| 9 | 专利集群设计 | Core/peripheral/improvement/application/defensive patent clusters |
| 10 | 行动计划（仅在用户要求时） | Filing quantity, priority, patent type, timeline, owner, next-step materials |

默认保留各模块的建议去向。第 10 页仅在用户要求行动计划时提供。短版保留第 1、2、5、7、8 页，若要求行动计划则保留第 10 页。长版可按技术模块展开第 5–9 页。

## Slide-Level Rules

### 课题范围与核心结论

State the exact boundary. Do not bury the conclusion behind method language.

Must include:
- Technology topic
- Target companies
- Time range and geography
- Data source and search date
- Key conclusion bullets

### 技术主题拆解

Show a business-readable technology tree. Each branch should become a search and analysis dimension.

Good branches are functions, components, algorithms, data flows, deployment locations, or application scenarios. Avoid vague labels such as "AI technology" or "platform capability".

### 竞对专利态势

Use normalized applicant groups. Label whether counts are publications, applications, or families.

Useful views:
- Filing trend by year
- Company ranking
- Module distribution
- Recent growth modules
- High-value patent examples

### 五类技术空间

This is the bridge from intelligence analysis to layout strategy.

Use five buckets:
- 企业现有技术
- 竞争对手现有技术
- 双方交集技术
- 竞争对手拓展技术
- 企业可拓展/拟拓展技术

For each bucket, provide evidence and action implication.

### 专利布局矩阵

Rows should be technology modules. Columns should be strategy types.

Use:
- 保护性布局: already or soon-to-be productized by enterprise
- 储备性布局: future roadmap or emerging opportunity
- 对抗性布局: competitor-heavy control point
- 规避/替代: high infringement or blocking risk
- 暂不布局: low business relevance or weak evidence

### 专利集群设计

Show how individual filings work together. A cluster is not just a list.

Common cluster types:
- 组合式: several complementary patents protect one complete solution
- 地毯式: dense coverage around variants and implementation details
- 包围式: peripheral alternatives around competitor core patents
- 阶梯式: basic, improvement, application, and manufacturing/process layers

## Quality Gate

Before delivery, check:

- No `XXX`, `XXXX`, "示例", or unfilled placeholders remain.
- Every patent number and claim summary can be traced to a source.
- Search scope and data date are stated.
- Counts use the adopted publication/application unit. Keep family relationships and counting bases separate.
- Applicant aliases are normalized.
- Recommendations map to evidence, not only intuition.
- Sensitive internal information is masked if requested.
