# 智慧芽插件市场

面向研发与知识产权团队的插件市场，提供专利检索、分析与报告工作流。

## 目录结构

```text
s-search-agent-plugins/
├── .codebuddy-plugin/marketplace.json # WorkBuddy / CodeBuddy 市场
├── .claude-plugin/marketplace.json    # Claude Code 市场
├── .agents/plugins/marketplace.json   # Codex 市场
├── plugins/
│   └── patsnap-ip/
│       ├── plugin.json              # 标准插件清单
│       ├── mcp.json                 # 标准 MCP 配置
│       ├── .codebuddy-plugin/plugin.json # WorkBuddy / CodeBuddy 插件清单
│       ├── .claude-plugin/plugin.json    # Claude Code 插件清单
│       ├── .codex-plugin/plugin.json     # Codex 插件清单
│       ├── .mcp.json                 # 兼容客户端的 MCP 配置
│       └── skills/
│           ├── competitive-patent-analysis/  # 竞对专利分析
│           ├── patent-search-report-reviewer/  # 专利检索报告审核
│           ├── ip-novelty-search/  # 查新检索
│           ├── ip-portfolio-analysis/  # 专利布局分析
│           ├── ip-innovation-harvesting/  # 专利挖掘
│           ├── ip-fto-search/  # 防侵权检索
│           └── ip-eou-investigation/  # 侵权线索发现
├── .gitignore
├── SKILL_MAINTENANCE.md              # Skill 编写、工具适配与维护规则
└── README.md
```

在 `patsnap-plugins` 市场中，各客户端统一使用插件标识 `patsnap-ip-plugin`。

## MCP 说明

`plugins/patsnap-ip/mcp.json` 与兼容配置 `.mcp.json` 定义同一个 `patsnap-ip` 服务，分别使用 `streamable-http` 和 `http` 传输标识，连接地址保持一致：

```text
https://connect.zhihuiya.com/2b0355/logic-mcp
```

客户端所在网络需要能够访问该服务。Skills 围绕专利检索、文献、全文、法律记录和聚合分析工具定义工作流程；工具参数以实际暴露的 schema 为准。

## Skill 说明

MCP 提供工具能力，Skill 定义调用流程，两者由 `plugin.json` 关联并随插件一起分发。

当前插件版本 **0.10.7**。
中文版使用 `main`，英文版使用 `release-en`。

### competitive-patent-analysis：竞对专利分析

文件：[SKILL.md](plugins/patsnap-ip/skills/competitive-patent-analysis/SKILL.md)

分析单一企业或集团的优势技术、技术路线及专利布局演进，解读代表专利并生成 HTML 研判报告。

### patent-search-report-reviewer：专利检索报告审核

文件：[SKILL.md](plugins/patsnap-ip/skills/patent-search-report-reviewer/SKILL.md)

复核已有专利检索、查新、FTO、EoU 或无效检索报告，核查检索策略、文献依据和事实引用，并提供书面审核意见。

### ip-novelty-search：查新检索

文件：[SKILL.md](plugins/patsnap-ip/skills/ip-novelty-search/SKILL.md)

检索已有技术，梳理差异、趋势与证据，形成可复核的立项审查参考。

### ip-portfolio-analysis：专利布局分析

文件：[SKILL.md](plugins/patsnap-ip/skills/ip-portfolio-analysis/SKILL.md)

结合企业自身专利覆盖和竞争态势，规划技术方向、专利组合、申请优先级及目标国家/地区，并生成 HTML 报告。

### ip-innovation-harvesting：专利挖掘

文件：[SKILL.md](plugins/patsnap-ip/skills/ip-innovation-harvesting/SKILL.md)

从研发问题、技术方案或交底材料中发现和完善可专利点，形成技术提案、现有技术差异分析及验证建议。

### ip-fto-search：防侵权检索

文件：[SKILL.md](plugins/patsnap-ip/skills/ip-fto-search/SKILL.md)

围绕产品或技术方案检索潜在专利风险，开展初筛、权项比对和报告分析。

### ip-eou-investigation：侵权线索发现

文件：[SKILL.md](plugins/patsnap-ip/skills/ip-eou-investigation/SKILL.md)

用自有专利调查第三方产品，梳理核心权利要求、检索产品证据，并生成专利与产品的对照矩阵及 HTML 报告。

### 文件职责

- 根目录 `plugin.json` 使用 Agent Plugins 1.0 格式，自动发现 `skills/` 和 `mcp.json`。三份客户端兼容清单共享 `./skills/` 与 `./.mcp.json`，使用同一服务。
- 每个`SKILL.md`说明业务场景、输入、流程、工具选择和交付要求。简短的工具规则直接放入对应步骤；较详细的规则按需放在`references/tool-usage.md`，不要求每个Skill提供独立工具参考文件。完整接口定义以运行时工具声明为准。
- `references/`保存业务方法和输出规范，`assets/`保存模板，`scripts/`保存本地转换程序。
- Skill 目录名与 `SKILL.md` 中的 `name` 保持一致，作为调用标识；`agents/openai.yaml` 的 `interface.display_name` 配置本分支语言的展示名称，并按需保留调用策略。`evals/` 保存业务审核用例，不参与正常报告生成。
- 技术方案查新的本地脚本仅负责报告与回执整理，HTML 渲染需要 `markdown-it-py` 和 `Pillow`；原始响应与本地分析字段分存。

### 交付格式

| Skill | 交付产物 |
|---|---|
| `competitive-patent-analysis` | 可离线打开的单文件 HTML，使用正式模板，代表专利表保留估值和布局国家。 |
| `ip-eou-investigation` | 可独立打开的 HTML，含产品型号与核心保护点的证据矩阵、逐格依据和待核条件。 |
| `ip-fto-search` | 先交付自包含 HTML 预览，内容确认后按所选 HTML、Word、PDF、Markdown 或组合交付。权项比对主表四列。 |
| `ip-novelty-search` | 查新结论与单文件 HTML，含实际检索、逐特征证据、Agent 核查、分别的新颖性/创造性评述及未决事项。 |
| `ip-portfolio-analysis` | 13 章 HTML，布局矩阵八列。行动计划仅在用户要求时提供。 |
| `ip-innovation-harvesting` | 对话用 Markdown，完整报告用浅色 HTML，保留 CP-0 六字段与六个月路线图。 |
| `patent-search-report-reviewer` | 默认三段式 Markdown，指定其他文件格式时保持三段结构。 |

## 安装方式

[Agent直接安装](#agent直接安装) · [WorkBuddy（国内版）](#workbuddy国内版) · [WorkBuddy AI（国际版）](#workbuddy-ai国际版) · [Codex（ChatGPT 桌面端）](#codexchatgpt-桌面端) · [Claude Code（CC）](#claude-codecc)

插件版本为 **0.10.7**。中文版使用 `main`，英文版使用 `release-en`。两个版本共用插件标识 `patsnap-ip-plugin`，同一客户端选择一个语言版本即可。本地安装示例中的 `/absolute/path/s-search-agent-plugins` 请替换为实际仓库路径。

使用检索服务会消耗当前企业的 API 积分，可用工具取决于企业和成员权限。

### Agent直接安装

选择要安装的语言版本，将对应指令复制给 Agent。如果客户端提示需要授权，请按提示完成授权。受模型能力影响，Agent 可能无法完成安装或连接 MCP。遇到问题时，可按下方对应客户端的步骤继续操作。

**中文**

```text
请从 https://github.com/patsnap/ip-plugin 安装中文版插件，连接其 MCP 服务并确认连接成功。
```

**English**

```text
Please install the English plugin from the release-en branch of https://github.com/patsnap/ip-plugin, connect to its MCP server, and verify the connection.
```

#### 安装后验证

安装后新建会话，将对应的验证指令发给 Agent。

**中文**

```text
请确认 patsnap-ip-plugin 已启用、插件技能已加载，并调用一个只读 MCP 工具验证连接；如果需要授权，请提示我，授权后继续验证。
```

**English**

```text
Please confirm that patsnap-ip-plugin is enabled and its skills are loaded, then call one of its read-only MCP tools to verify the connection. If authorization is required, prompt me and resume verification afterward.
```

# WorkBuddy（国内版）

## GitHub 市场安装

1. 打开 **专家·技能·连接器 → 技能 → 套件 → 添加市场**。
2. 在**市场源**中填入 `patsnap/ip-plugin`，点击**提交**。此入口默认安装中文版。
3. 打开 `patsnap-plugins`，找到 `patsnap-ip-plugin`，点击**安装**并启用。

## 本地安装

在终端进入已有仓库，切换到所需语言分支。

```bash
cd /absolute/path/s-search-agent-plugins
git switch main  # 英文版使用 git switch release-en
pwd
```

1. 打开 **专家·技能·连接器 → 技能 → 套件 → 添加市场**。
2. 在**市场源**中填入 `pwd` 输出的仓库根目录，点击**提交**。
3. 在 `patsnap-plugins` 中安装并启用 `patsnap-ip-plugin`。

## 连接智慧芽 MCP

打开 **专家·技能·连接器 → 连接器 → 自定义连接器 → 我的 MCP**，找到来自 `patsnap-ip-plugin` 的 `patsnap-ip`。若显示**需要认证**，点击**连接**，在浏览器中登录智慧芽开放平台并允许访问。返回后看到绿点和已启用工具数，即可新建任务。

# WorkBuddy AI（国际版）

## GitHub 市场安装

1. 打开 **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**。
2. 在 **Marketplace Source** 中填入 `patsnap/ip-plugin`，点击 **Submit**。此入口默认安装中文版。
3. 打开 `patsnap-plugins`，找到 `patsnap-ip-plugin`，点击 **Install** 并启用。

## 本地安装

在终端进入已有仓库，切换到所需语言分支。

```bash
cd /absolute/path/s-search-agent-plugins
git switch main  # 英文版使用 git switch release-en
pwd
```

1. 打开 **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**。
2. 在 **Marketplace Source** 中填入 `pwd` 输出的仓库根目录，点击 **Submit**。
3. 在 `patsnap-plugins` 中安装并启用 `patsnap-ip-plugin`。

## 连接智慧芽 MCP

打开 **Experts · Skills · Connectors → Connectors → Custom connectors → My MCP**，找到标有 **From plugin patsnap-ip-plugin** 的 `patsnap-ip`。若显示 **Needs authentication**，点击 **Connect**，按浏览器提示登录并授权。返回后看到绿点和已启用工具数，即可新建任务。

# Codex（ChatGPT 桌面端）

中文版市场和插件分别显示为 **智慧芽插件市场**、**智慧芽 IP 专家套件**，英文版分别显示为 **Patsnap Plugins**、**Patsnap IP Plugin**。

## GitHub 市场安装

1. 打开 **Plugins → Add → Add a marketplace**。
2. 在 **Source** 中填入 `patsnap/ip-plugin`，在 **Git ref** 中填入 `main`（中文）或 `release-en`（英文）。将 **Sparse paths** 留空，点击 **Add marketplace**。
3. 打开对应语言的市场，选择插件，点击 **Install**。

也可在终端按语言添加 GitHub 市场并安装插件。

```bash
branch=main  # 英文版改为 release-en
codex plugin marketplace add patsnap/ip-plugin --ref "$branch"
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

## 本地安装

在终端进入已有仓库，切换到所需语言分支。

```bash
cd /absolute/path/s-search-agent-plugins
git switch main  # 英文版使用 git switch release-en
pwd
```

1. 打开 **Plugins → Add → Add a marketplace**。
2. 在 **Source** 中填入 `pwd` 输出的仓库根目录。该目录包含 `.agents/plugins/marketplace.json`。点击 **Add marketplace**。
3. 打开对应语言的市场，选择插件，点击 **Install**。

也可在同一仓库根目录使用 CLI 安装，完成后重启桌面端并新建对话。

```bash
codex plugin marketplace add "$(pwd)"
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

## 连接智慧芽 MCP

安装后按浏览器提示登录并授权。如果浏览器没有自动打开，在插件详情页找到 **MCP servers → patsnap-ip**，点击设置齿轮，在 **From plugins** 下点击该服务的 **Authenticate**。浏览器显示 **Authentication complete** 后返回 Codex，确认该行的 **Authenticate** 按钮已消失，再新建对话。

# Claude Code（CC）

## GitHub 市场安装

1. 在 Claude 桌面应用打开 **Customize → Plugins → Discover**，点击 **＋（Add marketplace）→ Add from a repository**。
2. 在 **URL** 中填入 `patsnap/ip-plugin#main`（中文）或 `patsnap/ip-plugin#release-en`（英文），点击 **Sync**。
3. 在 **Personal → patsnap-plugins** 中找到发布者为 **Patsnap** 的插件，点击 **Install**。

也可在本机终端按语言添加 GitHub 市场并安装插件。

```bash
branch=main  # 英文版改为 release-en
claude plugin marketplace add "patsnap/ip-plugin#$branch"
claude plugin install patsnap-ip-plugin@patsnap-plugins --scope user
```

## 本地安装

在终端进入已有仓库，切换到所需语言分支。

```bash
cd /absolute/path/s-search-agent-plugins
git switch main  # 英文版使用 git switch release-en
```

### 安装到后续本地会话

在仓库根目录登记本地市场并安装插件。

```bash
claude plugin marketplace add "$(pwd)"
claude plugin install patsnap-ip-plugin@patsnap-plugins --scope user
```

以同一系统用户打开 **Claude 桌面应用 → Code**，新建本地项目会话。

### 开发调试（仅当前会话）

在仓库根目录运行以下命令，直接加载插件目录。

```bash
claude --plugin-dir "$(pwd)/plugins/patsnap-ip"
```

## 连接智慧芽 MCP

在 Claude 桌面应用打开插件详情 **Connectors → patsnap-ip**。若显示 **Not connected**，点击 **Connect**，按浏览器提示登录并授权。返回连接器详情页，看到 **Connected** 后新建 Code 会话。

# 验证与维护

## 安装后检查

在插件详情确认显示的版本与所选安装来源的插件版本一致。通过市场安装时，来源应为 `patsnap-plugins`。新建任务或会话，确认上文列出的七个 Skill 可用，并选择该插件提供的一项只读工具执行一次查询，检查是否返回结果。

### 维护者验证 MCP 与 Skill 联动

分别验证七个流程：

> 使用智慧芽 IP 专家套件中的 competitive-patent-analysis 技能，为一家指定公司生成技术与专利报告。先按技能要求确认技术方向，再完成检索和报告。

> 使用智慧芽 IP 专家套件中的 patent-search-report-reviewer 技能，审核我提供的专利报告，重点核对检索式与引用专利原文。

> 使用 ip-novelty-search，对我提供的完整方案检索、逐特征对比并核查决定性事实，分别评价新颖性和创造性，生成 HTML；明确实际范围和证据缺口。

> 使用 ip-portfolio-analysis，对指定技术主题和企业进行研发专利布局分析，保留十阶段流程和13章报告。

> 使用 ip-innovation-harvesting，按快速模式挖掘我提供的技术方案，先输出CP-0确认卡，确认后推进四块十步。

> 使用 ip-fto-search，对我提供的技术方案进行FTO检索与分析，落实实际国家与检索语言，筛选后确认CC范围和全文策略，再分批比对并生成报告。

> 使用 ip-eou-investigation，从我方公司及自有专利出发调查指定第三方产品。依次确认公司范围、专利组合、核心保护点和保留线索，交付含型号、逐格证据及待核条件的 HTML。

检查技能是否加载、工具调用与参数是否正确、证据是否可追溯。竞对报告应披露分页、同族与估值限制；审核流程应按争点取证。补充网页材料须记录来源、时点和实际读取范围。

### 常见问题

- **市场添加失败**：使用 GitHub 市场时，确认客户端能访问 [patsnap/ip-plugin](https://github.com/patsnap/ip-plugin)，并核对所填分支。使用本地市场时，确认所选路径指向仓库根目录。
- **Skill 未加载**：检查插件启用状态及 `plugin.json` 中的 `skills` 路径；刷新市场、更新插件后重新打开对话，仍未加载时重启客户端。
- **MCP 连接或调用失败**：检查 MCP 配置中的服务地址与网络连通性，依据实际错误定位问题。

## 维护

客户端适配在同一个分支内共存，不为 Codex 或 Claude Code 长期拆分发布分支。`main` / `release-en` 分别提供中文与英文默认语种和本地化文案，共用交付契约。

Skill 的目录组织、工具适配、文件清理和检查要求见 [Skill 维护说明](SKILL_MAINTENANCE.md)。

- **修改 MCP**：同步编辑 `plugins/patsnap-ip/mcp.json` 和 `.mcp.json`，保持服务名称、地址及连接参数一致。
- **修改 Skill**：编辑 `plugins/patsnap-ip/skills/<skill-name>/SKILL.md` 及其引用资源，更新工具使用流程和结果要求。
- **新增插件**：在 `plugins/` 下创建独立插件目录，并在 `.codebuddy-plugin/marketplace.json`、`.claude-plugin/marketplace.json` 和 `.agents/plugins/marketplace.json` 中同步登记。
- **发布更新**：同步更新标准清单和三份兼容清单的版本号。共同改动先进入 `main`，再同步到 `release-en` 并保留英文默认语种和本地化文案。两版 README 的安装说明和交付规则同步维护。提交并推送后，再让用户刷新市场、更新插件。

### 本地开发打包

在仓库根目录运行以下命令，可从指定分支最近一次提交生成单插件 ZIP，供本地试装。压缩包根目录包含插件清单、MCP 配置和 `skills/`。

```bash
branch=main # 英文版改为 release-en
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

## 按发布标签打包

正式分发使用不可变的发布标签，避免分支后续提交导致同名 ZIP 内容变化。完成版本、RN 和文档的发布提交后，在该提交上创建标签，再从标签导出单插件：

```bash
release_tag=v0.10.7-cn
mkdir -p outputs/releases
git archive --format=zip --output="outputs/releases/patsnap-ip-$release_tag.zip" "$release_tag:plugins/patsnap-ip"
(cd outputs/releases && shasum -a 256 "patsnap-ip-$release_tag.zip" > "patsnap-ip-$release_tag.zip.sha256")
unzip -t "outputs/releases/patsnap-ip-$release_tag.zip"
```

ZIP 根目录包含标准清单、三份隐藏客户端清单、两份 MCP 配置及七个 Skill；不包含仓库市场清单、发布文档或工作区临时文件。将 ZIP 和 `.sha256` 校验文件一起分发。上文按分支打包的方式适合本地开发，正式发布使用此处的标签包。

## 参考

- [WorkBuddy：插件](https://www.workbuddy.cn/docs/workbuddy/Plugins)
- [WorkBuddy AI：快速开始](https://www.workbuddy.ai/docs/workbuddy/Quickstart)
- [Codex（ChatGPT 桌面端）：插件结构与本地市场](https://developers.openai.com/plugins/build/plugins)
- [Codex（ChatGPT 桌面端）：插件界面](https://learn.chatgpt.com/docs/plugins)
- [Codex：CLI 命令](https://learn.chatgpt.com/docs/developer-commands)
- [Claude Code：桌面端插件安装](https://code.claude.com/docs/en/desktop#install-plugins)
- [Claude Code：插件安装与私有市场](https://code.claude.com/docs/en/plugins/install)
- [Claude Code：托管插件市场](https://code.claude.com/docs/en/plugins/host-marketplace)
- [Claude Code：CLI 参考](https://code.claude.com/docs/en/plugins/cli-reference)
- [Git：git archive](https://git-scm.com/docs/git-archive)
