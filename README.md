<div align="center">
  <img src="assets/open-platform-logo.png" alt="Open Platform by Patsnap" width="260">
</div>

# 智慧芽 IP 专家套件

在 AI 助手里检索专利与文献，开展查新、FTO 和专利分析，生成可回溯到原始证据的报告。

[English](https://github.com/patsnap/ip-plugin/tree/release-en) · [v0.10.5-cn](https://github.com/patsnap/ip-plugin/tree/v0.10.5-cn) · [安装](#安装) · [选择 Skill](#选择-skill) · [更新记录](CHANGELOG.md)

| 使用场景 | 可以得到什么 |
| --- | --- |
| 新技术准备立项或申请专利 | 找到接近的现有技术，逐项比对技术特征，分别评述新颖性和创造性 |
| 产品准备进入指定市场 | 筛选潜在专利风险，对用户选定的专利做权利要求比对 |
| 研究竞争对手或规划研发 | 梳理代表专利、技术方向、申请优先级和目标地区 |

## 怎么工作

用自然语言提供技术方案、产品配置或企业名称。对应的 Skill 会明确检索范围，通过智慧芽 MCP 检索和比对证据，再输出带来源、范围和证据缺口说明的结果。

```mermaid
flowchart LR
    A[描述问题] --> B[选择 Skill]
    B --> C[检索和比对证据]
    C --> D[生成带引用的报告]
```

## 效果示例

> 请对这份技术方案做专利查新。先把方案拆成可检索的技术特征，再列出最接近的文献、逐项证据和仍需核查的问题。

建议附上技术交底、关键日期和希望覆盖的地区。查新报告包含检索路线、逐特征证据及新颖性与创造性分析。

## 安装

### Claude Code

```bash
claude plugin marketplace add patsnap/ip-plugin
claude plugin install patsnap-ip-plugin@patsnap-plugins
```

### Codex

```bash
codex plugin marketplace add https://github.com/patsnap/ip-plugin.git --ref main
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

WorkBuddy、CodeBuddy、ChatGPT 自定义 MCP 接入、智慧芽账号登录及排错步骤见 [安装指南](INSTALL.md)。

## 选择 Skill

| 你要做什么 | Skill | 主要交付 |
| --- | --- | --- |
| 申请前查新 | `ip-novelty-search` | 逐特征证据及新颖性、创造性评述 |
| 上市前检索 FTO 风险 | `ip-fto-search` | 风险筛选、权利要求对照表与报告 |
| 了解竞争对手的技术方向 | `competitive-patent-analysis` | 代表专利与技术路线报告 |
| 规划专利布局 | `ip-portfolio-analysis` | 技术方向、申请优先级与目标地区 |
| 从研发成果挖掘发明点 | `ip-innovation-harvesting` | 候选发明、现有技术差异与验证建议 |
| 调查第三方产品的专利实施证据 | `ip-eou-investigation` | 专利与产品证据矩阵及报告 |
| 审核已有检索报告 | `patent-search-report-reviewer` | 对检索策略、文献、事实和引用的书面审核 |

给出准确的产品型号、企业范围、目标法域或日期，可以帮助 Skill 界定检索范围。请核对报告里的专利公开号、原文段落、法律状态和证据缺口，再把结果用于决策。[数据覆盖](https://open.patsnap.com/data-coverage) · [智慧芽信任中心](https://trust.patsnap.com/)

## 常见问题

- **安装成功但看不到工具？** 启用插件、完成账号授权，然后在新会话中确认工具可用。详见[安装指南](INSTALL.md#验证与排错)。
- **报告能否作为法律意见？** 报告提供可复核的证据和研究结论。法律判断需要由合格专业人员结合目标法域和实际情况复核。
- **如何从专利与文献融合检索 MCP 迁移？** 按[安装指南](INSTALL.md)核对客户端的服务配置及工具列表。检索和全文读取分别使用 `search_patent`、`search_literature`、`fetch_patent` 和 `fetch_literature`。

## 支持

使用问题和产品建议可通过 [GitHub Issues](https://github.com/patsnap/ip-plugin/issues) 提交。安全问题请参阅 [SECURITY.md](SECURITY.md)，维护说明见 [SKILL_MAINTENANCE.md](SKILL_MAINTENANCE.md)。
