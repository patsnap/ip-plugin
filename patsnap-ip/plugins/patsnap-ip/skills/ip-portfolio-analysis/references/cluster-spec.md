# Patent cluster design specification

## Three levels

1. Overall horizontal cluster cards: strategy, count and modules.
2. Core→improvement→peripheral framework tree, separating existing/proposed states.
3. Patent cards: application identity, technical features, drawing and legal status.

Use actual evidenced/applicable clusters. The three-cluster A/B/C layout is a template, not permission to invent three clusters.

## Overall strategy

Each cluster has one coherent core strategy. Examples: dense layered protection for a verified new direction; complementary first-mover combination; upstream/downstream surrounding of competitor cores; reinforcement around existing rights. “Blank space” requires bounded evidence, not an absolute no-patents claim.

```html
<div class="cv-overview">
  <div class="cvo-item cvo-a">
    <div class="cvo-badge">Cluster A</div>
    <div class="cvo-strategy">{{CORE_STRATEGY}}</div>
    <div class="cvo-title">{{CLUSTER_NAME}}</div>
    <div class="cvo-meta"><span>{{ACTUAL_COUNT_AND_UNIT}}</span><span>{{MODULES}}</span></div>
    <div class="cvo-note">{{ONE_SENTENCE_STRATEGY}}</div>
  </div>
  <div class="cvo-arrow">→</div>
  <!-- Add applicable C/B cards using actual cluster evidence. -->
</div>
<div class="cv-relation">
  <h4>Filing priorities and cluster relationships</h4>
  <p>{{EVIDENCED_SEQUENCE}}</p>
  <ul><li>{{HOW_EACH_CLUSTER_BUILDS_ON_OR_COMPLEMENTS_THE_OTHERS}}</li></ul>
</div>
```

```css
.cv-overview{display:flex;align-items:stretch;gap:12px;margin:24px 0}
.cvo-item{flex:1;border-radius:10px;padding:20px;border:2px solid}
.cvo-a{border-color:#1677ff;background:#f0f7ff}.cvo-a .cvo-badge{background:#1677ff;color:#fff}
.cvo-b{border-color:#52c41a;background:#f6ffed}.cvo-b .cvo-badge{background:#52c41a;color:#fff}
.cvo-c{border-color:#fa8c16;background:#fff7e6}.cvo-c .cvo-badge{background:#fa8c16;color:#fff}
.cvo-arrow{display:flex;align-items:center;font-size:24px;color:#8c8c8c}
```

## Framework tree and synchronized status

| Status | Node class | Border | Icon | Card class |
|---|---|---|---|---|
| Granted/active | cvn-existing-valid | #52c41a | ✅ | cvpc-valid (green) |
| Published/pending | cvn-existing-pending | #1677ff | 🔵 | cvpc-pend (blue) |
| Inactive | cvn-existing-expired | #f5222d | ⚫ | cvpc-exp (red) |
| Proposed P0 | cvn-planned-p0 | #f5222d | 🚀 | cvpc-plan-p0 (orange) |
| Proposed P1 | cvn-planned-p1 | #fa8c16 | 📋 | cvpc-plan-p1 (yellow) |

Any status change updates tree class, card border/badge class and tag text together. A proposed filing is not a legal status or existing right.

```html
<div class="cv-cluster" id="cv-a">
 <div class="cv-cluster-header cv-a-header">
  <span class="cv-cluster-badge">Cluster A</span><span>{{NAME}}</span>
  <span class="cv-strategy-tag">{{SINGLE_CORE_STRATEGY}}</span>
 </div>
 <div class="cv-nodes">
  <div class="cv-node-section">
   <div class="cvns-label cvns-existing">Existing patents</div>
   <div class="cv-node cvn-existing-valid" data-id="A-E1">
    <div class="cvn-icon">✅</div><div class="cvn-content">
     <div class="cvn-id">A-E1</div><div class="cvn-title">{{SHORT_TITLE}}</div>
     <div class="cvn-meta">{{APPLICATION_NUMBER}} · {{MODULE}}</div>
    </div>
   </div>
  </div>
  <div class="cv-connector"></div>
  <div class="cv-node-section">
   <div class="cvns-label cvns-planned">Proposed filings</div>
   <div class="cv-node cvn-planned-p0" data-id="A-1">
    <div class="cvn-icon">🚀</div><div class="cvn-content">
     <div class="cvn-id">A-1 <span class="p-tag p0">P0</span></div>
     <div class="cvn-title">{{PROPOSED_TITLE}}</div>
     <div class="cvn-meta">{{MODULE}} · {{EVIDENCE_QUALIFIED_DISPOSITION}}</div>
    </div>
   </div>
  </div>
 </div>
</div>
```

## Detail cards

```html
<div class="cv-patent-card cvpc-valid">
 <div class="cvpc-header">
  <div class="cvpc-id">A-E1</div><div class="cvpc-title">{{FULL_TITLE}}</div>
  <div class="cvpc-badge st-valid">Granted / active</div>
 </div>
 <div class="cvpc-meta"><span class="cvpc-appno">{{APPLICATION_NUMBER}}</span>
 <span class="cvpc-date">Filed: {{YYYY_MM_DD}}</span></div>
 <div class="cvpc-figure">{{ACQUIRED_ORIGINAL_IMAGE_OR_LABELED_SVG}}</div>
 <div class="cvpc-features"><div class="cvpc-feat-title">Core technical features</div>
 <ul><li>{{FEATURE_1}}</li><li>{{FEATURE_2}}</li><li>{{FEATURE_3}}</li></ul></div>
 <div class="cvpc-tags"><span class="tag tag-green">{{MODULE}}</span>
 <span class="tag tag-gray">{{VERIFIED_STATUS}}</span></div>
</div>
```

Use 3–4 concrete features with actual evidence, not padding. Original images may be embedded from already acquired permitted local files with source retained. Missing originals require a technical SVG labeled “Analytical illustration, not an original patent drawing,” not a blank placeholder or emoji. Do not claim an image is an original merely because a media URL exists.

SVG: viewBox 0 0 300 180, #f0f7ff background, #1677ff boxes, arrows/markers and short English labels (or requested language). Aim for at least three meaningful components with links, without inventing unsupported structure. Choose signal flow for algorithms, component architecture for systems, before/after timing for timing changes, source/path/target for energy/heat, and tiered fallback for redundancy.

## Summary and count checks

Summary bar: total cluster plan, invention/utility-model composition, proposed sequence (e.g. A→C→B only if supported), target offices.

For each cluster: total = existing A-E* + proposed A-1…A-N. Overall total sums actual clusters with shared-object counting disclosed. Reconcile cover proposed-filings count (proposed only), core conclusions, overview cards and summary bar; do not confuse existing+proposed totals with new filing counts.

## Protection layers

Typical illustration, not mandatory counts: one core (cvpc-core, #e6f0ff, 2px #1677ff border), three/four improvements (cvpc-improve, #f0f7ff, 1.5px #69b1ff), two/three peripheral applications/defense (cvpc-peripheral, #fafafa, 1px #d0e8ff). Actual evidence/implementation controls count and scope. Define used classes in final HTML, remove examples/placeholders and retain status/layer meanings separately.
