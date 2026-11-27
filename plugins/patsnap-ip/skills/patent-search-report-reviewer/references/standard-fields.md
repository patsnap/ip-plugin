# 标准字段简介

本文只说明报告审核中常用字段的角色和接力关系。调用前必须读取运行时 schema；若字段、类型或可选值与本文不同，以运行时 schema 为准并记录差异。

## 扩词与检索接力

### `expand_patent_search_terms`

| 方向 | 字段 | 用途 |
|---|---|---|
| 输入 | `technical_proposal` | 报告或委托材料中的完整技术方案，不传入仅有标题或孤立关键词。 |
| 输入 | `search_elements` | 可追溯的检索要素数组；优先复用报告已有结构。 |
| 输入 | `search_elements[].element_description` | 开放对象需要无损接力时，承载单个要素的原文；不补造类型、分数或新事实。 |
| 输入 | `input_lang` | 输入方案语言，仅使用运行时允许值。 |
| 输入 | `region` | 扩词语境或区域偏好；不等于检索法域过滤。 |
| 输入 | `task_id` | 可选追踪标识，不影响技术事实。 |
| 输出 | `search_elements[]` | 按元素返回的扩展结果，必须与输入原文对回。 |
| 输出 | `element_description` | 返回元素身份，用于核对接力是否丢失。 |
| 输出 | `chinese_keywords` / `english_keywords` | 该元素的根关键词；不能不经审核直接成为检索词。 |
| 输出 | `chinese_synonyms` / `english_synonyms` | 与根词槽位对应的候选表达；需区分同义、上下位、相关和歧义词。 |
| 输出 | `classifications` | 候选分类线索，不自动等同于 IPC，也不单独证明技术归属。 |

`expanded_keywords`、`expanded_keywords_data` 等展开容器只按当次真实回执解析。扩词完成后，先作专业取舍，再把采用表达重组成保留“主体—关系—对象／条件—限定”的完整短语。

### `search_patent`

| 字段 | 用途 |
|---|---|
| `search_strategy` | 声明语义、关键词、过滤或 Boolean 策略；Boolean 为独占策略。 |
| `semantic_query` | 完整技术意图和关系描述，仅在语义策略中使用。 |
| `keywords` | 审核后、保留技术关系的关键短语数组；这是检索入参，不应改名为扩词工具。 |
| `filters` | 结构化边界，常用 `pn`、`apno`、`assignees`、`assignee_ids`、`jurisdiction`、`date_type`、`date_from`、`date_to`、`legal_status`。 |
| `boolean_query` | 可执行 PatSnap Boolean 查询或构建工具返回的不透明引用；不解码、重建或手改。 |
| `collapse_family` | 同族折叠口径，A/B 复核时必须固定。 |
| `limit` / `offset` / `sort` | 分页和排序口径，A/B 复核时必须一致。 |
| `data.docs` | 本页文献结果。 |
| `data.returned_count` | 本页取回数，不是命中总数。 |
| `data.total_hits` | 可用时的命中总数，不单独证明检索有效性。 |

## Boolean 构式

### `build_patent_boolean_query`

| 方向 | 字段 | 用途 |
|---|---|---|
| 输入 | `text` | 完整自然语言检索意图；不传入已可执行字段式进行校验或改写。 |
| 输出 | `data.reference_query` | 人工审阅的参考表达，用于核对概念分组与逻辑。 |
| 输出 | `data.boolean_query` | 供 `search_patent.boolean_query` 原样接力的可执行查询或不透明引用。 |

## 专利原文与证据

### `fetch_patent`

| 方向 | 字段 | 用途 |
|---|---|---|
| 输入 | `patent_id` | 已核对身份的专利 ID 或公开号。 |
| 输入 | `format` | `json` 用于结构化核验；`markdown` 时只按实际 markdown 输出解析。 |
| 输入 | `language` | 原文或译文偏好；译文不冒充原文。 |
| 输入 | `include` | 只在需要时请求 `relations` 或 `media`；全文不写入该字段。 |
| 输出 | `response.bibliography` | 书目、日期、主体及简单状态。 |
| 输出 | `response.claims` | 权利要求原文，需保留从属关系和必要限定。 |
| 输出 | `response.description` | 说明书原文，不替代权利要求边界。 |
| 输出 | `response.relations` | 按需核对同族、引证和相似关系。 |
| 输出 | `response.media` | 原始 PDF 或附图线索；链接不等于已读正文。 |

`fetch_patent_lifecycle` 用于法律事件和时点性状态；不以简单状态替代完整事件记录。

## 主体与非专利文献

- `get_standard_assignee_name`：公司候选读取 `company.candidates[].company_id` 和 `company.candidates[].ans_ids`；申请人候选读取 `assignee.candidates[].ans_id`。
- `get_corptree_hierarchy`：输入已确认 `company_id`，按需核对 `direct_ans_ids`；不混用公司 ID 与申请人 ANS ID。
- `search_literature` / `fetch_literature`：从 `data.docs[].id` 取文献 ID，作为后者的 `paper_id`。
