# HTML 报告样式与结构规范

> 本文档定义了专利布局HTML报告的标准样式体系、组件规范和交互规范。
> 适用于任意研发项目的专利布局报告生成。

---

## 一、整体布局结构

```html
<body>
  <nav id="sidebar">          <!-- 固定左侧导航栏，宽度240px -->
  <main class="content">      <!-- 主内容区，margin-left:240px -->
    <header class="hero">     <!-- 封面区，深蓝渐变背景 -->
    <section id="s-conc">     <!-- 核心结论 -->
    <section id="s-tech">     <!-- 技术主题拆解 -->
    ... (共13个section)
    <section id="s-appendix"> <!-- 附录：检索式 -->
  </main>
</body>
```

---

## 二、颜色体系

### 主色调

| 变量 | 值 | 用途 |
|------|-----|------|
| `--blue` | `#1677ff` | 主色，链接/活跃状态 |
| `--blue-dark` | `#0d3b8c` | 封面背景深色 |
| `--blue-light` | `#e8f4ff` | 信息背景色 |
| `--green` | `#52c41a` | 成功/有效/√符号 |
| `--orange` | `#fa8c16` | 警告/部分覆盖/▲符号 |
| `--red` | `#f5222d` | 危险/失效；矩阵×仅表示当前核验范围未检出 |
| `--gray` | `#8c8c8c` | 次要文字 |
| `--bg` | `#f5f7fa` | 页面背景 |
| `--border` | `#e8ecf0` | 边框色 |

### 语义颜色规范

| 状态 | 文字颜色 | 背景色 | 边框色 |
|------|---------|-------|-------|
| 授权有效 | `#389e0d` | `#f6ffed` | `#b7eb8f` |
| 公开审中 | `#096dd9` | `#e6f7ff` | `#91d5ff` |
| 已失效 | `#a8071a` | `#fff1f0` | `#ffadd2` |
| 拟申请 | `#d46b08` | `#fff7e6` | `#ffd591` |
| P0优先级 | `#fff` | `#f5222d` | — |
| P1优先级 | `#fff` | `#fa8c16` | — |
| P2优先级 | `#fff` | `#52c41a` | — |

---

## 三、封面（Hero）规范

```css
.hero {
  background: linear-gradient(135deg, #0d1b2e 0%, #1a3a5c 50%, #0d3b8c 100%);
  color: #ffffff;
  padding: 60px 48px 48px;
}
```

### 封面必须包含的5个指标卡

```html
<div class="hero-stats">
  <div class="stat-card">
    <div class="stat-num">[集群规划件数]件</div>
    <div class="stat-label">建议申请专利</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">[P0方向数]个</div>
    <div class="stat-label">P0级创新方向</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">[自有专利总量]件</div>
    <div class="stat-label">现有专利（逐件核查）</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">[FTO数量]项</div>
    <div class="stat-label">优先FTO评估</div>
  </div>
  <div class="stat-card">
    <div class="stat-num">[有效件数]件</div>
    <div class="stat-label">当前有效专利</div>
  </div>
</div>
```

> ⚠️ 封面指标卡数字必须与核心结论/图表/详情章节完全一致，生成后必须逐一核查。

---

## 四、左侧导航栏规范

```css
#sidebar {
  position: fixed;
  left: 0; top: 0;
  width: 240px;
  height: 100vh;
  background: #0d1b2e;
  overflow-y: auto;
  z-index: 1000;
}
```

### 导航分组结构（6组）

```
📋 概览
  - 核心结论
  - 技术主题拆解

🔍 竞争格局
  - 行业动态与文献
  - 竞对全量态势
  - 关键供应商与产业链分析

📊 自有专利
  - 自有专利画像
  - 前沿高价值专利

🗺️ 布局策略
  - 五类技术空间
  - 规避设计方案
  - 创新点清单

🏗️ 布局方案
  - 专利布局矩阵
  - 专利集群设计

📎 附录
  - 可执行检索式
```

### 滚动高亮JS（防首屏未激活）

```javascript
const sections = document.querySelectorAll('section[id]');
let cur = sections[0]; // ← 关键：默认激活第一个section

const obs = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) cur = e.target; });
  document.querySelectorAll('.nav-link').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === '#' + cur.id);
  });
}, { rootMargin: '-30% 0px -60% 0px' });

sections.forEach(s => obs.observe(s));
```

---

## 五、核心结论卡片规范

```html
<div class="conc-card conc-[color]">
  <div class="conc-num">结论[N]</div>
  <div class="conc-tag">[标签]</div>
  <p class="conc-text">[结论内容，不超过100字，包含关键数字]</p>
</div>
```

颜色类：`conc-red`（警示）/ `conc-orange`（风险）/ `conc-blue`（机会）/ `conc-green`（行动）

---

## 六、ECharts图表规范

### 通用规则

1. 若工作区已有ECharts本地资源，可内联后通过`echarts.init(dom)`初始化；离线交付时内联所需资源。无本地库时用原生SVG/HTML保留相同图表、数据、排序和图注，后续ECharts片段仅作为布局参考。
2. 条形图数据必须使用 `sort()` 函数排序，不手写顺序
3. 饼图过滤0值项（`data.filter(d => d.value > 0)`）
4. 图注使用 `graphic` 组件展示，不使用 `title.subtext`

### 条形图排序模板

```javascript
const raw = [
  { name: '企业A', value: 411 },
  { name: '企业B', value: 84 },
  // ...
];
const sorted = [...raw].sort((a, b) => a.value - b.value); // 升序
option = {
  yAxis: { type: 'category', data: sorted.map(d => d.name) },
  series: [{ data: sorted.map(d => d.value) }]
};
```

### 图注模板（统计范围说明）

```javascript
graphic: [{
  type: 'text',
  left: 'center',
  bottom: 5,
  style: {
    text: '注：[说明文字]',
    fontSize: 11,
    fill: '#888'
  }
}]
```

---

## 七、专利矩阵表格规范

### 表头结构

使用 [布局方法](layout-report-method.md#布局矩阵格式规范) 的八个独立字段。示例：

```html
<thead><tr>
  <th>技术类别／方向</th><th>专利类型</th><th>已有覆盖</th>
  <th>未来动作</th><th>证据状态</th><th>布局策略</th>
  <th>已有权利的已核验地域</th><th>拟申请地域</th>
</tr></thead>
```

### 符号CSS

```css
.lm-check  { color: #389e0d; font-size: 20px; font-weight: 700; } /* ✓ */
.lm-partial { color: #d46b08; font-size: 20px; font-weight: 700; } /* ▲ */
.lm-no     { color: #cf1322; font-size: 20px; font-weight: 700; } /* × */
```

### 布局地域列注释（必须添加）

符号仅表示已有覆盖。已有权利地域与拟申请地域分列，待核项使用 `?`，已核验未检出使用 `×`。

---

## 八、专利集群卡片规范

见 `references/cluster-spec.md`。

---

## 九、附录检索式规范

### 代码块样式

```css
.formula-block {
  background: #0d1b2e;
  color: #a8d8ff;
  font-family: 'Consolas', 'Monaco', monospace;
  font-size: 13px;
  line-height: 1.7;
  padding: 20px 24px;
  border-radius: 8px;
  overflow-x: auto;
  white-space: pre;
}
```

### 三条展开式标签

```html
<div class="formula-label">S0 · 种子窄式（术语校验）</div>
<pre class="formula-block">...</pre>

<div class="formula-label">FINAL_BALANCED_EXPANDED（平衡式，可直接执行）</div>
<pre class="formula-block">...</pre>

<div class="formula-label">FINAL_PRECISION_EXPANDED（精确式，完全展开）</div>
<pre class="formula-block">...</pre>
```

> ⚠️ `FINAL_PRECISION_EXPANDED` 必须完整展开，不得引用"见FINAL_BALANCED_EXPANDED"等占位写法。

---

## 十、禁止使用的HTML模式

| 禁止模式 | 原因 | 替代方案 |
|---------|------|---------|
| 在图表数据中使用中文逗号（，）| 会破坏JSON解析 | 使用英文逗号（,）|
| 图片src使用已过期签名URL | 签名有效期约24小时，过期后变破图 | 仅使用已有本地图的Base64，缺失时改用注明性质的SVG示意图，不冒充原始附图 |
| CSS class未定义就使用 | 无样式效果 | 每个class先定义后使用 |
| 导航href="#id"但HTML无对应id | 死链 | 添加章节时同步添加导航项 |
| 饼图包含value=0的data项 | 图例与图形不一致 | filter(d => d.value > 0) |
| 在JavaScript中写中文注释后无semicolon | 可能导致解析错误 | 中英文注释后确保语句正常结束 |
