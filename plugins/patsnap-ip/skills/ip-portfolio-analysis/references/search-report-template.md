# Complete Search Report Template

Use this template as the required output structure for a Patsnap technology-topic retrieval report. Do not deliver only a final formula unless the user explicitly asks for a formula-only answer.

## 0. 执行方式与确认门

`待用户确认` 是流程闸口，不是普通备注。每个确认门需要用户点击确认按钮或明确回复确认后，才进入下一环节执行。

| 阶段 | 输出内容 | 确认动作 | 确认后进入 |
| --- | --- | --- | --- |
| Gate 1 | 原始需求理解 + 技术边界 | 用户确认边界无误 | 技术拆解 |
| Gate 2 | 技术拆解表 | 用户确认拆解无误 | 技术要素表 |
| Gate 3 | 技术要素表 + 噪音要素表 | 用户确认要素无误 | 检索策略表 |
| Gate 4 | 检索策略表 + 分类号/位置符策略 | 用户确认策略无误 | 逐条检索式 |
| Gate 5 | 逐条检索式 + 噪音检索式 + 总检索式 | 用户确认检索式无误 | 智慧芽执行/结果记录 |
| Gate 6 | 检索结果 + 查全查准校验方法 | 用户确认是否进入独立校验 | 后续查全查准校验/最终固化 |

If the user asks for a full draft in one pass, include every section but keep all gates marked `待用户确认`; do not treat the formulas as approved for execution.

## 1. 技术主题

- 用户原始检索需求（原文保留）:

```text

```

- 技术主题:
- 检索目的:
- 检索类型: 技术主题检索 / 问题型技术主题检索 / 申请人检索 / 混合检索
- 应用场景/产业边界:
- 数据库:
- 国家/地区:
- 时间范围:
- 法律状态:
- 专利类型:
- 去重口径:
- 检索日期:
- 用户提供的种子证据:
- 原始需求确认状态: 已确认 / 待用户确认 / 已根据用户反馈修订

### 需求理解与执行假设

| 项目 | 当前理解 | 来源 | 用户确认状态 |
| --- | --- | --- | --- |
| 技术主题 |  | 用户原文 / agent推断 | 待确认 |
| 应用场景 |  | 用户原文 / agent推断 | 待确认 |
| 检索目标 |  | 用户原文 / agent推断 | 待确认 |
| 数据范围 |  | 用户原文 / 默认假设 | 待确认 |
| 交付物 |  | 用户原文 / 默认完整报告 | 待确认 |

## 1.1 技术主题定义/概念说明

在进入技术边界前，先用文字说明本次检索主题的定义、核心技术特征、应纳入的概念、容易混淆但不属于核心边界的概念。

```text

```

确认状态: 待用户确认

## 2. 技术边界

### 纳入范围

| 边界项 | 说明 | 来源 | 用户确认状态 |
| --- | --- | --- | --- |
|  |  | 用户原文 / agent推断 / 样例方法 | 待确认 |

### 排除范围

| 排除项 | 排除原因 | 是否可能造成漏检 | 用户确认状态 |
| --- | --- | --- | --- |
|  |  | 是/否/待评估 | 待确认 |

### 边界判断说明

-

### 边界确认问题

- 请确认上述纳入/排除范围是否符合本次检索目标。
- 若有必须纳入或必须排除的技术场景、产品、企业、时间范围，请在执行检索前补充。

## 3. 技术拆解表

| 一级主题 | 二级技术/模块 | 三级技术/要素 | 技术描述 | 检索目的 | 对应策略编号 | 用户确认状态 |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | 待确认 |

### 技术拆解确认问题

- 请确认技术拆解层级是否过粗、过细或存在缺失分支。
- 请确认每个分支是否都需要进入检索式，或仅用于后续标引/分析。

## 4. 技术要素表

| 要素编号 | 要素名称 | 中文关键词 | 英文关键词 | 缩写/商品名/别名 | 分类号 | 字段建议 | 备注 | 用户确认状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A |  |  |  |  |  |  |  | 待确认 |

### 核心主题多维扩展检查表

| 扩展维度 | 扩展内容 | 扩展依据 | 是否纳入检索式 | 用户确认状态 |
| --- | --- | --- | --- | --- |
| 直接术语/同义词 |  | 用户原文/关键词助手/样本专利 | 是/否/待验证 | 待确认 |
| 上位/下位概念 |  | 背景调研/分类号/专家知识 | 是/否/待验证 | 待确认 |
| 对象/材料/组件 |  | 技术定义/样本专利 | 是/否/待验证 | 待确认 |
| 功能/效果 |  | 技术问题/功效表达 | 是/否/待验证 | 待确认 |
| 机理/工艺/方法 |  | 工艺链/说明书表达 | 是/否/待验证 | 待确认 |
| 应用场景/产品模块 |  | 用户边界/行业场景 | 是/否/待验证 | 待确认 |
| 商品名/商业表达 |  | 产品资料/样本专利 | 是/否/待验证 | 待确认 |
| 缩写/化学式/简称 |  | 行业表达/样本专利 | 是/否/待验证 | 待确认 |
| 分类号 |  | IPC/CPC助手/分类浏览 | 是/否/待验证 | 待确认 |
| 外文变体 |  | 翻译字段/同族专利 | 是/否/待验证 | 待确认 |
| 种子专利术语 |  | 种子样本 | 是/否/待验证 | 待确认 |
| 申请人术语线索 |  | 重点申请人样本 | 是/否/待验证 | 待确认 |

For problem-type searches, add:

| 问题型要素 | 表达 | 字段建议 | 备注 | 用户确认状态 |
| --- | --- | --- | --- | --- |
| 技术问题/效果 |  |  |  | 待确认 |
| 解决手段 |  |  |  | 待确认 |
| 关联模块 |  |  |  | 待确认 |
| 应用领域/背景 |  |  |  | 待确认 |
| 申请人 |  |  |  | 待确认 |

### 检索要素确认问题

- 请确认关键词、同义词、英文词、缩写、商品名是否有遗漏或不应纳入项。
- 请确认分类号是否用于精确限制还是下位组召回。
- 请确认是否有已知种子专利、重点申请人或必须覆盖的技术术语。

## 5. 噪音要素表

| 噪音编号 | 噪音类型 | 噪音关键词/分类号/字段 | 产生原因 | 去噪方式 | 是否直接加入最终式 | 用户确认状态 |
| --- | --- | --- | --- | --- | --- | --- |
| N1 |  |  |  |  | 待验证/是/否 | 待确认 |

### 结果反馈噪音记录

Use this table when the user provides noisy hit samples. Do not only list applicants; identify the technical, keyword, field, bracket, or classification reason for the noise.

| 反馈批次 | 噪音样本特征 | 代表申请人/分类号 | 误命中原因 | 修订方式 | 是否固化为通用规则 |
| --- | --- | --- | --- | --- | --- |
|  |  |  | stable industry noise / bracket issue / broad synonym / field too broad | add noise block / tighten positive blocks / fix parentheses | 是/否/本主题专用 |

### 噪音要素确认问题

- 请确认这些噪音是否可以排除。
- 请确认是否存在“看似噪音但业务上必须保留”的边界样本。

## 6. 分类号范围说明

| 分类号 | 分类号含义 | 使用目的 | 字段 | 范围说明 | 用户确认状态 |
| --- | --- | --- | --- | --- | --- |
|  |  | 召回/精确限制/去噪 | `IPC` / `IPC_LOW` / `CPC` / `CPC_LOW` | exact code only / include lower subgroups | 待确认 |

Rule: use `IPC_LOW`/`CPC_LOW` when the intent is to retrieve all lower subgroups under a parent group, such as `IPC_LOW:C22B3/00`.

## 7. 位置符策略

Document where proximity operators are used instead of flat Boolean logic.

| 关系类型 | 仅用 AND/OR 的风险 | 位置符表达 | 初始窗口 | 调整依据 | 用户确认状态 |
| --- | --- | --- | --- | --- | --- |
| 对象 + 动作 |  |  | `$W5-$W9` |  | 待确认 |
| 元素/材料体系 |  |  | `$W3-$W5` |  | 待确认 |
| 方法 + 设备 |  |  | `$W5` or `$SEN` |  | 待确认 |
| 功效 + 应用 |  |  | `$W5` or `$SEN` |  | 待确认 |

## 8. 检索策略表

| 策略编号 | 策略名称 | 检索逻辑 | 对应要素 | 字段选择 | 预期作用 | 风险/噪音 | 是否进入总式 | 用户确认状态 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S0 | 种子窄式 |  |  |  | 收集高相关样本 |  | 否/是 | 待确认 |
| S1 | 核心主式 |  |  |  |  |  | 是 | 待确认 |
| S2 | 召回扩展式 |  |  |  |  |  | 是 | 待确认 |
| S3 | 分类号辅助式 |  |  |  |  |  | 是 | 待确认 |
| S_LANGUAGE_RECALL | 小语种/机翻补漏式 |  |  | `TACD` with strict positive constraints | 补充非英语或机翻表达漏检 | 噪音较高，需单独抽样 | 视样本验证 | 待确认 |
| N1 | 噪音式 |  |  |  | 去噪 |  | 视验证 | 待确认 |
| N_STABLE_INDUSTRY_NOISE | 稳定行业噪音式 |  | classification + keyword | 去除稳定跨领域噪音 | 过度排除相邻应用 | 视样本验证 | 待确认 |

### 检索策略确认问题

- 请确认各策略是否符合检索目标。
- 请确认哪些策略进入总式，哪些仅用于验证或补充。
- 请确认是否先执行平衡召回式，再根据样本加入噪音式。
- 若存在噪音/漏检反馈，请确认新增策略是通用规则、本主题专用规则，还是边界争议样本。

## 9. 检索策略对应的逐条检索式

### S0 种子窄式

用途:

```text
S0 =
```

### S1 核心主式

用途:

```text
S1 =
```

### S2 召回扩展式

用途:

```text
S2 =
```

### S3 分类号辅助式

用途:

```text
S3 =
```

Add or remove strategy sections as needed. Every strategy listed in the strategy table must have a corresponding formula.

### S_LANGUAGE_RECALL 小语种/机翻补漏式

用途: missed relevant samples show systematic non-English or machine-translation variants. Keep this branch tightly constrained; do not use broad translation terms alone.

```text
S_LANGUAGE_RECALL =
```

## 10. 噪音检索式

### 噪音总式

```text
NOISE_TOTAL =
```

### N1

去噪对象:

```text
N1 =
```

### N2

去噪对象:

```text
N2 =
```

Add every noise formula used or proposed. If a noise formula is not added to the final formula, explain why.

### N_STABLE_INDUSTRY_NOISE

去噪对象: stable cross-domain noise confirmed by hit review, preferably using both classification and keyword/context terms.

```text
N_STABLE_INDUSTRY_NOISE =
```

### 噪音完整展开式（必须提供）

Provide an expanded noise expression without unresolved `N1/N2` placeholders. This is required even when the shorthand noise formula is also shown, because the user may need to paste it directly into Patsnap Expert Search.

```text
NOISE_TOTAL_EXPANDED =
```

## 11. 总检索式

### 智慧芽可直接粘贴执行式（必须优先展示）

The complete report must provide direct-execution expanded formulas. Do not provide only `S1 OR S2 OR S3` shorthand. Put these expanded formulas before downstream execution notes so they are easy to find.

```text
FINAL_BALANCED_EXPANDED =
(
  [S1 full formula body]
)
OR
(
  [S2 full formula body]
)
```

```text
NOISE_TOTAL_EXPANDED =
(
  [N1 full formula body]
)
OR
(
  [N2 full formula body]
)
```

```text
FINAL_PRECISION_EXPANDED =
(
  [FINAL_BALANCED expanded full formula body]
)
NOT
(
  [NOISE_TOTAL expanded full formula body]
)
```

### 平衡召回式（简写版，用于解释）

```text
FINAL_BALANCED =
```

确认状态: 待用户确认

### 平衡召回完整展开式（必须提供）

Provide a fully expanded expression without unresolved `S1/S2/S3` placeholders. If the expression is too long to maintain safely, still provide the complete expanded expression in an appendix or attachment, and additionally recommend saving each strategy formula in Expert Search and combining them.

```text
FINAL_BALANCED_EXPANDED =
```

### 高精度式（简写版，用于解释）

```text
FINAL_PRECISION =
```

确认状态: 待用户确认

### 高精度完整展开式

```text
FINAL_PRECISION_EXPANDED =
(
  [FINAL_BALANCED expanded full formula body]
)
NOT
(
  [NOISE_TOTAL expanded full formula body]
)
```

### 完整展开式检查

Before delivering the report, verify:

- `FINAL_BALANCED_EXPANDED` contains no unresolved `S1/S2/S3` placeholders.
- `NOISE_TOTAL_EXPANDED` contains no unresolved `N1/N2/N3` placeholders.
- `FINAL_PRECISION_EXPANDED` contains the expanded positive block and expanded noise block, not only `(FINAL_BALANCED_EXPANDED) NOT (NOISE_TOTAL_EXPANDED)`.
- The expanded formulas are visibly placed near the total-formula section, not only hidden after notes or appendices.

```text
检查状态:
```

## 12. 检索结果记录

Fill after running in Patsnap. If not executed, mark as `待用户在智慧芽执行`.

| 检索式 | 命中量 | 去重口径 | 执行日期 | 备注 |
| --- | ---: | --- | --- | --- |
| S0 |  |  |  |  |
| S1 |  |  |  |  |
| FINAL_BALANCED |  |  |  |  |

## 13. 查全查准校验方法引导

This search skill only provides the checking method. Do not fill validation results unless the user provides executed result sets, labeled samples, and independent recall samples.

### 查准校验方法

查准可以基于命中结果做。建议流程:

1. 执行 `FINAL_BALANCED` 或各策略式。
2. 按策略来源、年份、申请人、分类号、高频关键词分层抽样。
3. 人工标引: 相关 / 边界相关 / 不相关。
4. 统计噪音来源。
5. 决定是否加入噪音式或收紧字段/位置符窗口。

```text
查准率 = 相关样本数 / 抽样总数
```

建议记录表:

| 抽样范围 | 抽样量 | 相关 | 边界相关 | 不相关 | 查准率 | 主要噪音 | 调整建议 |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- |
|  |  |  |  |  |  |  |  |

### 查全校验方法

查全不能只基于命中结果做，必须构建独立相关样本。建议样本来源:

- 用户提供的种子专利；
- 重点申请人全量专利中人工筛选的相关样本；
- 竞品/产品/标准/论文反查得到的样本；
- 宽式检索或分类号检索中人工筛出的相关样本；
- 已知商品名、材料名、关键工艺路线反查得到的样本。

```text
查全率 = 检索式命中的独立相关样本数 / 独立相关样本总数
```

建议记录表:

| 独立样本来源 | 样本量 | 命中量 | 查全率 | 未命中原因 | 修订建议 |
| --- | ---: | ---: | ---: | --- | --- |
|  |  |  |  |  |  |

### 位置符窗口调整

| 概念块 | 当前位置符/窗口 | 基于结果观察到的问题 | 调整 |
| --- | --- | --- | --- |
|  |  | too noisy / missed known sample / good balance |  |

## 14. 迭代日志

| 版本 | 修改内容 | 命中量变化 | 查全影响 | 查准影响 | 决策 |
| --- | --- | ---: | --- | --- | --- |
| S0 |  |  |  |  |  |

### 噪音/漏检反馈迭代表

| 反馈类型 | 样本来源 | 观察结论 | 是否通用问题 | 本次修订 | 对skill的修订建议 |
| --- | --- | --- | --- | --- | --- |
| 噪音 |  |  | 是/否/待判断 |  |  |
| 漏检 |  |  | 是/否/待判断 |  |  |

## 15. 局限性与待确认项

- 字段/语法待智慧芽确认:
- 分类号待复核:
- 种子样本不足:
- 去噪待抽样验证:
- 时间/地区/法律状态范围:
- 后续建议:

## 16. 用户确认清单

| 确认门 | 确认节点 | 状态 | 用户确认动作 | 用户反馈/修订 | 下一步 |
| --- | --- | --- | --- | --- | --- |
| Gate 1 | 原始需求理解 + 技术边界 | 待用户确认 | 点击确认/回复确认 |  | 进入技术拆解 |
| Gate 2 | 技术拆解表 | 待用户确认 | 点击确认/回复确认 |  | 进入技术要素表 |
| Gate 3 | 技术要素表 + 噪音要素表 | 待用户确认 | 点击确认/回复确认 |  | 进入检索策略表 |
| Gate 4 | 分类号范围 + 位置符策略 + 检索策略表 | 待用户确认 | 点击确认/回复确认 |  | 进入逐条检索式 |
| Gate 5 | 逐条检索式 + 噪音检索式 + 总检索式 | 待用户确认 | 点击确认/回复确认 |  | 进入智慧芽执行 |
| Gate 6 | 查全查准校验方法/是否进入独立校验 | 待用户确认 | 点击确认/回复确认 |  | 后续校验或最终固化 |
