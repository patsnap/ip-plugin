"""专利原文阅读器：完整材料、逐字高亮与技术要点关联，全部来自保存回执。"""

import html
import re


def esc(value):
    return html.escape(str(value), quote=True)


def quote_match(text, quote):
    """允许提取材料的空白差异；没有逐字匹配时绝不制造高亮。"""
    return re.search(r'\s+'.join(re.escape(word) for word in quote.split()), text) if quote and quote.strip() else None


def source_context(text, quote):
    """完整引用段及相邻段落；对无编号材料使用实际空行段落。"""
    match = quote_match(text, quote)
    if not match:
        return ''
    parts = list(re.finditer(r'\[\d{4,}\][\s\S]*?(?=\[\d{4,}\]|【|$)', text))
    if not any(p.start() <= match.start() < p.end() for p in parts):
        parts = list(re.finditer(r'\S[\s\S]*?(?=\n\s*\n|$)', text))
    hit = [i for i, p in enumerate(parts) if p.start() < match.end() and p.end() > match.start()]
    if not hit:
        return ''
    result = []
    for i in range(max(0, hit[0] - 1), min(len(parts), hit[-1] + 2)):
        part = parts[i]
        left, right = max(part.start(), match.start()), min(part.end(), match.end())
        value = (esc(text[part.start():left]) + '<mark>' + esc(text[left:right]) + '</mark>' + esc(text[right:part.end()])) if left < right else esc(part.group())
        result.append('<p>' + value + '</p>')
    return '<div class="report-source-context">' + ''.join(result) + '</div>'


WORDS = {
    'title': ('技术要点与专利原文', 'Technical points and patent source', '技術要點與專利原文', '技術要素と特許原文', '기술 요소 및 특허 원문'),
    'features': ('技术方案与技术要点', 'Solution and technical points', '技術方案與技術要點', '技術案と技術要素', '평가안 및 기술 요소'),
    'select': ('选择要点，定位对应原文', 'Select a point to locate its source', '選擇要點，定位對應原文', '要素を選択して原文を表示', '요소를 선택하여 원문 찾기'),
    'abstract': ('摘要', 'Abstract', '摘要', '要約', '초록'),
    'claims': ('权利要求', 'Claims', '權利要求', '請求項', '청구항'),
    'description': ('说明书', 'Description', '說明書', '明細書', '명세서'),
    'figures': ('附图', 'Drawings', '附圖', '図面', '도면'),
    'source': ('专利原文', 'Patent source', '專利原文', '特許原文', '특허 원문'),
    'judgment': ('当前要点的判断与出处', 'Current point: finding and sources', '當前要點的判斷與出處', '選択した要素の判断と出典', '현재 요소의 판단 및 출처'),
    'missing': ('当前要点没有可定位的原文引句', 'No locatable source quote for this point', '當前要點沒有可定位的原文引句', 'この要素の引用箇所は未記録', '이 요소의 원문 인용 위치 없음'),
    'locate': ('定位引文', 'Locate quote', '定位引文', '引用箇所へ', '인용 찾기'),
    'full': ('查看专利原文与附图', 'Read patent source and drawings', '查看專利原文與附圖', '特許原文と図面を表示', '특허 원문 및 도면 보기'),
}


class PatentReader:
    def patent_word(self, key):
        return WORDS[key][self.LANGUAGES.index(self.language)]

    def patent_reader(self, document):
        """一篇一份原文，所有要点共享；多项重叠引文保持各自关联。"""
        d, text = document, document['text']
        matches, buttons, panels, drawings, seen = [], [], [], [], set()
        plan = self.plan or {}
        features = plan.get('features', d['request']['features'])
        summaries = plan.get('feature_summaries', features)
        for n, feature in enumerate(features, 1):
            value = d['effective'].get(feature)
            if not value:
                continue
            title, refs = (self.feature_title(n) if self.plan else feature), []
            for j, entry in enumerate(value.get('evidence', [])):
                match = quote_match(text, entry.get('quote'))
                token = f'{n}-{j}'
                if match:
                    matches.append((match.start(), match.end(), n, token))
                    refs.append(f'<button type="button" data-reader-locate="{token}">{esc(entry.get("location") or self.patent_word("locate"))}</button>')
                label = entry.get('image_label')
                if label:
                    link = self.evidence(d, entry)
                    key = re.search(r'href="#([^\"]+)', link)[1]
                    refs.append(f'<a href="#{key}">{esc(entry.get("location") or label)}</a>')
                    if label not in seen:
                        seen.add(label)
                        drawings.append(self.patent_drawing(d, label, key, entry.get('location') or label))
            buttons.append(f'<button type="button" data-reader-feature="{n}" aria-pressed="false"><span class="reader-feature-number">{n:02d}</span><span><strong>{esc(title)}</strong><small>{esc(summaries[n - 1])}</small>{self.badge(value["judgment"], value.get("disclosure_type"))}</span></button>')
            panels.append(f'<section class="reader-evidence-panel" data-reader-panel="{n}"><header><strong>{esc(title)}</strong>{self.badge(value["judgment"], value.get("disclosure_type"))}</header><p>{esc(self.reason_text(value["reason"]))}</p><div class="reader-locations">' + (''.join(refs) or '<span>' + self.patent_word('missing') + '</span>') + '</div></section>')
        boundaries = {0, len(text)}
        for match in re.finditer(r'(?=【(?:ABST|CLMS|DESC)】)|(?=\[\d{4,}\])|\n\s*\n', text):
            boundaries.update((match.start(), match.end()))
        spans, blocks = sorted(boundaries), []
        headings = {'【ABST】': 'abstract', '【CLMS】': 'claims', '【DESC】': 'description'}
        for a, b in zip(spans, spans[1:]):
            raw = text[a:b]
            if not raw.strip():
                continue
            heading = next((key for key in headings if raw.startswith(key)), None)
            if heading:
                section = headings[heading]
                blocks.append(f'<h4 data-reader-section="{section}">{self.patent_word(section)}</h4>')
                a += len(heading)
                raw = text[a:b]
                if not raw.strip():
                    continue
            cuts = sorted({a, b} | {max(a, min(b, x)) for m in matches for x in m[:2] if m[0] < b and m[1] > a})
            content = ''
            for left, right in zip(cuts, cuts[1:]):
                active = [m for m in matches if m[0] < right and m[1] > left]
                part = esc(text[left:right])
                if active:
                    part = '<mark data-reader-matches="' + ' '.join(m[3] for m in active) + '" data-reader-features="' + ' '.join(str(m[2]) for m in active) + '">' + part + '</mark>'
                content += part
            number = re.match(r'\[(\d{4,})\]', raw)
            if number:
                content = content.replace('[' + number[1] + ']', '', 1)
            blocks.append('<div class="reader-source-row"><span class="reader-paragraph-number">' + ('[' + number[1] + ']' if number else '') + '</span><p>' + content.strip() + '</p></div>')
        for label in d['images']:
            if label not in seen:
                link = self.evidence(d, {'image_label': label, 'location': label})
                key = re.search(r'href="#([^\"]+)', link)[1]
                drawings.append(self.patent_drawing(d, label, key, label))
        nav = ''.join(f'<button type="button" data-reader-section-jump="{name}">{self.patent_word(name)}</button>' for key, name in headings.items() if key in text)
        if drawings:
            nav += f'<button type="button" data-reader-section-jump="figures">{self.patent_word("figures")}</button>'
        return (
            f'<article class="patent-reader" data-reader-document="{esc(d["number"])}" id="patent-{d["anchor"]}"><h3>{esc(d["number"])} · {self.patent_word("title")}</h3>'
            f'<div class="patent-reader-layout"><aside class="reader-feature-nav"><h4>{self.patent_word("features")}</h4><p>{self.patent_word("select")}</p>{"".join(buttons)}</aside>'
            f'<section class="reader-workspace"><header class="reader-source-header"><h4>{esc(d["title"])}</h4><div><span>{esc(d["number"])} · {esc(d["date"])}</span><nav>{nav}</nav></div></header>'
            f'<div class="reader-source-pane" tabindex="0" aria-label="{self.patent_word("source")}">{"".join(blocks)}'
            + (f'<h4 data-reader-section="figures">{self.patent_word("figures")}</h4><div class="reader-drawings">{"".join(drawings)}</div>' if drawings else '')
            + f'</div><div class="reader-evidence-dock"><div class="reader-dock-label">{self.patent_word("judgment")}</div>{"".join(panels)}</div></section></div></article>'
        )

    def patent_drawing(self, document, label, key, caption):
        image = document['images'][label]
        source = self.image(image['host_file'], image.get('ref'))
        return f'<a class="reader-drawing" href="#{key}"><img src="{source}" alt="{esc(label)}" loading="lazy"><span>{esc(caption)}</span></a>'
