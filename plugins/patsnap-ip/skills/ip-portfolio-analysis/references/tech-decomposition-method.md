# Technology Decomposition And Patent Search

Use this reference to decompose technical topics, choose retrieval types, express search elements, reduce noise and evaluate sample coverage.

## End-To-End Business Flow

Patent retrieval follows the intelligence workflow:

```text
接收需求
→ 理解需求
→ 确认需求
→ 课题准备
→ 数据采集与处理
→ 专利分析
→ 报告形成
→ 交付应用
→ 成果管理与维护
```

For search-skill work, focus on:

```text
需求理解
→ 技术分解
→ 检索要素采集
→ 检索策略匹配
→ 检索式构建
→ 优化去噪
→ 查全查准验证
→ 数据入工作空间/标引
→ 支撑分析与报告
```

## Requirement-To-Search Routing

Choose the retrieval type based on the business question:

| Requirement type | Typical user goal | Search strategy |
| --- | --- | --- |
| 竞争现状/技术全景 | Understand industry development, hotspots, future directions, major competitors, and competitor selling points | Technology-topic search + applicant search |
| 技术创新/研发攻关 | Determine R&D direction, key functions, technical problems, product selling points, and source of technology | Technology-topic search + problem-type search |
| 风险预警 | Identify risk sources, target markets, self-developed vs outsourced modules, and risk technology modules | Applicant search + technology-topic search |
| 创新布局 | Identify core product technology, self-developed modules, advanced technology, and forward-looking directions | Technology-topic search |

Always collect search elements through RD+IP interaction before writing formulas.

## Technology Decomposition Dimensions

Decompose a topic using the dimensions that match the demand:

- **Technology problem**: what problem is solved.
- **Technology means**: mechanism, process, algorithm, material, structure, equipment, or method.
- **Technology effect/function**: efficiency, precision, preservation, water retention, noise reduction, cleaning quality, etc.
- **Application/product scenario**: product, module, use case, industry, market, or environment.
- **Structure/module**: components, subsystems, assemblies, interfaces.
- **Technical subfield**: lower-level technical route or branch.
- **Key elements**: composition, equipment, parameters, raw materials, intermediates, outputs.
- **Competition angle**: competitors, partners, suppliers, OEMs, and their match with problems/means/effects.

The decomposition should output search modules: technology branches, technical problems, technical effects, competitors, and any labels needed for later analysis.

## Core Topic Multi-Dimensional Expansion

For the core technical topic, expansion must be systematic and auditable. Do not only expand the literal user phrase.

| Dimension | Purpose | Examples |
| --- | --- | --- |
| Direct term/synonym | Capture obvious wording | 羧酸萃取剂, carboxylic acid extractant |
| Upper/lower concept | Avoid missing broader or narrower descriptions | 有机酸萃取剂, 环烷酸, 新癸酸 |
| Object/material/component | Capture what the invention is about | 萃取剂, 有机相, 羧酸类化合物 |
| Function/effect | Capture what the invention does | 萃取, 分离, 纯化, 选择性 |
| Mechanism/process | Capture how it works | 液液萃取, 反萃, 洗涤, 络合 |
| Application/scenario | Capture where it is used | 黑粉, 锂电池回收, 湿法冶金 |
| Product/trade name | Capture commercial or industry wording | Versatic acid, neodecanoic acid |
| Abbreviation/formula | Capture shorthand | NCM, NMC, Ni/Co/Mn |
| Classification | Capture language-independent records | IPC/CPC/FI/F-term/technology topic |
| Foreign-language variants | Capture non-English/non-Chinese patents | German/French/Japanese/Korean variants when important |
| Seed-patent terms | Capture real patent wording | terms from title/abstract/claims/description |
| Applicant/portfolio clues | Capture specialized industry wording | key applicant patents as terminology source |

For each dimension, record whether it was used, skipped, or pending user confirmation. If skipped, explain why.

## Three Main Search Types

### 1. Technology-Topic Search

Use when the user asks for a technical module, branch, or landscape.

General method:

1. Define the technical boundary and identify common/general technologies that need scope control.
2. Build a search-element table with keywords and classification codes.
3. Express keywords in Chinese and English.
4. Expand keywords through:
   - natural-language query construction via the same MCP build_patent_boolean_query when needed;
   - translation fields such as `TTL_ALL` for professional or rare foreign terms;
   - background research;
   - relevant patents and literature;
   - classification definitions.
5. Expand classifications through:
   - classifications actually returned by the same MCP search/fetch tools;
   - user-provided classification definitions (missing definitions remain unverified);
   - accurate patents from title-focused searches;
   - key applicants' target patents;
   - family patents for CPC, FI/F-term, and small-language classification coverage.
6. Construct modular formulas locally; execute approved formulas through the same MCP search_patent Boolean strategy.
7. Optimize through classification statistics, applicant statistics, keyword noise, and missed elements.
8. Validate recall and precision.

Example module logic from the training:

```text
Module 1 = (topic object keywords OR topic object classification)
           AND (technology keywords OR technology classification)
           AND feature/effect keywords

Module 2 = (topic object keywords OR topic object classification)
           AND precise technology classification

Module 3 = broader technology classification
           AND feature/effect keywords

Final = Module 1 OR Module 2 OR Module 3
```

### 2. Problem-Type Technology Search

Use when the user asks about a key technical problem, function, defect, effect, or R&D obstacle.

Problem search is harder because problem wording often appears only in description, is not standardized, and can create broad noisy results.

Element table:

| Element | Meaning |
| --- | --- |
| 技术问题/效果表达 | direct problem, opposite expression, desired effect |
| 解决手段 | methods the industry uses or R&D plans to use |
| 关联模块 | module where the problem occurs |
| 应用领域/背景 | scenario where the problem arises |
| 申请人 | competitors, suppliers, OEMs, or benchmark companies |

Search routes:

```text
Direct problem route:
  problem/effect terms + application/domain focus

Applicant-focused route:
  problem/effect terms + applicant

Means-focused route:
  problem/effect terms + solution means or related module
```

Field guidance:

- Use precise fields for direct problem expression when possible.
- In title/abstract (`TA`), keep proximity tight, often same sentence.
- In claims/description, allow wider proximity because problem/effect wording may be separated from technical means.
- If the problem is domain-specific, application-domain constraints may be unnecessary.
- If the problem is general, add application, module, applicant, or classification constraints.

### 3. Applicant Search

Use when the user asks about competitors, benchmark companies, partner portfolios, risk warning, or applicant-specific technology portfolios.

Applicant-name expansion:

- company tree;
- co-application relationships;
- family patents in different languages;
- company material already supplied by the user;
- business/news material already supplied by the user;
- industry expert knowledge;
- OEM or supplier names.

Applicant search strategy:

```text
Module 1 = field/topic object terms OR field/topic classification
Module 2 = broader topic terms AND field classification
Module 3 = core technology terms AND (field classification OR broader field terms)
Final = (Module 1 OR Module 2 OR Module 3) AND applicant names
```

For focused applicants, full applicant retrieval may be acceptable. For diversified groups, intersect with technical fields and validate precision.

Applicant field guidance:

- Use all relevant applicant fields and standardized names when available.
- Expand company names across languages and corporate structure.
- Use design-patent or LOC classification attention when the target industry values design patents.

## Patsnap Operation Lessons

Choose retrieval operations according to the available tools (see [工具使用要点](tool-usage.md)):

- Expand natural-language concepts with build_patent_boolean_query when appropriate; do not send an existing executable query to the builder.
- Read technical terms and classifications from actual search_patent/fetch_patent records and user-provided definitions; do not invent unavailable classification helpers.
- Execute formulas through search_patent; inspect field_analysis for supported classification and applicant dimensions.
- Keep sample sets, local labels, formula variants and coverage comparisons in local files. Local tables are sufficient for sample comparison.

## Field Selection Principles

Choose fields according to the role of the term:

| Field scope | Best use |
| --- | --- |
| Title/abstract/claims | object + core technical feature; high precision |
| Claims | protected technical features and necessary solution features |
| Description/full text | technical problem, effect, background, embodiment, application scenario; high recall |
| Classification | language-independent focus and recall expansion |
| Applicant | competitor or benchmark-company focus |

Training principle:

```text
对象 + 核心技术特征: use precise fields for focus.
重要技术特征: balance recall and precision.
技术问题 / 效果 / 优点: use broader fields for maximum recall, then validate and denoise.
```

## Optimization And Denoising

Use classification and keyword denoising in any order:

- Inspect classification statistics and remove clearly unrelated classification groups.
- Inspect applicant statistics and identify obviously unrelated applicants.
- Browse noisy records to identify which keywords caused noise.
- Add noise expressions only after reviewing records.
- Supplement missed keywords and classifications back into the search-element table before revising formulas.

Do not treat the first formula as final. Formula optimization is part of the business process.

## Recall And Precision Validation

Recommended validation:

- Choose key applicants to validate recall and precision.
- Sample patents manually and calculate precision; 80%+ sample precision can serve as a working target when appropriate.
- For recall validation, create an objective sample:
  - select one applicant;
  - retrieve all applicant patents;
  - filter by application year or other objective dimension;
  - manually screen relevant patents;
  - put retrieved sample and formula results into local tables;
  - tag sample records and compare hit coverage;
  - analyze missed records and decide whether to revise the formula.

Recall result formula:

```text
查全结果 = 检索结果中打上样本标签数 / 样本总数
```

Precision result formula remains:

```text
查准率 = 抽样相关记录数 / 抽样总数
```

## Application Checklist

Apply these criteria to select and validate the retrieval approach:

- Decide whether the task is technology-topic search, problem-type search, applicant search, or a combination.
- Choose decomposition dimensions from the business requirement.
- Use search/fetch, query construction, aggregation and local sample comparison according to the task.
- Treat keyword/classification expansion and denoising as iterative database operations, not purely offline reasoning.
- Use local record tagging to make sample coverage validation operational; sample coverage is not proof of complete corpus recall.
