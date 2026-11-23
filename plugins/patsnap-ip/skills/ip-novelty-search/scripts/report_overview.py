"""技术方案概述：只排版本次宿主保存的数据，不调用模型、不保存工具状态。"""

import html
import re

WORDS = {
    "other": ("其他评价方案", "Other solution", "其他評價方案", "その他の評価案", "기타 평가안"),
    "relations": ("主方案的关键关系", "Key relationships", "主方案的關鍵關係", "主案の主要な関係", "주 평가안의 핵심 관계"),
    "scopes": ("评价方案与范围", "Solutions and scope", "評價方案與範圍", "評価案と範囲", "평가안 및 범위"),
    "definitions": ("技术关系与交底依据", "Relationships and disclosure evidence", "技術關係與交底依據", "技術関係と開示の根拠", "기술 관계 및 개시 근거"),
    "relation": ("技术关系", "Technical relationship", "技術關係", "技術関係", "기술 관계"),
    "used_by": ("采用的方案", "Used by", "採用的方案", "採用する案", "채택한 평가안"),
    "source": ("交底出处", "Disclosure source", "交底出處", "開示の出典", "개시 출처"),
    "disclosure": ("原始技术交底", "Original disclosure", "原始技術交底", "元の技術開示", "원본 기술 개시"),
    "context": ("原文上下文", "Source context", "原文上下文", "原文の前後関係", "원문 맥락"),
    "highlight": ("引用内容已高亮", "Cited text highlighted", "引用內容已高亮", "引用箇所を強調", "인용 내용 강조"),
    "related": ("对应技术关系", "Related requirement", "對應技術關係", "対応する技術関係", "대응 기술 관계"),
    "figures": ("相关附图", "Related figures", "相關附圖", "関連図面", "관련 도면"),
    "added": ("新增关系", "Added relationships", "新增關係", "追加する関係", "추가 관계"),
    "steps": ("操作流程", "Operating sequence", "操作流程", "操作手順", "작동 순서"),
    "count": ("{solutions} 个评价方案 · {features} 项技术关系", "{solutions} solutions · {features} relationships", "{solutions} 個評價方案 · {features} 項技術關係", "{solutions} 評価案 · {features} 技術関係", "평가안 {solutions}개 · 기술 관계 {features}개"),
}


def esc(value):
    """源文和展示字段一律转义，不能携带 HTML。"""
    return html.escape(str(value), quote=True)


def relation_layout(count):
    """布局只取决于数量，不截断或隐藏任何技术关系。"""
    return f"columns-{count}" if count <= 3 else "pairs" if count == 4 else "list"


def highlighted(text, start, ranges):
    """按原文字偏移高亮；交叠的片段合并，原文自身不改写。"""
    merged = []
    for left, right in sorted(ranges):
        left, right = max(0, left - start), min(len(text), right - start)
        if left >= right:
            continue
        if merged and left <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(right, merged[-1][1]))
        else:
            merged.append((left, right))
    result, cursor = [], 0
    for left, right in merged:
        result.extend((esc(text[cursor:left]), '<mark>' + esc(text[left:right]) + '</mark>'))
        cursor = right
    return ''.join(result) + esc(text[cursor:])


def source_context(raw, quote, highlights):
    """显示引用所在段落及前后文；没有段落编号时保留引用两侧文字。"""
    start = raw.index(quote)
    ranges = [(start + quote.index(value), start + quote.index(value) + len(value)) for value in highlights]
    markers = list(re.finditer(r'\[\d{4,}\]', raw))
    chunks = [(m.start(), markers[i + 1].start() if i + 1 < len(markers) else len(raw), m[0])
              for i, m in enumerate(markers)]
    if not chunks or start < chunks[0][0]:
        left, right = max(0, start - 240), min(len(raw), start + len(quote) + 240)
        return '<p class="report-source-text">' + highlighted(raw[left:right], left, ranges) + '</p>'
    selected = [i for i, (a, b, _) in enumerate(chunks) if a < start + len(quote) and b > start]
    items = []
    for i in range(max(0, selected[0] - 1), min(len(chunks), selected[-1] + 2)):
        a, b, label = chunks[i]
        a += len(label)
        active = i in selected
        prefix = suffix = ''
        if not active and b - a > 240:
            if i < selected[0]:
                a = b - 240
                prefix = '…'
            else:
                b = a + 240
                suffix = '…'
        text = prefix + highlighted(raw[a:b], a, ranges) + suffix
        items.append(f'<div class="report-disclosure-paragraph {"is-cited" if active else "is-context"}">'
                     f'<span>{esc(label)}</span><p>{text}</p></div>')
    return ''.join(items)


class TechnicalOverview:
    """宿主渲染器的展示模块：旧数据可直接渲染，补充字段均为可选。"""

    def overview_word(self, key):
        return WORDS[key][self.LANGUAGES.index(self.language)]

    def validate_overview(self):
        """校验展示字段及关联，禁止用摘要替换正式特征或伪造出处。"""
        summaries = self.plan.get('feature_summaries')
        if summaries is not None and (not isinstance(summaries, list) or len(summaries) != len(self.plan['features'])
                                      or any(not isinstance(x, str) or not x.strip() for x in summaries)):
            raise ValueError('feature_summaries must contain one nonempty summary per feature')
        overview = self.draft['report'].get('technical_overview') or {}
        if not isinstance(overview, dict):
            raise ValueError('technical_overview must be an object')
        for key in ('title', 'technical_problem', 'technical_solution', 'technical_effect', 'solution_summary'):
            if key in overview and (not isinstance(overview[key], str) or not overview[key].strip()):
                raise ValueError(f'technical_overview.{key} must be nonempty text')
        for solution in self.solutions:
            steps = solution.get('steps', [])
            if not isinstance(steps, list):
                raise ValueError('Solution steps must be a list')
            for step in steps:
                if not isinstance(step, dict) or any(not isinstance(step.get(k), str) or not step[k].strip() for k in ('title', 'description')):
                    raise ValueError('Each step needs a title and description')
                numbers = step.get('feature_numbers')
                if (not isinstance(numbers, list) or not numbers or any(type(n) is not int for n in numbers)
                        or len(set(numbers)) != len(numbers) or not set(numbers) <= set(solution['feature_numbers'])):
                    raise ValueError('Step must reference features of its solution')

    def validate_disclosure_highlights(self, provenance):
        """精确高亮只能引用当前特征所保存的交底原句。"""
        values = provenance.get('highlight_quotes')
        if values is not None and (not isinstance(values, list) or not values
                                   or any(not isinstance(x, str) or not x.strip()
                                          or x not in provenance.get('source_quote', '') for x in values)):
            raise ValueError('Disclosure highlights must be exact excerpts of source_quote')

    def feature_title(self, number):
        """没有短标题时直接保留完整关系，不猜缩写。"""
        return self.plan.get('feature_labels', self.plan['features'])[number - 1]

    def disclosure_evidence(self, number, feature, provenance, document, identifier):
        """每项关系保留自己的证据目标，同段原文也可有不同高亮和关联图。"""
        if not provenance or not (provenance.get('source_quote') or provenance.get('image_labels')):
            return ''
        target = f'evidence-disclosure-{identifier}-f{number}'
        quote = provenance.get('source_quote', '')
        labels = list(dict.fromkeys(re.findall(r'\[\d{4,}\]', quote)))
        locator = ' · '.join(labels or provenance.get('image_labels', []))
        highlights = provenance.get('highlight_quotes') or [quote]
        context = source_context(document['request']['disclosure_text'], quote, highlights) if quote else ''
        images = {im['label']: im for im in document['request'].get('disclosure_images', [])}
        figures = []
        for label in provenance.get('image_labels', []):
            image = images[label]
            src = self.image(image['host_file'], image.get('ref'))
            figures.append(f'<figure><img src="{src}" alt="{esc(label)}" loading="lazy">'
                           f'<figcaption>{esc(label)}</figcaption></figure>')
        heading = self.overview_word('source') + (f' · {locator}' if locator else '')
        source = self.overview_word('disclosure')
        figure_html = (f'<section class="report-disclosure-figures"><h4>{self.overview_word("figures")}</h4>'
                       + ''.join(figures) + '</section>') if figures else ''
        title = self.feature_title(number)
        article = (
            f'<article class="report-evidence report-disclosure-evidence" id="{target}" '
            f'data-disclosure-source="{esc(source)}" data-disclosure-locator="{esc(locator)}">'
            f'<h3>{esc(heading)}</h3><div class="report-disclosure-inspector">'
            f'<aside class="report-disclosure-relation"><span>{self.overview_word("related")}</span>'
            f'<h4>{esc(title)}</h4><p>{esc(feature)}</p><dl><dt>{self.overview_word("source")}</dt><dd>{esc(source)}</dd>'
            + (f'<dt>{esc(locator)}</dt>' if locator else '') + '</dl></aside>'
            '<div class="report-disclosure-reader">'
            + (f'<div class="report-disclosure-reader-heading"><h4>{self.overview_word("context")}</h4>'
               f'<span>{self.overview_word("highlight")}</span></div>{context}' if context else '')
            + figure_html + '</div></div></article>'
        )
        if not hasattr(self, 'disclosure_library'):
            self.disclosure_library = {}
            self.disclosure_links = {}
        self.disclosure_library[target] = article
        link = f'<a class="report-disclosure-link" href="#{target}">{self.overview_word("source")}{" · " + esc(locator) if locator else ""}</a>'
        self.disclosure_links[number] = link
        return link

    def technical_overview(self):
        """概述、关键关系、方案范围和完整定义各写一次，全部直接可读。"""
        word = self.overview_word
        overview = self.draft['report'].get('technical_overview') or {}
        primary = next(s for s in self.solutions if s['name'] == self.primary)
        links = getattr(self, 'disclosure_links', {})
        summaries = self.plan.get('feature_summaries', self.plan['features'])
        count = word('count').format(solutions=len(self.solutions), features=len(self.plan['features']))
        intro = (
            f'<div class="report-tech-meta">{esc(count)}</div><div class="report-tech-intro">'
            f'<div><p class="report-tech-eyebrow">{esc(primary["name"] if overview.get("title") else self.t("primary_scheme"))}</p>'
            f'<h3>{"<span>" + "</span><span>".join(esc(overview.get("title") or primary["name"]).split(chr(10))) + "</span>"}</h3></div>'
            f'<div class="report-tech-lead">{self.markdown(overview.get("technical_solution") or primary["description"])}'
            f'<div class="report-tech-sources">{"".join(links.get(n, "") for n in primary["feature_numbers"])}</div></div></div>'
        )
        relations = []
        for i, n in enumerate(primary['feature_numbers'], 1):
            title = self.feature_title(n)
            summary = summaries[n - 1]
            relations.append(f'<article class="report-tech-relation"><div><span>{i:02d}</span><h4>{esc(title)}</h4></div>'
                             + (f'<p>{esc(summary)}</p>' if summary != title else '') + links.get(n, '') + '</article>')
        relation_html = (f'<div class="report-tech-relations" data-layout="{relation_layout(len(relations))}" '
                         f'aria-label="{word("relations")}">{"".join(relations)}</div>')
        logic = ''.join(f'<div><h4>{self.part_word(label)}</h4>{self.markdown(value)}</div>' for label, value in (
            ('technical_problem', overview.get('technical_problem')),
            ('technical_solution', overview.get('solution_summary')),
            ('solution_effect', overview.get('technical_effect')),
        ) if value)
        schemes = []
        for i, solution in enumerate(self.solutions, 1):
            parent = next((s for s in self.solutions if s['name'] == solution.get('parent')), None)
            added = set(solution['feature_numbers']) - set(parent['feature_numbers']) if parent else set()
            chips = ''.join(f'<a href="#comparison-f{n}"{" class=report-tech-added" if n in added else ""}>'
                            f'{esc(self.feature_title(n))}</a>' for n in solution['feature_numbers'])
            change = (f'<p class="report-tech-change">{esc(solution["change_description"])}</p>'
                      if solution.get('change_description') else '')
            role = self.t('primary_scheme') if solution['name'] == self.primary else word('other')
            schemes.append(f'<article class="report-tech-scheme" id="overview-{self.solution_keys[solution["name"]]}">'
                           f'<span class="report-tech-ordinal">{i:02d}</span><div><h4>{esc(solution["name"])}</h4><small>{role}</small></div>'
                           f'<div>{change}<p>{esc(solution["description"])}</p><div class="report-tech-chips">{chips}</div></div></article>')
            if solution.get('steps'):
                steps = ''.join(f'<li><span>{j:02d}</span><h4>{esc(step["title"])}</h4><p>{esc(step["description"])}</p>'
                                f'<div>{"".join(links.get(n, "") for n in step["feature_numbers"])}</div></li>'
                                for j, step in enumerate(solution['steps'], 1))
                schemes.append(f'<div class="report-tech-process"><h4>{word("steps")} · {esc(solution["name"])}</h4>'
                               f'<ol>{steps}</ol></div>')
        rows = []
        for n, feature in enumerate(self.plan['features'], 1):
            used_by = ''.join(f'<span>{esc(s["name"])}</span>' for s in self.solutions if n in s['feature_numbers'])
            title = self.feature_title(n)
            rows.append(f'<tr id="comparison-f{n}"{self.row_scope(n)}>'
                        f'<th scope="row"><div class="report-tech-feature-title"><span class="report-tech-id">F{n}</span><strong>{esc(title)}</strong></div>'
                        + (f'<p>{esc(feature)}</p>' if title != feature else '')
                        + f'</th><td class="report-tech-used">{used_by}</td><td>{links.get(n, "—")}</td></tr>')
        table = (f'<section class="report-tech-definitions"><h3>{word("definitions")}</h3><div class="report-table-wrap">'
                 f'<table><thead><tr><th>{word("relation")}</th><th>{word("used_by")}</th><th>{word("source")}</th></tr></thead>'
                 f'<tbody>{"".join(rows)}</tbody></table></div></section>')
        evidence = ''.join(getattr(self, 'disclosure_library', {}).values())
        return (f'<div class="report-technical-overview">{intro}{relation_html}'
                + (f'<div class="report-tech-logic">{logic}</div>' if logic else '')
                + f'<section class="report-tech-scopes"><h3>{word("scopes")}</h3>{"".join(schemes)}</section>{table}'
                + f'<div class="report-disclosure-library" hidden>{evidence}</div></div>')
