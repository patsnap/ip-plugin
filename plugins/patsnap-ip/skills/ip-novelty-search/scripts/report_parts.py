"""Fixed presentation parts and host-side consistency checks. No network or model calls."""

import hashlib
import html
import json
import re
from datetime import date
from pathlib import Path
from string import Template


def comparison_records(request, response=None):
    """Normalize one saved CC call into its independent document records."""
    patents = request.get("patents")
    if patents is None:
        return [(None, request, response)]
    if not isinstance(patents, list) or not 1 <= len(patents) <= 10:
        raise ValueError("Batch CC requires 1–10 patent inputs")
    results = response.get("results") if response is not None else None
    if response is not None and (not isinstance(results, list) or len(results) != len(patents)):
        raise ValueError("Batch CC receipt does not match its patent inputs")
    common = {k: v for k, v in request.items() if k != "patents"}
    records = []
    for index, patent in enumerate(patents):
        value = None
        if results is not None:
            item = results[index]
            if item.get("index") != index:
                raise ValueError("Batch CC results must retain their input indices")
            if item.get("status") == "failed":
                value = {"isError": True, "content": [{
                    "type": "text", "text": (item.get("error") or {}).get("message", "CC failed"),
                }]}
            else:
                value = item.get("result")
                if not isinstance(value, dict) or value.get("status") not in {"complete", "partial"}:
                    raise ValueError("Batch CC document is missing its comparison result")
        records.append((index, {**common, **patent}, value))
    return records

PARTS = (
    "overview",
    "novelty",
    "inventiveness",
    "recommendations",
    "comparison",
    "search",
)
HEADINGS = {
    "overview": (
        "技术方案概述",
        "Technical solution overview",
        "技術方案概述",
        "技術案の概要",
        "기술안 개요",
    ),
    "comparison": (
        "技术关系对照表",
        "Feature comparisons and evidence",
        "技術特徵對比與原文依據",
        "特徴対比と原文の根拠",
        "기술 특징 비교 및 원문 근거",
    ),
    "novelty": (
        "新颖性评估",
        "Novelty by solution",
        "逐方案新穎性分析",
        "技術案ごとの新規性",
        "기술안별 신규성",
    ),
    "inventiveness": (
        "创造性评估",
        "Inventiveness by solution",
        "逐方案創造性分析",
        "技術案ごとの進歩性",
        "기술안별 진보성",
    ),
    "recommendations": (
        "改进建议",
        "Filing and development recommendations",
        "申請與改進建議",
        "出願と改善の提案",
        "출원 및 개선 제안",
    ),
    "search": (
        "检索策略、文献与评价边界",
        "Search, documents and limits",
        "檢索策略、文獻與評價邊界",
        "検索・文献・評価範囲",
        "검색·문헌·평가 범위",
    ),
}
WORDS = {
    "solution_overview": ("方案与结论总览", "Solutions and findings", "方案與結論總覽", "技術案と結論の概要", "기술안 및 결론 개요"),
    "technical_problem": ("要解决的技术问题", "Technical problem", "要解決的技術問題", "解決すべき技術課題", "해결할 기술적 과제"),
    "technical_solution": ("采用的技术方案", "Technical solution", "採用的技術方案", "採用する技術案", "채택한 기술안"),
    "solution_effect": ("技术效果", "Technical effect", "技術效果", "技術的効果", "기술적 효과"),
    "no_separate": ("未单独评价", "Not separately assessed", "未單獨評價", "個別評価なし", "별도 평가 없음"),
    "route_covered": ("已有成立路径覆盖", "Covered by an established path", "已有成立路徑涵蓋", "成立した経路で対応済み", "성립한 경로로 충족"),
    "route_open": ("尚无成立路径", "No established path", "尚無成立路徑", "成立した経路なし", "성립한 경로 없음"),
    "verified_difference": ("有已核实区别", "Verified difference", "有已核實區別", "確認済みの相違点あり", "확인된 차이점 있음"),
    "material_gap": ("材料或比较未完成", "Material or comparison incomplete", "材料或比較未完成", "資料または対比が未完了", "자료 또는 비교 미완료"),
    "difference_pending": ("区别待核实", "Difference pending verification", "區別待核實", "相違点は要確認", "차이점 확인 필요"),
    "whole_pending": ("整体公开待核实", "Whole-solution disclosure pending", "整體公開待核實", "全体の開示は要確認", "전체 공개 확인 필요"),
    "whole_disclosure": ("同一安排完整公开", "Fully disclosed in one arrangement", "同一安排完整公開", "同一構成で全体が開示", "동일 구성에서 전체 공개"),
    "date_unknown": ("公开日待核实", "Publication date unverified", "公開日待核實", "公開日は未確認", "공개일 미확인"),
    "application_date": ("申请日", "Filing date", "申請日", "出願日", "출원일"),
    "publication_date_label": ("公开日", "Publication date", "公開日", "公開日", "공개일"),
    "search_purpose": ("检索目的", "Search purpose", "檢索目的", "検索目的", "검색 목적"),
    "current": (
        "对照表关注方案",
        "Comparison focus",
        "對照表關注方案",
        "比較表の注目案",
        "비교표 대상 방안",
    ),
    "required": (
        "采用的特征",
        "Included features",
        "採用的特徵",
        "採用する特徴",
        "적용 특징",
    ),
    "scope_note": (
        "选择方案后，只突出该方案采用的特征；其他特征仍保留作参照。",
        "Select a solution to highlight its features; other features remain for reference.",
        "選擇方案後，只突出該方案採用的特徵；其他特徵仍保留作參照。",
        "技術案を選ぶと対象の特徴を強調し、その他も参照用に残します。",
        "기술안을 선택하면 해당 특징을 강조하고 나머지는 참고용으로 유지합니다.",
    ),
    "closest": (
        "最接近文献",
        "Closest prior document",
        "最接近文獻",
        "最も近い文献",
        "가장 가까운 문헌",
    ),
    "differences": (
        "实际区别",
        "Actual differences",
        "實際區別",
        "実際の相違点",
        "실제 차이",
    ),
    "technical_effect": (
        "区别的技术效果",
        "Technical effects of differences",
        "區別的技術效果",
        "相違点の技術的効果",
        "차이의 기술적 효과",
    ),
    "objective_problem": (
        "实际技术问题",
        "Objective technical problem",
        "實際技術問題",
        "客観的な技術課題",
        "객관적 기술 과제",
    ),
    "teaching": (
        "原文起点与技术启示",
        "Starting evidence and teaching",
        "原文起點與技術啟示",
        "原文の出発点と示唆",
        "원문 출발점 및 기술적 시사점",
    ),
    "motivation": (
        "采用这条路径的动机",
        "Motivation",
        "採用這條路徑的動機",
        "採用する動機",
        "채택 동기",
    ),
    "obstacles": (
        "配合条件与障碍",
        "Compatibility and obstacles",
        "配合條件與障礙",
        "適合条件と障害",
        "적합 조건 및 장애",
    ),
    "reason": ("判断理由", "Reasoning", "判斷理由", "判断理由", "판단 이유"),
    "overall_reason": (
        "完整方案的综合判断",
        "Whole-solution finding",
        "完整方案的綜合判斷",
        "方案全体の判断",
        "전체 기술안 종합 판단",
    ),
    "established": (
        "路径成立",
        "Path established",
        "路徑成立",
        "経路が成立",
        "경로 성립",
    ),
    "not_established": (
        "路径未成立",
        "Path not established",
        "路徑未成立",
        "経路が未成立",
        "경로 미성립",
    ),
    "unresolved": (
        "路径待核实",
        "Path unresolved",
        "路徑待核實",
        "経路は要確認",
        "경로 확인 필요",
    ),
    "partial": (
        "当前为阶段结果",
        "Current partial result",
        "目前為階段結果",
        "現在は途中結果",
        "현재는 부분 결과",
    ),
    "whole_solution": (
        "完整方案路径",
        "Whole-solution path",
        "完整方案路徑",
        "方案全体の経路",
        "전체 기술안 경로",
    ),
    "local": (
        "局部区别路径",
        "Local-difference path",
        "局部區別路徑",
        "局所的相違点の経路",
        "국소 차이 경로",
    ),
    "novelty_why": (
        "为何得到这一结论",
        "Why this conclusion",
        "為何得到這一結論",
        "この結論に至った理由",
        "이 결론에 이른 이유",
    ),
    "novelty_rule": (
        "按完整方案逐篇判断：一篇在先文献在同一安排中公开全部必要条件，才足以否定新颖性。惯用手段直接置换须另有具体依据，不能把所有结构差异都当作新颖性区别。“未提及”限于已核对材料，不表示实际不存在。新颖性成立不直接推出创造性成立。",
        "Judged per document against the whole solution: only a prior document that discloses every required relationship in one arrangement defeats novelty. Routine substitution needs its own basis, and not every structural difference is a novelty difference. “Not mentioned” is limited to the material inspected and does not mean the feature does not exist. Novelty does not by itself establish inventive step.",
        "按完整方案逐篇判斷：一篇在先文獻在同一安排中公開全部必要條件，才足以否定新穎性。慣用手段直接置換須另有具體依據，不能把所有結構差異都當作新穎性區別。「未提及」限於已核對材料，不表示實際不存在。新穎性成立不直接推出創造性成立。",
        "技術案全体について文献ごとに判断します。必要な関係をすべて同一構成で開示する先行文献がある場合に限り新規性が否定されます。慣用手段への置換には個別の根拠が必要で、構造上の差異がすべて新規性の相違点になるわけではありません。「記載なし」は確認した資料の範囲に限られます。新規性があっても進歩性が直ちに認められるわけではありません。",
        "기술안 전체를 문헌별로 판단합니다. 필수 관계를 모두 같은 구성에서 공개한 선행문헌이 있어야 신규성이 부정됩니다. 관용 수단의 직접 치환에는 별도 근거가 필요하며, 모든 구조 차이가 신규성 차이는 아닙니다. ‘언급 없음’은 검토한 자료 범위에 한정됩니다. 신규성이 있어도 진보성이 곧바로 인정되지는 않습니다.",
    ),
    "doc_not_defeating": (
        "未见完整公开，不能据此否定新颖性",
        "No complete disclosure; does not defeat novelty",
        "未見完整公開，不能據此否定新穎性",
        "完全な開示は確認されず、新規性は否定されない",
        "완전한 공개가 확인되지 않아 신규성을 부정하지 않음",
    ),
    "doc_defeating": (
        "同一安排完整公开，足以否定新颖性",
        "Fully disclosed in one arrangement; defeats novelty",
        "同一安排完整公開，足以否定新穎性",
        "同一構成で全体が開示され、新規性を否定",
        "같은 구성에서 완전히 공개되어 신규성을 부정함",
    ),
    "doc_pending": (
        "尚待核实，暂不能判断",
        "Pending verification; cannot yet be judged",
        "尚待核實，暫不能判斷",
        "確認待ちのため判断不可",
        "확인 대기 중이라 아직 판단할 수 없음",
    ),
    "doc_outside": (
        "公开日不在查新范围内，不作为在先技术",
        "Outside the publication boundary; not prior art",
        "公開日不在查新範圍內，不作為在先技術",
        "公開日が範囲外のため先行技術としない",
        "공개일이 범위 밖이라 선행기술로 보지 않음",
    ),
    "doc_facts": (
        "已公开的相关内容",
        "Related content already disclosed",
        "已公開的相關內容",
        "開示済みの関連内容",
        "이미 공개된 관련 내용",
    ),
    "doc_required": ("本方案要求", "Required here", "本方案要求", "本案の要件", "본 안의 요건"),
    "doc_fact": ("文献事实", "Document fact", "文獻事實", "文献の事実", "문헌 사실"),
    "doc_more": (
        "查看事实、差异与原文依据",
        "View facts, differences and source evidence",
        "查看事實、差異與原文依據",
        "事実・相違点・原文根拠を見る",
        "사실, 차이 및 원문 근거 보기",
    ),
    "doc_other": (
        "其余未对应核对点",
        "Other unmatched features",
        "其餘未對應核對點",
        "その他の未対応の特徴",
        "그 밖의 미대응 특징",
    ),
    "doc_gap_note": (
        "材料或比较未完成，不能写成“未提及”或“明确不同”。",
        "Material or comparison is incomplete; this cannot be recorded as “not mentioned” or “different”.",
        "材料或比較未完成，不能寫成「未提及」或「明確不同」。",
        "資料または対比が未完了のため、「記載なし」「相違」とは記録できません。",
        "자료 또는 비교가 미완료이므로 ‘언급 없음’ 또는 ‘차이’로 기록할 수 없음",
    ),
    "primary_solution": ("主评方案", "Primary solution", "主評方案", "主評価案", "주 평가안"),
    "variant_solution": ("其他评价方案", "Other solution", "其他評價方案", "その他の評価案", "기타 평가안"),
    "comprehensive": (
        "综合判断",
        "Overall judgment",
        "綜合判斷",
        "総合判断",
        "종합 판단",
    ),
    "closest_art": (
        "最接近的现有技术",
        "Closest prior art",
        "最接近的現有技術",
        "最も近い先行技術",
        "가장 가까운 선행기술",
    ),
    "difference_points": (
        "区别所属技术特征",
        "Features in which the difference lies",
        "區別所屬技術特徵",
        "相違点に係る技術特徴",
        "차이가 있는 기술 특징",
    ),
    "difference_effect": (
        "区别产生的技术效果",
        "Technical effect of the difference",
        "區別產生的技術效果",
        "相違点による技術的効果",
        "차이로 인한 기술적 효과",
    ),
    "actual_problem": (
        "实际解决的技术问题",
        "Technical problem actually solved",
        "實際解決的技術問題",
        "実際に解決する技術課題",
        "실제로 해결하는 기술 과제",
    ),
    "routes_heading": (
        "组合路径与技术启示",
        "Combination paths and technical teaching",
        "組合路徑與技術啟示",
        "組合せ経路と技術的示唆",
        "조합 경로와 기술적 시사점",
    ),
    "risk_basis": (
        "风险提示口径 · 常规设计分析与文献事实分别记录；综合判断以完整方案为对象。",
        "Risk-oriented view · routine-design analysis and document facts are recorded separately; the overall judgment concerns the whole solution.",
        "風險提示口徑 · 常規設計分析與文獻事實分別記錄；綜合判斷以完整方案為對象。",
        "リスク提示の観点 · 通常の設計変更の分析と文献の事実は別に記録し、総合判断は方案全体を対象とします。",
        "위험 제시 관점 · 통상적 설계 분석과 문헌 사실은 따로 기록하며 종합 판단은 기술안 전체를 대상으로 합니다.",
    ),
    "advice_risk": ("主要风险", "Main risk", "主要風險", "主なリスク", "주요 위험"),
    "advice_direction": ("优化方向", "Direction to improve", "優化方向", "改善の方向", "개선 방향"),
    "advice_value": ("技术价值", "Technical value", "技術價值", "技術的価値", "기술적 가치"),
    "scope_heading": (
        "检索范围与局限", "Search scope and limits", "檢索範圍與局限", "検索範囲と限界", "검색 범위와 한계"
    ),
    "scope_statement": (
        "在先公开边界：{date}。完整表仅覆盖所选评价方案及纳入详细对照的文献，不包含未单独评价的可选组合。",
        "Prior-publication boundary: {date}. The full table covers only the selected solutions and the documents compared in detail, and excludes optional combinations that were not assessed separately.",
        "在先公開邊界：{date}。完整表僅涵蓋所選評價方案及納入詳細對照的文獻，不包含未單獨評價的可選組合。",
        "先行公開の境界：{date}。対比表は選択した評価案と詳細に対比した文献のみを対象とし、個別に評価していない任意の組合せは含みません。",
        "선행 공개 기준: {date}. 전체 표는 선택한 평가안과 상세 비교한 문헌만 포함하며 별도로 평가하지 않은 선택적 조합은 제외합니다.",
    ),
    "unevaluated": (
        "尚未单独评价的内容",
        "Content not assessed separately",
        "尚未單獨評價的內容",
        "個別に評価していない内容",
        "별도로 평가하지 않은 내용",
    ),
    "unevaluated_note": (
        "以下为原交底中的可选细化，本轮没有纳入任何评价方案，也没有被当作必要条件。",
        "These optional refinements in the original disclosure are not part of any assessed solution and were not treated as requirements.",
        "以下為原交底中的可選細化，本輪沒有納入任何評價方案，也沒有被當作必要條件。",
        "以下は原開示の任意の詳細化で、今回はいずれの評価案にも含めず、必須要件としても扱っていません。",
        "아래는 원 개시의 선택적 세부 사항으로, 이번에는 어떤 평가안에도 포함하지 않았고 필수 요건으로도 다루지 않았습니다.",
    ),
    "supplement_heading": (
        "这些区别能否由已有技术补足？",
        "Could existing technology fill these differences?",
        "這些區別能否由現有技術補足？",
        "これらの相違点は既存技術で補えるか",
        "이 차이를 기존 기술로 보완할 수 있는가?",
    ),
    "supplement_note": (
        "上表记录本篇文献的公开事实；下列文献启示与结合分析判断这些区别能否合理补足，只用于创造性评价，不把未提及改写为已公开。",
        "The table records what each document discloses. The analysis below judges whether the differences could reasonably be filled; it informs inventive step only and never turns a missing feature into a disclosed one.",
        "上表記錄本篇文獻的公開事實；下列文獻啟示與結合分析判斷這些區別能否合理補足，只用於創造性評價，不把未提及改寫為已公開。",
        "上表は各文献の開示事実を示します。下の分析は相違点を合理的に補えるかを判断するもので、進歩性の評価にのみ用い、記載なしを開示に書き換えることはありません。",
        "위 표는 각 문헌의 공개 사실을 기록합니다. 아래 분석은 차이를 합리적으로 보완할 수 있는지만 판단하며 진보성 평가에만 쓰고, 언급 없음을 공개로 바꾸지 않습니다.",
    ),
    "arrangement": (
        "整体配合与步骤关系", "Overall arrangement", "整體配合與步驟關係", "全体の構成と手順の関係", "전체 구성과 단계 관계"
    ),
    "arrangement_single_embodiment": (
        "对应内容来自同一实施例",
        "The matched content comes from one embodiment",
        "對應內容來自同一實施例",
        "対応する内容は同一の実施例によるもの",
        "대응 내용이 같은 실시예에서 나옴",
    ),
    "arrangement_linked_combination": (
        "对应内容分处各处，原文有逻辑联系",
        "The matched content sits in different places, linked by the text itself",
        "對應內容分處各處，原文有邏輯聯繫",
        "対応する内容は複数箇所にあるが、原文に論理的な結び付きがある",
        "대응 내용이 여러 곳에 있으나 원문이 논리적으로 연결함",
    ),
    "arrangement_incompatible_pieces": (
        "对应内容须拼接互斥实施例，不属同一方案",
        "The matched content needs mutually exclusive embodiments joined; not one solution",
        "對應內容須拼接互斥實施例，不屬同一方案",
        "対応には排他的な実施例の継ぎ合わせが必要で、同一の案ではない",
        "대응하려면 상충하는 실시예를 이어 붙여야 하며 같은 기술안이 아님",
    ),
    "arrangement_not_applicable": (
        "本方案下没有公开的特征，无需判断",
        "No feature is disclosed here, so no arrangement is judged",
        "本方案下沒有公開的特徵，無需判斷",
        "この案では開示された特徴がなく、判断は不要",
        "이 기술안에서 공개된 특징이 없어 판단하지 않음",
    ),
    "added": ("新增", "Added", "新增", "追加", "추가"),
    "optional_used": (
        "采用的可选实现",
        "Optional implementation used",
        "採用的可選實現",
        "採用した任意の実装",
        "채택한 선택적 구현",
    ),
    "see_full_comparison": (
        "查看本方案完整对照",
        "View the full comparison for this solution",
        "查看本方案完整對照",
        "この案の対比全体を見る",
        "이 기술안의 전체 비교 보기",
    ),
}


def esc(value):
    return html.escape(str(value), quote=True)


def validate_feature_source(plan, load):
    """Keep source relationships immutable and comparison units traceable."""
    version = plan.get("feature_plan_version", 1)
    if version == 1:
        return
    if version not in {2, 3}:
        raise ValueError("Unsupported feature plan version")
    source = plan.get("feature_source")
    if not isinstance(source, dict):
        raise ValueError("Versioned feature plans require feature_source")
    source_type = source.get("type")
    receipt = None
    if source_type == "extract_technical_features":
        response_file = source.get("response_file")
        if not isinstance(response_file, str) or not response_file.strip():
            raise ValueError("Tool-derived features require the extraction response file")
        receipt = load(response_file)
        if receipt.get("status") != "complete" or receipt.get("isError"):
            raise ValueError("Feature source must be a complete extraction receipt")
    elif source_type == "provided":
        reason = source.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ValueError("Provided features require their source and scope")
    else:
        raise ValueError("Unknown feature source type")

    if version == 2:
        if receipt is None:
            return
        if plan.get("features") != receipt.get("features"):
            raise ValueError(
                "Feature plan must preserve extracted features without merging, rewriting, deleting, splitting or reordering"
            )
        if plan.get("feature_evidence") != receipt.get("feature_evidence"):
            raise ValueError(
                "Feature plan must preserve extracted feature evidence without rewriting or reordering"
            )
        return

    source_features = plan.get("source_features")
    source_evidence = plan.get("source_feature_evidence")
    if (
        not isinstance(source_features, list)
        or not source_features
        or len(set(source_features)) != len(source_features)
        or not all(isinstance(value, str) and value.strip() for value in source_features)
    ):
        raise ValueError("Feature plan version 3 requires unique nonempty source_features")
    if receipt is not None and (
        source_features != receipt.get("features")
        or source_evidence != receipt.get("feature_evidence")
    ):
        raise ValueError(
            "Source features and evidence must exactly preserve the extraction receipt"
        )
    if not isinstance(source_evidence, list) or len(source_evidence) != len(source_features):
        raise ValueError("Every source feature requires its source evidence")
    evidence_by_number = {}
    for number, (feature, evidence) in enumerate(zip(source_features, source_evidence), 1):
        if (
            not isinstance(evidence, dict)
            or evidence.get("feature") != feature
            or not isinstance(evidence.get("source_quote"), str)
            or not evidence["source_quote"].strip()
            or not isinstance(evidence.get("image_labels", []), list)
        ):
            raise ValueError("Source feature evidence must retain its feature, quote and image labels")
        evidence_by_number[number] = evidence

    units = plan.get("comparison_units")
    if not isinstance(units, list) or not units:
        raise ValueError("Feature plan version 3 requires comparison_units")
    unit_features, unit_evidence, units_by_source = [], [], {
        number: [] for number in evidence_by_number
    }
    for number, unit in enumerate(units, 1):
        if not isinstance(unit, dict):
            raise ValueError("Each comparison unit must be an object")
        feature = unit.get("feature")
        source_number = unit.get("source_feature_number")
        quote = unit.get("source_quote")
        image_labels = unit.get("image_labels", [])
        if not isinstance(feature, str) or not feature.strip():
            raise ValueError("Each comparison unit requires a complete nonempty feature")
        if type(source_number) is not int or source_number not in evidence_by_number:
            raise ValueError("Each comparison unit must map to exactly one source feature")
        if (
            not isinstance(quote, str)
            or not quote.strip()
            or quote not in evidence_by_number[source_number]["source_quote"]
        ):
            raise ValueError("Comparison unit quote must be continuous text from its source feature evidence")
        if not isinstance(image_labels, list):
            raise ValueError("Comparison unit image_labels must be a list")
        unit_features.append(feature)
        unit_evidence.append({
            "feature": feature,
            "source_quote": quote,
            "image_labels": image_labels,
        })
        units_by_source[source_number].append(number)
    if len(set(unit_features)) != len(unit_features):
        raise ValueError("Comparison unit features must be unique")
    if plan.get("features") != unit_features:
        raise ValueError("Formal comparison features must exactly match comparison_units")
    if plan.get("feature_evidence") != unit_evidence:
        raise ValueError("Comparison feature evidence must exactly match comparison_units")
    if any(not numbers for numbers in units_by_source.values()):
        raise ValueError("Every source feature requires at least one comparison unit")

    groups = plan.get("groups")
    if not isinstance(groups, list) or len(groups) != len(source_features):
        raise ValueError("Version 3 requires one complete group per source feature")
    seen_sources = set()
    for group in groups:
        source_number = group.get("source_feature_number") if isinstance(group, dict) else None
        if (
            type(source_number) is not int
            or source_number not in units_by_source
            or source_number in seen_sources
            or group.get("feature_numbers") != units_by_source[source_number]
        ):
            raise ValueError("Each source group must exactly cover its comparison units")
        seen_sources.add(source_number)


class Parts:
    def part_word(self, key):
        return WORDS[key][self.LANGUAGES.index(self.language)]

    def template(self, template_name, **fields):
        """Only repository-owned templates are loaded; values are pre-escaped or rendered fragments."""
        return Template(
            (self.ASSETS / "report-parts" / f"{template_name}.html").read_text()
        ).substitute(fields)

    def prepare_parts(self):
        self.modular = "report" in self.draft
        self.fragments = {}
        if not self.modular:
            self.plan = None
            return
        report = self.draft["report"]
        self.plan = self.load(report["feature_plan_file"])
        validate_feature_source(self.plan, self.load)
        self.solutions = self.plan["solutions"]
        self.primary = report.get("primary_solution", self.solutions[0]["name"])
        names = [s["name"] for s in self.solutions]
        if not names or len(set(names)) != len(names) or self.primary not in names:
            raise ValueError(
                "Report solution names must be unique and primary must exist"
            )
        self.solution_keys = {
            s["name"]: f"solution-{i}" for i, s in enumerate(self.solutions, 1)
        }
        size = len(self.plan["features"])
        # 短标题只用于总览，不能替代 CC 使用的完整关系。
        labels = self.plan.get("feature_labels")
        if labels is not None and (not isinstance(labels, list) or len(labels) != size
                                   or any(not isinstance(x, str) or not x.strip() for x in labels)):
            raise ValueError("feature_labels must contain one nonempty title per feature")
        for solution in self.solutions:
            nums = solution["feature_numbers"]
            if (
                not nums
                or len(nums) != len(set(nums))
                or any(type(n) is not int or not 1 <= n <= size for n in nums)
            ):
                raise ValueError(
                    "Solution must reference existing feature numbers exactly once"
                )
        self.validate_plan_extensions(names, size)
        self.validate_overview()
        self.findings = {f["solution"]: f for f in report["findings"]}
        if set(self.findings) != set(names) or len(self.findings) != len(
            report["findings"]
        ):
            raise ValueError("Every planned solution requires exactly one finding")
        self.draft["purpose"] = "novelty_report"
        self.part_specs = self.draft.get("parts") or [{"type": kind} for kind in PARTS]
        kinds = [p["type"] for p in self.part_specs]
        if len(kinds) != len(set(kinds)) or (self.presentation and set(kinds) != set(PARTS)):
            raise ValueError("Default report requires all six distinct parts")
        self.narratives = []
        for part in self.part_specs:
            if "content_file" in part and "content" in part:
                raise ValueError("Use content or content_file, not both")
            content = part.get("content", "")
            if "content_file" in part:
                path = self.path(part["content_file"])
                if path.suffix.lower() != ".md":
                    raise ValueError("Report narrative files must use .md")
                content = path.read_text(encoding="utf-8")
            if not isinstance(content, str):
                raise TypeError("Report narrative must be Markdown text")
            self.markdown_tokens(content)
            self.narratives.append({
                "part": part["type"],
                "heading": part.get("heading", HEADINGS.get(part["type"], (part["type"],) * 5)[self.LANGUAGES.index(self.language)]),
                "markdown": content, "source_file": part.get("content_file"),
                "sha256": hashlib.sha256(content.encode()).hexdigest(),
            })
        self.draft["sections"] = [
            {
                "id": p["part"], "heading": p["heading"],
                "content": p["markdown"], "part_type": p["part"],
            }
            for p in self.narratives
        ]
        for section in self.draft["sections"]:
            if section["part_type"] == "comparison":
                section["comparison"] = {
                    "features_file": report["feature_plan_file"],
                    "documents": report["documents"],
                }
        main = next(s for s in self.solutions if s["name"] == self.primary)
        finding = self.findings[self.primary]
        self.draft["cover"] = {
            "solution_name": main["name"],
            "solution_description": main["description"],
            "headline": report["headline"],
            "publication_date": report.get("publication_date"),
            "notice": report.get("notice") or (
                self.part_word("partial") if report.get("status") == "partial" else ""
            ),
            "assessment": {
                field: {**finding[field], "target": field}
                for field in ["novelty", "inventiveness"]
            },
            "recommendation": finding["recommendation"],
        }
        self.coverage_complete = self.validate_coverage_plan()

    def validate_plan_extensions(self, names, size):
        """Optional feature-plan fields that shape the overview. Absent fields keep the plain layout."""

        def numbers(values, what):
            if (
                not isinstance(values, list)
                or len(values) != len(set(values))
                or any(type(n) is not int or not 1 <= n <= size for n in values)
            ):
                raise ValueError(f"{what} must list distinct existing feature numbers")

        for solution in self.solutions:
            parent = solution.get("parent")
            if parent is not None and (parent not in names or parent == solution["name"]):
                raise ValueError("Solution parent must be another planned solution")
            if "optional_feature_numbers" in solution:
                numbers(solution["optional_feature_numbers"], "optional_feature_numbers")
                if not set(solution["optional_feature_numbers"]) <= set(solution["feature_numbers"]):
                    raise ValueError("Optional features must belong to the solution that uses them")
            change = solution.get("change_description")
            if change is not None and (not isinstance(change, str) or not change.strip()):
                raise ValueError("change_description must be nonempty text when present")
        seen = set()
        for group in self.plan.get("groups", []):
            numbers(group.get("feature_numbers"), "Feature group")
            if not isinstance(group.get("title"), str) or not group["title"].strip():
                raise ValueError("Feature group needs a title")
            if seen & set(group["feature_numbers"]):
                raise ValueError("A feature belongs to at most one group")
            seen |= set(group["feature_numbers"])

    def validate_coverage_plan(self):
        raw = self.load_text("disclosure.txt")
        if (
            self.plan.get("disclosure_sha256")
            != hashlib.sha256(raw.encode()).hexdigest()
        ):
            raise ValueError("Feature plan does not match the original disclosure")
        covered = bytearray(len(raw))
        for item in self.plan.get("coverage", []):
            quote = item["quote"]
            start = raw.find(quote)
            if (
                not quote
                or start < 0
                or item["treatment"] not in {"evaluated", "optional", "background"}
            ):
                raise ValueError("Disclosure coverage must cite the original material")
            nums = item.get("feature_numbers", [])
            if any(
                type(n) is not int or not 1 <= n <= len(self.plan["features"])
                for n in nums
            ):
                raise ValueError("Coverage references an unknown feature")
            if item["treatment"] == "evaluated" and not nums:
                raise ValueError("Evaluated disclosure needs a feature reference")
            covered[start : start + len(quote)] = b"\1" * len(quote)
        return all(covered[i] for i, c in enumerate(raw) if not c.isspace())

    def load_text(self, path):
        return self.path(path).read_text()

    def row_scope(self, number):
        if not self.modular:
            return ""
        names = [s["name"] for s in self.solutions if number in s["feature_numbers"]]
        keys = " ".join(self.solution_keys[n] for n in names)
        outside = ' class="report-out-of-scheme"' if self.primary not in names else ""
        return f' data-scheme-ids="{keys}"{outside}'

    def solution_nav(self):
        if not self.modular or len(self.solutions) < 2:
            return ""
        buttons = "".join(
            f'<button type="button" data-report-scheme="{self.solution_keys[s["name"]]}" role="tab" aria-selected="{str(s["name"] == self.primary).lower()}" tabindex="{0 if s["name"] == self.primary else -1}">{esc(s["name"])}</button>'
            for s in self.solutions
        )
        return f'<nav class="report-scheme-bar report-analysis-controls"><strong>{self.part_word("current")}</strong><div class="report-scheme-tabs" role="tablist" aria-label="{self.part_word("current")}">{buttons}</div></nav><p class="report-scope-help">{self.part_word("scope_note")}</p>'

    def eligible_documents(self):
        bound = self.draft["report"].get("publication_date")
        return [
            d
            for d in self.comparisons
            if d["date"]
            and (not bound or date.fromisoformat(d["date"]) <= date.fromisoformat(bound))
        ]

    def difference_numbers(self, document, solution):
        return [
            n
            for n in solution["feature_numbers"]
            if document["effective"]
            .get(self.plan["features"][n - 1], {})
            .get("judgment")
            != "disclosed"
        ]

    def decisive_difference(self, document, number):
        feature = self.plan["features"][number - 1]
        value = document["effective"].get(feature, {})
        if value.get("judgment") == "not_disclosed":
            return True
        review = document["reviews"].get(feature, {})
        return value.get("judgment") == "not_mentioned" and review.get("status") in {
            "upheld",
            "overturned",
        }

    def evidence_refs(self, refs, *, render=True):
        links = []
        for ref in refs:
            document = next(
                (
                    d
                    for d in self.comparisons
                    if d["number"] == ref["publication_number"]
                ),
                None,
            )
            if not document or not 1 <= ref["feature_number"] <= len(
                self.plan["features"]
            ):
                raise ValueError("Analysis references an unknown document or feature")
            value = document["effective"].get(
                self.plan["features"][ref["feature_number"] - 1], {}
            )
            entries = value.get("evidence", [])
            index = ref["evidence_number"] - 1
            if not 0 <= index < len(entries):
                raise ValueError("Analysis evidence reference does not exist")
            self.validate_evidence(document, entries[index])
            if render:
                links.append(self.evidence(document, entries[index]))
        return "".join(links)

    def require_compatible_arrangement(self, arrangement, text):
        basis = (arrangement or {}).get("basis")
        if basis == "incompatible_pieces":
            raise ValueError("incompatible_pieces cannot establish whole disclosure for this solution")
        if basis not in {"single_embodiment", "linked_combination"}:
            raise ValueError("Whole disclosure requires a verified compatible arrangement")
        locators = arrangement.get("locators", [])
        quotes = arrangement.get("link_quotes", [])
        if not locators or any(not locator.strip() for locator in locators):
            raise ValueError("Whole disclosure requires nonempty arrangement locators")
        if basis == "linked_combination" and (
            not quotes or any(not quote.strip() or quote not in text for quote in quotes)
        ):
            raise ValueError("Linked arrangement requires nonempty verbatim patent quotes")

    def check_novelty_arrangement(self, document, solution, finding):
        features = [self.plan["features"][n - 1] for n in solution["feature_numbers"]]
        original = document["result"]
        arrangement = original.get("arrangement")
        check = finding.get("arrangement_check")
        changed = document["arrangement_changes"].intersection(features)
        if check is None:
            if changed:
                raise ValueError("Review changed disclosure evidence; provide an arrangement_check for this solution")
            if "arrangement" not in original:
                return  # Historical receipts predate the structured arrangement field.
            if (arrangement or {}).get("basis") == "incompatible_pieces":
                disclosed = {row["feature"] for row in original["comparisons"] if row["judgment"] == "disclosed"}
                if set(features) < disclosed:
                    raise ValueError("The broader incompatible_pieces result requires an arrangement_check for this solution")
            self.require_compatible_arrangement(arrangement, document["text"])
            return

        request = self.load(check["request_file"])
        response = self.load(check["response_file"])
        material = {"patent_text": document["text"], "patent_images": list(document["images"].values())}
        if (
            request.get("patents") is not None
            or request.get("publication_number") != document["number"]
            or request.get("features") != features
            or request.get("disclosure_text") != document["request"].get("disclosure_text")
            or self.material_key(request) != self.material_key(material)
            or self.material_key({"patent_images": request.get("disclosure_images") or []})
            != self.material_key({"patent_images": document["request"].get("disclosure_images") or []})
        ):
            raise ValueError("Arrangement check must use the same disclosure and patent material with exactly this solution's features")
        rows = response.get("comparisons", [])
        if (
            response.get("status") != "complete"
            or [row["feature"] for row in rows] != features
            or any(row.get("judgment") != "disclosed" or not row.get("evidence") for row in rows)
        ):
            raise ValueError("Arrangement check must establish disclosure for every feature of this solution")
        for row in rows:
            for evidence in row["evidence"]:
                self.validate_evidence(document, evidence)
        arrangement = response.get("arrangement")
        self.require_compatible_arrangement(arrangement, document["text"])
        self.scoped_arrangements[solution["name"]] = arrangement

    def validate_findings(self):
        if not self.modular:
            return
        self.validate_analysis_presentation()
        self.scoped_arrangements = {}
        eligible = self.eligible_documents()
        if self.draft["report"].get("status") == "complete" and self.failed_comparisons:
            raise ValueError("A complete report cannot contain unresolved batch failures")
        if self.draft["report"].get("status") == "complete" and any(
            d["result"].get("status") != "complete" for d in self.comparisons
        ):
            raise ValueError(
                "A complete report requires completed material comparisons"
            )
        if (
            not self.coverage_complete
            and self.draft["report"].get("status") == "complete"
        ):
            raise ValueError("Complete report requires disclosure coverage checks")
        for solution in self.solutions:
            finding = self.findings[solution["name"]]
            for kind in ("novelty", "inventiveness"):
                summary = finding[kind].get("summary")
                if summary is not None and (not isinstance(summary, str) or not summary.strip()):
                    raise ValueError("Finding summary must be nonempty text")
            novelty = finding["novelty"]
            if novelty["status"] == "supported":
                if not eligible or any(
                    not any(
                        self.decisive_difference(d, n)
                        for n in solution["feature_numbers"]
                    )
                    for d in eligible
                ):
                    raise ValueError(
                        "Positive novelty requires a verified difference in every eligible document"
                    )
                if any(not d["date"] for d in self.comparisons):
                    raise ValueError("Novelty requires verified publication dates")
            elif novelty["status"] == "not_supported":
                d = next(
                    (
                        d
                        for d in eligible
                        if d["number"] == novelty.get("whole_disclosure")
                    ),
                    None,
                )
                if (
                    not d
                    or self.difference_numbers(d, solution)
                    or not novelty.get("arrangement_reason", "").strip()
                ):
                    raise ValueError(
                        "Negative novelty needs one eligible whole-solution disclosure and arrangement reasoning"
                    )
                self.check_novelty_arrangement(d, solution, novelty)
                for n in solution["feature_numbers"]:
                    f = self.plan["features"][n - 1]
                    value = d["effective"][f]
                    if value.get("disclosure_type") != "explicit" and d["reviews"].get(
                        f, {}
                    ).get("status") not in {"upheld", "overturned"}:
                        raise ValueError(
                            "Decisive implicit disclosure needs a recorded fact-check"
                        )
            elif novelty["status"] not in {"pending", "not_assessed"}:
                raise ValueError("Unknown novelty finding")
            inv = finding["inventiveness"]
            analysis = inv.get("analysis")
            if inv["status"] in {"supported", "not_supported"}:
                if novelty["status"] != "supported":
                    raise ValueError(
                        "Separate inventive verdict requires established novelty"
                    )
                if not analysis:
                    raise ValueError("Inventive verdict requires a complete analysis")
            if analysis:
                closest = next(
                    (
                        d
                        for d in eligible
                        if d["number"] == analysis["closest_publication_number"]
                    ),
                    None,
                )
                if not closest:
                    raise ValueError(
                        "Closest document must be eligible and actually compared"
                    )
                differences = set(self.difference_numbers(closest, solution))
                if set(analysis["difference_feature_numbers"]) != differences:
                    raise ValueError(
                        "Inventive differences must match current CC facts"
                    )
                for key in ["technical_effect", "objective_problem", "overall_reason"]:
                    if not analysis.get(key, "").strip():
                        raise ValueError("Inventive reasoning is missing: " + key)
                whole = []
                for route in analysis.get("routes", []):
                    if (
                        route["result"]
                        not in {"established", "not_established", "unresolved"}
                        or not set(route["feature_numbers"]) <= differences
                    ):
                        raise ValueError(
                            "Invalid combination route or difference coverage"
                        )
                    for key in ["teaching", "motivation", "obstacles", "reason"]:
                        if not route.get(key, "").strip():
                            raise ValueError("Route reasoning is missing: " + key)
                    if not route.get("evidence_refs"):
                        raise ValueError("Every route requires actual evidence")
                    self.evidence_refs(route["evidence_refs"], render=False)
                    if route["scope"] == "whole_solution":
                        if set(route["feature_numbers"]) != differences:
                            raise ValueError(
                                "Whole-solution path must cover every difference"
                            )
                        whole.append(route["result"])
                if inv["status"] == "not_supported" and "established" not in whole:
                    raise ValueError(
                        "Adverse inventive verdict needs an established whole-solution path"
                    )
                if inv["status"] == "supported" and (
                    "not_established" not in whole
                    or any(r in {"established", "unresolved"} for r in whole)
                ):
                    raise ValueError(
                        "Positive inventive verdict requires resolved whole-solution analysis"
                    )
            if not finding.get("recommendation", "").strip():
                raise ValueError("Every solution needs a recommendation")
            self.validate_recommendation_detail(finding)
            if self.draft["report"].get("status") == "complete" and (
                novelty["status"] not in {"supported", "not_supported"}
                or (
                    novelty["status"] == "supported"
                    and inv["status"] not in {"supported", "not_supported"}
                )
            ):
                raise ValueError(
                    "A complete report cannot contain unresolved solution verdicts"
                )

    def panel(self, kind, solution, finding, details):
        key = self.solution_keys[solution["name"]]
        body = self.finding_badge(kind, finding) + self.markdown(finding["reason"])
        return self.template(
            "assessment",
            anchor=f"{kind}-{key}",
            solution_key=key,
            hidden="" if solution["name"] == self.primary else "hidden",
            name=esc(solution["name"]),
            description=esc(solution["description"]),
            finding=body,
            details=details,
        )

    def validate_common_knowledge(self):
        report = self.draft["report"]
        documents = {doc["number"]: doc for doc in self.comparisons}
        records = {}
        for record in report.get("common_knowledge", []):
            key = record["publication_number"], record["feature_number"]
            doc = documents.get(key[0])
            number = key[1]
            if doc is None or type(number) is not int or not 1 <= number <= len(self.plan["features"]):
                raise ValueError("Common knowledge requires an existing document and feature")
            feature = self.plan["features"][number - 1]
            fact = doc["effective"].get(feature, {})
            if (
                fact.get("judgment") not in {"not_disclosed", "not_mentioned"}
                or self.comparison_key(fact) != self.comparison_key(record["comparison"])
                or doc["reviews"].get(feature, {}).get("status") == "material_insufficient"
            ):
                raise ValueError("Common knowledge must refer to a current factual difference")
            if key in records:
                raise ValueError("Duplicate common knowledge analysis for the same cell")
            source = record["source"]
            if not all(isinstance(source.get(field), str) and source[field].strip()
                       for field in ("file", "title", "date", "locator", "quote")) or not record["reason"].strip():
                raise ValueError("Common knowledge requires a dated source, quotation and reason for applying it")
            source_date = date.fromisoformat(source["date"])
            bound = report.get("publication_date")
            if bound and source_date > date.fromisoformat(bound):
                raise ValueError("Common knowledge source falls outside the publication boundary")
            if source["quote"] not in self.load_text(source["file"]):
                raise ValueError("Common knowledge quotation is absent from the saved source")
            records[key] = record
        self.common_knowledge = records

    def solution_overview(self):
        rows = []
        groups = {n: g for g in self.plan.get("groups", []) for n in g["feature_numbers"]}
        by_name = {s["name"]: s for s in self.solutions}
        for solution in self.solutions:
            name = solution["name"]
            key = self.solution_keys[name]
            findings = self.findings[name]
            parent = by_name.get(solution.get("parent"))
            added = set(solution["feature_numbers"]) - set(parent["feature_numbers"]) if parent else set()
            optional = set(solution.get("optional_feature_numbers", []))

            def point(n):
                title = (self.plan["feature_labels"][n - 1] if self.plan.get("feature_labels") else
                         (groups[n]["title"] + " · " if n in groups else "") + self.plan["features"][n - 1])
                new = f' <span class="report-point-added">{self.part_word("added")}</span>' if n in added else ""
                return f'<a class="report-point" href="#comparison-f{n}">{esc(title)}</a>{new}'

            points = '<ul class="report-scheme-points">' + "".join(
                f'<li>{point(n)}</li>' for n in solution["feature_numbers"] if n not in optional
            ) + '</ul>'
            if optional:
                points += (
                    f'<details class="report-scheme-options"><summary>{self.part_word("optional_used")} · '
                    f'{len(optional)}</summary>'
                    + "".join(f"<p>{point(n)} · {esc(self.plan['features'][n - 1])}</p>" for n in sorted(optional))
                    + "</details>"
                )
            if solution.get("change_description"):
                points += f'<p class="report-scope-change">{esc(solution["change_description"])}</p>'
            role = self.part_word("primary_solution") if name == self.primary else self.part_word("variant_solution")
            verdicts = []
            for kind in ("novelty", "inventiveness"):
                finding = findings[kind]
                # 缺少独立摘要时保留第一句完整文字，不按字符硬截断。
                reason = self.markdown_plain_text(finding.get("summary") or finding["reason"])
                preview = self.cover_text(reason if finding.get("summary") else re.split(r"(?<=[。！？])|(?<=[.!?])\s+", reason, maxsplit=1)[0])
                verdicts.append(
                    f'<td><a class="report-basis-link" href="#{kind}-{key}">{self.finding_badge(kind, finding)}</a>'
                    f'<p class="report-gist">{esc(preview)}</p></td>'
                )
            primary = " data-primary" if name == self.primary else ""
            rows.append(
                f'<tr{primary}><th scope="row">{esc(name)}<small>{role}</small></th><td>{points}</td>{"".join(verdicts)}</tr>'
            )
        return self.template(
            "solutions",
            heading=self.part_word("solution_overview"),
            summary="",
            solution_label=self.t("scheme"),
            features_label=self.t("included_points"),
            novelty_label=self.t("novelty"),
            inventiveness_label=self.t("inventiveness"),
            rows="".join(rows),
        )

    def novelty_basis(self, solution, finding):
        eligible = {d["number"] for d in self.eligible_documents()}
        rows = []
        for doc in self.comparisons:
            differences = self.difference_numbers(doc, solution)
            if doc["number"] not in eligible:
                outcome = self.t("outside_date") if doc["date"] else self.part_word("date_unknown")
            elif any(self.decisive_difference(doc, n) for n in differences):
                outcome = self.part_word("verified_difference")
            elif any(
                doc["effective"].get(self.plan["features"][n - 1], {}).get("judgment") is None
                for n in differences
            ):
                outcome = self.part_word("material_gap")
            elif differences:
                outcome = self.part_word("difference_pending")
            elif finding.get("whole_disclosure") == doc["number"] and finding["status"] == "not_supported":
                outcome = self.part_word("whole_disclosure")
            else:
                outcome = self.part_word("whole_pending")
            points = " · ".join(
                f'<a href="#{doc["anchor"]}-f{n}">F{n} {self.badge(value["judgment"], value.get("disclosure_type"))}</a>'
                for n in differences
                if (value := doc["effective"].get(self.plan["features"][n - 1]))
            )
            rows.append(
                f'<tr><th scope="row"><a href="#{doc["anchor"]}">{esc(doc["label"])} · {esc(doc["number"])}</a></th>'
                f'<td>{outcome}</td><td>{points or "—"}</td></tr>'
            )
        summary = (
            '<div class="report-table-wrap report-novelty-basis"><table><thead><tr>'
            f'<th>{self.t("publication")}</th><th>{self.t("novelty")}</th>'
            f'<th>{self.part_word("differences")}</th></tr></thead><tbody>{"".join(rows)}</tbody></table></div>'
        )
        return summary + self.novelty_cards(solution, finding, eligible)

    def document_outcome(self, document, solution, finding, eligible):
        """Per-document novelty outcome: the tone class, the label key and the features that decide it."""
        differences = self.difference_numbers(document, solution)
        if document["number"] not in eligible:
            return "attention", "doc_outside", differences
        if finding.get("whole_disclosure") == document["number"] and finding["status"] == "not_supported":
            return "attention", "doc_defeating", differences
        if any(
            document["effective"].get(self.plan["features"][n - 1], {}).get("judgment") is None
            for n in differences
        ):
            return "neutral", "doc_pending", differences
        if any(self.decisive_difference(document, n) for n in differences):
            return "positive", "doc_not_defeating", differences
        return "neutral", "doc_pending", differences

    def difference_item(self, document, number):
        feature = self.plan["features"][number - 1]
        value = document["effective"].get(feature)
        if not value:
            return ""
        badge = self.badge(value["judgment"], value.get("disclosure_type"))
        review = self.review_html(document, feature)
        if value["judgment"] is None:
            fact = f'<p>{esc(self.part_word("doc_gap_note"))}</p>'
        else:
            fact = f'<p><b>{self.part_word("doc_fact")}：</b>{esc(self.reason_text(value["reason"]))}</p>'
        return (
            '<li class="report-decisive-difference">'
            f'<p>{badge}<a class="report-relation-code" href="#{document["anchor"]}-f{number}">F{number}</a></p>'
            f'<p class="report-required-check">{self.part_word("doc_required")}：{esc(feature)}</p>'
            f"{fact}{review}"
            f'<a class="report-basis-link" href="#{document["anchor"]}-f{number}">{self.t("detail")} →</a></li>'
        )

    def novelty_cards(self, solution, finding, eligible):
        """One card per compared document, led by the decisive differences; the remainder is folded."""
        cards = []
        for document in self.comparisons:
            tone, key, differences = self.document_outcome(document, solution, finding, eligible)
            decisive = [n for n in differences if self.decisive_difference(document, n)]
            lead = decisive or differences[:1]
            rest = [n for n in differences if n not in lead]
            disclosed = [
                self.plan["features"][n - 1]
                for n in solution["feature_numbers"]
                if document["effective"].get(self.plan["features"][n - 1], {}).get("judgment") == "disclosed"
            ]
            facts = (
                f'<p class="report-disclosed-facts"><b>{self.part_word("doc_facts")}：</b>'
                + esc("；".join(disclosed))
                + "</p>"
                if disclosed else ""
            )
            brief = ""
            if lead:
                value = document["effective"].get(self.plan["features"][lead[0] - 1], {})
                if value.get("reason"):
                    reason = " ".join(self.reason_text(value["reason"]).split())
                    brief = (
                        f'<p class="report-decision-brief"><b>F{lead[0]}：</b>'
                        f'{esc(reason if len(reason) <= 150 else reason[:150] + "…")}</p>'
                    )
            body = "".join(self.difference_item(document, n) for n in lead)
            tail = ""
            if rest:
                tail = (
                    f'<details class="report-other-differences"><summary>{self.part_word("doc_other")} · {len(rest)}</summary>'
                    f'<ul class="report-decisive-list">{"".join(self.difference_item(document, n) for n in rest)}</ul></details>'
                )
            link = f'<a href="#{document["anchor"]}">{esc(document["number"])}</a>'
            cards.append(
                f'<article class="report-document-decision" data-document-decision="{key}">'
                f'<div class="report-document-decision-heading"><strong>{esc(document["label"])} {link}</strong>'
                f'<span class="report-state {tone}">{self.part_word(key)}</span></div>'
                f'<p class="report-decision-title">{esc(document["title"])}</p>{brief}'
                f'<details class="report-decision-detail"><summary>{self.part_word("doc_more")}</summary>'
                f'{facts}<ul class="report-decisive-list">{body}</ul>{tail}</details></article>'
            )
        return (
            f'<div class="report-novelty-cards"><h4>{self.part_word("novelty_why")}</h4>'
            f'<p class="report-decision-rule">{esc(self.part_word("novelty_rule"))}</p>{"".join(cards)}</div>'
        )

    def supplement_block(self):
        """Beside the facts table: which differences an existing teaching could fill. Read from the authored routes only."""
        panels = []
        for solution in self.solutions:
            analysis = self.findings[solution["name"]]["inventiveness"].get("analysis")
            if not analysis:
                continue
            key = self.solution_keys[solution["name"]]
            routes = []
            for route in analysis["routes"]:
                features = ", ".join(f"F{n}" for n in route["feature_numbers"])
                routes.append(
                    f'<details class="report-matrix-reasoning"><summary>{esc(features)} · {esc(route["title"])}'
                    f' · {self.part_word(route["result"])}</summary>'
                    f'<p><b>{self.part_word("teaching")}：</b>{esc(route["teaching"])}</p>'
                    f'<p><b>{self.part_word("motivation")}：</b>{esc(route["motivation"])}</p>'
                    f'<p><b>{self.part_word("obstacles")}：</b>{esc(route["obstacles"])}</p></details>'
                )
            hidden = "" if solution["name"] == self.primary else " hidden"
            panels.append(f'<div data-scheme-panel="{key}"{hidden}>{"".join(routes)}</div>')
        if not panels:
            return ""
        return (
            f'<section class="report-difference-analysis"><h4>{self.part_word("supplement_heading")}</h4>'
            f'<p>{esc(self.part_word("supplement_note"))}</p>{"".join(panels)}</section>'
        )

    def inventiveness_baseline(self, analysis, closest):
        """Closest art, where the difference lies, its effect and the problem it actually solves."""
        features = self.plan["features"]
        groups = {n: g for g in self.plan.get("groups", []) for n in g["feature_numbers"]}
        points = "".join(
            f'<p><a class="report-relation-code" href="#{closest["anchor"]}-f{n}">F{n}</a>'
            f'{(" " + esc(groups[n]["title"])) if n in groups else ""} · {esc(features[n - 1])}</p>'
            for n in analysis["difference_feature_numbers"]
        )
        rows = (
            (
                "closest_art",
                f'{esc(closest["label"])} <a href="#{closest["anchor"]}">{esc(closest["number"])}</a>'
                f' · {esc(closest["title"])}',
            ),
            ("difference_points", points),
            ("difference_effect", self.markdown(analysis["technical_effect"])),
            ("actual_problem", self.markdown(analysis["objective_problem"])),
        )
        covered = {
            n for route in analysis["routes"] if route["result"] == "established"
            for n in route["feature_numbers"]
        }
        status = ""
        for label, selected in (
            ("route_covered", [n for n in analysis["difference_feature_numbers"] if n in covered]),
            ("route_open", [n for n in analysis["difference_feature_numbers"] if n not in covered]),
        ):
            if selected:
                links = " · ".join(f'<a href="#{closest["anchor"]}-f{n}">F{n}</a>' for n in selected)
                status += f'<p class="report-basis-item"><b>{self.part_word(label)}</b> · {links}</p>'
        return (
            '<div class="report-inventiveness-analysis">'
            f'<p class="report-muted">{esc(self.part_word("risk_basis"))}</p><dl>'
            + "".join(
                f"<div><dt>{self.part_word(key)}</dt><dd>{value}</dd></div>" for key, value in rows
            )
            + f"</dl></div><h4>{self.part_word('routes_heading')}</h4>{status}"
        )

    RECOMMENDATION_PARTS = (
        ("risk", "advice_risk"),
        ("direction", "advice_direction"),
        ("value", "advice_value"),
    )

    def recommendation_body(self, finding):
        """Three labelled parts when the author supplies them; otherwise the single recommendation as written."""
        detail = finding.get("recommendation_detail")
        if not detail:
            return self.markdown(finding["recommendation"])
        return "".join(
            f'<div class="report-brief-row"><strong>{self.part_word(label)}</strong>{self.markdown(detail[key])}</div>'
            for key, label in self.RECOMMENDATION_PARTS
            if detail.get(key, "").strip()
        )

    def validate_recommendation_detail(self, finding):
        detail = finding.get("recommendation_detail")
        if detail is None:
            return
        keys = {key for key, _ in self.RECOMMENDATION_PARTS}
        if (
            not isinstance(detail, dict)
            or not set(detail) <= keys
            or not any(isinstance(v, str) and v.strip() for v in detail.values())
            or any(not isinstance(v, str) for v in detail.values())
        ):
            raise ValueError("recommendation_detail takes risk, direction and value text; at least one is required")

    def comprehensive_judgment(self, analysis):
        """Closing blocks. `overall_reason` is the author's whole-solution reasoning and is shown once, as the judgment."""
        return (
            f'<div class="report-reasoning-conclusion"><b>{self.part_word("comprehensive")}</b>'
            f'{self.markdown(analysis["overall_reason"])}</div>'
        )

    def render_part(self, kind):
        if kind == "comparison":
            return ""
        if kind == "overview":
            return self.technical_overview()
        if kind in {"novelty", "inventiveness"}:
            return self.analysis_chapter(kind)
        if kind == "recommendations":
            return self.recommendation_chapter()
        raise ValueError("Unknown report part")

    def search_limitations(self):
        limits = list(self.draft["report"].get("limitations", []))
        if not self.coverage_complete:
            limits.append(self.part_word("partial"))
        listed = self.template(
            "limitations",
            heading=self.t("limitations"),
            items="".join(f"<li>{esc(x)}</li>" for x in limits),
        ) if limits else ""
        bound = self.draft["report"].get("publication_date")
        scope = self.part_word("scope_statement").format(
            date=bound or self.t("no_date"),
        )
        return (
            listed
            + f'<h3>{self.part_word("scope_heading")}</h3><p>{esc(scope)}</p>'
        )

    def unevaluated_content(self):
        """Disclosure passages the plan marked optional or background: listed so nothing is silently dropped."""
        items = [c for c in self.plan.get("coverage", []) if c["treatment"] in {"optional", "background"}]
        optional = [c for c in items if c["treatment"] == "optional"]
        if not optional:
            return ""
        rows = "".join(
            f'<li><blockquote>{esc(c["quote"].strip())}</blockquote><p class="report-muted">{esc(c["reason"])}</p></li>'
            for c in optional
        )
        return (
            f'<details class="report-reading-details report-unevaluated"><summary>{self.part_word("unevaluated")}'
            f' · {len(optional)}</summary><p class="report-muted">{esc(self.part_word("unevaluated_note"))}</p>'
            f'<ul class="report-decisive-list">{rows}</ul></details>'
        )

    def export_parts(self, directory):
        target = Path(directory)
        target.mkdir(parents=True, exist_ok=True)
        files = []
        for key, body in self.fragments.items():
            body = re.sub(r'src="report-image:([a-f0-9]{64})"', r'data-report-image="\1"', body)
            path = target / (key + ".html")
            path.write_text(body)
            files.append(
                {
                    "part": key,
                    "file": str(path),
                    "sha256": hashlib.sha256(body.encode()).hexdigest(),
                }
            )
        image_assets = json.dumps(self.image_data, ensure_ascii=False, sort_keys=True)
        image_file = target / "image-assets.json"
        image_file.write_text(image_assets)
        (target / "report-runtime.js").write_text(self.reader_script())
        manifest = {
            "title": self.draft["title"],
            "language": self.language,
            "parts": files,
            "data_file": str(target / "report-data.json"),
            "stylesheets": [
                str(self.ASSETS / "report.css"),
                str(self.ASSETS / "report-host.css"),
                str(self.ASSETS / "report-analysis.css"),
                str(self.ASSETS / "report-patent-reader.css"),
                str(self.ASSETS / "report-recommendations.css"),
                str(self.ASSETS / "report-comparison.css"),
                str(self.ASSETS / "report-evidence-reader.css"),
                str(self.ASSETS / "report-appendices.css"),
                str(self.ASSETS / "report-print.css"),
            ],
            "reader_script": str(target / "report-runtime.js"),
            "image_assets_file": str(image_file),
            "image_assets_sha256": hashlib.sha256(image_assets.encode()).hexdigest(),
        }
        self.export_data(target / "report-data.json")
        (target / "manifest.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2)
        )
        return manifest

    def export_data(self, path):
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "schema": "novelty.report.data.v1",
            "title": self.draft["title"], "language": self.language,
            "workspace_root": str(self.base),
            "report": self.draft.get("report"),
            "feature_plan": self.plan,
            "narratives": getattr(self, "narratives", []),
            "assets": self.draft.get("assets", []),
            "searches": self.search_records,
            "documents": [
                {
                    "publication_number": d["number"],
                    "label": d["label"],
                    "title": d["title"],
                    "application_date": d["application_date"],
                    "publication_date": d["date"],
                    "comparisons": list(d["effective"].values()),
                    "original_comparisons": d["result"].get("comparisons", []),
                    "reviews": d["reviews"],
                    "coverage": d["result"].get("coverage", {}),
                    "patent_text": d["text"],
                    "disclosure_text": d["request"].get("disclosure_text", ""),
                    "disclosure_images": d["request"].get("disclosure_images", []),
                    "images": list(d["images"].values()),
                    "request_file": d["spec"]["request_file"],
                    "response_file": d["spec"]["comparison_file"],
                    **({"document_index": d["spec"]["document_index"]} if "document_index" in d["spec"] else {}),
                }
                for d in self.comparisons
            ],
        }
        target.write_text(json.dumps(data, ensure_ascii=False, indent=2))
        return str(target)
