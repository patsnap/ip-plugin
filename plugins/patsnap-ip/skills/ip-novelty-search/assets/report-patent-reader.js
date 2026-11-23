/** 原文阅读器共享交互：只读取渲染后的数据，不请求网络、不修改评价。 */
const patentReaderStates = new WeakMap();

/** 挂载一份弹窗副本；返回清理函数供独立报告和 App 关闭弹窗时使用。 */
export function mountPatentReader(root, reader) {
  if (!reader) return () => {};
  let states = patentReaderStates.get(root);
  if (!states) { states = new Map(); patentReaderStates.set(root, states); }
  const pane = reader.querySelector('.reader-source-pane');
  const buttons = [...reader.querySelectorAll('[data-reader-feature]')];
  if (!pane || !buttons.length) return () => {};
  const key = reader.dataset.readerDocument;
  const saved = states.get(key);
  const remember = () => states.set(key, { feature: reader.dataset.selectedFeature, top: pane.scrollTop });
  const locate = node => {
    if (!node) return;
    pane.scrollTop = Math.max(0, pane.scrollTop + node.getBoundingClientRect().top - pane.getBoundingClientRect().top - 40);
  };
  const select = (number, jump = true) => {
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.readerFeature === number)));
    reader.querySelectorAll('[data-reader-panel]').forEach(panel => { panel.dataset.active = String(panel.dataset.readerPanel === number); });
    reader.querySelectorAll('mark[data-reader-features]').forEach(mark => mark.classList.toggle('reader-mark-active', mark.dataset.readerFeatures.split(' ').includes(number)));
    reader.dataset.selectedFeature = number;
    if (jump) locate([...reader.querySelectorAll('mark[data-reader-features]')].find(mark => mark.dataset.readerFeatures.split(' ').includes(number)));
  };
  select(saved?.feature || buttons[0].dataset.readerFeature, !saved);
  if (saved) pane.scrollTop = saved.top;
  const click = event => {
    const target = event.target instanceof Element ? event.target : null;
    if (!target) return;
    const feature = target.closest('[data-reader-feature]');
    if (feature) select(feature.dataset.readerFeature);
    const ref = target.closest('[data-reader-locate]');
    if (ref) locate([...reader.querySelectorAll('[data-reader-matches]')].find(mark => mark.dataset.readerMatches.split(' ').includes(ref.dataset.readerLocate)));
    const jump = target.closest('[data-reader-section-jump]');
    if (jump) locate([...reader.querySelectorAll('[data-reader-section]')].find(section => section.dataset.readerSection === jump.dataset.readerSectionJump));
    remember();
  };
  // 按钮原生支持 Enter/Space；不劫持原文的方向键滚动。
  reader.addEventListener('click', click);
  pane.addEventListener('scroll', remember);
  remember();
  return () => { remember(); reader.removeEventListener('click', click); pane.removeEventListener('scroll', remember); };
}
