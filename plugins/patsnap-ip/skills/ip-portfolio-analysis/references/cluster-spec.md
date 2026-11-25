# 专利集群设计规范

> 本文档定义了专利布局报告中"专利集群设计"章节的标准展示结构、内容规范和CSS样式体系。

---

## 一、核心设计理念

**三层递进式信息架构：让领导一目了然**

| 层级 | 展示内容 | 用户感受 |
|------|---------|---------|
| 第1层：全局总览 | 三集群横排卡片（策略名/件数/模块标签）| 一眼看清全局框架 |
| 第2层：集群框架树 | 核心→改进→外围节点树，颜色区分状态 | 理解分解思路和布局路线 |
| 第3层：专利明细卡片 | 申请号+技术特征+摘要附图+法律状态 | 感受落地细节和可执行性 |

---

## 二、第1层：全局总览

### 单一策略原则

**每个集群只采用一种核心策略**，不混用多种策略。

| 策略名 | 适用场景 | 示例 |
|--------|---------|------|
| 地毯式+阶梯式 | 核心技术白点，从宽到窄层层保护 | 集群A：能量管理（全新方向）|
| 组合式·先发布局 | 竞对完全空白，多技术方向组合保护 | 集群B：热管理协同（白点）|
| 包围式·上下游 | 竞对有核心专利，从上游和下游包围 | 集群C：对抗包围（规避+进攻）|
| 保护式·存量强化 | 已有有效专利，周边补全防御体系 | 适用于自有专利较多的领域 |

### 全局总览HTML结构

```html
<!-- 第1层：全局总览 -->
<div class="cv-overview">
  <div class="cvo-item cvo-a">
    <div class="cvo-badge">集群 A</div>
    <div class="cvo-strategy">地毯式+阶梯式布局</div>
    <div class="cvo-title">[集群名称]</div>
    <div class="cvo-meta">
      <span>[件数]件发明</span>
      <span>M3·M4模块</span>
    </div>
    <div class="cvo-note">[一句话策略说明]</div>
  </div>
  <div class="cvo-arrow">→</div>
  <div class="cvo-item cvo-c">...</div>
  <div class="cvo-arrow">→</div>
  <div class="cvo-item cvo-b">...</div>
</div>

<!-- 集群关联关系说明框（必须包含）-->
<div class="cv-relation">
  <h4>集群申请优先顺序与关联逻辑</h4>
  <p>集群A（[策略]）→ 集群C（[策略]）→ 集群B（[策略]）</p>
  <ul>
    <li><strong>A→C关联：</strong>[说明C如何基于A或与A互补]</li>
    <li><strong>C→B关联：</strong>[说明B如何在A/C基础上升维]</li>
  </ul>
</div>
```

### 全局总览CSS

```css
.cv-overview {
  display: flex;
  align-items: stretch;
  gap: 12px;
  margin: 24px 0;
}

.cvo-item {
  flex: 1;
  border-radius: 10px;
  padding: 20px;
  border: 2px solid;
}

/* 集群A：蓝色 */
.cvo-a { border-color: #1677ff; background: #f0f7ff; }
.cvo-a .cvo-badge { background: #1677ff; color: #fff; }

/* 集群B：绿色 */
.cvo-b { border-color: #52c41a; background: #f6ffed; }
.cvo-b .cvo-badge { background: #52c41a; color: #fff; }

/* 集群C：红色/橙色 */
.cvo-c { border-color: #fa8c16; background: #fff7e6; }
.cvo-c .cvo-badge { background: #fa8c16; color: #fff; }

.cvo-arrow {
  display: flex;
  align-items: center;
  font-size: 24px;
  color: #8c8c8c;
}
```

---

## 三、第2层：集群框架树

### 节点状态颜色体系

| 状态 | CSS类 | 左边框色 | 图标 | 适用 |
|------|-------|---------|------|------|
| 授权有效 | `cvn-existing-valid` | `#52c41a` | ✅ | 已有有效专利 |
| 公开审中 | `cvn-existing-pending` | `#1677ff` | 🔵 | 已有审中专利 |
| 已失效 | `cvn-existing-expired` | `#f5222d` | ⚫ | 已失效专利 |
| 拟申请P0 | `cvn-planned-p0` | `#f5222d` | 🚀 | P0级立即申请 |
| 拟申请P1 | `cvn-planned-p1` | `#fa8c16` | 📋 | P1级补充细化 |

> ⚠️ **三处联动原则**：修改专利法律状态时，必须同步更新：
> 1. 框架树节点的CSS类（`cvn-*`）
> 2. 明细卡片的边框类（`cvpc-*`）
> 3. 明细卡片的tags文字

### 框架树HTML结构

```html
<div class="cv-cluster" id="cv-a">
  <div class="cv-cluster-header cv-a-header">
    <span class="cv-cluster-badge">集群 A</span>
    <span>[集群名称]</span>
    <span class="cv-strategy-tag">[单一策略名]</span>
  </div>

  <!-- 节点树 -->
  <div class="cv-nodes">
    <!-- 节点分区：现有专利 -->
    <div class="cv-node-section">
      <div class="cvns-label cvns-existing">📁 现有专利</div>
      <div class="cv-node cvn-existing-valid" data-id="A-E1">
        <div class="cvn-icon">✅</div>
        <div class="cvn-content">
          <div class="cvn-id">A-E1</div>
          <div class="cvn-title">[专利简称]</div>
          <div class="cvn-meta">[申请号] · M[X]模块</div>
        </div>
      </div>
    </div>

    <!-- 连接线 -->
    <div class="cv-connector"></div>

    <!-- 节点分区：拟申请专利 -->
    <div class="cv-node-section">
      <div class="cvns-label cvns-planned">🚀 拟申请专利</div>
      <div class="cv-node cvn-planned-p0" data-id="A-1">
        <div class="cvn-icon">🚀</div>
        <div class="cvn-content">
          <div class="cvn-id">A-1 <span class="p-tag p0">P0</span></div>
          <div class="cvn-title">[专利名称]</div>
          <div class="cvn-meta">M[X]模块 · 立即申请</div>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 四、第3层：专利明细卡片

### 卡片类型

| 类型 | CSS类 | 适用 |
|------|-------|------|
| 有效专利 | `cvpc-valid` | 授权有效，绿色左边框 |
| 审中专利 | `cvpc-pend` | 公开审中，蓝色左边框 |
| 失效专利 | `cvpc-exp` | 已失效，红色左边框 |
| 拟申请P0 | `cvpc-plan-p0` | 橙色左边框，🚀标识 |
| 拟申请P1 | `cvpc-plan-p1` | 黄色左边框，📋标识 |

### 明细卡片HTML结构

```html
<div class="cv-patent-card cvpc-valid">
  <!-- 卡片头部 -->
  <div class="cvpc-header">
    <div class="cvpc-id">A-E1</div>
    <div class="cvpc-title">[专利完整名称]</div>
    <div class="cvpc-badge st-valid">✅ 授权有效</div>
  </div>

  <!-- 申请号信息 -->
  <div class="cvpc-meta">
    <span class="cvpc-appno">[申请号]</span>
    <span class="cvpc-date">申请日：[YYYY-MM-DD]</span>
  </div>

  <!-- 摘要附图（真实专利图或SVG示意图）-->
  <div class="cvpc-figure">
    <!-- 已取得的原图可转成data URI；无原图时使用下方SVG -->
    <img src="[已有本地原图的data URI]" alt="[专利名称]摘要附图"
         onerror="this.parentElement.innerHTML='<div class=\'fig-fallback\'>未取得本地原图，使用分析示意图</div>'">
    <!-- 或SVG示意图（注明分析示意，非原始专利附图）-->
    <svg viewBox="0 0 300 180" xmlns="http://www.w3.org/2000/svg">
      <!-- SVG内容 -->
    </svg>
  </div>

  <!-- 技术特征（3—4条）-->
  <div class="cvpc-features">
    <div class="cvpc-feat-title">核心技术特征</div>
    <ul>
      <li>特征1：[具体描述]</li>
      <li>特征2：[具体描述]</li>
      <li>特征3：[具体描述]</li>
    </ul>
  </div>

  <!-- 标签 -->
  <div class="cvpc-tags">
    <span class="tag tag-green">M[X] [模块名]</span>
    <span class="tag tag-gray">⚫ 法律状态</span>
  </div>
</div>
```

### SVG示意图规范（拟申请专利）

当无法获取真实摘要图时，必须提供SVG技术示意图，不可使用空白占位或emoji图标。

**SVG规范：**
- viewBox: `0 0 300 180`
- 背景色：`#f0f7ff`（浅蓝）
- 主色：`#1677ff`（流程图框）
- 箭头：`→`（文字）或 `<marker>` 箭头
- 内容：信号流图/架构图/时序对比图（选择最能说明技术方案的类型）
- 每张图包含：至少3个组件框 + 连接箭头 + 简短标签

**SVG类型选择指南：**

| 技术类型 | 推荐SVG类型 | 示例 |
|---------|-----------|------|
| 控制策略/算法 | 信号流图（输入→处理→输出）| 变换/调节类控制策略 |
| 系统架构 | 架构框图（组件+连接）| 多功能控制器集成 |
| 时序优化 | 时序对比图（优化前vs优化后）| 意图预判/提前介入类 |
| 能量与热流 | 流路径图（源→传导→目标）| 余热回收与预热类 |
| 安全/冗余 | 层级降级图（一级→二级→三级）| 故障冗余控制 |

---

## 五、章节末尾统计栏

```html
<div class="cv-summary-bar">
  <div class="cv-sum-item">
    <span class="cv-sum-num">[总件数]件</span>
    <span class="cv-sum-label">集群总规划</span>
  </div>
  <div class="cv-sum-item">
    <span class="cv-sum-num">[发明件数]件发明 + [实用新型件数]件实用新型</span>
    <span class="cv-sum-label">专利类型构成</span>
  </div>
  <div class="cv-sum-item">
    <span class="cv-sum-num">A→C→B</span>
    <span class="cv-sum-label">建议申请顺序</span>
  </div>
  <div class="cv-sum-item">
    <span class="cv-sum-num">[目标局别]</span>
    <span class="cv-sum-label">建议申请局</span>
  </div>
</div>
```

---

## 六、件数一致性检查规则

集群设计章节完成后，必须执行以下检查：

```
集群A件数 = 现有专利数(A-E*) + 拟申请专利数(A-1...A-N)
集群B件数 = 现有专利数(B-E*) + 拟申请专利数(B-1...B-N)
集群C件数 = 现有专利数(C-E*) + 拟申请专利数(C-1...C-N)

总件数 = 集群A件数 + 集群B件数 + 集群C件数

必须与以下4处一致：
□ 封面指标卡"建议申请专利：X件"（仅统计拟申请部分）
□ 核心结论"X件集群布局"
□ 全局总览每个集群卡片的件数标注
□ 统计栏数字
```

---

## 七、分层色阶规范（核心/改进/外围）

集群内部专利按层次使用不同色阶，帮助评审人快速理解保护结构：

| 层次 | CSS类 | 背景色 | 边框色 | 说明 |
|------|-------|-------|-------|------|
| 核心专利（1件）| `cvpc-core` | `#e6f0ff` | `#1677ff` 2px粗 | 最宽保护范围，宏观框架 |
| 改进专利（3—4件）| `cvpc-improve` | `#f0f7ff` | `#69b1ff` 1.5px | 具体技术方案改进 |
| 外围专利（2—3件）| `cvpc-peripheral` | `#fafafa` | `#d0e8ff` 1px细 | 应用场景/防御性保护 |
