# 候选台账与阶段对账

## 目录

- 目标与边界
- 台账数据
- 阶段对账闸门
- 弱召回与范围漂移
- 校验命令

## 目标与边界

台账保证“搜到了什么”与“为什么继续或排除”可追溯，不用原始排名代替技术判断，也不把未知的评分参考专利当作检索目标。每份保留的 `search_patent` 回执都是台账来源；用户给定的候选或旧报告核心文献也要入账。

台账按精确公开号保留记录，同族只用于技术证据归组，不得把不同法域或公开阶段的身份直接删掉。

## 台账数据

任务目录保存 `candidate-ledger.json`，最小结构如下：

```json
{
  "ledger_version": 2,
  "dedup_fill_policy": "required",
  "route_reflection_policy": "required",
  "scope": {
    "publication_date": "2018-12-03",
    "publication_date_inclusive": false,
    "required_publication_jurisdictions": ["CN"]
  },
  "search_response_files": [
    "calls/Q1-page-0.json", "calls/Q1-page-100.json",
    "calls/Q2-page-0.json", "calls/Q3-page-0.json", "calls/Q4-page-0.json"
  ],
  "queries": [{
    "query_id": "Q1",
    "route": "complete_combination",
    "comparison_unit_numbers": [1, 2, 3],
    "dedup_fill": {
      "query_signature": "sha256-of-request-excluding-offset",
      "target_unique_groups": 100,
      "pages": [
        {"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q1-page-0.json"},
        {"offset": 100, "limit": 100, "returned_count": 100, "response_file": "calls/Q1-page-100.json"}
      ],
      "raw_result_count": 200,
      "unique_identity_count": 132,
      "unique_group_count": 100,
      "status": "target_met"
    }
  }, {
    "query_id": "Q2",
    "route": "relation",
    "comparison_unit_numbers": [2],
    "semantic_query": "刀具护罩沿手柄导槽纵向滑动，伸出时覆盖刀刃、缩回时露出刀刃",
    "keywords": ["刀具护罩纵向导槽滑动", "blade guard sliding in longitudinal guide"],
    "relation_proposition": {
      "subject": "刀具护罩",
      "relation": "沿手柄导槽纵向滑动",
      "object_or_condition": "伸出时覆盖刀刃、缩回时露出刀刃",
      "constraints": ["护罩与刀体可分离"],
      "source": "disclosure",
      "source_refs": ["feature-plan.json#comparison_units/2"]
    },
    "dedup_fill": {
      "query_signature": "sha256-Q2-excluding-offset",
      "target_unique_groups": 20,
      "pages": [{"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q2-page-0.json"}],
      "raw_result_count": 100,
      "unique_identity_count": 78,
      "unique_group_count": 20,
      "status": "target_met"
    }
  }, {
    "query_id": "Q3",
    "route": "synonym",
    "derived_from_query_id": "Q2",
    "comparison_unit_numbers": [2],
    "semantic_query": "可拆卸刀具护罩沿纵向导向结构移动以覆盖或露出刀刃",
    "keywords": [
      "可从刀体分离的刀具护罩沿手柄导槽滑动并覆盖或露出刀刃",
      "removable blade guard sliding in a longitudinal handle guide to cover or expose the blade"
    ],
    "relation_synonym_expansion": {
      "subject_variants": ["刀具护罩", "removable blade guard"],
      "relation_variants": ["沿手柄导槽纵向滑动", "沿手柄导槽滑动", "sliding in a longitudinal handle guide"],
      "object_or_condition_variants": [
        "伸出时覆盖刀刃、缩回时露出刀刃",
        "extended to cover the blade and retracted to expose the blade"
      ],
      "constraint_variant_groups": [{
        "source_constraint": "护罩与刀体可分离",
        "variants": ["护罩与刀体可分离", "可从刀体分离", "removable from the knife body"]
      }],
      "composed_phrases": [{
        "text": "可从刀体分离的刀具护罩沿手柄导槽滑动并覆盖或露出刀刃",
        "language": "zh-CN",
        "subject_variant": "刀具护罩",
        "relation_variant": "沿手柄导槽滑动",
        "object_or_condition_variant": "伸出时覆盖刀刃、缩回时露出刀刃",
        "constraint_variants": ["可从刀体分离"]
      }, {
        "text": "removable blade guard sliding in a longitudinal handle guide to cover or expose the blade",
        "language": "en-US",
        "subject_variant": "removable blade guard",
        "relation_variant": "sliding in a longitudinal handle guide",
        "object_or_condition_variant": "extended to cover the blade and retracted to expose the blade",
        "constraint_variants": ["removable from the knife body"]
      }]
    },
    "dedup_fill": {
      "query_signature": "sha256-Q3-excluding-offset",
      "target_unique_groups": 20,
      "pages": [{"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q3-page-0.json"}],
      "raw_result_count": 100,
      "unique_identity_count": 74,
      "unique_group_count": 20,
      "status": "target_met"
    }
  }, {
    "query_id": "Q4",
    "route": "relation",
    "reconstructed_from_reflection_id": "R1",
    "comparison_unit_numbers": [2],
    "semantic_query": "护罩凸缘嵌入手柄纵向槽并受槽壁约束，在两个止挡位置之间平移",
    "keywords": ["护罩凸缘嵌入纵向槽并在止挡位置之间平移", "guard flange captured in a longitudinal slot and translating between stops"],
    "relation_proposition": {
      "subject": "护罩凸缘",
      "relation": "嵌入手柄纵向槽并在槽内平移",
      "object_or_condition": "由槽壁导向并在两个止挡位置定位",
      "constraints": ["护罩与刀体可分离"],
      "source": "disclosure",
      "source_refs": ["feature-plan.json#comparison_units/2"]
    },
    "dedup_fill": {
      "query_signature": "sha256-Q4-excluding-offset",
      "target_unique_groups": 20,
      "pages": [{"offset": 0, "limit": 100, "returned_count": 100, "response_file": "calls/Q4-page-0.json"}],
      "raw_result_count": 100,
      "unique_identity_count": 82,
      "unique_group_count": 20,
      "status": "target_met"
    }
  }],
  "retrieval_assessment": {
    "strength": "weak",
    "reason": "前列候选与决定性关系仍不对应",
    "family_diversity": {"top_k": 20, "unique_families": 7, "dominant_family_count": 11},
    "object_precision_sample": {"reviewed": 10, "on_object": 5},
    "decisive_comparison_unit_numbers": [2],
    "feedback_query_ids": ["Q2", "Q3"]
  },
  "route_reflections": [{
    "reflection_id": "R1",
    "query_ids": ["Q1", "Q2", "Q3"],
    "sample_size": 20,
    "unique_families_or_provisional_groups": 8,
    "dominant_mechanism_count": 13,
    "decisive_relation_coverage": "partial",
    "effect_term_echo": true,
    "missing_dimensions": ["position", "kinematics"],
    "evidence_basis": "retrieval_sample",
    "evidence_refs": ["calls/Q1-page-0.json", "calls/Q2-page-0.json", "calls/Q3-page-0.json"],
    "decision": "route_reconstruct",
    "decision_reason": "前列由复述效果词的同一核心机理主导，位置和运动关系未形成独立路线",
    "followup_query_ids": ["Q4"]
  }],
  "candidates": [{
    "publication_number": "CN1234567A",
    "aliases": ["CN1234567"],
    "family_id": "optional-family-id",
    "publication_date": "2018-11-16",
    "jurisdiction": "CN",
    "discoveries": [{"query_id": "Q1", "rank": 2, "channels": ["semantic"]}],
    "eligibility": {"jurisdiction": "eligible", "date": "eligible"},
    "priority": "high",
    "stage": "compared",
    "decision": "advance",
    "reason": "整体结构与主组合接近",
    "evidence_refs": ["calls/fetch-CN1234567A/response.json"]
  }],
  "jurisdiction_reconciliation": {
    "CN": {"status": "represented", "reason": "范围内高优先级候选已比较", "evidence_refs": ["calls/compare/response.json"]}
  },
  "unexplained_drop_count": 0
}
```

新任务使用 `ledger_version: 2`；版本 1 只兼容续跑的历史台账。`route` 使用 `complete_combination`、`relation`、`synonym`、`classification`、`citation` 或 `user_candidate`。`stage` 使用 `searched`、`shortlisted`、`fetched`、`compared`、`final`、`excluded`。`priority` 使用 `high`、`normal`、`background`。

新任务设置 `dedup_fill_policy: "required"`。除 `user_candidate` 外，每条查询记录 `dedup_fill`：目标有效组数、去除 `offset` 后固定查询的签名、连续分页及回执、原始结果数、精确身份数、有效技术组数和停止状态。停止状态使用 `target_met`、`results_exhausted`、`tool_limit`、`budget_limit` 或 `tool_error`；后两者必须写 `limitation`。完全同题只是临时阅读簇，所有被折叠公开号仍须出现在 `candidates` 和原始回执对账中。

新任务同时设置 `route_reflection_policy: "required"`，并在补足后保存至少一张 `route_reflections` 卡。`evidence_basis` 只允许 `disclosure`、`user_clarification`、`candidate_feedback` 或 `retrieval_sample`；不得使用评分参考或隐藏GT。`route_reconstruct`／`term_rewrite` 必须列出后续查询，且后续查询以 `reconstructed_from_reflection_id` 回指反思卡。单一机理达到样本60%且决定性关系未覆盖，或出现效果词回声且关系未覆盖时，只能重构路线或请求补充；仅有同族占位且关系已覆盖时可选择 `family_expand`。

版本 2 的 `relation` 查询必须保存实际 `semantic_query`、非空 `keywords` 和完整 `relation_proposition`。关系来源只允许 `disclosure`、`user_clarification`、`candidate_feedback`；候选反馈还必须记录 `source_publication_number`。评分参考或隐藏 GT 不能作为正式关系来源。弱召回必须列出 `decisive_comparison_unit_numbers`，每个决定性单元至少由一条关系查询覆盖。

版本 2 的 `synonym` 查询必须通过 `derived_from_query_id` 引用一条关系查询，继承相同比对单元，并保存 `relation_synonym_expansion`。每个最终短语都要回指已声明的主体、关系、对象／条件和限定变体；实际 `keywords` 必须与 `composed_phrases[].text` 内容及顺序完全一致。这样同义扩展只改变表达，不拆散或改造原技术关系。

同一条 `search_patent` 结果中的 `pn` 数组是一组等价标识，不是多篇候选。选一个规范 `publication_number`，其余写入 `aliases`；不同候选不得共享别名。逗号、空格、连字符和斜杠只在身份核对时归一化，例如 `US3,457,643` 与 `US3457643` 视为同一标识，报告展示仍保留正确格式。

排除项必须使用 `decision: "exclude"`，写出可复核的 `reason` 和实际 `evidence_refs`。“未选中”、“相关性低”、“排名靠后”不是充分理由；应说明对象、关系、目的、日期、范围或同族证据中哪一项不符合。

## 阶段对账闸门

在三个转换点执行对账：

1. **取文前**：核对每轮前列、范围内、用户给定及与主组合明显接近的候选。高优先级项必须取文，或基于已有摘要／书目／范围证据明确排除。
2. **正式比较前**：所有已取文的高优先级项必须进入比较，或根据正文记录排除理由。
3. **报告前**：每个候选必须有终态 `final` 或 `excluded`；用户给定、高优先级及范围内前列候选的排除必须带证据。最终文献清单从已对账台账生成，不从已取文文件手工回忆。

同族归并时，当作证据主文本的成员可进入 `final`；其他成员仍保留 `excluded`记录，理由写明同族关系、主文本公开号和日期／法域身份是否仍被保留。

## 弱召回与范围漂移

出现以下任一情形，将 `retrieval_assessment.strength` 设为 `weak` 并补检：

- 前列候选只命中孤立部件，未覆盖决定性关系；
- 某个必要比对单元未被任何查询以完整关系表达；
- 结果高度集中在一个术语、一个分类或一条机理路线；
- 最强候选的决定性关系均为 `not_mentioned`，或与交底的整体改造起点明显不同。
- 前列样本中，最大同族占比超过 50%，说明 Top 页被同族版本挤占；
- 前列至少 10 件的人工快审中，保留目标技术对象链的文献少于 60%，说明关系词已跨领域漂移。

弱召回补检至少包含：一个保留主体—动作／配合—对象／条件的 `relation` 查询，以及一个独立的 `synonym`、`classification` 或 `citation` 路线。分类号只作召回分支，不静默变成全局硬过滤。

用户明确限定公开地域时，范围内候选不得在后续阶段整体消失，却只留范围外文献。如果全部排除，`jurisdiction_reconciliation` 必须逐项引用排除证据，并在报告限制中说明范围内未留下正式比较文献。目标审查法域不等于公开地域硬限定；只有用户确实设定该范围时才触发本闸门。

设置了 `scope.publication_date` 时，必须同时明确 `publication_date_inclusive`：用户说“之前”通常为 `false`，说“截至／不晚于”通常为 `true`。版本 2 的每个候选写入实际 `publication_date`；校验器据此计算 `eligibility.date`，不采信自报结果。后公开或日期未核实文献可作线索或辅助读文，不得进入日期合格的最终现有技术清单。

明确限定公开地域时，版本 2 的每个候选写入实际 `jurisdiction`。校验器据此计算 `eligibility.jurisdiction`，并只用实际法域核对 `represented`，不再从公开号前缀猜测法域。

## 校验命令

```sh
python3 scripts/validate_candidate_ledger.py --ledger /任务目录/candidate-ledger.json --root /任务目录 --phase final
```

`--phase fetch`、`compare`、`final` 分别用于三个闸门。校验器核对查询引用、阶段、高优先级候选的处置、弱召回补检、明确公开地域的对账，并从检索结果别名组和候选终态重新计算无解释丢弃计数。排除证据文件必须实际出现该候选公开号或别名；这只能确认身份关联，不能自动判断技术相关性或人工排除理由是否专业正确。
