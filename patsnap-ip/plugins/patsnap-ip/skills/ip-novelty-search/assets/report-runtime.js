// Presentation only: read saved report content, never fetch or change assessments.
(() => {
  const translations = {"en-US":{"Esc 关闭 · 关闭后继续原位置阅读":"Esc to close · Return to your reading position","← 返回上一层":"← Back","关闭":"Close","关闭弹窗，继续阅读":"Close dialog and continue reading","关闭（Esc）":"Close (Esc)","关闭，继续阅读":"Close and continue reading","原文 ":"Text ","在弹窗中查看，保留当前阅读位置":"Open in a dialog; keep your reading position","在新标签页打开文献网站 ↗":"Open document website in a new tab ↗","展开全文":"Expand all","展开全部证据":"Expand all evidence","当前核对点与文献事实":"Current feature and document facts","恢复分层阅读":"Restore reading view","报告详情":"Report details","收起全部证据":"Collapse all evidence","放大附图":"Zoom figure","文献详情":"Document details","本报告已保存该文献的以下引用依据，可直接查看原文与附图。":"The cited text and figures below are embedded in this report.","本条对照的引用依据":"Evidence for this comparison","这份报告未保存该文献的可预览原文。":"No preview text for this document is embedded in the report.","适应宽度":"Fit to width","逐项对照":"Feature comparison","附图 ":"Figure "},"zh-TW":{"Esc 关闭 · 关闭后继续原位置阅读":"Esc 關閉 · 關閉後繼續原位置閱讀","← 返回上一层":"← 返回上一層","关闭":"關閉","关闭弹窗，继续阅读":"關閉彈窗，繼續閱讀","关闭（Esc）":"關閉（Esc）","关闭，继续阅读":"關閉，繼續閱讀","原文 ":"原文 ","在弹窗中查看，保留当前阅读位置":"在彈窗中查看，保留目前閱讀位置","在新标签页打开文献网站 ↗":"在新分頁開啟文獻網站 ↗","展开全文":"展開全文","展开全部证据":"展開全部證據","当前核对点与文献事实":"目前核對點與文獻事實","恢复分层阅读":"恢復分層閱讀","报告详情":"報告詳情","收起全部证据":"收起全部證據","放大附图":"放大附圖","文献详情":"文獻詳情","本报告已保存该文献的以下引用依据，可直接查看原文与附图。":"本報告已儲存該文獻的以下引用依據，可直接查看原文與附圖。","本条对照的引用依据":"本條對照的引用依據","这份报告未保存该文献的可预览原文。":"這份報告未儲存該文獻的可預覽原文。","适应宽度":"適應寬度","逐项对照":"逐項對照","附图 ":"附圖 "},"ja-JP":{"Esc 关闭 · 关闭后继续原位置阅读":"Escで閉じて元の位置へ","← 返回上一层":"← 戻る","关闭":"閉じる","关闭弹窗，继续阅读":"閉じて続きを読む","关闭（Esc）":"閉じる（Esc）","关闭，继续阅读":"閉じて続きを読む","原文 ":"原文 ","在弹窗中查看，保留当前阅读位置":"元の位置を保ってダイアログで確認","在新标签页打开文献网站 ↗":"文献サイトを新しいタブで開く ↗","展开全文":"すべて展開","展开全部证据":"すべての根拠を展開","当前核对点与文献事实":"現在の特徴と文献の事実","恢复分层阅读":"通常表示に戻す","报告详情":"レポート詳細","收起全部证据":"すべての根拠を折りたたむ","放大附图":"図を拡大","文献详情":"文献詳細","本报告已保存该文献的以下引用依据，可直接查看原文与附图。":"引用した原文と図面をこのレポート内で確認できます。","本条对照的引用依据":"この対比の根拠","这份报告未保存该文献的可预览原文。":"この文献のプレビュー原文は保存されていません。","适应宽度":"幅に合わせる","逐项对照":"特徴ごとの対比","附图 ":"図面 "},"ko-KR":{"Esc 关闭 · 关闭后继续原位置阅读":"Esc로 닫고 원래 위치로","← 返回上一层":"← 뒤로","关闭":"닫기","关闭弹窗，继续阅读":"대화상자를 닫고 계속 읽기","关闭（Esc）":"닫기(Esc)","关闭，继续阅读":"닫고 계속 읽기","原文 ":"원문 ","在弹窗中查看，保留当前阅读位置":"읽기 위치를 유지하며 대화상자로 보기","在新标签页打开文献网站 ↗":"새 탭에서 문헌 사이트 열기 ↗","展开全文":"모두 펼치기","展开全部证据":"모든 근거 펼치기","当前核对点与文献事实":"현재 특징 및 문헌 사실","恢复分层阅读":"기본 읽기 화면 복원","报告详情":"보고서 상세","收起全部证据":"모든 근거 접기","放大附图":"도면 확대","文献详情":"문헌 상세","本报告已保存该文献的以下引用依据，可直接查看原文与附图。":"인용한 원문과 도면이 보고서에 포함되어 있습니다.","本条对照的引用依据":"이 비교의 인용 근거","这份报告未保存该文献的可预览原文。":"이 문헌의 미리보기 원문이 보고서에 없습니다.","适应宽度":"너비에 맞추기","逐项对照":"특징별 비교","附图 ":"도면 "}};
  const tr = value => translations[document.documentElement.lang]?.[value] ?? value;
  const root = document.querySelector('.novelty-report') ?? document.body;
  // Each original is embedded once; all thumbnails and dialog clones share one URL.
  const imageData = JSON.parse(document.getElementById('report-image-assets')?.textContent ?? '{}');
  const imageUrls = new Map();
  root.querySelectorAll('img[data-report-image]').forEach(image => {
    const ref = image.dataset.reportImage;
    if (!imageData[ref] && !imageUrls.has(ref)) return;
    if (!imageUrls.has(ref)) {
      const [header, encoded] = imageData[ref].split(',');
      const bytes = Uint8Array.from(atob(encoded), char => char.charCodeAt(0));
      imageUrls.set(ref, URL.createObjectURL(new Blob([bytes], { type: header.slice(5, -7) })));
      delete imageData[ref];
    }
    image.src = imageUrls.get(ref);
  });
  const text = (node, selector) => (selector ? node?.querySelector(selector) : node)?.textContent?.trim() ?? '';
  const button = (label, action) => {
    const node = document.createElement('button');
    node.type = 'button'; node.textContent = label; node.dataset.reportAction = action;
    return node;
  };
  const find = id => {
    try { id = decodeURIComponent(id); } catch { /* An old unencoded ID may contain %. */ }
    const node = document.getElementById(id);
    return node && root.contains(node) ? node : null;
  };
  function selectScheme(id) {
    root.dataset.activeScheme = id;
    root.querySelectorAll('[data-scheme-panel],[data-matrix-result]').forEach(panel => {
      panel.hidden = root.dataset.reportReading !== "complete" && (panel.dataset.schemePanel ?? panel.dataset.matrixResult) !== id;
    });
    root.querySelectorAll('[data-report-scheme]').forEach(tab => {
      const selected = tab.dataset.reportScheme === id;
      tab.setAttribute('aria-selected', String(selected)); tab.tabIndex = selected ? 0 : -1;
    });
    root.querySelectorAll('tr[data-scheme-ids]').forEach(row => {
      row.classList.toggle('report-out-of-scheme', !row.dataset.schemeIds.split(' ').includes(id));
    });
    root.querySelectorAll('[data-report-scheme-select]').forEach(select => { select.value = id; });
  }
  function pinOffset() {
    const bar = document.querySelector('.standalone-toolbar');
    if (bar) root.style.setProperty('--report-sticky', bar.getBoundingClientRect().height + 'px');
  }
  pinOffset();
  window.addEventListener('resize', pinOffset);

  // One modal, with a local trail. Following another reference never moves the report.
  let modal = null, body = null, heading = null, back = null, footer = null;
  let origin = null, originTop = 0, originLeft = 0, overflow = '', trail = [], current = null;
  let disposePatentReader = () => {};
  function clone(target, expand = true) {
    const copy = target.cloneNode(true);
    for (const node of [copy, ...copy.querySelectorAll('[id]')]) node.removeAttribute('id');
    copy.querySelectorAll('dialog').forEach(node => node.remove());
    copy.hidden = false;
    if (copy.tagName === 'DETAILS') copy.open = true;
    if (expand) copy.querySelectorAll('details').forEach(node => { node.open = true; });
    // 只显露请求的目标，内部原文库与对照仓库继续隐藏。
    decorate(copy);
    return copy;
  }
  function decorate(container) {
    container.querySelectorAll('a[href^="#"],[data-report-cell-open],a[data-external-link]').forEach(link => {
      const destination = find((link.getAttribute('href') ?? '').slice(1));
      if (link.hasAttribute('data-report-chapter-link') || destination?.matches('[data-report-part],.report-cover')) return;
      link.setAttribute('aria-haspopup', 'dialog');
      link.title = tr("在弹窗中查看，保留当前阅读位置");
    });
  }
  decorate(root);
  function ensureModal(opener) {
    if (modal) return;
    origin = opener; originTop = window.scrollY; originLeft = window.scrollX;
    overflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    modal = document.createElement('dialog');
    modal.className = 'report-cell-dialog report-row-popup report-reader-dialog';
    modal.dataset.rowCard = '';
    modal.setAttribute('aria-label', tr("报告详情"));
    const head = document.createElement('header');
    back = button(tr("← 返回上一层"), 'back'); back.hidden = true;
    heading = document.createElement('h3');
    const close = button(tr("关闭"), 'close'); close.autofocus = true;
    close.setAttribute('aria-label', tr("关闭弹窗，继续阅读")); close.title = tr("关闭（Esc）");
    head.append(back, heading, close);
    body = document.createElement('div'); body.className = 'report-cell-dialog-body'; body.tabIndex = -1;
    footer = document.createElement('footer');
    const hint = document.createElement('span'); hint.textContent = tr("Esc 关闭 · 关闭后继续原位置阅读");
    footer.append(hint, button(tr("关闭，继续阅读"), 'close'));
    modal.append(head, body, footer); root.append(modal);
    modal.addEventListener('cancel', event => { event.preventDefault(); modal.close(); });
    modal.addEventListener('close', () => {
      disposePatentReader(); disposePatentReader = () => {};
      const old = modal; modal = null; trail = []; current = null;
      old.remove(); document.body.style.overflow = overflow;
      if (window.scrollY !== originTop || window.scrollX !== originLeft) window.scrollTo({top:originTop,left:originLeft,behavior:'instant'});
      if (origin?.isConnected) origin.focus({preventScroll:true});
    }, {once:true});
    modal.showModal(); close.focus({preventScroll:true});
  }
  function groupFor(link) {
    const group = link?.closest('.report-matrix-judgment,.report-check,.report-decisive-difference,td,.report-inline-figure') ?? link?.parentElement;
    const entries = [...(group?.querySelectorAll('a[href^="#evidence-"]') ?? [])]
      .map(a => find(a.getAttribute('href').slice(1))).filter(Boolean);
    return [...new Set(entries)];
  }
  function contextFor(link) {
    const group = link?.closest('.report-matrix-judgment,.report-check,.report-decisive-difference');
    if (!group) return null;
    const context = document.createElement('details'); context.className = 'report-popup-context'; context.open = window.innerWidth > 640;
    const summary = document.createElement('summary'); summary.textContent = tr("当前核对点与文献事实");
    if (typeof evidencePoint === 'function') {
      const point = evidencePoint(root, link);
      context.dataset.featureTitle = point.title;
      context.dataset.judgment = point.status;
    }
    context.append(summary);
    const nodes = group.querySelectorAll(':scope > p,dt,.report-fact,.report-check-reason,.report-map-facts');
    nodes.forEach(node => context.append(clone(node, false)));
    return nodes.length ? context : null;
  }
  function openTarget(target, link, options = {}) {
    ensureModal(link);
    if (current && !options.replace) {
      // 双栏原文各自滚动，返回上一层时同时恢复，不能只记外层 body。
      trail.push({...current, top:body.scrollTop, focus:document.activeElement,
        completeIndex:body.dataset.completeEntry,
        completeTop:body.querySelector('.report-complete-source-pane')?.scrollTop ?? 0,
        analysisTop:body.querySelector('.report-complete-analysis')?.scrollTop ?? 0,
        sourceTop:body.querySelector('.report-citation-pane')?.scrollTop ?? 0,
        contextTop:body.querySelector('.report-citation-sidebar')?.scrollTop ?? 0});
    }
    const entries = options.entries ?? (target.matches('.report-evidence,[id^="evidence-"]') ? groupFor(link) : []);
    if (target.matches('.report-evidence,[id^="evidence-"]') && !entries.includes(target)) entries.push(target);
    current = {target, entries, context:options.context ?? contextFor(link)};
    renderCurrent();
    // Keyboard users can immediately read the new content; evidence tabs retain focus when switching.
    if (options.focusTab) body.querySelector('[role="tab"][aria-selected="true"]')?.focus({preventScroll:true});
  }
  function renderCurrent() {
    const {target, entries, context} = current;
    disposePatentReader(); disposePatentReader = () => {};
    if (typeof resetComparisonReader === 'function') resetComparisonReader(modal, heading);
    delete body.dataset.completeEntry;
    body.replaceChildren(); modal.classList.remove('report-image-zoomed', 'report-citation-reader');
    back.hidden = !trail.length;
    const isEvidence = target.matches('.report-evidence,[id^="evidence-"]');
    // 交底上下文按内容决定弹窗高度，避免短引用留下整屏空白。
    modal.classList.toggle('report-disclosure-dialog', target.matches('.report-disclosure-evidence'));
    const isRow = target.tagName === 'TR';
    const doc = target.closest('.report-doc-comparison');
    const title = isEvidence ? text(target, 'h3') : isRow
      ? [text(target,'.report-feature-letter'), text(target,'th strong')].filter(Boolean).join(' ')
      : text(target, ':scope > summary strong,h2,h3,h4,strong') || text(target).slice(0,65) || tr("报告详情");
    heading.textContent = title || tr("逐项对照"); modal.setAttribute('aria-label', heading.textContent);
    if (isRow && typeof renderComparisonReader === 'function' && renderComparisonReader(root, modal, body, heading, target, document.documentElement.lang)) {
      modal.classList.remove('patent-reader-modal');
      body.scrollTop = 0;
      return;
    }
    if (doc && isRow) {
      const caption = document.createElement('p'); caption.className = 'report-popup-document';
      caption.textContent = text(doc, '.report-document-summary'); body.append(caption);
    }
    if (context && isEvidence) body.append(context.cloneNode(true));
    if (isEvidence && entries.length > 1) {
      const tabs = document.createElement('nav'); tabs.className = 'report-popup-tabs';
      tabs.setAttribute('role','tablist'); tabs.setAttribute('aria-label',tr("本条对照的引用依据"));
      entries.forEach((entry, index) => {
        const tab = button((entry.querySelector('img') ? tr("附图 ") : tr("原文 ")) + (index+1), 'evidence');
        tab.dataset.reportEvidenceIndex = index; tab.setAttribute('role','tab');
        tab.setAttribute('aria-selected', String(entry === target)); tab.tabIndex = entry === target ? 0 : -1;
        tab.title = text(entry, 'h3'); tabs.append(tab);
      });
      body.append(tabs);
    }
    const copy = clone(target, isEvidence || isRow || !target.matches('.report-relation-scope,.report-doc-comparison,[data-report-section]'));
    if (isRow) {
      const wrap = document.createElement('div'); wrap.className = 'report-table-wrap report-document-table';
      const table = document.createElement('table'), tbody = document.createElement('tbody');
      tbody.append(copy); table.append(tbody); wrap.append(table); body.append(wrap);
    } else if (target.tagName === 'DIALOG') {
      const oldHead = copy.querySelector(':scope > header'); oldHead?.remove();
      body.append(...copy.childNodes);
    } else body.append(copy);
    // Website names inside a saved passage are labels. The explicit website control below is the only external action.
    if (isEvidence) body.querySelectorAll('h3 a[href^="http"]').forEach(a => {
      const label = document.createElement('strong'); label.textContent = a.textContent; a.replaceWith(label);
    });
    if (isEvidence && body.querySelector('img')) {
      const tools = document.createElement('div'); tools.className = 'report-popup-image-tools';
      tools.append(button(tr("放大附图"), 'zoom')); body.prepend(tools);
    }
    if (isEvidence && typeof renderEvidenceReader === 'function') {
      renderEvidenceReader(modal, body, heading, target, context, entries, document.documentElement.lang);
    }
    body.scrollTop = 0; body.scrollLeft = 0;
    const reader = body.querySelector('.patent-reader');
    modal.classList.toggle('patent-reader-modal', !!reader);
    if (reader && typeof mountPatentReader === 'function') disposePatentReader = mountPatentReader(root, reader);
  }
  function openSource(link) {
    const href = link.getAttribute('href');
    const entries = [...root.querySelectorAll('.report-evidence')].filter(entry => !entry.closest('dialog') &&
      [...entry.querySelectorAll('h3 a[href]')].some(a => a.getAttribute('href') === href));
    // Show local evidence first: this also works offline and doesn't depend on an external site's iframe policy.
    const article = document.createElement('article');
    const h = document.createElement('h3'); h.textContent = text(link) || tr("文献详情");
    const notice = document.createElement('p'); notice.textContent = entries.length
      ? tr("本报告已保存该文献的以下引用依据，可直接查看原文与附图。") : tr("这份报告未保存该文献的可预览原文。");
    article.append(h,notice);
    entries.forEach((entry, index) => {
      const a = document.createElement('a'); a.href = '#' + entry.id;
      a.className = 'report-source-entry'; a.textContent = (index+1) + '. ' + text(entry,'h3'); article.append(a);
    });
    const external = document.createElement('a'); external.href = href;
    external.target = '_blank'; external.rel = 'noopener noreferrer'; external.dataset.reportWebsite = '';
    external.textContent = tr("在新标签页打开文献网站 ↗"); external.className = 'report-website-option';
    article.append(external); openTarget(article,link);
  }
  function chooseEvidence(index, focusTab = true) {
    const target = current?.entries[index]; if (!target) return;
    openTarget(target, origin, {entries:current.entries,context:current.context,replace:true,focusTab});
  }
  function navigateChapter(id) {
    const element = find(id); if (!element) return;
    const chapterSelect = document.querySelector('[data-report-chapter-select]');
    if (chapterSelect && [...chapterSelect.options].some(option => option.value === id)) chapterSelect.value = id;
    const panel = element.closest('[data-scheme-panel]'); if (panel) selectScheme(panel.dataset.schemePanel);
    for (let parent = element; parent; parent = parent.parentElement) if (parent.tagName === 'DETAILS') parent.open = true;
    element.scrollIntoView({behavior:window.matchMedia?.('(prefers-reduced-motion: reduce)').matches?'instant':'smooth',block:'start'});
  }
  document.addEventListener('keydown', event => {
    const tab = event.target.closest?.('[role="tab"][data-report-evidence-index]');
    if (tab && ['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) {
      event.preventDefault();
      const count = current.entries.length, index = current.entries.indexOf(current.target);
      chooseEvidence(event.key === 'Home' ? 0 : event.key === 'End' ? count-1 : (index+(event.key==='ArrowRight'?1:-1)+count)%count);
      return;
    }
    const target = event.target.closest?.('[data-report-scheme]');
    if (!target || !['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
    const tabs = [...target.parentElement.querySelectorAll('[data-report-scheme]')];
    const index = event.key === 'Home' ? 0 : event.key === 'End' ? tabs.length-1
      : (tabs.indexOf(target)+(event.key==='ArrowRight'?1:-1)+tabs.length)%tabs.length;
    event.preventDefault(); selectScheme(tabs[index].dataset.reportScheme); tabs[index].focus();
  });
  let collapsedState = null;
  document.addEventListener('click', event => {
    const target = event.target instanceof Element ? event.target : null;
    if (!target) return;
    const action = target.closest('[data-report-action]');
    if (action) {
      const name = action.dataset.reportAction;
      if (name === 'close') modal?.close();
      if (name === 'back' && trail.length) {
        const previous = trail.pop(); current = previous; renderCurrent(); body.scrollTop = previous.top;
        const sourcePane = body.querySelector('.report-citation-pane');
        const contextPane = body.querySelector('.report-citation-sidebar');
        if (sourcePane) sourcePane.scrollTop = previous.sourceTop;
        if (contextPane) contextPane.scrollTop = previous.contextTop;
        if (previous.completeIndex != null) {
          body.querySelectorAll('.report-complete-tabs button')[Number(previous.completeIndex)]?.click();
          const completePane = body.querySelector('.report-complete-source-pane');
          const analysis = body.querySelector('.report-complete-analysis');
          if (completePane) completePane.scrollTop = previous.completeTop;
          if (analysis) analysis.scrollTop = previous.analysisTop;
        }
        // Focus an equivalent control if it survived the rerender; otherwise focus the reading panel.
        body.focus({preventScroll:true});
      }
      if (name === 'evidence') chooseEvidence(Number(action.dataset.reportEvidenceIndex));
      if (name === 'zoom') {
        const zoomed = modal.classList.toggle('report-image-zoomed');
        action.textContent = zoomed ? tr("适应宽度") : tr("放大附图"); action.setAttribute('aria-pressed',String(zoomed));
      }
      return;
    }
    if (target === modal) {
      const r = modal.getBoundingClientRect();
      if (event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom) modal.close();
      return;
    }
    const scheme = target.closest('[data-report-scheme]');
    if (scheme) { selectScheme(scheme.dataset.reportScheme); return; }
    const cell = target.closest('[data-report-cell-open]');
    if (cell) { const entry = find(cell.dataset.reportCellOpen); if (entry) openTarget(entry,cell); return; }
    const cellClose = target.closest('[data-report-cell-close]');
    if (cellClose) { modal?.close(); return; }
    const close = target.closest('[data-report-close-document]');
    if (close) {
      const record = close.closest('.report-doc-comparison');
      if (record) { record.open = false; record.querySelector('summary')?.focus({preventScroll:true}); record.scrollIntoView({behavior:'smooth',block:'start'}); }
      return;
    }
    const toggle = target.closest('[data-report-matrix-toggle]');
    if (toggle) {
      const group = toggle.closest('.report-doc-comparison') ?? toggle.closest('.report-saas-matrix');
      const details = [...(group?.querySelectorAll('td details.evidence-details') ?? [])];
      const open = details.some(item => !item.open); details.forEach(item => { item.open = open; });
      toggle.textContent = open ? tr("收起全部证据") : tr("展开全部证据"); toggle.setAttribute('aria-expanded',String(open)); return;
    }
    const expand = target.closest('[data-report-expand-all]');
    if (expand) {
      const open = expand.getAttribute('aria-pressed') !== 'true';
      if (open) {
        collapsedState = [...root.querySelectorAll('details')].map(element => [element,element.open]);
        collapsedState.forEach(([element]) => { element.open = true; });
      } else { collapsedState?.forEach(([element,state]) => { element.open = state; }); collapsedState = null; }
      root.classList.toggle('report-all-schemes',open); expand.setAttribute('aria-pressed',String(open));
      expand.textContent = open ? tr("恢复分层阅读") : tr("展开全文"); return;
    }
    const link = target.closest('a[href]');
    if (!link || !root.contains(link)) return;
    const href = link.getAttribute('href');
    if (href.startsWith('#')) {
      event.preventDefault();
      const entry = find(href.slice(1));
      if (entry && (link.hasAttribute('data-report-chapter-link') || entry.matches('[data-report-part],.report-cover'))) {
        if (link.dataset.reportFocusScheme) selectScheme(link.dataset.reportFocusScheme);
        navigateChapter(entry.id);
        entry.tabIndex = -1; entry.focus({preventScroll:true});
      } else if (entry) openTarget(entry,link);
    } else if (/^https?:\/\//i.test(href) && !link.hasAttribute('data-report-website')) {
      event.preventDefault(); openSource(link);
    }
  });
  document.addEventListener('change', event => {
    if (event.target.matches?.('[data-report-chapter-select]')) navigateChapter(event.target.value);
    if (event.target.matches?.('[data-report-scheme-select]')) selectScheme(event.target.value);
    if (event.target.matches?.('[data-report-fold-toggle]')) event.target.closest('[data-fold-gaps]')?.toggleAttribute('data-fold-open', event.target.checked);
  });
})();
