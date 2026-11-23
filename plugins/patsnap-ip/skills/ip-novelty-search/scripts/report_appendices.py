"""附录的固定阅读版式；只读取宿主回执，不调用模型或保存工具状态。"""

from html import escape
import json


def esc(value):
    """纯文本进入 HTML 前统一转义，包括原始请求和宿主摘要。"""
    return escape(str(value))


# 与默认报告相同的五种语言；业务摘要由宿主按报告语言提供。
WORDS = {
    'keyword': ('关键词检索', 'Keyword search', '關鍵詞檢索', 'キーワード検索', '키워드 검색'),
    'filter': ('字段过滤', 'Metadata filters', '欄位篩選', 'フィールド絞り込み', '메타데이터 필터'),
    'boolean': ('布尔检索', 'Boolean search', '布林檢索', '論理式検索', '불리언 검색'),
    'semantic': ('语义检索', 'Semantic search', '語義檢索', '意味検索', '의미 검색'),
    'citations': ('引证追踪', 'Citation tracking', '引證追蹤', '引用追跡', '인용 추적'),
    'publication': ('公开号核实', 'Publication lookup', '公開號核實', '公開番号確認', '공개번호 확인'),
    'returned_items': ('条返回', 'returned', '筆返回', '件取得', '건 반환'),
    'strategy': ('检索策略与记录', 'Search strategy and records', '檢索策略與記錄', '検索戦略と記録', '검색 전략 및 기록'),
    'documents': ('对比文献清单', 'Compared documents', '對比文獻清單', '比較文献一覧', '비교 문헌 목록'),
    'strategy_note': ('检索方向、输入与实际返回结果', 'Search routes, inputs and returned results', '檢索方向、輸入與實際返回結果', '検索方針・入力・取得結果', '검색 방향, 입력 및 반환 결과'),
    'documents_note': ('收录实际进入逐项对比的文献，编号与技术关系对照表一致', 'Documents used in feature comparison; identifiers match the matrix', '收錄實際進入逐項對比的文獻，編號與技術關係對照表一致', '特徴比較に使用した文献。番号は対照表と共通です', '기술 요소 비교에 사용된 문헌이며 번호는 대조표와 동일합니다'),
    'records': ('已保存检索记录', 'Saved search records', '已保存檢索記錄', '保存済み検索記録', '저장된 검색 기록'),
    'returned': ('累计返回条目', 'Returned entries', '累計返回條目', '取得件数の合計', '누적 반환 항목'),
    'unique': ('按公开号去重候选', 'Unique publication numbers', '按公開號去重候選', '公開番号で重複除外した候補', '공개번호 기준 중복 제거 후보'),
    'compared': ('正式对比文献', 'Compared documents', '正式對比文獻', '比較対象文献', '비교 문헌'),
    'boundary': ('公开日上限', 'Publication date boundary', '公開日上限', '公開日の上限', '공개일 상한'),
    'inclusive': ('（含当天）', '(inclusive)', '（含當天）', '（当日を含む）', '(당일 포함)'),
    'ledger': ('逐次检索记录', 'Search records', '逐次檢索記錄', '検索ごとの記録', '개별 검색 기록'),
    'order': ('保留原记录顺序', 'In original record order', '保留原記錄順序', '元の記録順', '원래 기록 순서'),
    'record_link': ('查看完整检索记录', 'View full search record', '查看完整檢索記錄', '検索記録を表示', '전체 검색 기록 보기'),
    'conditions': ('完整检索条件', 'Full search conditions', '完整檢索條件', '検索条件の全文', '전체 검색 조건'),
    'limit': ('返回上限', 'Return limit', '返回上限', '取得上限', '반환 상한'),
    'service_total': ('服务返回总数', 'Service-reported total', '服務返回總數', 'サービス返却総数', '서비스 반환 총수'),
    'accounting': ('累计返回包含重复公开号；去重候选不等于已完成全文对比的文献。', 'Returned entries include duplicate publications; unique candidates are not the same as fully compared documents.', '累計返回包含重複公開號；去重候選不等於已完成全文對比的文獻。', '取得件数には重複を含みます。重複除外した候補数と全文比較済み文献数は異なります。', '누적 반환에는 중복 공개번호가 포함됩니다. 중복 제거 후보 수와 전문 비교 문헌 수는 다릅니다.'),
    'patent_hint': ('点击公开号，查看专利原文与附图', 'Select a publication number to read the patent and figures', '點擊公開號，查看專利原文與附圖', '公開番号から原文と図面を表示', '공개번호를 선택하여 원문과 도면 보기'),
    'identity': ('文献 / 申请日 / 公开日', 'Document / filing / publication dates', '文獻 / 申請日 / 公開日', '文献 / 出願日 / 公開日', '문헌 / 출원일 / 공개일'),
    'related': ('相关技术内容', 'Relevant technical content', '相關技術內容', '関連する技術内容', '관련 기술 내용'),
    'materials': ('已核对材料', 'Materials checked', '已核對材料', '確認した資料', '확인한 자료'),
    'compared_status': ('已完成对比', 'Comparison completed', '已完成對比', '比較完了', '비교 완료'),
    'record': ('核对记录', 'Comparison record', '核對記錄', '確認記録', '확인 기록'),
    'record_view': ('查看核对记录', 'View comparison record', '查看核對記錄', '確認記録を表示', '확인 기록 보기'),
    'unknown_scope': ('未记录材料范围', 'Material scope not recorded', '未記錄材料範圍', '資料範囲の記録なし', '자료 범위 미기록'),
    'unknown_related': ('查看正文中的逐项对照', 'See feature comparisons in the report', '查看正文中的逐項對照', '本文の特徴比較を参照', '본문의 항목별 대조 참조'),
    'supplementary': ('补读资料', 'Supplementary reading', '補讀資料', '補足資料', '추가 자료'),
    'supplementary_note': ('用于局部核实与背景参考，具体用途见记录。', 'Used for targeted checks and background; see the record for their role.', '用於局部核實與背景參考，具體用途見記錄。', '個別の確認と背景資料。用途は記録を参照', '개별 확인 및 배경 참고 자료. 용도는 기록 참조'),
    'supplementary_view': ('查看资料与用途', 'View sources and their role', '查看資料與用途', '資料と用途を表示', '자료 및 용도 보기'),
    'scope': ('评价范围', 'Evaluation scope', '評價範圍', '評価範囲', '평가 범위'),
    'scope_view': ('查看范围与未决事项', 'View scope and open questions', '查看範圍與未決事項', '範囲と未解決事項を表示', '범위 및 미해결 사항 보기'),
    'strategy_record': ('检索说明与原始记录', 'Search narrative and original records', '檢索說明與原始記錄', '検索説明と元の記録', '검색 설명 및 원본 기록'),
    'strategy_view': ('查看完整检索说明', 'View full search narrative', '查看完整檢索說明', '検索説明の全文を表示', '전체 검색 설명 보기'),
    'boolean_note': ('通过关键词组合查找相关专利。', 'Find patents with keyword combinations.', '透過關鍵詞組合查找相關專利。', 'キーワードの組み合わせで特許を検索', '키워드 조합으로 관련 특허 검색'),
    'semantic_note': ('按输入的技术描述查找相关专利。', 'Find patents using the supplied technical description.', '按輸入的技術描述查找相關專利。', '入力した技術記述で特許を検索', '입력한 기술 설명으로 관련 특허 검색'),
    'citations_note': ('从已知文献追踪引证关系。', 'Follow citation relationships from known publications.', '從已知文獻追蹤引證關係。', '既知の文献から引用関係を追跡', '알려진 문헌의 인용 관계 추적'),
}

class AppendicesPresentation:
    def appendix_word(self, key):
        """附录固定文案跟随报告语言。"""
        return WORDS[key][self.LANGUAGES.index(self.language)]

    def validate_appendix_presentation(self):
        """只允许摘要字段；状态、日期和数量必须来自原始回执。"""
        if not self.modular:
            return
        report = self.draft['report']
        view = report.get('appendix_presentation', {})
        if not isinstance(view, dict):
            raise ValueError('Appendix presentation must be an object')
        self.display_text_fields({k: v for k, v in view.items() if k != 'supplementary'},
                                 {'introduction', 'search_note', 'scope_summary', 'supplementary_summary'})
        supplements = view.get('supplementary', [])
        if not isinstance(supplements, list):
            raise ValueError('Appendix supplementary must be a list')
        for item in supplements:
            self.display_text_fields(item, {'title', 'description'}, {'title', 'description'})
        for item in report.get('searches', []):
            self.display_text_fields(item.get('appendix', {}), {'title', 'summary'})
        for item in report['documents']:
            value = item.get('appendix', {})
            if not isinstance(value, dict):
                raise ValueError('Appendix document presentation must be an object')
            self.display_text_fields({k: v for k, v in value.items() if k != 'materials'}, {'title', 'summary'})
            materials = value.get('materials', [])
            if not isinstance(materials, list) or any(not isinstance(x, str) or not x.strip() for x in materials):
                raise ValueError('Appendix materials must be nonempty text entries')

    def appendix_record(self, anchor, title, body):
        """原始记录进入已有弹窗通道，保留标题供两个阅读端取用。"""
        return f'<article id="{anchor}" data-appendix-record><h3>{esc(title)}</h3>{body}</article>'

    def appendix_search_ledger(self, records):
        """不截掉原始输入；主列表摘要与完整回执分别呈现。"""
        rows, depot, candidates, returned = [], [], set(), 0
        for index, item in enumerate(records, 1):
            request, result = item['request'], item['response']
            normalized = self.search_result(result)
            patents = normalized['patents']
            returned += len(patents)
            candidates.update(p['publication_number'] for p in patents if p.get('publication_number'))
            query = self.search_query(request)
            route_keys = self.search_routes(request)
            route = ' + '.join(self.appendix_word(key) for key in route_keys)
            failed = normalized['failed']
            state = 'failed' if failed else 'partial' if normalized['partial'] else 'complete'
            status = self.t('search_' + state)
            view = item.get('appendix', {})
            title = view.get('title') or item.get('purpose') or request.get('purpose') or route
            anchor = f'appendix-query-{index}'
            actual, hit_count = result.get('query'), normalized['total']
            short_route = route
            meta = f'{route} · {status} · {self.t("returned")} {len(patents)}'
            body = f'<p class="appendix-record-meta">{esc(meta)}</p>'
            if item.get('purpose') or request.get('purpose'):
                body += f'<h4>{self.part_word("search_purpose")}</h4><p>{esc(item.get("purpose") or request["purpose"])}</p>'
            body += f'<h4>{self.t("query")}</h4><pre>{esc(query)}</pre>'
            if actual and actual != query:
                body += f'<h4>{self.t("search_actual")}</h4><pre>{esc(actual)}</pre>'
            # 完整条件与服务回执保留在记录弹窗中，列表只展示摘要。
            conditions = request
            body += f'<h4>{self.appendix_word("conditions")}</h4><pre>{esc(json.dumps(conditions, ensure_ascii=False, indent=2))}</pre>'
            if hit_count is not None:
                body += f'<p>{self.appendix_word("service_total")} {esc(hit_count)}</p>'
            body += f'<pre>{esc(json.dumps(result, ensure_ascii=False, indent=2))}</pre>'
            depot.append(self.appendix_record(anchor, f'S{index:02d} · {title}', body))
            if view.get('summary'):
                preview = f'<p class="appendix-query-summary">{esc(view["summary"])}</p>'
            else:
                preview = f'<pre class="appendix-query-input">{esc(query[:300] + "…" if len(query) > 300 else query)}</pre>'
            secondary = (f'{self.t("hits")} {esc(hit_count)}' if hit_count is not None else '')
            rows.append(f'<article class="appendix-search-row" data-search-state="{state}"><div class="appendix-search-index">'
                        f'<span>S{index:02d}</span><p>{esc(short_route)}</p></div><div class="appendix-search-content"><h3>{esc(title)}</h3>{preview}'
                        f'<a href="#{anchor}" class="appendix-record-link">{self.appendix_word("record_link")}</a></div>'
                        f'<div class="appendix-search-count"><span class="appendix-status" data-status="{state}">{status}</span>'
                        f'<p><strong>{len(patents)}</strong> {self.appendix_word("returned_items")}</p><small>{secondary}</small></div></article>')
        return ''.join(rows), depot, returned, len(candidates)

    def appendix_documents(self, documents):
        """每篇只展示身份、相关内容和核对材料，完整范围与缺口保留在弹窗。"""
        rows, depot = [], []
        narratives = {d['publication_number']: d for d in self.findings[self.primary]['novelty'].get('presentation', {}).get('documents', [])}
        for doc in documents:
            view, coverage = doc['spec'].get('appendix', {}), doc['result'].get('coverage') or {}
            narrative = narratives.get(doc['number'], {})
            title = view.get('title') or narrative.get('title') or doc['title']
            summary = view.get('summary') or doc['spec'].get('reason') or narrative.get('known') or self.appendix_word('unknown_related')
            state = ('incomplete' if not doc['result'].get('comparisons') else
                     'complete' if doc['result'].get('status') == 'complete' else 'partial')
            status = self.appendix_word('compared_status') if state == 'complete' else self.t('cc_incomplete') if state == 'incomplete' else self.part_word('partial')
            anchor = 'appendix-material-' + doc['anchor']
            date_text = (f'{self.part_word("application_date")}：{doc["application_date"] or self.t("no_date")} · '
                         f'{self.part_word("publication_date_label")}：{doc["date"] or self.t("no_date")}')
            body = f'<p class="appendix-record-meta">{esc(doc["title"])} · {esc(date_text)}</p>'
            if doc['spec'].get('reason'):
                body += f'<h4>{self.t("cc_scope")}</h4><p>{esc(doc["spec"]["reason"])}</p>'
            body += f'<h4>{self.t("coverage")}</h4><p>{esc(coverage.get("text_scope") or self.appendix_word("unknown_scope"))}</p>'
            if coverage.get('images_read'):
                body += '<ul>' + ''.join(f'<li>{esc(image)}</li>' for image in coverage['images_read']) + '</ul>'
            if coverage.get('limitations'):
                body += f'<h4>{self.t("limitations")}</h4><ul>' + ''.join(f'<li>{esc(x)}</li>' for x in coverage['limitations']) + '</ul>'
            body += f'<p><a href="#patent-{doc["anchor"]}">{self.appendix_word("patent_hint")}</a></p>'
            depot.append(self.appendix_record(anchor, doc['number'] + ' · ' + self.appendix_word('record'), body))
            materials = view.get('materials') or [coverage.get('text_scope') or self.appendix_word('unknown_scope')]
            original = f'<p class="appendix-original-title">{esc(doc["title"])}</p>' if title != doc['title'] else ''
            rows.append(f'<article class="appendix-document-row" data-comparison-state="{state}"><span class="appendix-document-index">{esc(doc["label"])}</span>'
                        f'<div class="appendix-document-identity"><h3>{esc(title)}</h3><a class="appendix-publication" href="#patent-{doc["anchor"]}">{esc(doc["number"])}</a>'
                        f'{original}<p class="appendix-date">{esc(date_text)}</p></div>'
                        f'<div class="appendix-document-relevance"><p>{esc(summary)}</p></div><div class="appendix-document-coverage">'
                        f'<span class="appendix-status" data-status="{state}">{status}</span><p>{"<br>".join(esc(x) for x in materials)}</p>'
                        f'<a href="#{anchor}">{self.appendix_word("record_view")}</a></div></article>')
        return ''.join(rows), depot

    def appendix_section(self, anchor, letter, title, note, body):
        """保留章节锚点与标题结构，兼容目录、阅读位置及导出。"""
        return (f'<section id="{anchor}" class="report-section agentic-report-section appendix-redesign" data-report-section="{anchor}">'
                f'<div class="report-section-heading"><span class="appendix-letter">{letter}</span>'
                f'<div><h2>{esc(title)}</h2><p>{esc(note)}</p></div></div>{body}</section>')

    def render_appendices(self, narrative=''):
        """数据驱动的两个附录；不把某个案例的数量或材料写入模板。"""
        report = self.draft['report']
        view = report.get('appendix_presentation', {})
        records = self.search_data(report.get('searches', []))
        rows, depot, returned, unique = self.appendix_search_ledger(records)
        documents = list({d['number']: d for d in self.comparisons}.values())
        compared = [d for d in documents if d['result'].get('comparisons')]
        incomplete = [d for d in documents if not d['result'].get('comparisons')]
        counts = [(len(records), 'records'), (returned, 'returned'), (unique, 'unique'), (len(compared), 'compared')]
        strategy = '<div class="appendix-statistics">' + ''.join(f'<div><strong>{n}</strong><span>{self.appendix_word(key)}</span></div>' for n, key in counts) + '</div>'
        boundary = report.get('publication_date')
        note = f'<p>{esc(view["search_note"])}</p>' if view.get('search_note') else ''
        strategy += (f'<div class="appendix-boundary"><p><span>{self.appendix_word("boundary")}</span>'
                     f'{esc(boundary or self.t("no_date"))} {self.appendix_word("inclusive") if boundary else ""}</p>{note}</div>')
        route_keys = list(dict.fromkeys(key for item in records for key in self.search_routes(item['request'])))
        routes = ''.join(f'<div><h3>{self.appendix_word(key)}</h3></div>' for key in route_keys)
        if routes:
            strategy += f'<div class="appendix-route">{routes}</div>'
        strategy += f'<div class="appendix-ledger-heading"><h3>{self.appendix_word("ledger")}</h3><span>{self.appendix_word("order")}</span></div>'
        strategy += rows or f'<p>{self.t("search_missing")}</p>'
        strategy += f'<p class="appendix-accounting">{self.appendix_word("accounting")}</p>'
        original = narrative + self.markdown(report.get('search_summary', ''))
        if original:
            depot.append(self.appendix_record('appendix-search-narrative', self.appendix_word('strategy_record'), original))
            strategy += f'<a href="#appendix-search-narrative">{self.appendix_word("strategy_view")}</a>'
        listing = f'<div class="appendix-document-summary"><p><strong>{len(compared)}</strong> {self.appendix_word("compared")}</p><span>{self.appendix_word("patent_hint")}</span></div>'
        listing += '<div class="appendix-document-columns"><span></span>' + ''.join(f'<span>{self.appendix_word(key)}</span>' for key in ('identity', 'related', 'materials')) + '</div>'
        for group in (compared, incomplete):
            if group and group is incomplete:
                listing += f'<h3 class="appendix-incomplete">{self.t("cc_incomplete")}</h3>'
            content, details = self.appendix_documents(group)
            listing += content
            depot.extend(details)
        for failure in self.failed_comparisons:
            listing += (f'<article class="appendix-document-row" data-comparison-state="failed"><h3>{esc(failure["identity"])}</h3>'
                        f'<span class="appendix-status" data-status="failed">{self.t("cc_incomplete")}</span>'
                        f'<p>{esc(failure["error"])}</p></article>')
        tail = ''
        supplements = view.get('supplementary', [])
        if supplements:
            content = ''.join(f'<h4>{esc(x["title"])}</h4><p>{esc(x["description"])}</p>' for x in supplements)
            depot.append(self.appendix_record('appendix-supplementary', self.appendix_word('supplementary'), content))
            tail += (f'<div><h3>{self.appendix_word("supplementary")}</h3><p>{esc(view.get("supplementary_summary") or self.appendix_word("supplementary_note"))}</p>'
                     f'<a href="#appendix-supplementary">{self.appendix_word("supplementary_view")}</a></div>')
        depot.append(self.appendix_record('appendix-scope', self.appendix_word('scope'), self.search_limitations()))
        tail += (f'<div><h3>{self.appendix_word("scope")}</h3><p>{esc(view.get("scope_summary") or " / ".join(s["name"] for s in self.solutions))}</p>'
                 f'<a href="#appendix-scope">{self.appendix_word("scope_view")}</a></div>')
        listing += f'<div class="appendix-tail">{tail}</div>'
        return (self.appendix_section('search-strategy', 'A', self.appendix_word('strategy'), view.get('introduction') or self.appendix_word('strategy_note'), strategy)
                + self.appendix_section('search-results', 'B', self.appendix_word('documents'), self.appendix_word('documents_note'), listing)
                + '<div class="report-comparison-depot" hidden>' + ''.join(depot) + '</div>')
