"""02/03 的阅读排版；只组织宿主保存的判断，不重新评价或调用工具。"""

import html
import re
from html.parser import HTMLParser


def esc(value):
    return html.escape(str(value), quote=True)


WORDS = {
    'documents': ('逐篇看清关键区别', 'Decisive differences by document', '逐篇看清關鍵區別', '文献ごとの主要な相違点', '문헌별 핵심 차이'),
    'known': ('文献已经公开', 'What the document discloses', '文獻已經公開', '文献の開示内容', '문헌의 개시 내용'),
    'difference': ('与本方案的关键区别', 'Decisive difference from this solution', '與本方案的關鍵區別', '本案との主要な相違点', '본 평가안과의 핵심 차이'),
    'none_known': ('未记录已公开的对应关系', 'No disclosed relationship recorded', '未記錄已公開的對應關係', '対応する開示の記録なし', '개시된 대응 관계 기록 없음'),
    'path': ('从已有技术到本方案', 'From prior art to this solution', '從已有技術到本方案', '先行技術から本案への経路', '선행기술에서 본 평가안까지'),
    'scope': ('本次评价', 'Evaluation scope', '本次評價', '評価範囲', '평가 범위'),
    'changes': ('需要解决的区别', 'Differences to address', '需要解決的區別', '解決すべき相違点', '해결할 차이점'),
    'novelty_note': ('逐篇确认 · 单篇是否完整公开', 'One document at a time · complete disclosure', '逐篇確認 · 單篇是否完整公開', '文献ごとに完全な開示を確認', '문헌별 전체 개시 확인'),
    'inventiveness_note': ('从已有技术出发 · 评估完整改造路径', 'From prior art · assess the complete modification', '從已有技術出發 · 評估完整改造路徑', '先行技術から改変経路を評価', '선행기술에서 전체 변경 경로 평가'),
    'prior_documents': ('在先文献', 'Prior documents', '在先文獻', '先行文献', '선행 문헌'),
    'document_count': ('{count} 篇文献，逐篇看区别', '{count} documents, compared individually', '{count} 篇文獻，逐篇看區別', '{count} 件の文献を個別に比較', '문헌 {count}건 개별 비교'),
    'verified_differences': ('下列每篇均存在已核实的必要区别', 'Each document has a verified necessary difference', '下列每篇均存在已核實的必要區別', '各文献に確認済みの相違点あり', '각 문헌에 확인된 필수 차이 존재'),
    'other_novelty': ('其他方案，结论有什么变化？', 'Other solutions: what changes?', '其他方案，結論有什麼變化？', '他の案で結論はどう変わるか', '다른 평가안의 결론 변화'),
    'other_inventiveness': ('其他方案，风险停在哪里？', 'Other solutions: where does risk remain?', '其他方案，風險停在哪裡？', '他の案でリスクはどこに残るか', '다른 평가안의 남은 위험'),
    'path_heading': ('这条改造路径怎样形成', 'How this modification takes shape', '這條改造路徑怎樣形成', '改変経路の形成', '변경 경로의 구성'),
    'starting_point': ('现有起点', 'Starting point', '現有起點', '出発点', '출발점'),
    'adapt': ('沿既有需求改造', 'Adapt to existing needs', '沿既有需求改造', '既存の課題に沿う改変', '기존 요구에 따른 변경'),
    'motivation_label': ('动机', 'Motivation', '動機', '動機', '동기'),
    'motivation_question': ('为什么会这样改？', 'Why make this change?', '為什麼會這樣改？', 'なぜこの改変を行うか', '왜 이렇게 변경하는가'),
    'compatibility_label': ('配合', 'Compatibility', '配合', '両立性', '양립성'),
    'compatibility_question': ('这些改动能共存吗？', 'Can these changes work together?', '這些改動能共存嗎？', '改変は両立するか', '변경 사항은 양립하는가'),
    'overall_label': ('整体判断', 'Overall finding', '整體判斷', '総合判断', '종합 판단'),
    'overall_question': ('完整方案的判断依据', 'Basis for the whole-solution finding', '完整方案的判斷依據', '全体の判断根拠', '전체 평가안의 판단 근거'),
    'engineering': ('工程适配仍需满足', 'Engineering conditions to satisfy', '工程適配仍需滿足', '実装上の条件', '충족할 공학적 조건'),
    'next': ('下一步要看', 'Read next', '下一步要看', '次に確認', '다음 확인 사항'),
    'next_question': ('单篇没有完整公开，已有技术之间是否仍能形成合理的改造路径？', 'Without full disclosure in one document, can prior teachings still form a reasoned modification?', '單篇沒有完整公開，已有技術之間是否仍能形成合理的改造路徑？', '単独の完全開示がなくても改変経路は成立するか', '단일 문헌의 전체 개시가 없어도 변경 경로가 성립하는가'),

}


class PublicationLinks(HTMLParser):
    """只将叙述中的真实公开号设为链接，不嵌套链接，不处理原始引文。"""
    def __init__(self, documents):
        super().__init__(convert_charrefs=False)
        self.documents = {d['number']: d for d in documents}
        self.output, self.depth = [], 0
        self.pattern = re.compile('|'.join(re.escape(n) for n in sorted(self.documents, key=len, reverse=True))) if documents else None

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            self.depth += 1
        self.output.append(self.get_starttag_text())

    def handle_startendtag(self, tag, attrs):
        self.output.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        self.output.append(f'</{tag}>')
        if tag == 'a':
            self.depth = max(0, self.depth - 1)

    def handle_data(self, data):
        if self.pattern and not self.depth:
            data = self.pattern.sub(lambda m: f'<a href="#patent-{esc(self.documents[m[0]]["anchor"])}">{m[0]}</a>', data)
        self.output.append(data)

    def handle_entityref(self, name):
        self.output.append(f'&{name};')

    def handle_charref(self, name):
        self.output.append(f'&#{name};')


class AnalysisPresentation:
    def analysis_word(self, key):
        return WORDS[key][self.LANGUAGES.index(self.language)]

    def analysis_text(self, value):
        """展示名称取已有特征标题；只替换叙述编号，不变更原文或存储数据。"""
        names = {d['label']: d['number'] for d in self.comparisons}
        names.update({f'F{n}': self.feature_title(n) for n in range(1, len(self.plan['features']) + 1)})
        value = re.sub(r'(?<![A-Za-z0-9])[DF]\d+(?![A-Za-z0-9])', lambda m: names.get(m[0], m[0]), value)
        parser = PublicationLinks(self.comparisons)
        parser.feed(self.markdown(self.reason_text(value)))
        return ''.join(parser.output)

    def display_refs(self, refs, *, document=None, features=None):
        """展示出处只能指向现有回执，且必须属于这一文献或改造要点。"""
        if not isinstance(refs, list) or not refs:
            raise ValueError('Display evidence_refs must be a nonempty list')
        for ref in refs:
            if (not isinstance(ref, dict) or set(ref) != {'publication_number', 'feature_number', 'evidence_number'}
                    or not isinstance(ref['publication_number'], str)
                    or type(ref['feature_number']) is not int or type(ref['evidence_number']) is not int):
                raise ValueError('Invalid display evidence reference')
            if document and ref['publication_number'] != document:
                raise ValueError('Display evidence must belong to its document')
            if features is not None and ref['feature_number'] not in features:
                raise ValueError('Display evidence must belong to its technical point')
        self.evidence_refs(refs, render=False)

    @staticmethod
    def display_text_fields(value, allowed, required=()):
        """纯文本展示字段不允许混入结果状态或 HTML 模板。"""
        if not isinstance(value, dict) or set(value) - set(allowed):
            raise ValueError('Unknown analysis presentation field')
        for key in required:
            if key not in value:
                raise ValueError('Missing required analysis presentation field')
        for key in set(value) & set(allowed):
            if not isinstance(value[key], str) or not value[key].strip():
                raise ValueError('Analysis presentation text must be nonempty')

    def validate_analysis_presentation(self):
        """摘要只承担阅读表达；路线、阶段状态与全部出处仍由原分析决定。"""
        for name, finding in self.findings.items():
            solution = next(s for s in self.solutions if s['name'] == name)
            for kind in ('novelty', 'inventiveness'):
                view = finding[kind].get('presentation', {})
                text_keys = {'headline', 'introduction', 'verdict_summary', 'scope'}
                nested = {'documents', 'delta'} if kind == 'novelty' else {'routes', 'starting_point', 'delta'}
                if not isinstance(view, dict) or set(view) - text_keys - nested:
                    raise ValueError('Unknown analysis presentation field')
                self.display_text_fields({k: v for k, v in view.items() if k in text_keys}, text_keys)
                docs = view.get('documents', [])
                if not isinstance(docs, list):
                    raise ValueError('Presentation documents must be a list')
                seen = set()
                for row in docs:
                    if not isinstance(row, dict):
                        raise ValueError('Invalid presentation document')
                    self.display_text_fields({k: v for k, v in row.items() if k != 'evidence_refs'},
                                             {'publication_number', 'title', 'known', 'difference'}, {'publication_number', 'known', 'difference'})
                    number = row['publication_number']
                    if number not in {d['number'] for d in self.comparisons} or number in seen:
                        raise ValueError('Presentation document must identify one current comparison')
                    seen.add(number)
                    if 'evidence_refs' in row:
                        self.display_refs(row['evidence_refs'], document=number, features=solution['feature_numbers'])
                analysis = finding[kind].get('analysis') or {}
                actual = analysis.get('routes', [])
                if 'starting_point' in view:
                    start = view['starting_point']
                    if not analysis or not isinstance(start, dict):
                        raise ValueError('Starting point requires an actual analysis')
                    self.display_text_fields({k: v for k, v in start.items() if k != 'evidence_refs'}, {'title', 'description'}, {'title', 'description'})
                    if 'evidence_refs' in start:
                        self.display_refs(start['evidence_refs'], document=analysis['closest_publication_number'], features=solution['feature_numbers'])
                routes = view.get('routes', [])
                if not isinstance(routes, list) or (routes and len(routes) != len(actual)):
                    raise ValueError('Presentation routes must match every analysis route in order')
                for i, row in enumerate(routes):
                    if not isinstance(row, dict):
                        raise ValueError('Invalid presentation route')
                    self.display_text_fields({k: v for k, v in row.items() if k != 'changes'}, {'title', 'teaching', 'motivation', 'obstacles', 'reason', 'engineering'})
                    changes = row.get('changes')
                    if changes is not None:
                        covered = set()
                        if not isinstance(changes, list) or not changes:
                            raise ValueError('Route changes must be a nonempty list')
                        for change in changes:
                            if not isinstance(change, dict):
                                raise ValueError('Invalid route change')
                            self.display_text_fields({k: v for k, v in change.items() if k not in {'feature_numbers', 'evidence_refs'}}, {'title', 'description'}, {'title', 'description'})
                            numbers = change.get('feature_numbers')
                            if (not isinstance(numbers, list) or not numbers or any(type(n) is not int for n in numbers)
                                    or len(numbers) != len(set(numbers)) or not set(numbers) <= set(actual[i]['feature_numbers'])):
                                raise ValueError('Changes must reference features of this route')
                            covered.update(numbers)
                            # 改造启示也可能来自同方案的另一项既有关系，不等于该区别已公开。
                            self.display_refs(change.get('evidence_refs'), features=solution['feature_numbers'])
                        if covered != set(actual[i]['feature_numbers']):
                            raise ValueError('Display changes must cover every feature of the route')
                if 'delta' in view:
                    delta = view['delta']
                    if name == self.primary or not isinstance(delta, dict):
                        raise ValueError('Only other solutions may use a delta summary')
                    self.display_text_fields({k: v for k, v in delta.items() if k != 'stages'}, {'title', 'scope', 'reason'}, {'scope', 'reason'})
                    stages = delta.get('stages')
                    if stages is not None:
                        if kind != 'inventiveness' or not isinstance(stages, list) or not stages:
                            raise ValueError('Stages require inventive routes')
                        covered = set()
                        for stage in stages:
                            if not isinstance(stage, dict):
                                raise ValueError('Invalid analysis stage')
                            self.display_text_fields({k: v for k, v in stage.items() if k != 'route_numbers'}, {'title', 'description'}, {'title', 'description'})
                            numbers = stage.get('route_numbers')
                            if (not isinstance(numbers, list) or not numbers or any(type(n) is not int or not 1 <= n <= len(actual) for n in numbers)):
                                raise ValueError('Stages must reference actual route numbers')
                            covered.update(numbers)
                        if covered != set(range(1, len(actual) + 1)):
                            raise ValueError('Stage summary must represent every route')

    def source_links(self, refs):
        """段落号和图号各有独立可访问链接，不用计数掩盖实际出处。"""
        links, seen = [], set()
        for ref in refs:
            doc = next(d for d in self.comparisons if d['number'] == ref['publication_number'])
            entry = doc['effective'][self.plan['features'][ref['feature_number'] - 1]]['evidence'][ref['evidence_number'] - 1]
            link = self.evidence(doc, entry)
            target = re.search(r'href="([^\"]+)"', link)[1]
            if target in seen:
                continue
            seen.add(target)
            location = entry.get('location') or entry.get('image_label') or self.t('evidence')
            # 优先使用材料自带的规范定位；无编号时保留完整描述而不是编造简称。
            markers = re.findall(r'\[\d{4,}\]|(?:权利要求|claim[s]?)[ \t]*\d+(?:[–—-]\d+)?|图\s*\d+[A-Za-z]?(?:、图?\s*\d+[A-Za-z]?)*|Fig(?:ure)?\.?\s*\d+[A-Za-z]?', location, re.I)
            label = '、'.join(dict.fromkeys(markers)) if markers else re.sub(r'^(?:ABST|CLMS|DESC)[，,：: ]*', '', location)
            if entry.get('quote') and markers and all(re.match(r'(图|Fig)', x, re.I) for x in markers):
                label += ('说明', ' text', '說明', 'の説明', ' 설명')[self.LANGUAGES.index(self.language)]
            links.append(f'<a href="{target}" title="{esc(doc["number"] + " · " + location)}">{esc(label)}</a>')
        return '<span class="report-analysis-sources">' + ''.join(links) + '</span>' if links else ''

    def analysis_verdict(self, kind, finding):
        """保持原判断文案，仅把填色标签改成确认稿的文字与圆点。"""
        return self.finding_badge(kind, finding).replace('report-state', 'report-state report-analysis-verdict', 1).replace('<span ', f'<span data-analysis-kind="{kind}" ', 1)

    def analysis_panel(self, kind, solution, finding, body):
        """左侧结论、右侧判断摘要，下方保留评价范围与完整解释。"""
        key = self.solution_keys[solution['name']]
        view = finding.get('presentation', {})
        title = view.get('headline') or solution['name']
        heading = '<br>'.join(esc(line) for line in title.splitlines())
        introduction = view.get('introduction') or finding['reason']
        summary = view.get('verdict_summary') or finding.get('summary', '')
        scope = view.get('scope') or solution['description']
        eyebrow = (self.t('primary_scheme') + ' · ' if solution['name'] == self.primary else '') + solution['name']
        return (
            f'<article class="report-scope-assessment report-analysis" id="{kind}-{key}" data-scheme-panel="{key}">'
            f'<header class="report-analysis-heading"><div><p class="report-analysis-eyebrow">{esc(eyebrow)}</p>'
            f'<h3 class="report-analysis-title">{heading}</h3></div><aside>{self.analysis_verdict(kind, finding)}'
            f'{self.analysis_text(summary) if summary else ""}</aside></header>'
            f'<div class="report-analysis-explanation"><p class="report-analysis-scope"><b>{self.analysis_word("scope")}：</b>{esc(scope)}</p>'
            f'<div class="report-analysis-intro">{self.analysis_text(introduction)}</div></div>{body}</article>'
        )

    def analysis_chapter(self, kind):
        """主方案详述一次；有完整阅读摘要的其他方案以变化表呈现。"""
        primary = next(s for s in self.solutions if s['name'] == self.primary)
        render = self.novelty_editorial if kind == 'novelty' else self.inventiveness_editorial
        body = render(primary, self.findings[self.primary][kind])
        others = [s for s in self.solutions if s['name'] != self.primary]
        if others:
            body += f'<div class="report-analysis-deltas"><h3>{self.analysis_word("other_" + kind)}</h3>'
            for solution in others:
                finding = self.findings[solution['name']][kind]
                delta = finding.get('presentation', {}).get('delta')
                body += self.analysis_delta(kind, solution, finding, delta) if delta else render(solution, finding)
            body += '</div>'
        if kind == 'novelty':
            body += f'<div class="report-analysis-next"><span>{self.analysis_word("next")}</span><p>{self.analysis_word("next_question")}</p></div>'
        body += f'<a class="report-basis-link" data-report-chapter-link data-report-focus-scheme="{self.solution_keys[self.primary]}" href="#comparison">{self.part_word("see_full_comparison")}</a>'
        return body

    def analysis_delta(self, kind, solution, finding, delta):
        """方案变化直接展开，阶段颜色来自原路线结果，不能由展示文字指定。"""
        key = self.solution_keys[solution['name']]
        title = delta.get('title') or solution['name']
        stages = delta.get('stages', [])
        body = f'<article class="report-analysis-delta {"has-stages" if stages else ""}" id="{kind}-{key}" data-scheme-panel="{key}">'
        body += f'<div><h4>{esc(title)}</h4><p>{esc(delta["scope"])}</p></div>{self.analysis_verdict(kind, finding)}'
        if stages:
            body += '<div class="report-analysis-track">'
            routes = finding['analysis']['routes']
            for stage in stages:
                results = {routes[n - 1]['result'] for n in stage['route_numbers']}
                state = 'established' if results == {'established'} else 'not_established' if results == {'not_established'} else 'unresolved'
                # 每一段保留实际 scope/result，方便审计与打印，不把局部成立写成完整成立。
                body += f'<div data-stage-result="{state}"><h4>{esc(stage["title"])}</h4><p>{esc(stage["description"])}</p>'
                for n in stage['route_numbers']:
                    body += f'<span class="report-analysis-route-state" data-route-scope="{routes[n-1]["scope"]}" data-route-result="{routes[n-1]["result"]}">{self.part_word(routes[n-1]["scope"])} · {self.part_word(routes[n-1]["result"])}</span>'
                body += '</div>'
            body += '</div>'
        body += '<div class="report-analysis-delta-reason">' + self.analysis_text(delta['reason']) + '</div></article>'
        return body

    def novelty_editorial(self, solution, finding):
        """逐篇只展示已有内容、决定性区别与出处；完整逐格记录仍在 05。"""
        eligible = {d['number'] for d in self.eligible_documents()}
        summaries = {d['publication_number']: d for d in finding.get('presentation', {}).get('documents', [])}
        rows = []
        for index, doc in enumerate(self.comparisons, 1):
            tone, outcome, differences = self.document_outcome(doc, solution, finding, eligible)
            view = summaries.get(doc['number'], {})
            known = [self.feature_title(n) for n in solution['feature_numbers'] if doc['effective'].get(self.plan['features'][n - 1], {}).get('judgment') == 'disclosed']
            known_text = view.get('known') or '；'.join(known) or self.analysis_word('none_known')
            decisive = [n for n in differences if self.decisive_difference(doc, n)] or differences
            facts = [doc['effective'].get(self.plan['features'][n - 1], {}).get('reason') for n in decisive]
            fact_text = view.get('difference') or '\n\n'.join(x for x in facts if x) or self.part_word(outcome)
            refs = view.get('evidence_refs')
            if refs is None:
                refs = [{'publication_number': doc['number'], 'feature_number': n, 'evidence_number': j + 1}
                        for n in decisive or solution['feature_numbers']
                        for j, _ in enumerate(doc['effective'].get(self.plan['features'][n - 1], {}).get('evidence', []))]
            sources = self.source_links(refs)
            status = '' if outcome == 'doc_not_defeating' else f'<span class="report-state {tone}">{self.part_word(outcome)}</span>'
            rows.append(
                f'<article class="report-analysis-document" data-document-decision="{outcome}"><div class="report-analysis-document-meta">'
                f'<span class="report-analysis-index">{index:02d}</span><div><h4>{esc(view.get("title") or doc["title"])}</h4>'
                f'<a href="#patent-{doc["anchor"]}">{esc(doc["number"])}</a><small>{esc(doc["date"] or self.t("no_date"))}</small></div></div>'
                f'<div data-analysis-label="{self.analysis_word("known")}">{self.analysis_text(known_text)}</div>'
                f'<div data-analysis-label="{self.analysis_word("difference")}">{status}'
                f'{self.analysis_text(fact_text)}{sources}</div></article>'
            )
        verified = all(self.document_outcome(d, solution, finding, eligible)[1] == 'doc_not_defeating' for d in self.comparisons)
        note = self.analysis_word('verified_differences') if verified else ''
        body = f'<div class="report-analysis-section-label"><h4>{self.analysis_word("document_count").format(count=len(self.comparisons))}</h4><span>{note}</span></div><div class="report-analysis-ledger">'
        body += f'<div class="report-analysis-columns"><span>{self.analysis_word("prior_documents")}</span><span>{self.analysis_word("known")}</span><span>{self.analysis_word("difference")}</span></div>' + ''.join(rows) + '</div>'
        if finding.get('arrangement_reason'):
            body += self.analysis_text(finding['arrangement_reason'])
        body += self.arrangement_callout(self.scoped_arrangements.get(solution['name']))
        return self.analysis_panel('novelty', solution, finding, body)

    def reasoning_row(self, label, title, content):
        return f'<div class="report-analysis-reason-row"><div><span>{self.analysis_word(label)}</span><h4>{self.analysis_word(title)}</h4></div><div>{content}</div></div>'

    def inventiveness_editorial(self, solution, finding):
        """已有起点、逐项改造、配合与结论；结构数量完全由原分析决定。"""
        analysis = finding.get('analysis')
        if not analysis:
            return self.analysis_panel('inventiveness', solution, finding, '')
        view = finding.get('presentation', {})
        closest = next(d for d in self.comparisons if d['number'] == analysis['closest_publication_number'])
        start = view.get('starting_point', {})
        summaries = view.get('routes', [])
        body = ''
        for i, route in enumerate(analysis['routes']):
            display = summaries[i] if summaries else {}
            changes = display.get('changes', [])
            body += f'<section class="report-analysis-route" data-route-scope="{esc(route["scope"])}" data-route-result="{esc(route["result"])}">'
            title = display.get('title') or route['title']
            body += f'<div class="report-analysis-section-label"><h4>{esc(title)}</h4><span class="report-analysis-path-state">{self.part_word(route["scope"])} · {self.part_word(route["result"])}</span></div>'
            body += '<div class="report-analysis-path"><div class="report-analysis-path-start">'
            body += f'<small>{self.analysis_word("starting_point") if start else self.part_word("closest_art")}</small><h4>{"<br>".join(esc(x) for x in (start.get("title") or closest["title"]).splitlines())}</h4>'
            if start.get('description'):
                body += self.analysis_text(start['description'])
            body += f'<div class="report-analysis-path-source"><a href="#patent-{closest["anchor"]}">{esc(closest["number"])}</a>{self.source_links(start.get("evidence_refs", []))}</div></div>'
            body += f'<div class="report-analysis-path-connect"><span>{self.analysis_word("adapt")}</span></div><div class="report-analysis-changes">'
            if changes:
                for j, change in enumerate(changes, 1):
                    body += f'<div class="report-analysis-change"><span>{j:02d}</span><h4>{esc(change["title"])}</h4>{self.analysis_text(change["description"])}{self.source_links(change["evidence_refs"])}</div>'
                sources = list(dict.fromkeys(ref['publication_number'] for change in changes for ref in change['evidence_refs']))
                body += '<div class="report-analysis-shared-source">' + self.analysis_text(' · '.join(sources)) + '</div>'
            else:
                body += self.analysis_text(display.get('teaching') or route['teaching']) + self.source_links(route['evidence_refs'])
            body += '</div></div><div class="report-analysis-reasoning">'
            body += self.reasoning_row('motivation_label', 'motivation_question', self.analysis_text(display.get('motivation') or route['motivation']))
            compatibility = self.analysis_text(display.get('obstacles') or route['obstacles'])
            if display.get('engineering'):
                compatibility += f'<div class="report-analysis-engineering"><b>{self.analysis_word("engineering")}</b>{self.analysis_text(display["engineering"])}</div>'
            body += self.reasoning_row('compatibility_label', 'compatibility_question', compatibility)
            body += self.reasoning_row('overall_label', 'overall_question', self.analysis_text(display.get('reason') or route['reason']))
            body += '</div></section>'
        # 未提供阅读版时不静默省略独立论证字段，旧草稿保持完整。
        if not summaries:
            body += f'<div class="report-analysis-original-reasoning"><h4>{self.part_word("difference_effect")}</h4>{self.analysis_text(analysis["technical_effect"])}<h4>{self.part_word("actual_problem")}</h4>{self.analysis_text(analysis["objective_problem"])}<h4>{self.part_word("comprehensive")}</h4>{self.analysis_text(analysis["overall_reason"])}</div>'
        return self.analysis_panel('inventiveness', solution, finding, body)
