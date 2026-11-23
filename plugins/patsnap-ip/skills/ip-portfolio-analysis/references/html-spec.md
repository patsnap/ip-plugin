# HTML portfolio report style and structure

Applies across R&D topics. Default labels/prose to English and set html lang="en"; honor explicit alternate output language consistently.

## Layout and palette

```html
<body>
  <nav id="sidebar"><!-- Fixed left navigation, 240px --></nav>
  <main class="content"><!-- margin-left:240px -->
    <header class="hero"><!-- Cover --></header>
    <section id="s-conc"><!-- Key conclusions --></section>
    <section id="s-tech"><!-- Technical decomposition --></section>
    <!-- Include all 13 required report sections. -->
    <section id="s-appendix"><!-- Executable queries --></section>
  </main>
</body>
```

| Variable | Value | Use |
|---|---|---|
| --blue | #1677ff | Links/active state |
| --blue-dark | #0d3b8c | Cover |
| --blue-light | #e8f4ff | Information background |
| --green | #52c41a | Active/success/coverage √ |
| --orange | #fa8c16 | Warning/partial coverage ▲ |
| --red | #f5222d | Danger/inactive; matrix × only means not found within verified scope |
| --gray | #8c8c8c | Secondary text |
| --bg | #f5f7fa | Page |
| --border | #e8ecf0 | Borders |

Status text/background/border: Active #389e0d/#f6ffed/#b7eb8f; Pending #096dd9/#e6f7ff/#91d5ff; Inactive #a8071a/#fff1f0/#ffadd2; Proposed #d46b08/#fff7e6/#ffd591. Priorities P0/P1/P2 use white on #f5222d/#fa8c16/#52c41a respectively. Pair color with text.

## Cover and conclusions

```css
.hero{background:linear-gradient(135deg,#0d1b2e 0%,#1a3a5c 50%,#0d3b8c 100%);color:#fff;padding:60px 48px 48px}
```

Five metric cards: Proposed filings (planned only), P0 innovation directions, Existing patents (individually checked), Priority FTO reviews, Currently active patents. Populate actual counts/units or explicit unavailable status, not invented precision. Reconcile with conclusions/charts/details.

```html
<div class="hero-stats">
  <div class="stat-card"><div class="stat-num">{{PROPOSED_COUNT}}</div><div class="stat-label">Proposed filings</div></div>
  <!-- Repeat for the other four supported metrics. -->
</div>
<div class="conc-card conc-blue">
  <div class="conc-num">Conclusion {{N}}</div><div class="conc-tag">{{LABEL}}</div>
  <p class="conc-text">{{CONCISE_EVIDENCED_CONCLUSION}}</p>
</div>
```

Keep each conclusion concise, normally ≤60 English words, adapting for requested language. conc-red=warning, orange=risk, blue=opportunity, green=action. Replace all placeholders in final delivery.

## Navigation

```css
#sidebar{position:fixed;left:0;top:0;width:240px;height:100vh;background:#0d1b2e;overflow-y:auto;z-index:1000}
```

Six groups: Overview (conclusions/decomposition); Competition (industry/literature, landscape, supply chain); Own portfolio (profile/frontier patents); Strategy (five spaces/design-around/innovations); Plan (matrix/clusters); Appendix (queries).

```javascript
const sections = document.querySelectorAll('section[id]');
let cur = sections[0];
const activate = () => document.querySelectorAll('.nav-link').forEach(a =>
  a.classList.toggle('active', !!cur && a.getAttribute('href') === '#' + cur.id));
activate();
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) cur = e.target; });
  activate();
}, { rootMargin: '-30% 0px -60% 0px' });
sections.forEach(s => obs.observe(s));
```

## Charts

Inline available local ECharts for offline delivery and initialize with echarts.init(dom). Without a local library, use native SVG/HTML preserving data/order/captions; examples are layout references, not a network dependency. Sort bars programmatically ascending; filter zero pie values or use bars. Use graphic captions rather than title.subtext.

```javascript
const sorted = [...raw].sort((a,b) => a.value-b.value);
const option = {
  yAxis:{type:'category',data:sorted.map(d=>d.name)},
  series:[{type:'bar',data:sorted.map(d=>d.value)}],
  graphic:[{type:'text',left:'center',bottom:5,
    style:{text:'Scope: '+scopeNote,fontSize:11,fill:'#888'}}]
};
```

## Matrix

Use layout-report-method.md's canonical separate fields, not a combined symbol for current coverage/future plans. Header example:

```html
<thead><tr>
<th>Category / direction</th><th>Patent type</th><th>Existing coverage</th>
<th>Future action</th><th>Evidence status</th><th>Strategy</th>
<th>Verified existing rights regions</th><th>Proposed filing regions</th>
</tr></thead>
```

```css
.lm-check{color:#389e0d;font-size:20px;font-weight:700}
.lm-partial{color:#d46b08;font-size:20px;font-weight:700}
.lm-no{color:#cf1322;font-size:20px;font-weight:700}
```

Include text: “Symbols indicate existing coverage; existing rights and proposed regions are separate. Pending evidence is ?, not ×.” Cluster cards follow cluster-spec.md.

## Query appendix

```css
.formula-block{background:#0d1b2e;color:#a8d8ff;font-family:Consolas,Monaco,monospace;font-size:13px;line-height:1.7;padding:20px 24px;border-radius:8px;overflow-x:auto;white-space:pre}
```

Label S0 (seed terminology check), FINAL_BALANCED_EXPANDED, NOISE_TOTAL_EXPANDED and applicable FINAL_PRECISION_EXPANDED clearly. Precision must be fully expanded, never “see balanced query.” Only verified syntax is labeled executable.

## Avoid

Use ASCII commas in JSON, not full-width punctuation. Do not rely on expired signed images or assume a fixed lifetime; embed already acquired permitted local originals with provenance, otherwise labeled SVG. Define every used CSS class and remove unused ones. Every navigation href needs a real ID. Exclude zero pie slices. Write syntactically valid JavaScript regardless of comment language.
