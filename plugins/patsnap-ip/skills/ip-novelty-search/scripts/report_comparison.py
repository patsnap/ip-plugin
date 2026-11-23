"""05 的展示层：保留逐格事实，集中展示补充依据、真实复核和可选交底。"""
from html import escape as esc
import re

WORDS = {
    'public': ('公开（含必要隐含）', 'Disclosed (including necessary implication)', '公開（含必要隱含）', '開示（必然的な黙示を含む）', '공개 (필연적 묵시 포함)'),
    'headline': ('逐项看公开情况，', 'Compare each feature, ', '逐項看公開情況，', '特徴ごとの開示を比較し、', '특징별 공개 내용을 비교하고, '),
    'emphasis': ('逐格核对依据', 'verify each source', '逐格核對依據', '根拠を確認', '근거를 확인'),
    'intro': ('点击格内的段落、附图或详情，可查看原文上下文和判断理由。', 'Open a passage, figure or cell detail to read the source in context and the reasoning.', '點擊格內的段落、附圖或詳情，可查看原文上下文和判斷理由。', '段落・図面・詳細から原文の文脈と判断理由を確認できます。', '단락, 도면 또는 셀 상세에서 원문의 문맥과 판단 이유를 확인할 수 있습니다.'),
    'supplement': ('补充依据', 'Supporting sources', '補充依據', '補足資料', '보충 근거'),
    'supplement_note': ('公知资料说明支持范围；常规设计理由保留在对应格。', 'Sources specify their scope; routine-design reasoning remains in each cell.', '公知資料說明支持範圍；常規設計理由保留在對應格。', '資料の適用範囲を示します。通常設計の理由は各セルに記載。', '자료의 적용 범위를 명시하며 통상 설계 이유는 해당 셀에 유지합니다.'),
    'reviews': ('关键复核记录', 'Review records', '關鍵複核記錄', '再確認の記録', '재검토 기록'),
    'reviews_note': ('展示实际复核结果，完整理由与原文保留在对应格。', 'Actual review outcomes; full reasoning and sources remain in the linked cells.', '展示實際複核結果，完整理由與原文保留在對應格。', '実際の再確認結果。理由全文と原文は対応するセルに保存。', '실제 재검토 결과입니다. 전체 이유와 원문은 해당 셀에 유지합니다.'),
    'optional': ('未纳入评价的内容', 'Outside the evaluated scope', '未納入評價的內容', '評価対象外の内容', '평가에 포함하지 않은 내용'),
    'optional_note': ('交底中的可选细化，未作为本次方案的必要条件。', 'Optional disclosure details, not required conditions of the evaluated solutions.', '交底中的可選細化，未作為本次方案的必要條件。', '開示の任意の詳細であり、評価案の必須条件には含みません。', '공개 자료의 선택적 세부 사항으로 평가안의 필수 조건에 포함하지 않습니다.'),
    'optional_item': ('可选细化', 'Optional detail', '可選細化', '任意の詳細', '선택적 세부 사항'),
    'source': ('原始交底', 'Original disclosure', '原始交底', '元の開示', '원본 자료'),
    'cell': ('复核理由与原文', 'Review reasoning and sources', '複核理由與原文', '再確認の理由と原文', '재검토 이유와 원문'),
    'related': ('对应格', 'Related cell', '對應格', '対応するセル', '관련 셀'),
    'end': ('完整事实、上下文和附图均保留在表格对应的证据入口中', 'Full facts, context and figures are available through the table’s evidence links.', '完整事實、上下文和附圖均保留在表格對應的證據入口中', '事実・文脈・図面は表の根拠リンクから確認できます。', '전체 사실, 문맥 및 도면은 표의 근거 링크에서 확인할 수 있습니다.'),
}


class ComparisonPresentation:
    def comparison_word(self, key):
        """固定界面文案随报告语言变化。"""
        return WORDS[key][self.LANGUAGES.index(self.language)]

    def validate_comparison_presentation(self):
        """展示摘要只能指向已存在的复核或可选段落，不能新增判断。"""
        if not self.modular:
            return
        value = self.draft['report'].get('comparison_presentation', {})
        if not isinstance(value, dict) or set(value) - {'reviews', 'optional'}:
            raise ValueError('comparison_presentation: invalid fields')
        for kind, rows in value.items():
            if not isinstance(rows, list):
                raise ValueError('comparison_presentation: list required')
            seen = set()
            for row in rows:
                fields = {'publication_number', 'feature_number', 'summary'} if kind == 'reviews' else {'coverage_index', 'title', 'summary'}
                if not isinstance(row, dict) or set(row) != fields or any(not isinstance(row.get(k), str) or not row[k].strip() for k in fields - {'coverage_index', 'feature_number'}):
                    raise ValueError('comparison_presentation: invalid entry')
                if kind == 'reviews':
                    n = row['feature_number']
                    doc = next((d for d in self.comparisons if d['number'] == row['publication_number']), None)
                    if type(n) is not int or not 1 <= n <= len(self.plan['features']) or not doc or self.plan['features'][n - 1] not in doc['reviews']:
                        raise ValueError('comparison_presentation: review does not exist')
                    key = row['publication_number'], n
                else:
                    key = row['coverage_index']
                    coverage = self.plan.get('coverage', [])
                    if type(key) is not int or not 0 <= key < len(coverage) or coverage[key]['treatment'] != 'optional':
                        raise ValueError('comparison_presentation: optional passage does not exist')
                if key in seen:
                    raise ValueError('comparison_presentation: duplicate entry')
                seen.add(key)

    def comparison_block(self, key, content):
        """只有真实条目才展示分区；条目数量不影响布局。"""
        if not content:
            return ''
        return (f'<section class="report-comparison-block"><header class="report-comparison-label"><h3>{self.comparison_word(key)}</h3>'
                f'<p>{self.comparison_word(key + "_note")}</p></header><div>{content}</div></section>')

    def comparison_intro(self):
        """紧凑图例与本节方案选择，共用现有选择事件。"""
        keys = ('disclosed', 'not_disclosed', 'not_mentioned', 'material_gap')
        labels = {key: self.badge(key) for key in keys}
        labels['disclosed'] = f'<span class="report-state satisfied">{self.comparison_word("public")}</span>'
        legend = ''.join(f'<span class="report-comparison-key {key}">{labels[key]}</span>' for key in keys)
        return (f'<div class="report-comparison-intro"><h3>{self.comparison_word("headline")}<span>{self.comparison_word("emphasis")}</span></h3>'
                f'<p>{self.comparison_word("intro")}</p></div>'
                f'<div class="report-comparison-legend">{legend}<span class="report-comparison-secondary">{self.t("routine_tag")} · {self.t("common_knowledge_tag")}</span></div>')

    def comparison_after(self, narrative):
        """已有资料与原始记录均保留，长原文只进入引用阅读器。"""
        presentation = self.draft['report'].get('comparison_presentation', {})
        supplements = self.markdown(narrative) if narrative.strip() else ''
        # 公知依据去重展示；每个具体适用格仍独立可核对。
        sources = {}
        for (publication, n), record in self.common_knowledge.items():
            source = record['source']
            key = source['file'], source['title']
            sources.setdefault(key, []).append((publication, n, record))
        for (_, title), entries in sources.items():
            links, anchors = [], []
            for publication, n, record in entries:
                doc = next(d for d in self.comparisons if d['number'] == publication)
                anchors.append(f'href="#{doc["anchor"]}-f{n}"')
                links.append(f'<a href="#{doc["anchor"]}-f{n}">{esc(publication)} · {esc(self.feature_title(n))}</a>')
            if all(anchor in supplements for anchor in anchors):
                continue
            supplements += (f'<article class="report-comparison-item"><h4>{esc(title)}</h4><p>{esc(entries[0][2]["source"]["date"])}</p>'
                            f'<div class="report-comparison-links">{"".join(links)}</div></article>')
        supplements = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" data-report-website target="_blank" rel="noopener noreferrer"', supplements)
        document_titles = {d['publication_number']: d.get('title') for d in self.findings[self.primary]['novelty'].get('presentation', {}).get('documents', [])}
        review_summaries = {(r['publication_number'], r['feature_number']): r['summary'] for r in presentation.get('reviews', [])}
        reviews = []
        for doc in self.comparisons:
            for feature, review in doc['reviews'].items():
                n = self.plan['features'].index(feature) + 1
                text = review_summaries.get((doc['number'], n), review['reason'])
                fact = doc['effective'].get(feature, {})
                outcome = self.badge(fact.get('judgment'), fact.get('disclosure_type'))
                reviews.append(f'<article class="report-comparison-item"><h4>{esc(document_titles.get(doc["number"]) or doc["title"])}<span class="report-comparison-result">{self.review_source(review)} · {self.t(review["status"])} · {outcome}</span></h4>'
                               f'<p class="report-comparison-review-point">{esc(self.feature_title(n))}</p>'
                               f'<p>{esc(text)}</p><div class="report-comparison-links"><a href="#patent-{doc["anchor"]}">{esc(doc["number"])}</a>'
                               f'<a href="#{doc["anchor"]}-f{n}">{self.comparison_word("cell")}</a></div></article>')
        optional_summaries = {r['coverage_index']: r for r in presentation.get('optional', [])}
        optional = []
        raw = self.comparisons[0]['request'].get('disclosure_text', '')
        for i, item in enumerate(self.plan.get('coverage', [])):
            if item['treatment'] != 'optional':
                continue
            authored = optional_summaries.get(i, {})
            title = authored.get('title', self.comparison_word('optional_item'))
            summary = authored.get('summary', item['reason'])
            quote = item['quote']
            labels = ' · '.join(dict.fromkeys(re.findall(r'\[\d{4,}\]', quote)))
            anchor = f'evidence-optional-{i}'
            # 使用专利阅读器的原文定位函数，保留完整前后段和精确高亮。
            self.library[anchor] = (f'<article class="report-evidence report-disclosure-evidence" id="{anchor}" data-disclosure-source="{self.comparison_word("source")}" data-disclosure-locator="{esc(labels)}">'
                                    f'<h3>{self.comparison_word("source")} · {esc(labels)}</h3>{self.comparison_source_context(raw, quote) or "<blockquote>" + esc(quote) + "</blockquote>"}</article>')
            optional.append(f'<article class="report-comparison-item"><h4>{esc(title)}</h4><p>{esc(summary)}</p><div class="report-comparison-links">'
                            f'<a href="#{anchor}">{self.comparison_word("source")} {esc(labels)}</a></div></article>')
        return ('<div class="report-comparison-after">' + self.comparison_block('supplement', supplements)
                + self.comparison_block('reviews', ''.join(reviews)) + self.comparison_block('optional', ''.join(optional))
                + f'</div><p class="report-comparison-end">{self.comparison_word("end")}</p>')
