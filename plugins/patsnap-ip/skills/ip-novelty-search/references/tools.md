# 工具含义与输入输出范式

## 目录

- 通用规则
- `extract_technical_features`
- `search_patent`
- `fetch_patent`
- `assess_feature_disclosure`

## 通用规则

以下是本 Skill 使用的明确契约；工具当前 Schema 更新时以实际 Schema 为准，并同步修订本文件。专利检索、正文、附图和 PDF 使用工具返回的材料；本地脚本只整理记录和生成报告。

缺少所需工具时说明阻塞步骤，不猜造旧工具名、不切换其他专利服务。工具失败不是零命中，材料缺失不是未公开。

## `extract_technical_features`

含义：只从交底中提取后续检索和比较共用的技术方案、完整技术关系及出处；不检索专利，不判断新颖性或创造性。

输入：

```json
{
  "disclosure_text": "用户原始技术交底全文",
  "language": "zh-CN",
  "disclosure_images": [{
    "label": "图1",
    "mime_type": "image/png",
    "data_base64": "完整图片字节的Base64",
    "ref": "图片引用标识",
    "pdf_page": 1,
    "text_locations": ["说明书第3页"]
  }]
}
```

`disclosure_images` 可省略。输出读取：

```json
{
  "status": "complete",
  "technical_solution": "方案概括",
  "features": ["完整特征关系1"],
  "feature_evidence": [
    {"feature": "完整特征关系1", "source_quote": "交底原句", "image_labels": []}
  ],
  "questions": [],
  "language": "zh-CN",
  "audit": []
}
```

`questions` 有会改变评价对象的未决项时按入口第1步处理；不能用概括替代原始交底，也不能在本地静默改写 `features`。

## `search_patent`

含义：发现候选专利及书目信息。支持语义、关键词、结构化过滤和布尔检索；返回摘要或片段，不返回可替代全文比较的完整正文。

语义＋关键词混合输入：

```json
{
  "search_strategy": ["semantic", "keyword", "filter"],
  "semantic_query": "完整技术意图、关系和问题",
  "keywords": ["中文完整关系短语", "English technical relationship"],
  "filters": {"date_type": "publication", "date_to": 20201231},
  "limit": 20,
  "offset": 0,
  "collapse_family": false,
  "sort": "relevance"
}
```

日期未确定时移除 `filter` 和 `filters`。可用 `filters` 包括 `pn`、`apno`、`assignees`、`assignee_ids`、`inventors`、`ipc`、`jurisdiction`、`legal_status`、`date_type`、`date_from`、`date_to`、`cited_min`；只设置用户已确定或本流程已核实的条件。

布尔输入与其他策略互斥：

```json
{
  "search_strategy": ["boolean"],
  "boolean_query": "B_CITES:(US6394621B1) AND PBD:[* TO 20000101]",
  "limit": 20,
  "offset": 0,
  "collapse_family": false
}
```

输出读取：

```json
{
  "status": "success",
  "data": {
    "total_hits": 100,
    "returned_count": 20,
    "docs": [{
      "id": "patent_id",
      "patent_number": "US...A1",
      "pn": ["US...A1"],
      "title": "标题",
      "text": "摘要或相关片段",
      "publication_date": 20200101,
      "priority_date": [20190101],
      "application_date": 20190101,
      "jurisdiction": "US",
      "legal_status": "pending",
      "ipc": "B23K...",
      "assignees": [],
      "inventors": [],
      "url": "来源页",
      "view_url": "浏览链接"
    }]
  }
}
```

`total_hits`、本页返回、去重候选和正式比较数量分开记录。`status=error` 或工具失败不等于零命中。

## `fetch_patent`

含义：读取一个已知专利的精确公开版本、书目信息、权利要求和说明书；需要时附加同族、引证关系或真实媒体。

输入：

```json
{
  "patent_id": "search_patent返回的id",
  "language": "zh-CN",
  "format": "json",
  "include": ["relations", "media"]
}
```

`include` 可省略；只在需要同族、引证或图证时请求 `relations`、`media`。`format=json` 输出：

```json
{
  "tool": "fetch_patent",
  "input": {},
  "response": {
    "bibliography": {
      "publication_number": "US...A1",
      "publication_date": "2020-01-01",
      "priority_dates": ["2019-01-01"],
      "title": "标题"
    },
    "claims": "权利要求全文",
    "description": "说明书全文",
    "technical_problem": "可选高价值字段",
    "technical_solution": "可选高价值字段",
    "technical_effect": "可选高价值字段",
    "relations": {"simple_family": [], "cited_patents": [], "citing_patents": []},
    "media": {"figures": [], "pdf": []}
  },
  "executed_at": "时间"
}
```

`format=markdown` 时读取 `response.markdown`。媒体链接只有实际取得并阅读后才能作为图证。

## `assess_feature_disclosure`

含义：以同一原始交底和同一特征清单逐篇核对专利公开事实；输出逐特征判断、引文、阅读范围和同一技术安排，不替代最终法律结论。

单篇输入：

```json
{
  "disclosure_text": "原始交底全文",
  "features": ["完整特征关系1", "完整特征关系2"],
  "language": "zh-CN",
  "publication_number": "US...A1",
  "patent_text": "已取得的权利要求与说明书全文"
}
```

没有现成正文时，在 `publication_number` 与 `patent_id` 中选一种让工具取文；有正文或图片时用公开号标注。批量输入用 `patents`，每批 1—10 篇，与顶层单篇文献字段互斥：

```json
{
  "disclosure_text": "原始交底全文",
  "features": ["完整特征关系1"],
  "language": "zh-CN",
  "patents": [
    {"publication_number": "US...A1"},
    {"publication_number": "CN...A", "patent_text": "完整正文"}
  ]
}
```

单篇输出读取：

```json
{
  "status": "complete",
  "comparisons": [{
    "feature": "完整特征关系1",
    "judgment": "disclosed | not_disclosed | not_mentioned | null",
    "disclosure_type": "explicit | implicit | combined | null",
    "evidence": [{"location": "[0020]", "quote": "原文"}],
    "reason": "完整理由"
  }],
  "coverage": {"text_scope": "实际阅读范围", "images_read": [], "limitations": []},
  "arrangement": {
    "basis": "single_embodiment | linked_combination | incompatible_pieces | not_applicable",
    "reason": "同一安排理由"
  },
  "language": "zh-CN",
  "audit": []
}
```

批量输出读取 `status`、`total`、`succeeded`、`failed` 和按输入顺序保存的 `results[]`；每项包含原始 `index`、公开号、`status`，成功项在 `result`，失败项在 `error`。只重试 `retryable=true` 或材料可补足的失败项，不能丢弃成功项后整批重跑。
