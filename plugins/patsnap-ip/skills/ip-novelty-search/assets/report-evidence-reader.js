// App 和独立报告共用的原文展示函数；仅操作现有 DOM。
const EVIDENCE_WORDS = {
  title: ["原文与附图", "Source and figures", "原文與附圖", "原文と図面", "원문 및 도면"],
  point: ["当前核对点", "Current point", "目前核對點", "確認対象", "현재 검토 항목"],
  facts: ["文献事实与判断", "Document facts and finding", "文獻事實與判斷", "文献の事実と判断", "문헌 사실 및 판단"],
  context: ["上下文保留 · 引用内容高亮", "Context retained · Citation highlighted", "上下文保留 · 引用內容高亮", "前後の文脈・引用箇所を強調", "문맥 유지 · 인용 강조"],
  figure: ["引用附图", "Cited figure", "引用附圖", "引用図面", "인용 도면"],
};
export function evidenceReaderWord(language, key) {
  const index = ["zh-CN", "en-US", "zh-TW", "ja-JP", "ko-KR"].indexOf(language);
  return EVIDENCE_WORDS[key][Math.max(0, index)];
}

/** 优先读取明确的来源字段；兼容历史报告标题。 */
export function evidenceIdentity(entry) {
  const title = entry.querySelector('h3')?.textContent?.trim() || '';
  const parts = title.split(' · ');
  return {
    source: entry.dataset.evidenceSource || entry.dataset.disclosureSource || parts.find(x => /^(?:[A-Z]{2})\d/.test(x)) || parts[0],
    locator: entry.dataset.evidenceLocator || entry.dataset.disclosureLocator || parts.at(-1) || title,
  };
}

/** 从对应格的实际锚点寻找要点标题，不能用列位置猜文献。 */
export function evidencePoint(root, link) {
  const group = link?.closest('.report-matrix-judgment,.report-check,.report-decisive-difference');
  const href = group?.querySelector('a.report-map-open,a.report-basis-link')?.getAttribute('href');
  const rowId = href?.slice(1) || group?.closest('tr[id]')?.id || '';
  const match = rowId.match(/^(.*)-f(\d+)$/);
  const reader = match ? root.ownerDocument.getElementById('patent-' + match[1]) : null;
  const title = reader && root.contains(reader) ? reader.querySelector('[data-reader-feature="' + match[2] + '"] strong')?.textContent : '';
  return { title: title?.trim() || '', status: group?.querySelector('.report-state')?.textContent?.trim() || '' };
}

/** 拆分段落编号而不改写字句；逐个原始段落处理，保留已有 mark。 */
export function formatEvidenceParagraphs(container) {
  const doc = container.ownerDocument;
  const blocks = [...container.querySelectorAll('.report-source-text,.report-source-context')];
  for (const block of blocks) {
    if (block.querySelector('.report-citation-paragraph')) continue;
    const paragraphs = block.matches('p') ? [block] : [...block.querySelectorAll(':scope > p')];
    for (const paragraph of paragraphs.length ? paragraphs : [block]) {
      const raw = paragraph.textContent || '';
      const matches = [...raw.matchAll(/(?:^|\n\s*)(\[\d{4,}\])/g)];
      if (!matches.length) continue;
      const nodes = [];
      let offset = 0;
      const walker = doc.createTreeWalker(paragraph, 4);
      for (let node = walker.nextNode(); node; node = walker.nextNode()) {
        nodes.push({ text: node.textContent, start: offset, end: offset + node.textContent.length, marked: !!node.parentElement.closest('mark') });
        offset += node.textContent.length;
      }
      const fragment = doc.createDocumentFragment();
      const appendSlice = (target, from, to) => {
        for (const n of nodes) {
          const start = Math.max(from, n.start), end = Math.min(to, n.end);
          if (end <= start) continue;
          const value = n.text.slice(start - n.start, end - n.start);
          if (n.marked) { const mark = doc.createElement('mark'); mark.textContent = value; target.append(mark); }
          else target.append(doc.createTextNode(value));
        }
      };
      if (matches[0].index > 0) {
        const intro = doc.createElement('p'); appendSlice(intro, 0, matches[0].index); fragment.append(intro);
      }
      matches.forEach((m, index) => {
        const row = doc.createElement('div'); row.className = 'report-citation-paragraph';
        const label = doc.createElement('span'); label.className = 'report-citation-paragraph-number';
        const numberStart = m.index + m[0].length - m[1].length;
        appendSlice(label, numberStart, numberStart + m[1].length);
        const text = doc.createElement('p');
        appendSlice(text, m.index + m[0].length, matches[index + 1]?.index ?? raw.length);
        row.append(label, text);
        if (row.querySelector('mark')) row.classList.add('report-citation-quoted');
        fragment.append(row);
      });
      paragraph.replaceWith(fragment);
    }
  }
}

  // 展示已保存的依据；不修改原文、判断，也不发起请求。
  export function renderEvidenceReader(modal, body, heading, target, context, entries, language = "zh-CN") {
    const document = body.ownerDocument;
    const tr = key => evidenceReaderWord(language, key);
    modal.classList.add('report-citation-reader');
    const source = body.querySelector('.report-evidence');
    if (!source) return;
    const identity = evidenceIdentity(target);
    const location = identity.locator;
    heading.textContent = identity.source + ' · ' + tr('title');
    modal.setAttribute('aria-label', heading.textContent);
    source.querySelector('h3')?.remove();
    const tabs = body.querySelector('.report-popup-tabs');
    const tools = body.querySelector('.report-popup-image-tools');
    const layout = document.createElement('div'); layout.className = 'report-citation-layout';
    if (context) {
      const side = document.createElement('aside'); side.className = 'report-citation-sidebar';
      const label = document.createElement('p'); label.className = 'report-citation-eyebrow'; label.textContent = tr('point');
      const title = document.createElement('h4'); title.textContent = context.dataset.featureTitle || tr('facts');
      side.append(label,title);
      if (context.dataset.judgment) {
        const state = document.createElement('span'); state.className = 'report-citation-state'; state.textContent = context.dataset.judgment; side.append(state);
      }
      const rule = document.createElement('div'); rule.className = 'report-citation-reason';
      for (const child of context.children) if(child.tagName !== 'SUMMARY') rule.append(child.cloneNode(true));
      side.append(rule); layout.append(side);
    } else layout.classList.add('report-citation-no-context');
    const work = document.createElement('div'); work.className = 'report-citation-workspace';
    const head = document.createElement('div'); head.className = 'report-citation-source-head';
    const caption = document.createElement('h4'); caption.textContent = location;
    const hint = document.createElement('span'); hint.textContent = source.querySelector('img') ? tr('figure') : tr('context');
    head.append(caption,hint); work.append(head);
    if(tabs) {
      tabs.querySelectorAll('button').forEach((tab,index)=>{
        const entry = entries[index]; const name = evidenceIdentity(entry).locator || tab.textContent;
        tab.textContent = name; tab.title = entry.querySelector('h3')?.textContent || name;
      });
      work.append(tabs);
    }
    if(tools) work.append(tools);
    const pane = document.createElement('div'); pane.className='report-citation-pane';
    source.classList.add('report-citation-source');
    formatEvidenceParagraphs(source);
    pane.append(source);work.append(pane);layout.append(work);body.replaceChildren(layout);
  }

// 完整对照的界面文字；所有判断与引文仍从已保存报告读取。
const COMPARISON_WORDS = {
  title: ["技术关系对照 · 完整依据", "Technical comparison · Full evidence", "技術關係對照 · 完整依據", "技術対比・根拠の詳細", "기술 비교 · 전체 근거"],
  requirement: ["本方案要求", "Scheme requirement", "本方案要求", "本案の要件", "본 방안의 요구사항"],
  supplemental: ["补充判断依据", "Additional grounds", "補充判斷依據", "補足判断根拠", "추가 판단 근거"],
  date: ["公开日", "Publication date", "公開日", "公開日", "공개일"],
  locate: ["定位引文", "Locate quote", "定位引文", "引用箇所へ", "인용 위치"],
  zoom: ["放大附图", "Zoom figure", "放大附圖", "図を拡大", "도면 확대"],
  fit: ["适应宽度", "Fit to width", "適應寬度", "幅に合わせる", "너비에 맞추기"],
  empty: ["本条未保存可预览的引用依据", "No preview evidence saved for this comparison", "本條未儲存可預覽的引用依據", "この対比の引用資料は保存されていません", "이 비교에 저장된 인용 근거가 없습니다"],
  full: ["查看专利原文与附图", "View patent text and figures", "查看專利原文與附圖", "特許の原文と図面", "특허 원문 및 도면 보기"],
  return: ["Esc 关闭 · 关闭后继续原位置阅读", "Esc to close · Return to your reading position", "Esc 關閉 · 關閉後繼續原位置閱讀", "Escで閉じて元の位置へ", "Esc로 닫고 원래 위치로"],
  before: ["前文", "Before", "前文", "前文", "앞 문맥"],
  quoted: ["引用段", "Quote", "引用段", "引用", "인용"],
  after: ["后文", "After", "後文", "後文", "뒤 문맥"],
};

/** 返回其他类型弹窗时恢复原标题位置，不影响单点说明书阅读器。 */
export function resetComparisonReader(modal, heading) {
  modal.classList.remove('report-complete-reader');
  const group = modal.querySelector('.report-complete-heading');
  if (group) group.replaceWith(heading);
}

/** 使用原始对照行构建双栏阅读器；不修改表格、不生成或缩写事实。 */
export function renderComparisonReader(root, modal, body, heading, row, language = 'zh-CN') {
  const doc = row.closest('.report-doc-comparison');
  const match = row.id.match(/^(.*)-f(\d+)$/);
  const check = row.querySelector('.report-check');
  if (row.tagName !== 'TR' || !doc || !match || !check) return false;
  const document = body.ownerDocument;
  const index = Math.max(0, ['zh-CN','en-US','zh-TW','ja-JP','ko-KR'].indexOf(language));
  const tr = key => COMPARISON_WORDS[key][index];
  const word = key => evidenceReaderWord(language, key);
  const make = (tag, className, text) => {
    const element = document.createElement(tag);
    element.className = className;
    if (text) element.textContent = text;
    return element;
  };
  const local = id => { const entry = document.getElementById(id); return entry && root.contains(entry) ? entry : null; };
  const reader = local('patent-' + match[1]);
  const feature = reader?.querySelector('[data-reader-feature="' + match[2] + '"] strong')?.textContent?.trim()
    || row.querySelector('th strong')?.textContent?.trim() || word('point');
  const entries = [...new Set([...row.querySelectorAll('a[href^="#evidence-"]')]
    .map(a => local(a.getAttribute('href').slice(1))).filter(Boolean))];
  // 克隆只用于展示，原始锚点、上下文、高亮和附图内容保持不变。
  const copy = element => {
    const node = element.cloneNode(true);
    node.removeAttribute('id');
    node.querySelectorAll('[id]').forEach(child => child.removeAttribute('id'));
    node.querySelectorAll('details').forEach(child => { child.open = true; });
    return node;
  };
  const fullLink = label => {
    const a = make('a', '', label); a.href = '#patent-' + match[1]; return a;
  };
  modal.classList.add('report-complete-reader');
  heading.textContent = feature;
  modal.setAttribute('aria-label', feature);
  const titlebox = make('div', 'report-complete-heading');
  heading.replaceWith(titlebox);
  titlebox.append(make('p', 'report-complete-kicker', tr('title')), heading);
  const metadata = (doc.querySelector('.report-document-summary small')?.textContent || '').split(' · ');
  const meta = make('p', 'report-complete-meta');
  if (metadata[0]) meta.append(reader ? fullLink(metadata[0]) : make('span', '', metadata[0]));
  if (metadata[1]) meta.append(make('span', '', tr('date') + ' ' + metadata[1]));
  titlebox.append(meta, make('p', 'report-complete-patent-title', doc.querySelector('.report-document-summary strong')?.textContent));

  const columns = make('div', 'report-complete-columns');
  const analysis = make('aside', 'report-complete-analysis');
  const block = label => {
    const section = make('section', 'report-complete-block');
    section.append(make('h4', '', label)); analysis.append(section); return section;
  };
  block(tr('requirement')).append(make('p', '', row.querySelector('th strong')?.textContent));
  const result = block(word('facts'));
  const badge = check.querySelector(':scope > .report-state');
  if (badge) result.querySelector('h4').append(make('span', 'report-complete-state ' + [...badge.classList].filter(c => c !== 'report-state').join(' '), badge.textContent));
  const fact = check.querySelector(':scope > .report-fact');
  if (fact) result.append(copy(fact));
  // 复核记录、公知常识与常规设计依据全部保留，不能按段落数量截断。
  const review = make('div', 'report-complete-review');
  check.querySelectorAll(':scope > .report-atomic-review,:scope > .report-review-notes').forEach(element => review.append(copy(element)));
  if (review.childNodes.length) result.append(review);
  const supplemental = [...check.children].filter(element => !element.matches('.report-state,.report-fact,.report-atomic-review,.report-review-notes,.evidence-details'));
  if (supplemental.length) { const section = block(tr('supplemental')); supplemental.forEach(element => section.append(copy(element))); }

  const work = make('section', 'report-complete-workspace');
  const sourceTitle = make('div', 'report-complete-source-title');
  sourceTitle.append(make('h4', '', word('title')));
  const tabs = make('nav', 'report-complete-tabs');
  tabs.setAttribute('role', 'tablist'); tabs.setAttribute('aria-label', word('title'));
  const tools = make('div', 'report-complete-source-tools');
  const hint = make('span', '', word('context'));
  const locate = make('button', '', tr('locate')); locate.type = 'button';
  tools.append(hint, locate);
  const pane = make('div', 'report-complete-source-pane'); pane.setAttribute('role', 'tabpanel');
  // 使用原行 ID 作为前缀，避免嵌套弹窗间的 tab/panel ID 冲突。
  pane.id = 'complete-source-' + row.id;
  const position = () => {
    const mark = pane.querySelector('mark');
    if (!mark) return;
    const passage = mark.closest('.report-citation-paragraph,.report-complete-passage') || mark;
    pane.scrollTop += passage.getBoundingClientRect().top - pane.getBoundingClientRect().top - 24;
  };
  const draw = selected => {
    const entry = entries[selected];
    if (!entry) return;
    const source = copy(entry);
    source.querySelector('h3')?.remove();
    source.querySelector('.report-source-full-link')?.remove();
    formatEvidenceParagraphs(source);
    // 无段号的旧专利用前文、引用段和后文区分，绝不编造段号。
    const paragraphs = [...source.querySelectorAll('.report-source-context > p')];
    const firstQuote = paragraphs.findIndex(p => p.querySelector('mark'));
    const lastQuote = paragraphs.findLastIndex(p => p.querySelector('mark'));
    paragraphs.forEach((p, i) => {
      if (firstQuote < 0) return;
      const passage = make('div', 'report-complete-passage' + (p.querySelector('mark') ? ' quoted' : ''));
      passage.append(make('span', '', p.querySelector('mark') ? tr('quoted') : i < firstQuote ? tr('before') : i > lastQuote ? tr('after') : ''));
      p.replaceWith(passage); passage.append(p);
    });
    pane.replaceChildren(...source.childNodes);
    pane.classList.remove('is-zoomed');
    const image = !!pane.querySelector('img');
    hint.textContent = image ? word('figure') : word('context');
    locate.textContent = image ? tr('zoom') : tr('locate');
    locate.hidden = !image && !pane.querySelector('mark');
    locate.onclick = () => {
      if (image) { pane.classList.toggle('is-zoomed'); locate.textContent = pane.classList.contains('is-zoomed') ? tr('fit') : tr('zoom'); }
      else position();
    };
    [...tabs.children].forEach((tab, i) => { tab.setAttribute('aria-selected', String(i === selected)); tab.tabIndex = i === selected ? 0 : -1; });
    pane.setAttribute('aria-labelledby', tabs.children[selected].id);
    body.dataset.completeEntry = String(selected);
    pane.scrollTop = 0;
  };
  entries.forEach((entry, i) => {
    const label = evidenceIdentity(entry).locator.replace(/^DESC[，,]\s*/, '').replace(/的说明$/, '');
    const tab = make('button', '', label); tab.type = 'button';
    tab.id = pane.id + '-tab-' + i;
    tab.setAttribute('role', 'tab'); tab.setAttribute('aria-controls', pane.id);
    tab.onclick = () => draw(i);
    tab.onkeydown = event => {
      if (!['ArrowRight','ArrowLeft','Home','End'].includes(event.key)) return;
      event.preventDefault(); event.stopPropagation();
      const next = event.key === 'Home' ? 0 : event.key === 'End' ? entries.length - 1 : (i + (event.key === 'ArrowRight' ? 1 : -1) + entries.length) % entries.length;
      draw(next); tabs.children[next].focus({preventScroll:true});
    };
    tabs.append(tab);
  });
  work.append(sourceTitle, tabs, tools, pane);
  if (!entries.length) { tabs.hidden = true; tools.hidden = true; pane.append(make('p', '', tr('empty'))); }
  columns.append(analysis, work);
  const footer = make('div', 'report-complete-footer');
  footer.append(make('span', '', tr('return')));
  if (reader) footer.append(fullLink(tr('full')));
  body.replaceChildren(columns, footer);
  if (entries.length) draw(0);
  return true;
}
