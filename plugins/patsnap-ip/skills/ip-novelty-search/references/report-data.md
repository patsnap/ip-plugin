# 报告数据与命令

## 目录

- 保存输入和回执
- 方案与特征
- 报告草稿
- Agent 核查
- 创造性与补充依据
- 生成与验证

## 保存输入和回执

复用已有任务目录，保存原始交底、特征计划、每次实际请求与完整回执、原图和报告草稿。建议每次调用使用 `calls/唯一标识/request.json`、`response.json`；请求保存工具实际业务参数，工具完整名称和来源另记。目录组织可沿用原任务，不要求宿主特有协议。

渲染器接受直接结构化结果、带 `structuredContent` 的 MCP 回执及 JSON-RPC 结果，不修改原文件。纯文本摘要不足以替代完整结果。回执缺失、失败或过大未取全时，明确缺口，不补写成功结果。

媒体链接需实际读取；工具传入图片使用当前 Schema 的 `ref: image:<文件SHA256>`、`mime_type`、`data_base64`、`label` 和可用的 `pdf_page`、`text_locations`。本地报告可用 `host_file` 指向保存的原图；渲染器也支持把回执中 `material.assets` 按 `ref` 关联到 `material.patent_images`，将完整 Base64 图片校验后保存到任务内 `evidence/`。这一步不代表已经看图。

报告引用的文件均在任务目录内，路径相对草稿；原文引句不改写，不把摘要或工具生成的技术概括当作原文。

## 方案与特征

`feature-plan.json` 的最小结构：

```json
{
  "feature_plan_version": 3,
  "disclosure_sha256": "原始disclosure.txt的SHA256",
  "feature_source": {
    "type": "extract_technical_features",
    "response_file": "calls/extract_features_response.json"
  },
  "source_features": ["源关系1", "源关系2"],
  "source_feature_evidence": [
    {"feature": "源关系1", "source_quote": "工具返回的交底原句1", "image_labels": []},
    {"feature": "源关系2", "source_quote": "工具返回的交底原句2", "image_labels": []}
  ],
  "comparison_units": [
    {"feature": "可独立判断的完整关系1A", "source_feature_number": 1, "source_quote": "原句1中支持1A的连续文字", "image_labels": []},
    {"feature": "可独立判断的完整关系1B", "source_feature_number": 1, "source_quote": "原句1中支持1B的连续文字", "image_labels": []},
    {"feature": "不需拆分的完整关系2", "source_feature_number": 2, "source_quote": "工具返回的交底原句2", "image_labels": []}
  ],
  "features": ["可独立判断的完整关系1A", "可独立判断的完整关系1B", "不需拆分的完整关系2"],
  "feature_evidence": [
    {"feature": "可独立判断的完整关系1A", "source_quote": "原句1中支持1A的连续文字", "image_labels": []},
    {"feature": "可独立判断的完整关系1B", "source_quote": "原句1中支持1B的连续文字", "image_labels": []},
    {"feature": "不需拆分的完整关系2", "source_quote": "工具返回的交底原句2", "image_labels": []}
  ],
  "solutions": [
    {"name": "主方案", "kind": "product", "description": "原交底支持的完整组合", "feature_numbers": [1, 2, 3]}
  ],
  "groups": [
    {"title": "源关系1", "source_feature_number": 1, "feature_numbers": [1, 2]},
    {"title": "源关系2", "source_feature_number": 2, "feature_numbers": [3]}
  ],
  "coverage": [
    {"quote": "原始交底完整连续文字", "treatment": "evaluated", "feature_numbers": [1, 2, 3], "reason": "纳入主方案"}
  ]
}
```

`feature_plan_version` 新建任务使用 `3`。调用过提取工具时，`feature_source.type` 必须为 `extract_technical_features` 并指向实际完整回执；`source_features` 和 `source_feature_evidence` 必须与该回执在内容及顺序上完全相同。用户直接提供了已确定清单时，可使用 `{"type":"provided","reason":"来源及适用范围"}`，并把该清单同时保存为 `source_features`。

`comparison_units` 只能在单个源关系内做可判断粒度的拆分，每项用 `source_feature_number` 回指唯一源关系，`source_quote` 必须是该源关系出处中的连续原文。不跨源关系重组，不拆成失去技术关系的部件名或效果词。每条源关系至少对应一个比对单元。

`features` 必须等于按顺序取得的 `comparison_units[].feature`，并与各篇正式比对请求一致。`feature_evidence` 由比对单元的 `feature/source_quote/image_labels` 原样生成。`groups` 每组对应一条源关系，其 `feature_numbers` 必须恰好覆盖该源关系的所有比对单元。`solutions` 和 `coverage` 均引用1基的比对单元编号。

渲染器会核对版本3的源回执、比对单元映射、原文出处及分组完整性。工具回执与源关系不一致、单元跨源关系或请求清单与单元不一致时直接报错。版本1、2仅用于历史报告兼容；续跑并重新生成报告时升级为版本3。

`coverage` 逐段交代交底去向，`treatment` 使用 `evaluated`、`optional` 或 `background`，保留理由；必要关系不能藏到可选项，决定性歧义先解决。完整报告要求覆盖原始交底。保存 UTF-8 原始 `disclosure.txt`，`disclosure_sha256` 必须是该文件实际内容的 SHA256。

## 报告草稿

`report-draft.json`：

```json
{
  "title": "技术方案查新报告",
  "language": "zh-CN",
  "report": {
    "feature_plan_file": "feature-plan.json",
    "primary_solution": "主方案",
    "status": "partial",
    "headline": "主要结论及阶段状态",
    "findings": [{
      "solution": "主方案",
      "novelty": {"status": "pending", "reason": "已有事实、决定性文献及尚待核实的关系"},
      "inventiveness": {"status": "pending", "reason": "实际已查路径和未决点"},
      "recommendation": "与真实风险和缺口对应的下一步"
    }],
    "documents": [{
      "label": "D1",
      "request_file": "calls/对比/request.json",
      "comparison_file": "calls/对比/response.json",
      "metadata_file": "calls/取文/response.json",
      "reason": "本篇纳入理由",
      "reviews": [{"request_file": "checks/本项/request.json", "response_file": "checks/本项/result.json"}]
    }],
    "searches": [{
      "tool": "search_patent",
      "purpose": "本次真实查证目标",
      "request_file": "calls/检索/request.json",
      "response_file": "calls/检索/response.json"
    }],
    "search_summary": "实际检索思路、收敛理由及复用说明",
    "limitations": ["具体缺口及受影响范围"]
  }
}
```

示例文件名表示任务中真实保存的文件；没有核查时省略 `reviews`。按编号对比结果已带身份时可省略 `metadata_file`；按已有材料对比时，用精确匹配公开号的 `fetch_patent` 原始回执补标题、申请日和公开日，读取 `response.bibliography`。正式比较文献缺申请日或公开日时明确标为待核实，不静默省略。正文和图片以本次对比实际使用的材料为准；不要把补取全文冒充已经比较。

批量调用共用整批请求和回执，每篇增加 `document_index`，使用原始 `index`（0 基）；正式表只纳入成功项。失败项由同批原始记录识别并在附录展示，仍有失败时报告为 `partial`；成功恢复同一文献后引用新结果，不重编号原批次。

检索附录直接读取 `search_strategy` 和实际参数、`data.docs`、`total_hits`、`returned_count`。累计条目用实际文献数，按精确公开号去重，保留页大小、偏移和同族折叠口径；未知总数不写零。引用/被引策略根据实际 `B_CITES`、`F_CITES` 表达式识别。

`publication_date` 为含当天的 ISO 公开日上限，仅用户给定时填写。拟申请日或有效优先权日已确定时可另存 `target_filing_date`，供目标法域抵触申请审计；它不能替代公开日过滤。结论状态为 `supported`、`not_supported`、`pending`、`not_assessed`；每个方案恰好一项。整体只有所有应评价内容、交底覆盖和决定性核查均完成时才为 `complete`，否则为 `partial`。

否定新颖性另填 `novelty.whole_disclosure` 为决定性公开号，`arrangement_reason` 解释同一安排。隐含公开必须有有效核查。肯定新颖性须逐篇有有效区别；未核查的决定性“未提及”不够。

正文可通过顶层 `parts` 配置六类：`overview`、`novelty`、`inventiveness`、`recommendations`、`comparison`、`search`。每类用 `content` 或 `content_file`（任务内 `.md`），二选一；省略 `parts` 时使用默认章节。正文不能代替矩阵、改变事实或覆盖结论。

可选展示字段：`recommendation_detail` 按 `risk/direction/value` 分段建议；方案 `feature_labels`、`feature_summaries` 在特征计划顶层提供等长简述。`report.technical_overview` 可写 `title/technical_problem/technical_solution/technical_effect`；缺乏依据的效果不填写。默认模板已经支持这些数据，不需要重写样式。

## Agent 核查

这是 Agent 实际核查后写出的本地记录，不是 MCP 工具响应。请求文件保存与原对比一致的交底、共同特征、文献全文和图片，以及待核查的原始 `comparison`：

```json
{
  "disclosure_text": "原始交底",
  "features": ["同一份全部特征"],
  "publication_number": "精确公开号",
  "patent_text": "与原对比相同的实际全文",
  "patent_images": [],
  "comparison": {"feature": "待核查特征", "judgment": "not_mentioned", "disclosure_type": null, "evidence": [], "reason": "原判断理由"}
}
```

结果文件：

```json
{
  "method": "agent",
  "status": "upheld",
  "checked_scope": "实际重新阅读的章节、段落、图页或复算范围",
  "reason": "实际核查方法、发现与判断依据",
  "original_comparison": {"原始comparison": "此处实际复制完整原对象"},
  "reviewed_comparison": {"当前comparison": "此处填写完整有效对象"}
}
```

上面两个 comparison 占位对象须替换为真实完整对象，不能原样提交。`upheld` 的当前对象与原判断一致；`overturned` 必须有真实改变；`material_insufficient` 不表示核查通过，可以将 `reviewed_comparison` 置空。原文、原图、特征或原判断不匹配时记录为陈旧，不用于结论。脚本验证关联和引句存在，不能证明 Agent 确实完成专业阅读。

核查改变了用于否定新颖性的公开事实/依据时，另用同一对比工具、同一图文材料和该方案全部特征核对整体安排，把实际 `request_file/response_file` 填到 `novelty.arrangement_check`；不能凭逐格改判直接断言整体公开。

## 创造性与补充依据

确定创造性结论时填写该方案 `inventiveness.analysis`：

```json
{
  "closest_publication_number": "已比较且日期合格的公开号",
  "difference_feature_numbers": [2],
  "technical_effect": "真实区别的效果",
  "objective_problem": "不包含目标解法的实际问题",
  "routes": [{
    "title": "具体改造或结合路径",
    "scope": "whole_solution",
    "result": "unresolved",
    "feature_numbers": [2],
    "teaching": "原文起点与启示",
    "motivation": "为何采用",
    "obstacles": "必要配合、障碍和解决情况",
    "reason": "实际判断",
    "evidence_refs": [{"publication_number": "实际公开号", "feature_number": 2, "evidence_number": 1}]
  }],
  "overall_reason": "完整方案中各项改动能否共同成立"
}
```

`scope` 为 `local` 或 `whole_solution`；`result` 为 `established`、`not_established`、`unresolved`。区别与当前事实一致，完整路径覆盖全部区别。证据编号从 1 开始，引用当前有效比较的真实证据。路径未决时不填确定创造性结论。

有实际公知资料时，可填 `report.common_knowledge[]`：`publication_number`、1 基 `feature_number`、当前完整 `comparison`、适用理由 `reason`，以及 `source` 的 `file/title/date/locator/quote`。资料须为任务内可核对原文，日期合格；常规标签不代替公知性证据，不改变原公开事实。

## 生成与验证

依赖 Python 3、`markdown-it-py`、`Pillow`；在独立 Python 环境安装缺失依赖：

```sh
python3 -m pip install markdown-it-py Pillow
python3 scripts/render_report_html.py --input /任务目录/report-draft.json --validate-only
python3 scripts/render_report_html.py --input /任务目录/report-draft.json --output /任务目录/report.html
```

命令在 Skill 根目录执行。可用 `--data-output` 导出校验后的结构化数据，用 `--parts-dir` 导出完整章节及资源清单；用户模板也须保留相同事实和缺口。无需启动任务面板或上报 Skill 版本。

打开成品检查原文与附图、核查来源、方案切换、完整矩阵、检索记录及窄屏/打印；可用 `scripts/preview_report.py --file /任务目录/report.html` 只预览该文件。交付实际文件链接。
