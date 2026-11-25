#!/usr/bin/env python3
"""Render a self-contained report from host-owned evidence and Skill-authored analysis."""

import argparse
import base64
import hashlib
import html
import importlib.util
import io
import json
import re
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

from markdown_it import MarkdownIt
from PIL import Image

_parts_spec = importlib.util.spec_from_file_location(
    "novelty_report_parts", Path(__file__).with_name("report_parts.py")
)
_parts_module = importlib.util.module_from_spec(_parts_spec)
_parts_spec.loader.exec_module(_parts_module)


def continuous_reading(markup):
    """默认展示报告全文；不修改事实、引文和原有交互锚点。"""
    markup = re.sub(r"<details\b([^>]*)>",
                    lambda match: match[0] if re.search(r"\bopen(?:\s|=|$)", match[1])
                    else "<details open" + match[1] + ">", markup)
    return re.sub(r'(<[^>]+data-(?:scheme-panel|matrix-result)="[^"]*"[^>]*?)\s+hidden(?=[\s>])',
                  r"\1", markup)


def compact_css(css):
    """减少离线报告体积；保留引号内的字体、URL 和 content 字面量。"""
    tokens = re.split(r"(\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|/\*[\s\S]*?\*/)", css)
    result = []
    for index, token in enumerate(tokens):
        if index % 2:
            result.append("" if token.startswith("/*") else token)
        else:
            value = re.sub(r"[ \t]*\n[ \t]*", "\n", token)
            result.append(value.replace("; ", ";").replace(": ", ":").replace(" {", "{").replace("}\n", "}"))
    return "".join(result)

LANGUAGES = ("zh-CN", "en-US", "zh-TW", "ja-JP", "ko-KR")
ASSETS = Path(__file__).resolve().parents[1] / "assets"
# Columns are the five public output languages, in LANGUAGES order.
COPY = {
    "evaluation_scope": ("本次评价什么", "What this report evaluates", "本次評價什麼", "今回の評価対象", "이번 평가 대상"),
    "included_points": ("本次包含的技术要点", "Technical points evaluated", "本次包含的技術要點", "評価する技術要素", "평가 기술 요소"),
    "novelty_supported": ("具备新颖性", "Novel", "具備新穎性", "新規性あり", "신규성 있음"),
    "novelty_not_supported": ("不具备新颖性", "Lacks novelty", "不具備新穎性", "新規性なし", "신규성 없음"),
    "inventiveness_supported": ("创造性有支持", "Inventive step supported", "創造性有支持", "進歩性の根拠あり", "진보성 근거 있음"),
    "inventiveness_not_supported": ("创造性支持不足", "Inventive step not supported", "創造性支持不足", "進歩性の根拠不足", "진보성 근거 부족"),
    "primary_scheme": ("主评方案", "Primary solution", "主評方案", "主評価案", "주 평가안"),
    "primary_conclusion": ("查新结论 · 主方案", "Findings · Primary solution", "查新結論 · 主方案", "調査結果 · 主方案", "조사 결과 · 주 평가안"),
    "primary_not_novel": ("主方案不具备新颖性", "The primary solution lacks novelty", "主方案不具備新穎性", "主方案に新規性なし", "주 평가안은 신규성이 없음"),
    "primary_not_novel_or_inventive": ("主方案不具备新颖性，创造性支持不足", "The primary solution lacks novelty; inventive step not supported", "主方案不具備新穎性，創造性支持不足", "主方案に新規性なし、進歩性の根拠不足", "주 평가안은 신규성이 없으며 진보성 근거 부족"),
    "novelty_pending": ("新颖性查新尚未完成，需补齐关键依据", "Novelty review is incomplete; key evidence is needed", "新穎性查新尚未完成，需補齊關鍵依據", "新規性調査は未完了、主要証拠の確認が必要", "신규성 조사 미완료, 핵심 근거 확인 필요"),
    "primary_both_supported": ("本轮证据支持新颖性与创造性", "Reviewed evidence supports novelty and inventive step", "本輪證據支持新穎性與創造性", "今回の証拠は新規性と進歩性を支持", "검토 근거가 신규성과 진보성을 뒷받침함"),
    "primary_novel_only": ("具备新颖性，创造性支持不足", "Novelty supported; inventive step not supported", "具備新穎性，創造性支持不足", "新規性あり、進歩性の根拠不足", "신규성은 있으나 진보성 근거 부족"),
    "primary_inventiveness_pending": ("本轮支持新颖性，创造性依据不足", "Novelty supported; evidence for inventive step is insufficient", "本輪支持新穎性，創造性依據不足", "新規性を支持、進歩性の根拠は不足", "신규성은 뒷받침되나 진보성 근거는 부족함"),
    "search_appendix": ("附录 A · 检索策略", "Appendix A · Search strategy", "附錄 A · 檢索策略", "付録 A · 検索戦略", "부록 A · 검색 전략"),
    "documents_appendix": ("附录 B · 对比文献清单", "Appendix B · Compared documents", "附錄 B · 對比文獻清單", "付録 B · 比較文献一覧", "부록 B · 비교 문헌 목록"),
    "search_accounting": ("检索数量口径", "Search counts", "檢索數量口徑", "検索件数の内訳", "검색 건수 내역"),
    "search_calls": ("次检索或引证查询", "search or citation calls", "次檢索或引證查詢", "件の検索・引用調査", "회 검색 또는 인용 조회"),
    "search_unique": ("篇按公开号去重", "unique by publication number", "篇按公開號去重", "件（公開番号で重複除外）", "건 (공개번호 기준 중복 제외)"),
    "search_actual": ("实际执行检索式", "Executed query", "實際執行檢索式", "実行した検索式", "실행된 검색식"),
    "search_missing": ("本次未保存可展示的检索回执。", "No displayable search receipts were saved.", "本次未保存可展示的檢索回執。", "表示できる検索記録は保存されていません。", "표시할 수 있는 검색 기록이 없습니다."),
    "search_complete": ("已完成", "Completed", "已完成", "完了", "완료"),
    "search_partial": ("部分完成", "Partially completed", "部分完成", "一部完了", "부분 완료"),
    "search_failed": ("检索未完成", "Search did not complete", "檢索未完成", "検索未完了", "검색 미완료"),
    "cc_incomplete": ("比较未完成", "Comparison incomplete", "比較未完成", "比較未完了", "비교 미완료"),
    "cc_scope": ("纳入理由与核对范围", "Inclusion reason and comparison scope", "納入理由與核對範圍", "採用理由と比較範囲", "포함 이유 및 비교 범위"),
    "route_boolean": ("关键词组合检索", "Keyword combination search", "關鍵詞組合檢索", "キーワード組み合わせ検索", "키워드 조합 검색"),
    "route_semantic": ("按技术描述查找专利", "Search patents by technical description", "按技術描述查找專利", "技術記述による特許検索", "기술 설명으로 특허 검색"),
    "route_citations": ("相关文献追踪", "Citation tracking", "相關文獻追蹤", "引用文献の追跡", "인용 문헌 추적"),
    "original_disclosure": (
        "原始交底全文与图片",
        "Original disclosure text and images",
        "原始交底全文與圖片",
        "元の開示全文と画像",
        "원본 사용자 자료 전문 및 이미지",
    ),
    "outside_date": (
        "晚于公开日边界，不作为本次在先依据",
        "After the publication boundary; excluded as prior evidence",
        "晚於公開日邊界，不作為本次在先依據",
        "公開日上限より後・先行技術の根拠には不採用",
        "공개일 기준 이후: 이번 선행 근거에서 제외",
    ),
    "eligible_date": (
        "公开日符合本次边界",
        "Publication date meets the boundary",
        "公開日符合本次邊界",
        "公開日は指定範囲内",
        "공개일이 이번 기준에 부합",
    ),
    "caption": (
        "专利查新分析报告",
        "Patent novelty analysis",
        "專利查新分析報告",
        "特許新規性調査レポート",
        "특허 신규성 분석 보고서",
    ),
    "contents": ("报告目录", "Contents", "報告目錄", "目次", "목차"),
    "expand": ("展开全文", "Expand all", "展開全文", "すべて展開", "모두 펼치기"),
    "scheme": (
        "评价方案",
        "Evaluated solution",
        "評價方案",
        "評価対象の技術案",
        "평가 대상 기술안",
    ),
    "conclusion": ("查新结论", "Findings", "查新結論", "調査結果", "조사 결과"),
    "novelty": ("新颖性", "Novelty", "新穎性", "新規性", "신규성"),
    "inventiveness": ("创造性", "Inventiveness", "創造性", "進歩性", "진보성"),
    "recommendation": (
        "申请建议",
        "Filing recommendation",
        "申請建議",
        "出願に向けた提案",
        "출원 제안",
    ),
    "overall_risk": (
        "综合新创性风险",
        "Overall patentability risk",
        "綜合新創性風險",
        "総合リスク",
        "종합 특허성 위험",
    ),
    "low": ("低风险", "Low risk", "低風險", "低リスク", "낮은 위험"),
    "high": ("高风险", "High risk", "高風險", "高リスク", "높은 위험"),
    "pending": ("尚待核实", "Pending verification", "尚待核實", "要確認", "확인 필요"),
    "not_assessed": (
        "未单独评价",
        "Not separately assessed",
        "未單獨評價",
        "個別評価なし",
        "별도 평가 없음",
    ),
    "supported": (
        "本轮证据支持",
        "Supported by reviewed evidence",
        "本輪證據支持",
        "確認済み資料が支持",
        "검토 자료가 뒷받침함",
    ),
    "not_supported": (
        "本轮已有否定依据",
        "Adverse evidence identified",
        "本輪已有否定依據",
        "否定する根拠あり",
        "부정적 근거 확인",
    ),
    "risk_note": (
        "风险等级反映本次证据下的判断，不代表授权概率。",
        "Risk levels reflect the evidence-based findings, not the probability of grant.",
        "風險等級反映本次證據下的判斷，不代表授權概率。",
        "リスク水準は証拠に基づく判断を示し、登録確率ではありません。",
        "위험 수준은 증거에 따른 판단이며 등록 확률을 뜻하지 않습니다.",
    ),
    "documents": (
        "篇比较文献",
        "Compared documents",
        "篇比較文獻",
        "対比文献",
        "비교 문헌",
    ),
    "features": (
        "项技术特征",
        "Technical features",
        "項技術特徵",
        "技術的特徴",
        "기술적 특징",
    ),
    "reviews": (
        "条事实核查",
        "Fact-checks",
        "條事實核查",
        "事実確認",
        "사실 확인",
    ),
    "date": (
        "在先公开边界",
        "Publication date boundary",
        "在先公開邊界",
        "公開日の上限",
        "공개일 기준",
    ),
    "inclusive": ("含当天", "inclusive", "含當天", "当日を含む", "당일 포함"),
    "no_date": (
        "未设置，需核实日期资格",
        "Not set; eligibility requires verification",
        "未設置，需核實日期資格",
        "未設定・日付の適格性を要確認",
        "미설정: 날짜 적격성 확인 필요",
    ),
    "boundary": (
        "评价边界与交底依据",
        "Scope and disclosure evidence",
        "評價邊界與交底依據",
        "評価範囲と開示の根拠",
        "평가 범위와 사용자 자료 근거",
    ),
    "source": (
        "交底依据",
        "Disclosure evidence",
        "交底依據",
        "開示の根拠",
        "사용자 자료 근거",
    ),
    "matrix": (
        "特征 × 文献对比表",
        "Feature × document matrix",
        "特徵 × 文獻對比表",
        "特徴 × 文献 対比表",
        "특징 × 문헌 비교표",
    ),
    "feature": (
        "技术特征",
        "Technical feature",
        "技術特徵",
        "技術的特徴",
        "기술적 특징",
    ),
    "disclosed": ("公开", "Disclosed", "公開", "開示あり", "공개됨"),
    "not_disclosed": (
        "未公开 · 明确不同",
        "Not disclosed · different arrangement",
        "未公開 · 明確不同",
        "非開示・異なる構成",
        "미공개 · 다른 구성",
    ),
    "not_mentioned": ("未提及", "Not mentioned", "未提及", "記載なし", "언급 없음"),
    "material_gap": (
        "材料不足 · 未作判断",
        "Insufficient material · no finding",
        "材料不足 · 未作判斷",
        "資料不足・未判断",
        "자료 부족 · 미판단",
    ),
    "uncompared": ("尚未比较", "Not yet compared", "尚未比較", "未対比", "미비교"),
    "detail": (
        "查看完整对照与依据",
        "View comparison and evidence",
        "查看完整對照與依據",
        "対比と根拠を見る",
        "전체 비교 및 근거 보기",
    ),
    "reason": ("判断理由", "Reasoning", "判斷理由", "判断理由", "판단 이유"),
    "evidence": (
        "原文与附图依据",
        "Text and figure evidence",
        "原文與附圖依據",
        "原文と図面の根拠",
        "원문 및 도면 근거",
    ),
    "observation": (
        "图中观察",
        "Figure observation",
        "圖中觀察",
        "図からの観察",
        "도면 관찰",
    ),
    "no_evidence": (
        "本条没有可引用的证据；不能据此推定文献不存在该特征。",
        "No citable evidence for this finding; absence of a feature must not be inferred from this alone.",
        "本條沒有可引用的證據；不能據此推定文獻不存在該特徵。",
        "引用できる根拠がありません。これだけで特徴が存在しないとは判断できません。",
        "인용할 근거가 없습니다. 이것만으로 해당 특징이 없다고 추정할 수 없습니다.",
    ),
    "review": (
        "事实核查",
        "Fact-check",
        "事實核查",
        "事実確認",
        "사실 확인",
    ),
    "upheld": (
        "已复核 · 维持原判断",
        "Reviewed · upheld",
        "已複核 · 維持原判斷",
        "再確認済み・元の判断を維持",
        "재검토 완료 · 원판단 유지",
    ),
    "overturned": (
        "已复核 · 已改判",
        "Reviewed · overturned",
        "已複核 · 已改判",
        "再確認済み・判断変更",
        "재검토 완료 · 판단 변경",
    ),
    "material_insufficient": (
        "复核材料不足",
        "Insufficient review material",
        "複核材料不足",
        "再確認の資料不足",
        "재검토 자료 부족",
    ),
    "unreviewed": (
        "本条未记录事实核查",
        "No recorded fact-check",
        "本條未記錄事實核查",
        "事実確認の記録なし",
        "사실 확인 기록 없음",
    ),
    "stale": (
        "旧复核与当前材料或判断不一致，未采用",
        "Previous review does not match current material or finding; not applied",
        "舊複核與目前材料或判斷不一致，未採用",
        "旧再確認は現資料・判断と一致せず未適用",
        "이전 재검토가 현재 자료·판단과 달라 적용하지 않음",
    ),
    "original": (
        "原 CC 判断",
        "Original CC finding",
        "原 CC 判斷",
        "元の対比判断",
        "기존 CC 판단",
    ),
    "after_review": (
        "复核后的判断",
        "Reviewed finding",
        "複核後的判斷",
        "再確認後の判断",
        "재검토 후 판단",
    ),
    "coverage": (
        "本篇实际检查范围",
        "Material actually examined",
        "本篇實際檢查範圍",
        "実際の確認範囲",
        "실제 검토 범위",
    ),
    "limitations": (
        "范围与未决事项",
        "Scope and unresolved issues",
        "範圍與未決事項",
        "範囲と未解決事項",
        "범위 및 미해결 사항",
    ),
    "fulltext": (
        "查看本次使用的完整文献正文",
        "Read the full text used for this comparison",
        "查看本次使用的完整文獻正文",
        "対比に使用した全文を見る",
        "이번 비교에 사용한 전문 보기",
    ),
    "legend": (
        "标记怎么读",
        "How to read the labels",
        "標記怎麼讀",
        "ラベルの読み方",
        "표시 읽는 법",
    ),
    "common_knowledge": (
        "公知常识与常规设计", "Common general knowledge and routine design", "公知常識與常規設計",
        "周知技術と通常の設計変更", "공통 일반지식과 통상적 설계",
    ),
    "common_knowledge_note": (
        "用于分析区别能否由已有技术补足。应在创造性评价中说明具体依据和改造动机；属于常规设计的判断，仍需依据才能认定为公知常识。",
        "Assess whether existing techniques can address a difference. Explain the evidence and motivation in the inventive-step analysis. Treating a change as routine does not establish that it was common general knowledge.",
        "用於分析區別能否由已有技術補足。應在創造性評價中說明具體依據和改造動機；屬於常規設計的判斷，仍需依據才能認定為公知常識。",
        "既存技術で相違点を補えるかを評価します。根拠と変更の動機は進歩性評価で示します。通常の設計変更と判断しても、周知技術と認定するには根拠が必要です。",
        "기존 기술로 차이점을 보완할 수 있는지 평가합니다. 진보성 평가에서 근거와 변경 동기를 설명합니다. 통상적 설계 변경이라는 판단을 공통 일반지식으로 인정하려면 별도의 근거가 필요합니다.",
    ),
    "routine_tag": ("常规设计", "Routine design", "常規設計", "通常の設計変更", "통상적 설계"),
    "common_knowledge_tag": ("公知常识", "Common general knowledge", "公知常識", "周知技術", "공통 일반지식"),
    "design_difference": ("具体区别", "Specific difference", "具體區別", "具体的な相違点", "구체적 차이"),
    "design_basis": ("改造依据", "Basis for the change", "改造依據", "変更の根拠", "변경 근거"),
    "design_expectation": ("预期效果", "Expected effect", "預期效果", "予期される効果", "예상 효과"),
    "search": ("检索记录", "Search records", "檢索記錄", "検索記録", "검색 기록"),
    "query": (
        "实际检索输入",
        "Actual search input",
        "實際檢索輸入",
        "実際の検索入力",
        "실제 검색 입력",
    ),
    "hits": ("数据库命中", "Database hits", "資料庫命中", "ヒット数", "검색 결과 수"),
    "returned": (
        "本次返回",
        "Returned in this call",
        "本次傳回",
        "今回の返却数",
        "이번 호출 반환 수",
    ),
    "publication": (
        "公开号 / 公开日",
        "Publication / date",
        "公開號 / 公開日",
        "公開番号 / 公開日",
        "공개번호 / 공개일",
    ),
    "title": ("文献名称", "Document title", "文獻名稱", "文献名", "문헌 제목"),
    "status": ("核对进度", "Review progress", "核對進度", "確認状況", "검토 진행 상황"),
    "candidate": (
        "仅检索返回，未完成详细比较",
        "Search result only; detailed comparison not completed",
        "僅檢索傳回，未完成詳細比較",
        "検索結果のみ・詳細対比未完了",
        "검색 결과만 확보, 상세 비교 미완료",
    ),
    "partial": ("阶段结果", "Partial result", "階段結果", "途中結果", "부분 결과"),
    "complete": (
        "已完成本次比较",
        "Comparison completed",
        "已完成本次比較",
        "今回の対比完了",
        "이번 비교 완료",
    ),
    "search_note": (
        "数据库命中、实际返回、去重候选和正式对比文献分别计数。仅正式对比结果用于评价。",
        "Database hits, returned results, unique candidates and compared documents are counted separately. Findings use the formal comparisons.",
        "資料庫命中、實際傳回、去重候選和正式對比文獻分別計數。僅正式對比結果用於評價。",
        "ヒット数、返却件数、重複除外件数、比較文献数を区別します。評価には正式比較の結果を使用します。",
        "검색 건수, 반환 건수, 중복 제외 후보 및 비교 문헌을 별도로 집계합니다. 평가는 정식 비교를 근거로 합니다.",
    ),
}


def esc(value):
    return html.escape(str(value), quote=True)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


class LinkCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.images = [], [], []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "a" and a.get("href", "").startswith("#"):
            self.links.append(a["href"][1:])
        if a.get("data-report-cell-open"):
            self.links.append(a["data-report-cell-open"])
        if tag == "img":
            self.images.append(a.get("src", ""))


_overview_spec = importlib.util.spec_from_file_location(
    "novelty_report_overview", Path(__file__).with_name("report_overview.py")
)
_overview_module = importlib.util.module_from_spec(_overview_spec)
_overview_spec.loader.exec_module(_overview_module)


_analysis_spec = importlib.util.spec_from_file_location("novelty_report_analysis", Path(__file__).with_name("report_analysis.py"))
_analysis_module = importlib.util.module_from_spec(_analysis_spec)
_analysis_spec.loader.exec_module(_analysis_module)
_patent_spec = importlib.util.spec_from_file_location("novelty_report_patent", Path(__file__).with_name("report_patent.py"))
_patent_module = importlib.util.module_from_spec(_patent_spec)
_patent_spec.loader.exec_module(_patent_module)


_recommendations_spec = importlib.util.spec_from_file_location("novelty_report_recommendations", Path(__file__).with_name("report_recommendations.py"))
_recommendations_module = importlib.util.module_from_spec(_recommendations_spec)
_recommendations_spec.loader.exec_module(_recommendations_module)


_comparison_spec = importlib.util.spec_from_file_location("novelty_report_comparison", Path(__file__).with_name("report_comparison.py"))
_comparison_module = importlib.util.module_from_spec(_comparison_spec)
_comparison_spec.loader.exec_module(_comparison_module)

_appendices_spec = importlib.util.spec_from_file_location("novelty_report_appendices", Path(__file__).with_name("report_appendices.py"))
_appendices_module = importlib.util.module_from_spec(_appendices_spec)
_appendices_spec.loader.exec_module(_appendices_module)

_receipts_spec = importlib.util.spec_from_file_location("novelty_report_receipts", Path(__file__).with_name("report_receipts.py"))
_receipts_module = importlib.util.module_from_spec(_receipts_spec)
_receipts_spec.loader.exec_module(_receipts_module)


class Report(_appendices_module.AppendicesPresentation, _comparison_module.ComparisonPresentation, _recommendations_module.RecommendationPresentation, _analysis_module.AnalysisPresentation, _patent_module.PatentReader, _overview_module.TechnicalOverview, _parts_module.Parts):
    comparison_source_context = staticmethod(_patent_module.source_context)
    search_result = staticmethod(_receipts_module.search_result)
    search_query = staticmethod(_receipts_module.search_query)
    search_routes = staticmethod(_receipts_module.search_routes)
    LANGUAGES = LANGUAGES
    ASSETS = ASSETS

    def __init__(self, draft, base, *, presentation=True):
        self.draft, self.base = draft, Path(base).resolve()
        self.presentation = presentation
        self._comparison_cache = {}
        self._search_cache = {}
        self.search_records = []
        self.common_knowledge = {}
        self.language = draft.get("language", "zh-CN")
        if self.language not in LANGUAGES:
            raise ValueError("Unsupported report language")
        self.assets, self.library, self.comparisons = {}, {}, []
        self.image_files, self.image_data = {}, {}
        self.feature_names, self.review_count = set(), 0
        self.failed_comparisons = []
        self.md = MarkdownIt("commonmark", {"html": False, "breaks": True}).enable(
            "table"
        )
        self.md.renderer.rules["table_open"] = lambda *args: (
            '<div class="report-table-wrap"><table>\n'
        )
        self.md.renderer.rules["table_close"] = lambda *args: "</table></div>\n"
        for item in draft.get("assets", []):
            if item["name"] in self.assets:
                raise ValueError("Duplicate report asset name")
            self.assets[item["name"]] = (
                self.image(item["path"], item.get("ref")) if presentation
                else self.image_bytes(item["path"], item.get("ref"))[1]
            )

        self.prepare_parts()

    def t(self, key):
        return COPY[key][LANGUAGES.index(self.language)]

    def path(self, value):
        path = (self.base / value).resolve()
        if not path.is_relative_to(self.base):
            raise ValueError("Report file must be inside the task workspace")
        return path

    def load(self, value):
        path = self.path(value)
        raw = path.read_bytes()
        checksum = path.with_suffix(".sha256")
        if (
            checksum.exists()
            and checksum.read_text().strip()
            != hashlib.sha256(canonical(json.loads(raw)).encode()).hexdigest()
        ):
            raise ValueError("Report input SHA256 mismatch")
        return _receipts_module.payload(json.loads(raw))

    def image_bytes(self, value, ref=None):
        path = self.path(value)
        expected = (ref or "").rsplit(":", 1)[-1] or (
            path.stem if re.fullmatch(r"[a-f0-9]{64}", path.stem) else None
        )
        data = path.read_bytes()
        checksum = hashlib.sha256(data).hexdigest()
        if expected and checksum != expected:
            raise ValueError("Report image SHA256 mismatch")
        with Image.open(io.BytesIO(data)) as image:
            if image.format not in {"PNG", "JPEG"}:
                raise ValueError("Report only embeds PNG/JPEG images")
            image.verify()
            mime = "image/png" if image.format == "PNG" else "image/jpeg"
        return data, mime

    def saved_images(self, images, assets=()):
        """Materialize wire images locally while retaining their original identity."""
        blobs = {asset["ref"]: asset for asset in assets}
        saved = []
        for image in images or []:
            image = {**blobs.get(image.get("ref"), {}), **image}
            if not image.get("host_file"):
                data = base64.b64decode(image.get("data_base64", ""), validate=True)
                checksum = hashlib.sha256(data).hexdigest()
                if not data or image.get("ref") != "image:" + checksum:
                    raise ValueError("Wire image requires matching bytes and SHA256")
                extension = {"image/png": ".png", "image/jpeg": ".jpg"}.get(image.get("mime_type"))
                if not extension:
                    raise ValueError("Unsupported wire image type")
                relative = "evidence/" + checksum + extension
                target = self.path(relative)
                target.parent.mkdir(parents=True, exist_ok=True)
                if not target.exists():
                    target.write_bytes(data)
                image["host_file"] = relative
            self.image_bytes(image["host_file"], image.get("ref"))
            saved.append(image)
        return saved

    def image(self, value, ref=None):
        path = self.path(value)
        expected = (ref or "").rsplit(":", 1)[-1] or (path.stem if re.fullmatch(r"[a-f0-9]{64}", path.stem) else None)
        if path in self.image_files:
            checksum = self.image_files[path]
            if expected and checksum != expected:
                raise ValueError("Report image SHA256 mismatch")
        else:
            data, mime = self.image_bytes(value, ref)
            checksum = hashlib.sha256(data).hexdigest()
            self.image_files[path] = checksum
            self.image_data[checksum] = f"data:{mime};base64," + base64.b64encode(data).decode()
        return "report-image:" + checksum

    def markdown_tokens(self, content):
        tokens = self.md.parse(content)
        for token in tokens:
            for child in token.children or []:
                if child.type == "image":
                    src = child.attrGet("src") or ""
                    if not src.startswith("asset:") or src[6:] not in self.assets:
                        raise ValueError("Report image must resolve to a saved asset")
        return tokens

    def markdown(self, content, *, cover=False):
        tokens = self.markdown_tokens(content)
        for token in tokens:
            for child in token.children or []:
                if cover and child.type == "text":
                    child.content = self.cover_text(child.content)
                if child.type == "image":
                    child.attrSet("src", self.assets[child.attrGet("src")[6:]])
        return self.md.renderer.render(tokens, self.md.options, {})

    def markdown_plain_text(self, content):
        """总览摘要只取 Markdown 的可见文字，避免露出加粗符号或链接语法。"""
        parts = []
        for token in self.md.parse(content):
            if token.type == "inline":
                parts.append("".join(
                    " " if child.type in {"softbreak", "hardbreak"} else child.content
                    for child in token.children or []
                    if child.type in {"text", "code_inline", "softbreak", "hardbreak"}
                ))
        return " ".join(" ".join(parts).split())

    def reason_text(self, value):
        """Translate implementation markers in explanations, never in evidence quotations."""
        value = re.sub(
            r"basis\s*=\s*implicit[.。]?", self.badge_label("implicit") + "：", value
        )
        value = re.sub(r"basis\s*=\s*explicit[.。]?", self.t("disclosed") + "：", value)
        for code in ("not_mentioned", "not_disclosed", "material_insufficient"):
            value = value.replace(code, self.t(code))
        return value

    def badge_label(self, basis):
        labels = {
            "implicit": (
                "必要隐含公开",
                "Necessarily implicit",
                "必要隱含公開",
                "必然的な黙示開示",
                "필연적 묵시 공개",
            ),
            "mixed": (
                "明确及必要隐含公开",
                "Explicit and necessarily implicit",
                "明確及必要隱含公開",
                "明示及び必然的な黙示開示",
                "명시 및 필연적 묵시 공개",
            ),
        }
        return labels[basis][LANGUAGES.index(self.language)]

    def badge(self, judgment, disclosure_type=None):
        classes = {
            "disclosed": "satisfied",
            "not_disclosed": "different",
            "not_mentioned": "not_mentioned",
            "material_gap": "material-gap",
        }
        judgment = judgment or "material_gap"
        if judgment not in classes:
            raise ValueError("Unknown comparison judgment")
        if judgment == "disclosed" and disclosure_type in {"implicit", "mixed"}:
            return f'<span class="report-state implicit">{self.badge_label(disclosure_type)}</span>'
        return (
            f'<span class="report-state {classes[judgment]}">{self.t(judgment)}</span>'
        )

    def comparison_status_guide(self):
        entries = (
            ("disclosed", "explicit", (
                "文献证据支持该特征。明确公开时可在原文或附图中直接找到对应关系。",
                "Document evidence supports the feature. Explicit disclosure is directly shown in the text or drawings.",
                "文獻證據支持該特徵。明確公開時可在原文或附圖中直接找到對應關係。",
                "文献の証拠が特徴を裏付けます。明示開示は本文や図面で直接確認できます。",
                "문헌 근거가 특징을 뒷받침합니다. 명시적 공개는 본문이나 도면에서 직접 확인할 수 있습니다.",
            )),
            ("disclosed", "implicit", (
                "该特征可从文献直接、毫无疑义地推得。若可能决定单篇完整公开，须核查决定性事实。",
                "The feature follows directly and unambiguously from the document. Record a fact-check if it may determine whole-solution disclosure.",
                "該特徵可從文獻直接、毫無疑義地推得。若可能決定單篇完整公開，須核查決定性事實。",
                "文献から直接かつ一義的に導けます。単一文献による全体開示を左右し得る場合は事実を再確認して記録します。",
                "문헌으로부터 직접적이고 명확하게 도출됩니다. 단일 문헌의 전체 공개 여부를 좌우할 수 있다면 사실을 재검토하고 기록합니다.",
            )),
            ("disclosed", "mixed", (
                "部分关系明确记载，其余必要关系可直接推得。",
                "The document states part of the relationship explicitly and necessarily implies the rest.",
                "部分關係明確記載，其餘必要關係可直接推得。",
                "一部の関係は明示され、残りの関係は必然的に導かれます。",
                "관계의 일부는 명시되어 있고 나머지는 필연적으로 도출됩니다.",
            )),
            ("not_disclosed", None, (
                "有证据表明文献采用了不同的实现。可作为该篇文献的区别，创造性需另行分析。",
                "Evidence shows a different implementation. It can distinguish this document. Assess inventive step separately.",
                "有證據表明文獻採用了不同的實現。可作為該篇文獻的區別，創造性需另行分析。",
                "文献に異なる実装の証拠があります。この文献との相違点になり、進歩性は別途評価します。",
                "문헌이 다른 구현을 사용했다는 근거가 있습니다. 해당 문헌과의 차이점이 되며 진보성은 별도로 평가합니다.",
            )),
            ("not_mentioned", None, (
                "在已核查的材料中未找到该特征。若新颖性判断依赖这一点，须核查决定性事实。",
                "The feature was not found in the material examined. Record a fact-check if the novelty finding depends on it.",
                "在已核查的材料中未找到該特徵。若新穎性判斷依賴這一點，須核查決定性事實。",
                "確認した資料では見つかりませんでした。新規性判断がこれに依存する場合は事実を再確認して記録します。",
                "검토한 자료에서 해당 특징을 찾지 못했습니다. 신규성 판단이 이에 의존한다면 사실을 재검토하고 기록합니다.",
            )),
            ("material_gap", None, (
                "缺少作出判断所需的材料，该格保留待核实。",
                "Material needed for a finding is missing. This comparison remains unresolved.",
                "缺少作出判斷所需的材料，該格保留待核實。",
                "判断に必要な資料が不足しており、この対比は未確定です。",
                "판단에 필요한 자료가 부족해 해당 비교는 미확정입니다.",
            )),
        )
        language = LANGUAGES.index(self.language)
        return "".join(
            f'<div><dt>{self.badge(judgment, basis)}</dt><dd>{esc(explanations[language])}</dd></div>'
            for judgment, basis, explanations in entries
        )

    def validate_evidence(self, document, entry):
        label = entry.get("image_label")
        if label and label not in document["images"]:
            raise ValueError(f"Evidence image not found in actual comparison material: {label}")
        quote = entry.get("quote")
        if quote and " ".join(quote.split()) not in " ".join(document["text"].split()):
            raise ValueError("Report quote is absent from comparison material")

    def evidence(self, document, entry):
        self.validate_evidence(document, entry)
        identifier = (
            "evidence-"
            + hashlib.sha256(
                canonical([document["number"], entry]).encode()
            ).hexdigest()[:20]
        )
        if identifier not in self.library:
            label = entry.get("image_label")
            figure = document["images"].get(label) if label else None
            quote, observation = entry.get("quote"), entry.get("observation")
            body = (_patent_module.source_context(document["text"], quote) or f"<blockquote>{esc(quote)}</blockquote>") if quote else ""
            if quote or figure:
                body += f'<p class="report-source-full-link"><a href="#patent-{document["anchor"]}">{self.patent_word("full")}</a></p>'
            if figure:
                src = self.image(figure["host_file"], figure.get("ref"))
                body += f'<img src="{src}" alt="{esc(label)}" loading="lazy">'
            if observation:
                body += f"<p><b>{self.t('observation')}：</b>{esc(observation)}</p>"
            self.library[identifier] = (
                f'<article class="report-evidence" data-evidence-source="{esc(document["number"])}" data-evidence-locator="{esc(entry.get("location") or label or "")}" id="{identifier}"><h3>{esc(document["label"])} · {esc(document["number"])} · {esc(entry.get("location") or label or "")}</h3>'
                + (f'<p class="report-muted">{esc(label)}</p>' if label else "")
                + body
                + "</article>"
            )
        locator = (
            entry.get("location") or entry.get("image_label") or self.t("evidence")
        )
        link = f'<a class="report-map-location" href="#{identifier}">{esc(locator)}</a>'
        if entry.get("image_label"):
            src = self.image(
                document["images"][entry["image_label"]]["host_file"],
                document["images"][entry["image_label"]].get("ref"),
            )
            link += f'<a class="report-atomic-thumbnail" href="#{identifier}"><img src="{src}" alt="{esc(entry["image_label"])}" loading="lazy"></a>'
        return link

    @staticmethod
    def material_key(material):
        return canonical(
            [
                material.get("patent_text", ""),
                [
                    (
                        x.get("ref"),
                        x.get("label"),
                        x.get("pdf_page"),
                        x.get("text_locations") or [],
                    )
                    for x in (material.get("patent_images") or [])
                ],
            ]
        )

    @staticmethod
    def comparison_key(value):
        if value is None:
            return canonical(None)
        return canonical({"disclosure_type": None, **{k: v for k, v in value.items() if k != "routine"}})

    @staticmethod
    def disclosure_basis(value):
        if value.get("judgment") == "disclosed":
            return value.get("disclosure_type"), value.get("evidence", [])
        return None

    def apply_reviews(self, document):
        original_facts = {x["feature"]: x for x in document["result"].get("comparisons", [])}
        current = original_facts.copy()
        document["reviews"] = {}
        for files in document["spec"].get("reviews", []):
            request, result = (
                self.load(files["request_file"]),
                self.load(files["response_file"]),
            )
            original = request.get("comparison", {})
            feature = original.get("feature")
            method = result.get("method", "tool")
            if method not in {"agent", "tool"}:
                raise ValueError("Unknown fact-check method")
            if method == "agent" and (
                request.get("publication_number") != document["number"]
                or not isinstance(result.get("checked_scope"), str)
                or not result["checked_scope"].strip()
                or not isinstance(result.get("reason"), str)
                or not result["reason"].strip()
            ):
                raise ValueError("Agent checks require the exact publication, checked scope and reason")
            material = {
                "patent_text": document["text"],
                "patent_images": list(document["images"].values()),
            }
            compatible = (
                self.comparison_key(original)
                == self.comparison_key(current.get(feature))
                and self.comparison_key(result.get("original_comparison"))
                == self.comparison_key(original)
                and request.get("features") == document["request"].get("features")
                and request.get("disclosure_text")
                == document["request"].get("disclosure_text")
                and self.material_key({"patent_images": request.get("disclosure_images")})
                == self.material_key({"patent_images": document["request"].get("disclosure_images")})
                and self.material_key(request) == self.material_key(material)
            )
            if not compatible:
                if feature in current and feature not in document["reviews"]:
                    document["reviews"][feature] = {
                        "status": "stale",
                        "reason": self.t("stale"),
                        "method": method,
                    }
                continue
            if result["status"] not in {
                "upheld",
                "overturned",
                "material_insufficient",
            }:
                raise ValueError("Unsupported review outcome")
            reviewed = result.get("reviewed_comparison")
            if result["status"] in {"upheld", "overturned"}:
                if (
                    not reviewed
                    or reviewed["feature"] != feature
                    or reviewed.get("judgment") not in {"disclosed", "not_disclosed", "not_mentioned"}
                ):
                    raise ValueError("Review must identify the original feature")
                if method == "agent" and (
                    (result["status"] == "upheld")
                    != (self.comparison_key(reviewed) == self.comparison_key(original))
                ):
                    raise ValueError("Agent check outcome must agree with its original and reviewed facts")
                if reviewed.get("judgment") in {"disclosed", "not_disclosed"} and not reviewed.get("evidence"):
                    raise ValueError("Reviewed disclosure or difference requires actual evidence")
                for entry in reviewed.get("evidence", []):
                    self.validate_evidence(document, entry)
                routine = current[feature].get("routine")
                if routine and result["status"] == "upheld" and self.comparison_key(reviewed) == self.comparison_key(current[feature]):
                    reviewed = {**reviewed, "routine": routine}
                current[feature] = reviewed
                self.review_count += 1
            elif feature in current:
                current[feature] = {
                    **current[feature], "judgment": None, "disclosure_type": None,
                    "reason": result["reason"], "evidence": [], "routine": None,
                }
            document["reviews"][feature] = {**result, "method": method, "original": original}
        document["effective"] = current
        document["arrangement_changes"] = {
            feature for feature, fact in current.items()
            if self.disclosure_basis(fact) != self.disclosure_basis(original_facts[feature])
        }

    def review_html(self, document, feature, full=False):
        review = document["reviews"].get(feature)
        if not review:
            return f'<small class="report-atomic-review unreviewed">{self.t("unreviewed")}</small>'
        status = review["status"]
        source = self.review_source(review)
        label = f'<span class="report-atomic-review" data-review="{status}" data-review-method="{esc(review.get("method", "tool"))}">{source} · {self.t(status)}</span>'
        if not full:
            return label
        original = review.get("original")
        body = f"<p>{esc(review['reason'])}</p>"
        if review.get("checked_scope"):
            body += f'<p>{esc(review["checked_scope"])}</p>'
        if original:
            body += f"<p><b>{self.t('original')}：</b>{self.badge(original['judgment'])} {esc(original['reason'])}</p>"
        return f'<details class="report-atomic-review-detail"><summary>{label}</summary>{body}</details>'

    def review_source(self, review):
        labels = (("Agent 核查", "Agent fact-check", "Agent 核查", "Agent による確認", "Agent 사실 확인")
                  if review.get("method") == "agent" else
                  ("工具复核", "Tool review", "工具複核", "ツールによる再確認", "도구 재검토"))
        return labels[LANGUAGES.index(self.language)]

    def cell_design(self, doc, number, value, *, details=False):
        if value["judgment"] not in {"not_disclosed", "not_mentioned"}:
            return ""
        if doc["reviews"].get(value["feature"], {}).get("status") == "material_insufficient":
            return ""
        entries = []
        if routine := value.get("routine"):
            entries.append(("routine_tag", "".join(
                f'<p><b>{self.t(label)}</b> · {esc(routine[key])}</p>'
                for label, key in (
                    ("design_difference", "difference"), ("design_basis", "basis"), ("design_expectation", "expectation")
                )
            ) if details else ""))
        if record := self.common_knowledge.get((doc["number"], number)):
            source = record["source"]
            entries.append(("common_knowledge_tag", (
                f'<p>{esc(source["title"])} · {esc(source["date"])} · {esc(source["locator"])}</p>'
                f'<blockquote>{esc(source["quote"])}</blockquote><p>{esc(record["reason"])}</p>'
            ) if details else ""))
        return "".join(
            f'<details class="report-routine"><summary>{self.t(label)}</summary>{body}</details>'
            if details else f'<span class="report-state report-routine-tag">{self.t(label)}</span>'
            for label, body in entries
        )

    def arrangement_label(self, arrangement):
        label = self.part_word("arrangement_" + arrangement["basis"])
        where = "、".join(arrangement.get("locators", []))
        return label + (f"：{where}" if where else "")

    def arrangement_callout(self, arrangement):
        """The model's judgment of whether the disclosed pieces form one solution. Earlier receipts have none."""
        if not arrangement:
            return ""
        quotes = "".join(f"<blockquote>{esc(quote)}</blockquote>" for quote in arrangement.get("link_quotes", []))
        return (
            f'<div class="report-arrangement-callout"><strong>{self.part_word("arrangement")}</strong>'
            f'<span>{esc(self.arrangement_label(arrangement))}</span><p>{esc(arrangement["reason"])}</p>{quotes}</div>'
        )

    def comparison_data(self, spec, identifier):
        key = canonical([identifier, spec])
        if key in self._comparison_cache:
            return self._comparison_cache[key]
        extraction = self.load(spec["features_file"])
        features = (
            extraction["features"] if isinstance(extraction, dict) else extraction
        )
        if (
            not features
            or len(set(features)) != len(features)
            or not all(isinstance(f, str) and f.strip() for f in features)
        ):
            raise ValueError("Comparison needs a unique, nonempty feature list")
        feature_evidence = (
            {x["feature"]: x for x in extraction.get("feature_evidence", [])}
            if isinstance(extraction, dict)
            else {}
        )
        docs, labels, numbers = [], set(), set()
        failures, succeeded = {}, set()
        for i, item in enumerate(spec["documents"], 1):
            request, result = (
                self.load(item["request_file"]),
                self.load(item["comparison_file"]),
            )
            if request.get("patents") is not None:
                index = item.get("document_index")
                records = _parts_module.comparison_records(request, result)
                for failed_index, source, outcome in records:
                    if outcome.get("isError"):
                        identity = source.get("publication_number") or source.get("patent_id") or f'index {failed_index}'
                        failures[(item["request_file"], failed_index)] = {
                            "identity": identity, "index": failed_index,
                            "request_file": item["request_file"],
                            "error": json.dumps(outcome.get("content", []), ensure_ascii=False),
                        }
                if type(index) is not int or not 0 <= index < len(records):
                    raise ValueError("Batch report document requires its original document_index")
                _, request, result = records[index]
                if result.get("isError"):
                    raise ValueError("Failed batch CC cannot be used as a completed comparison")
            if request.get("features") != features:
                raise ValueError("Comparison and report must use the same feature list")
            if (
                result.get("comparisons")
                and [x["feature"] for x in result["comparisons"]] != features
            ):
                raise ValueError(
                    "CC response features do not match the requested feature list"
                )
            material = result.get("material") or request
            patent = result.get("patent") or {}
            if item.get("metadata_file"):
                receipt = self.load(item["metadata_file"])
                number = patent.get("publication_number") or request.get("publication_number")
                source = _receipts_module.bibliography(receipt)
                candidates = [source] if source else [
                    entry["source"] for entry in receipt.get("materials", [])
                ]
                matches = [source for source in candidates if source.get("publication_number") == number]
                if len(matches) != 1:
                    raise ValueError("Patent metadata belongs to a different document")
                patent = matches[0]
            number = patent.get("publication_number") or request.get(
                "publication_number", ""
            )
            succeeded.update(x for x in (number, request.get("patent_id"), patent.get("patent_id")) if x)
            label = item.get("label", f"D{i}")
            if not number or number in numbers or label in labels:
                raise ValueError(
                    "Document identity and labels must be unique within a matrix"
                )
            numbers.add(number)
            labels.add(label)
            images = self.saved_images(material.get("patent_images", []), material.get("assets") or [])
            if request.get("disclosure_images"):
                request = {**request, "disclosure_images": self.saved_images(request["disclosure_images"])}
            if len({x["label"] for x in images}) != len(images):
                raise ValueError("Ambiguous material image label")
            if patent.get("publication_date"):
                date.fromisoformat(patent["publication_date"])
            if patent.get("application_date"):
                date.fromisoformat(patent["application_date"])
            document = {
                "spec": item,
                "request": request,
                "result": result,
                "number": number,
                "label": label,
                "title": patent.get("title") or number,
                "application_date": patent.get("application_date") or "",
                "date": patent.get("publication_date") or "",
                "text": material.get("patent_text", ""),
                "images": {x["label"]: x for x in images},
                "anchor": f"{identifier}-d{i}",
            }
            self.apply_reviews(document)
            docs.append(document)
            self.comparisons.append(document)
        if not docs:
            raise ValueError("Comparison matrix needs at least one actual document")
        self.failed_comparisons = [failure for failure in failures.values() if failure["identity"] not in succeeded]
        self.feature_names.update(features)
        for document in docs:
            for image in [*document["images"].values(), *document["request"].get("disclosure_images", [])]:
                self.image_bytes(image["host_file"], image.get("ref"))
            for value in document["effective"].values():
                for entry in value.get("evidence", []):
                    self.validate_evidence(document, entry)
        disclosure = docs[0]["request"].get("disclosure_text", "")
        images = {im["label"] for im in docs[0]["request"].get("disclosure_images", [])}
        for feature, provenance in feature_evidence.items():
            self.validate_disclosure_highlights(provenance)
            if feature not in features:
                raise ValueError("Feature evidence refers to an unknown feature")
            if provenance.get("source_quote") and provenance["source_quote"] not in disclosure:
                raise ValueError("Feature evidence is absent from the disclosure")
            if not set(provenance.get("image_labels", [])) <= images:
                raise ValueError("Disclosure evidence image is missing")
        data = features, feature_evidence, docs
        self._comparison_cache[key] = data
        return data

    def comparison(self, spec, identifier):
        features, feature_evidence, docs = self.comparison_data(spec, identifier)
        catalog, rows, details, print_rows = [], [], [], []
        for i, feature in enumerate(features, 1):
            anchor = f"{identifier}-f{i}"
            provenance = feature_evidence.get(feature)
            source = ""
            if self.modular:
                source = self.disclosure_evidence(i, feature, provenance, docs[0], identifier)
            elif provenance:
                source = f'<details class="report-atomic-provenance"><summary>{self.t("source")}</summary>'
                if provenance.get("source_quote"):
                    quote = provenance["source_quote"]
                    if quote not in docs[0]["request"].get("disclosure_text", ""):
                        raise ValueError(
                            "Feature evidence is absent from the disclosure"
                        )
                    source += f"<blockquote>{esc(quote)}</blockquote>"
                for label in provenance.get("image_labels", []):
                    image = next(
                        (
                            x
                            for x in docs[0]["request"].get("disclosure_images", [])
                            if x["label"] == label
                        ),
                        None,
                    )
                    if not image:
                        raise ValueError("Disclosure evidence image is missing")
                    source += f'<img src="{self.image(image["host_file"], image.get("ref"))}" alt="{esc(label)}" loading="lazy">'
                source += "</details>"
            catalog.append(
                f'<article id="{anchor}"><h4>F{i}</h4><p>{esc(feature)}</p>{source}</article>'
            )
            cells = []
            for document in docs:
                value = document["effective"].get(feature)
                if not value:
                    cells.append(
                        f'<td data-cell-state="uncompared">{self.t("uncompared")}</td>'
                    )
                    continue
                cell_id = f"{document['anchor']}-f{i}"
                links = "".join(
                    self.evidence(document, entry)
                    for entry in value.get("evidence", [])
                )
                cells.append(
                    f'<td data-cell-state="{esc(value["judgment"] or "material_gap")}"><div class="report-matrix-judgment">{self.badge(value["judgment"], value.get("disclosure_type"))}'
                    f'{self.cell_design(document, i, value)}'
                    f'<div class="report-map-facts"><p>{esc(self.reason_text(value["reason"]))}</p></div>{self.review_html(document, feature)}{links}'
                    f'<a class="report-map-open" href="#{cell_id}">{self.t("detail")} →</a></div></td>'
                )
            rows.append(
                f'<tr{self.row_scope(i)}><th scope="row"><a class="report-relation-code" href="#{anchor}">F{i}</a><p>{esc(feature)}</p></th>{"".join(cells)}</tr>'
            )
            print_rows.append((f'<th scope="row">F{i}<p>{esc(feature)}</p></th>', cells))
        for document in docs:
            result = document["result"]
            coverage = result.get("coverage") or {}
            date_label = self.t("no_date")
            boundary = self.draft.get("cover", {}).get("publication_date")
            if document["date"] and boundary:
                date_label = self.t(
                    "eligible_date"
                    if date.fromisoformat(document["date"])
                    <= date.fromisoformat(boundary)
                    else "outside_date"
                )
            text = (f'<p class="report-atomic-date">{self.part_word("application_date")}：'
                    f'{esc(document["application_date"] or self.t("no_date"))} · '
                    f'{self.part_word("publication_date_label")}：{esc(document["date"] or self.t("no_date"))} · {date_label}</p>')
            if result.get("arrangement") and document["arrangement_changes"]:
                text += (
                    f'<div class="report-arrangement-callout"><strong>{self.part_word("arrangement")}</strong>'
                    f'<p>{self.part_word("whole_pending")}</p></div>'
                )
            else:
                text += self.arrangement_callout(result.get("arrangement"))
            text += f'<div class="report-arrangement-callout"><strong>{self.t("coverage")}</strong><p>{esc(coverage.get("text_scope", ""))}</p>'
            text += f"<p>{esc(' · '.join(coverage.get('images_read', [])))}</p></div>"
            if coverage.get("limitations"):
                text += (
                    f'<details class="report-atomic-limitations" open><summary>{self.t("limitations")}</summary><ul>'
                    + "".join(f"<li>{esc(x)}</li>" for x in coverage["limitations"])
                    + "</ul></details>"
                )
            table_rows = []
            for i, feature in enumerate(features, 1):
                value = document["effective"].get(feature)
                if not value:
                    continue
                evidence = "".join(
                    self.evidence(document, entry)
                    for entry in value.get("evidence", [])
                )
                table_rows.append(
                    f'<tr id="{document["anchor"]}-f{i}"><th scope="row"><span class="report-feature-letter">F{i}</span><strong>{esc(feature)}</strong></th>'
                    f'<td><div class="report-check">{self.badge(value["judgment"], value.get("disclosure_type"))}<p class="report-fact">{esc(self.reason_text(value["reason"]))}</p>'
                    f'{self.review_html(document, feature, full=True)}{self.cell_design(document, i, value, details=True)}'
                    f'<details class="evidence-details"><summary>{self.t("evidence")}</summary>{evidence or self.t("no_evidence")}</details></div></td></tr>'
                )
            text += f'<div class="report-table-wrap report-document-table"><table><colgroup><col style="width:36%"><col style="width:64%"></colgroup><tbody>{"".join(table_rows)}</tbody></table></div>'
            text += f'<details class="report-atomic-fulltext"><summary>{self.t("fulltext")}</summary><pre>{esc(document["text"])}</pre></details>'
            details.append(
                f'<details class="report-doc-comparison" id="{document["anchor"]}"><summary><span class="report-document-code">{esc(document["label"])}</span>'
                f'<span class="report-document-summary"><strong>{esc(document["title"])}</strong><small>{esc(document["number"])} · {self.part_word("application_date")} {esc(document["application_date"] or self.t("no_date"))} · {self.part_word("publication_date_label")} {esc(document["date"] or self.t("no_date"))}</small></span>'
                f'<span class="report-document-open">{self.t("detail")}</span></summary><div class="report-doc-comparison-body">{text}</div></details>'
            )
        disclosure = docs[0]["request"].get("disclosure_text", "")
        disclosure_images = "".join(
            f'<figure><img src="{self.image(im["host_file"], im.get("ref"))}" alt="{esc(im["label"])}" loading="lazy"><figcaption>{esc(im["label"])}</figcaption></figure>'
            for im in docs[0]["request"].get("disclosure_images", [])
        )
        disclosure_detail = (
            f'<details class="report-atomic-fulltext"><summary>{self.t("original_disclosure")}</summary><pre>{esc(disclosure)}</pre>{disclosure_images}</details>'
        )
        feature_catalog = (
            f'<details class="report-reading-details report-atomic-catalog"><summary>{self.t("feature")} · {len(features)}</summary>{"".join(catalog)}</details>'
        )
        if self.modular:
            self.comparison_catalog = disclosure_detail + feature_catalog
        else:
            feature_catalog = disclosure_detail + feature_catalog
        headings = "".join(
            f'<th scope="col"><strong>{esc(d["label"])}</strong><small>{esc(d["number"])}</small><small>{esc(d["title"])}</small><small>{self.part_word("application_date")} {esc(d["application_date"] or self.t("no_date"))}</small><small>{self.part_word("publication_date_label")} {esc(d["date"] or self.t("no_date"))}</small></th>'
            for d in docs
        )
        # 每组最多两篇，重复技术特征和完整文献身份；不复制可交互详情或 ID。
        print_groups = []
        for start in range(0, len(docs) if len(docs) > 2 else 0, 2):
            group = docs[start:start + 2]
            headers = ''.join(f'<th scope="col">{esc(d["label"])} · {esc(d["number"])}<small>{esc(d["title"])}</small><small>{self.part_word("application_date")} {esc(d["application_date"] or self.t("no_date"))}</small><small>{self.part_word("publication_date_label")} {esc(d["date"] or self.t("no_date"))}</small></th>' for d in group)
            grouped_rows = ''.join('<tr>' + label + ''.join(cells[start:start + 2]).replace('loading="lazy"', 'loading="eager"').replace('data-cell-state=', 'data-print-cell-state=') + '</tr>' for label, cells in print_rows)
            print_groups.append(f'<div class="report-print-group"><h3>{self.t("matrix")} · {esc(" / ".join(d["label"] for d in group))}</h3><table><thead><tr><th scope="col">{self.t("feature")}</th>{headers}</tr></thead><tbody>{grouped_rows}</tbody></table></div>')
        return self.template(
            "matrix",
            catalog="" if self.modular else feature_catalog,
            legend_label=self.t("legend"),
            legend_rows=self.comparison_status_guide(),
            guide_hidden=" hidden" if self.modular else "",
            common_knowledge=self.t("common_knowledge"),
            common_knowledge_note=self.t("common_knowledge_note"),
            matrix_label=self.t("matrix"),
            minimum_width=max(650, 280 + 220 * len(docs)),
            counts=f"{len(features)} × {len(docs)}",
            feature_label=self.t("feature"),
            headings=headings,
            rows="".join(rows),
            print_matrix=('<div class="report-print-matrix">' + "".join(print_groups) + "</div>") if print_groups else "",
            document_details=('<div class="report-comparison-depot" hidden>' + "".join(details) + "</div>") if self.modular else "".join(details),
        )

    def search_data(self, spec):
        key = canonical(spec)
        if key not in self._search_cache:
            self._search_cache[key] = [
                {"tool": item["tool"], "request_file": item["request_file"],
                 **({"purpose": item["purpose"]} if item.get("purpose") else {}),
                 **({"appendix": item["appendix"]} if item.get("appendix") else {}),
                 "response_file": item["response_file"], "request": self.load(item["request_file"]),
                 "response": self.load(item["response_file"])} for item in spec
            ]
        return self._search_cache[key]

    def verdict_label(self, field, status):
        if self.modular and field == "inventiveness" and status == "not_assessed":
            return self.part_word("no_separate")
        return self.t(f"{field}_{status}") if status in {"supported", "not_supported"} else self.t(status)

    def finding_badge(self, field, finding):
        status = finding["status"]
        tone = {"supported": "satisfied", "not_supported": "different"}.get(status, "neutral")
        return f'<span class="report-state {tone}">{self.verdict_label(field, status)}</span>'

    def primary_headline(self, assessment):
        novelty, inventive = (assessment[field]["status"] for field in ("novelty", "inventiveness"))
        if novelty == "not_supported":
            return self.t("primary_not_novel_or_inventive" if inventive == "not_supported" else "primary_not_novel")
        if novelty != "supported":
            return self.t("novelty_pending")
        if inventive == "supported":
            return self.t("primary_both_supported")
        if inventive == "not_supported":
            return self.t("primary_novel_only")
        return self.t("primary_inventiveness_pending")

    def cover_text(self, text):
        """旧草稿的已知编号只在封面文字中展开；原始数据与链接目标不变。"""
        if not self.modular:
            return text
        names = {d["label"]: d["number"] for d in self.comparisons}
        names.update({f"F{i}": feature.rstrip("。.")
                      for i, feature in enumerate(self.plan["features"], 1)})
        return re.sub(r"(?<![A-Za-z0-9])[DF]\d+(?![A-Za-z0-9])",
                      lambda match: names.get(match[0], match[0]), text)

    def cover_reason_html(self, key, finding):
        """展示宿主写好的连贯说明；结构化论证保留在详细章节，不拼接字段清单。"""
        return self.markdown(finding["reason"], cover=True)

    def cover(self):
        title = esc(self.cover_text(self.draft["title"]))
        logo = (
            "data:image/png;base64,"
            + base64.b64encode((ASSETS / "eureka-logo.png").read_bytes()).decode()
        )
        brand = f'<div class="report-brand"><div><p>{self.t("caption")}</p><h1>{title}</h1></div><img src="{logo}" alt="Eureka by Patsnap" style="filter:brightness(0) invert(1)"></div>'
        cover = self.draft.get("cover")
        if not cover:
            return f'<header class="report-cover">{brand}</header>'
        assessment = cover["assessment"]
        values = [assessment["novelty"], assessment["inventiveness"]]
        for value in values:
            if (
                value["status"]
                not in {"supported", "not_supported", "pending", "not_assessed"}
                or not value.get("reason", "").strip()
            ):
                raise ValueError("Cover findings require an explicit status and reason")
        risks = [
            {
                "supported": "low",
                "not_supported": "high",
                "pending": "pending",
                "not_assessed": "not_assessed",
            }[v["status"]]
            for v in values
        ]
        overall = (
            "high"
            if "high" in risks
            else "pending"
            if any(x in {"pending", "not_assessed"} for x in risks)
            else "low"
        )
        tone, symbol = {"high": ("negative", "×"), "low": ("positive", "✓")}.get(
            overall, ("neutral", "i")
        )
        reasons = "".join(
            f'<section class="report-conclusion-reason"><h3 class="report-reason-heading"><span class="report-reason-number" aria-hidden="true">{index:02d}</span><span class="report-reason-name">{self.t(key)}</span>'
            f'{self.finding_badge(key, v)}</h3><div class="report-prose">{self.cover_reason_html(key, v)}</div></section>'
            for index, (key, v) in enumerate(zip(["novelty", "inventiveness"], values, strict=True), 1)
        )
        # 风险只传达已保存状态，不再成为章节弹卡的点击入口。
        cards = "".join(
            f'<div class="report-risk-card" data-report-risk="{level if level in {"low", "high"} else "unknown"}"><span class="report-risk-label">{self.t(key)}</span><strong>{self.verdict_label(key, level) if level == "not_assessed" else self.t(level)}</strong></div>'
            for key, level in [("overall_risk", overall), ("novelty", risks[0]), ("inventiveness", risks[1])]
        )
        count_docs = len(
            {d["number"] for d in self.comparisons if d["result"].get("comparisons")}
        )
        metrics = [
            ("⇄", self.t("documents"), count_docs),
            ("#", self.t("features"), len(self.feature_names)),
            ("✓", self.t("reviews"), self.review_count),
        ]
        if self.modular:
            metrics.insert(1, ("▦", self.t("scheme"), len(self.solutions)))
        stats = "".join(
            f'<div class="report-stat-card"><span class="report-stat-icon" aria-hidden="true">{icon}</span>'
            f'<p class="report-stat-label">{label}</p><p class="report-stat-value">{value}</p></div>'
            for icon, label, value in metrics
        )
        publication_date = cover.get("publication_date")
        if publication_date:
            date.fromisoformat(publication_date)
        date_label = (
            f"{esc(publication_date)}（{self.t('inclusive')}）"
            if publication_date
            else self.t("no_date")
        )
        notice = (
            f'<div class="report-delivery-notice">{esc(cover["notice"])}</div>'
            if cover.get("notice")
            else ""
        )
        headline = esc(self.primary_headline(assessment) if self.modular else cover["headline"])
        if headline == "具备新颖性，创造性支持不足":
            headline = '具备新颖性，<span class="report-headline-risk">创造性支持不足</span>'
        return self.template(
            "summary",
            brand=brand,
            notice=notice,
            scope_heading=self.t("evaluation_scope"),
            scope_description="",
            scheme_label=self.t("primary_scheme"),
            solution_name=esc(self.cover_text(cover["solution_name"])),
            solution_description=esc(self.cover_text(cover["solution_description"])),
            conclusion_label=self.t("primary_conclusion" if self.modular else "conclusion"),
            tone=tone,
            symbol=symbol,
            headline=headline,
            date_label=self.t("date") + "：" + date_label,
            reasons=reasons,
            recommendation_label=self.t("recommendation"),
            recommendation_body=self.markdown(cover["recommendation"], cover=True),
            cards=cards,
            risk_note=self.t("risk_note"),
            stats=stats,
            overview=self.solution_overview() if self.modular else (
                f'<div class="report-cover-body report-prose">{self.markdown(cover["overview"])}</div>'
                if cover.get("overview") else ""
            ),
        )

    def validate(self):
        if self.modular:
            self.comparison_data({"features_file": self.draft["report"]["feature_plan_file"],
                                  "documents": self.draft["report"]["documents"]}, "comparison")
            self.search_records = self.search_data(self.draft["report"].get("searches", []))
            self.validate_common_knowledge()
        else:
            for i, section in enumerate(self.draft.get("sections", []), 1):
                if section.get("comparison"):
                    self.comparison_data(section["comparison"], section.get("id", f"section-{i}"))
        self.validate_findings()
        self.validate_recommendation_presentation()
        self.validate_comparison_presentation()
        self.validate_appendix_presentation()

    def reader_script(self):
        """同一份原文阅读交互用于独立报告和 App，不引入工具状态。"""
        reader = (ASSETS / "report-patent-reader.js").read_text().replace("export function ", "function ")
        evidence = (ASSETS / "report-evidence-reader.js").read_text().replace("export function ", "function ")
        return reader + "\n" + evidence + "\n" + (ASSETS / "report-runtime.js").read_text()

    def reader_links(self, markup):
        """公开号直接打开阅读器；原逐格锚点保留，用于 05 和证据核对。"""
        for document in self.comparisons:
            markup = markup.replace(f'href="#{document["anchor"]}"', f'href="#patent-{document["anchor"]}"')
        return re.sub(r"[ \t]*[↗→](?=</a>)", "", markup)

    def render(self):
        if not self.presentation:
            raise ValueError("Data-only validation does not render the default template")
        if not self.draft.get("title", "").strip() or not self.draft.get("sections"):
            raise ValueError("Report needs a title and at least one section")
        if self.draft.get("purpose") == "novelty_report" and (
            not self.draft.get("cover")
            or not any(s.get("comparison") for s in self.draft["sections"])
        ):
            raise ValueError(
                "A novelty report needs findings and an evidence-backed comparison matrix"
            )
        self.validate()
        sections, nav = [], []
        # Render comparisons first so searches and the cover can reference actual CC progress.
        matrices = {
            i: self.comparison(s["comparison"], s.get("id", f"section-{i + 1}"))
            for i, s in enumerate(self.draft["sections"])
            if s.get("comparison")
        }
        readers = ''.join(self.patent_reader(d) for d in self.comparisons)
        if matrices:
            first = next(iter(matrices))
            matrices[first] += '<div class="report-patent-library" hidden>' + readers + '</div>'
        for i, section in enumerate(self.draft["sections"], 1):
            identifier = section.get("id", f"section-{i}")
            if not re.fullmatch(r"[a-zA-Z][a-zA-Z0-9_-]*", identifier):
                raise ValueError("Invalid section anchor")
            heading = esc(section["heading"])
            body = "" if self.modular and section["part_type"] == "comparison" else self.markdown(section.get("content", ""))
            if self.modular and section["part_type"] == "search":
                appendices = self.render_appendices(body)
                section_html = f'<div id="search" data-report-part="search" role="group" aria-label="{heading}">{appendices}</div>'
                sections.append(section_html)
                self.fragments[identifier] = section_html
                nav.extend((anchor, self.t(label)) for anchor, label in (("search-strategy", "search_appendix"), ("search-results", "documents_appendix")))
                continue
            if self.modular:
                body += self.render_part(section["part_type"])
            matrix = matrices.get(i - 1, "")
            if self.modular and matrix:
                matrix = self.comparison_intro() + self.solution_nav() + matrix
            body += matrix
            if self.modular and section["part_type"] == "comparison":
                body += self.comparison_after(section.get("content", ""))
                if self.library:
                    body += f'<div class="report-evidence-library report-comparison-depot" id="report-evidence" hidden>{"".join(self.library.values())}</div>'
            for detail in section.get("details", []):
                body += (
                    f'<details class="report-reading-details report-atomic-narrative" {"open" if detail.get("open") else ""}><summary>{esc(detail["heading"])}</summary>'
                    + self.markdown(detail["content"])
                    + "</details>"
                )
            section_html = self.template(
                "section",
                anchor=identifier,
                part=f' data-report-part="{section.get("part_type", "custom")}"',
                number=f"{i:02d}",
                heading=heading,
                body=body,
            )
            if self.modular and section["part_type"] in {"novelty", "inventiveness"}:
                note = self.analysis_word(section["part_type"] + "_note")
                section_html = section_html.replace("</h2></div>", f'</h2><p class="report-analysis-chapter-note">{esc(note)}</p></div>', 1)
            if self.modular and section["part_type"] == "comparison":
                note = f'{len(self.plan["features"])} {self.t("feature")} · {len(self.comparisons)} {self.t("documents")}'
                section_html = section_html.replace("</h2></div>", f'</h2><p class="report-comparison-meta">{esc(note)}</p></div>', 1)
            if self.modular and section["part_type"] == "recommendations":
                note = self.draft["report"].get("recommendation_presentation", {}).get("chapter_note")
                if note:
                    section_html = section_html.replace("</h2></div>", f'</h2><p class="report-advice-chapter-note">{esc(note)}</p></div>', 1)
            sections.append(section_html)
            self.fragments[identifier] = section_html
            nav.append((identifier, heading))
        if self.library and not self.modular:
            sections.append(
                f'<section class="report-section" id="report-evidence" data-report-section="evidence"><details class="report-evidence-library"><summary>{self.t("evidence")} · {len(self.library)}</summary>{"".join(self.library.values())}</details></section>'
            )
            nav.append(("report-evidence", self.t("evidence")))
        if self.draft.get("cover"):
            nav.insert(0, ("report-cover", self.t("conclusion")))
        options = "".join(
            f'<option value="{esc(identifier)}">{heading}</option>'
            for identifier, heading in nav
        )
        toolbar = f'<nav class="standalone-toolbar" data-report-page-nav aria-label="{self.t("contents")}"><label>{self.t("contents")} <select data-report-chapter-select>{options}</select></label><button data-report-expand-all type="button" aria-pressed="false">{self.t("expand")}</button></nav>'
        script = self.reader_script()
        css = (
            (ASSETS / "report.css").read_text()
            + "\n"
            + (ASSETS / "report-host.css").read_text()
            + (ASSETS / "report-analysis.css").read_text()
            + (ASSETS / "report-recommendations.css").read_text()
            + (ASSETS / "report-patent-reader.css").read_text()
            + ((ASSETS / "report-comparison.css").read_text() if self.modular else "")
            + (ASSETS / "report-evidence-reader.css").read_text()
            + ((ASSETS / "report-appendices.css").read_text() if self.modular else "")
        )
        css += (ASSETS / "report-print.css").read_text()
        # 导出样式去掉注释与行首空白，避免把源文件格式成本带入每份报告。
        css = compact_css(css)
        digest = base64.b64encode(hashlib.sha256(script.encode()).digest()).decode()
        cover = self.cover()
        self.fragments["summary"] = cover
        self.fragments["controls"] = self.solution_nav() if self.modular else ""
        images = '<script type="application/json" id="report-image-assets">' + json.dumps(self.image_data) + "</script>"
        active = f' data-active-scheme="{self.solution_keys[self.primary]}"' if self.modular else ""
        result = f'<!doctype html><html lang="{self.language}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src \'none\'; img-src data: blob:; style-src \'unsafe-inline\'; script-src \'sha256-{digest}\'; base-uri \'none\'"><title>{esc(self.draft["title"])}</title><style>{css}</style></head><body class="report-standalone">{toolbar}<main class="novelty-report" data-report-reading="complete"{active}>{cover}{"".join(sections)}</main>{images}<script>{script}</script></body></html>'
        self.fragments = {key: self.reader_links(continuous_reading(value)) for key, value in self.fragments.items()}
        result = self.reader_links(continuous_reading(result))
        result = re.sub(r'src="report-image:([a-f0-9]{64})"', r'data-report-image="\1"', result)
        check = LinkCheck()
        check.feed(result)
        if len(check.ids) != len(set(check.ids)) or not set(check.links) <= set(
            check.ids
        ):
            raise ValueError("Duplicate or unresolved report anchor")
        return result


def render(draft, base):
    return Report(draft, base).render()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    p.add_argument("--output")
    p.add_argument(
        "--parts-dir", help="Export filled HTML parts and data for harness templates"
    )
    p.add_argument(
        "--data-output",
        help="Export validated, binary-free data for a harness-owned template",
    )
    p.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate data without writing the default report",
    )
    args = p.parse_args()
    if not args.output and not args.validate_only:
        p.error("--output is required unless --validate-only is used")
    source = Path(args.input).resolve()
    if not source.is_file():
        p.error(f"--input must be an existing JSON file: {source}")
    try:
        draft = json.loads(source.read_text(encoding="utf-8"))
    except OSError as exc:
        p.error(f"cannot read --input {source}: {exc}")
    except json.JSONDecodeError as exc:
        p.error(f"--input is not valid JSON: {source}: {exc}")
    if "report" not in draft:
        p.error(
            "Report data requires the report object and feature plan; see references/report-data.md"
        )
    report = Report(draft, source.parent, presentation=not args.validate_only)
    if args.validate_only:
        if args.parts_dir:
            p.error("--parts-dir requires rendering the default report")
        report.validate()
        result = None
    else:
        result = report.render()
    if args.parts_dir:
        report.export_parts(Path(args.parts_dir).resolve())
    if args.data_output:
        report.export_data(Path(args.data_output).resolve())
    record = {"validated": True}
    if result is not None:
        record["sha256"] = hashlib.sha256(result.encode()).hexdigest()
    if not args.validate_only:
        target = Path(args.output).resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(result)
        record.update(file=str(target), mime_type="text/html")
    if args.data_output:
        record["data_file"] = str(Path(args.data_output).resolve())
    print(json.dumps(record, ensure_ascii=False))


if __name__ == "__main__":
    main()
