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
│       ├── plugin.json              # 标准插件清单，供 ZIP 上传及兼容客户端读取
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

当前插件版本 **0.10.5**。
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

[WorkBuddy](#workbuddy国内版) · [WorkBuddy AI](#workbuddy-ai国际版) · [Codex（ChatGPT 桌面端）](#codexchatgpt-桌面端) · [Claude Code（CC）](#claude-codecc)

- 中文版：`main`；英文版：`release-en`。两版采用相同的交付格式、章节、必填字段及模板结构。对话和交付默认分别使用中文和英文，用户明确指定语种时优先。检索语言、法域和证据原文独立保留。
- 同一客户端选择一个语言版本安装。两个语言版本在同一客户端使用相同的插件标识。
- 本地安装使用已有仓库目录；示例中的 `/absolute/path/...` 替换为实际路径。GitLab 安装需要公司网络访问权限及 SSH 凭据。
- 命令在终端执行，示例适用于 macOS / Linux / Git Bash。正式版本安装包从[插件版本与安装包](https://xa3hdkuita.feishu.cn/docx/Wc5Dd2mDqoQ3C2xSgYucxWninwb)获取；本地开发打包方式见下文。

### GitHub 市场入口

公开仓库为 [patsnap/ip-plugin](https://github.com/patsnap/ip-plugin)。插件市场标识为 `patsnap-plugins`。按客户端选择语言版本：

| 客户端 | GitHub 市场源与语言版本 |
| --- | --- |
| Codex | Source 填 `patsnap/ip-plugin`，Git ref 按语言填 `main`（中文）或 `release-en`（英文）。 |
| Claude Code | 中文版填 `patsnap/ip-plugin#main`，英文版填 `patsnap/ip-plugin#release-en`。 |
| WorkBuddy 国内版和国际版 | 市场源填 `patsnap/ip-plugin`，默认安装中文版（`main`）。 |

# WorkBuddy（国内版）

## 本地安装

### 界面：Marketplace → 插件

在已有仓库中选择中文或英文分支：

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git switch "$branch"
pwd
```

1. 打开 **专家·技能·连接器 → 技能 → 套件 → 添加市场**。
2. 在 **市场源** 填入 `pwd` 输出的仓库根目录，点击 **提交**。
3. 选择 `patsnap-plugins → patsnap-ip-plugin → 安装`，启用后新建任务。

## GitLab 安装

### 界面：Marketplace → 插件

1. 打开 **专家·技能·连接器 → 技能 → 套件 → 添加市场**。
2. 在 **市场源** 填入以下仓库地址，点击 **提交**。
3. 选择 `patsnap-plugins → patsnap-ip-plugin → 安装`，启用后新建任务。

```text
git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git
```

该方式安装仓库默认分支；选择指定中文 / 英文版本时，在本地切换分支后添加目录。

# WorkBuddy AI（国际版）

## 本地安装

### 界面：Marketplace → 插件

在已有仓库中选择中文或英文分支：

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git switch "$branch"
pwd
```

1. 打开 **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**。
2. 在 **Marketplace Source** 填入 `pwd` 输出的仓库根目录，点击 **Submit**。
3. 选择 `patsnap-plugins → patsnap-ip-plugin → Install`，启用后新建任务。

## GitLab 安装

### 界面：Marketplace → 插件

1. 打开 **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**。
2. 在 **Marketplace Source** 填入以下仓库地址，点击 **Submit**。
3. 选择 `patsnap-plugins → patsnap-ip-plugin → Install`，启用后新建任务。

```text
git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git
```

该方式安装仓库默认分支；选择指定中文 / 英文版本时，在本地切换分支后添加目录。

# Codex（ChatGPT 桌面端）

## 本地安装

### 界面：Marketplace → 插件

中文版市场和插件分别显示为 **智慧芽插件市场**、**智慧芽 IP 专家套件**；英文版分别显示为 **Patsnap Plugins**、**Patsnap IP Plugin**。下文界面名称以中文版为例。

在已有仓库中选择中文或英文分支：

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git switch "$branch"
pwd
```

1. 打开桌面端 **Plugins / 插件 → Add / 添加 → Add a marketplace / 添加市场**。
2. 在 **Source / 来源** 中填写 `pwd` 输出的仓库根目录绝对路径。该目录须包含 `.agents/plugins/marketplace.json`。
3. 在 **Git ref / 分支** 中按语言选择对应分支：中文版为 `main`，英文版为 `release-en`，与上方切换的本地分支保持一致。
4. 点击 **Add marketplace / 添加市场**，等待市场加载完成。
5. 在市场列表选择 **智慧芽插件市场**，找到 **智慧芽 IP 专家套件**，点击 **＋ / Install** 安装。
6. 完成连接提示，确认插件已安装并启用，然后新建对话。

### CLI：Marketplace → 插件

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git switch "$branch"
codex plugin marketplace add "$(pwd)"
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

安装完成后重启桌面端并新建对话。

## GitLab 安装

### 界面：Marketplace → 插件

本机需具备公司 GitLab 的访问权限和 SSH 凭据。

1. 打开 **Plugins / 插件 → Add / 添加 → Add a marketplace / 添加市场**。
2. 在 **Source / 来源** 中填写以下 GitLab 仓库地址。
3. 在 **Git ref** 中填写所需语言分支：`main` 为中文版，`release-en` 为英文版。
4. 点击 **Add marketplace / 添加市场**，等待市场加载完成。
5. 选择 **智慧芽插件市场 → 智慧芽 IP 专家套件 → ＋ / Install**，完成连接提示后新建对话。

```text
git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git
```

### CLI：Marketplace → 插件

```bash
branch=main # 中文版；英文版改为 release-en
codex plugin marketplace add 'git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git' --ref "$branch"
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

安装完成后重启桌面端并新建对话。

## ZIP 安装

### 界面：上传单插件 ZIP

在仓库根目录打包单插件。目标分支须已提交所需的插件清单和 MCP 配置；`git archive` 不包含暂存区或未提交修改。

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

本仓库同时保留两种受支持的格式：Agent Plugins 格式使用根目录 `plugin.json`、`mcp.json` 和 `skills/`；Codex 兼容格式使用 `.codex-plugin/plugin.json` 引用 `skills/` 和 `.mcp.json`。前者的根清单须声明 Agent Plugins 1.0 schema；兼容格式不要求额外的根清单。打包整个插件目录即可，无需包含仓库级 Marketplace 清单，也无需手动解压。

1. 打开桌面端 **Plugins / 插件 → Add / 添加 → Upload plugin archive / 上传插件压缩包**。
2. 选择生成的 `patsnap-ip-main.zip`（中文）或 `patsnap-ip-release-en.zip`（英文），点击 **Add plugin / 添加插件**。
3. 上传完成后，在插件详情中安装或确认已安装，按提示连接 MCP，然后新建对话。

工作空间需允许上传插件及包含自定义 MCP 的插件。

# Claude Code（CC）

## 本地安装

### CLI：直接加载插件（开发调试）

在已有仓库中切换语言分支，直接加载插件目录，无需添加 Marketplace：

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git switch "$branch"
claude --plugin-dir "$(pwd)/plugins/patsnap-ip"
```

插件仅在本次终端会话生效，不会持久安装到桌面端。

### CLI：安装插件（供后续本地会话使用）

此方式通过本地 Marketplace 安装，需要先登记市场，再安装插件：

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git switch "$branch"
claude plugin marketplace add "$(pwd)"
claude plugin install patsnap-ip-plugin@patsnap-plugins --scope user
```

安装后打开 **Claude 桌面应用 → Code**，在同一系统用户下新建本地项目会话，按提示连接 MCP。

## GitLab 安装

### 界面：从仓库安装插件

此方式先同步仓库中的 Marketplace，再选择插件安装。同步环境的出站网络策略必须允许访问 `git.patsnap.com`；仅本机能访问 GitLab 并不足够。使用仓库默认分支，默认分支为 `main` 时安装中文版。

1. 打开 **Claude 桌面应用 → Code**，点击输入框旁 **＋ → Add plugins**，进入 **Directory → Plugins**。
2. 点击 **Filter by** 右侧的 **＋（Add marketplace）**，选择 **Add from a repository**。
3. 展开 **URL / Select a repository**，在 **Search GitHub or paste a repository URL** 中粘贴以下 GitLab 仓库地址，并选中该地址：

   ```text
   https://git.patsnap.com/search-engine/search-service/s-search-agent-plugins.git
   ```

4. 点击 **Sync**，等待市场同步完成；此页面没有单独的分支选择字段。
5. 在插件目录中搜索 `patsnap-ip-plugin`，确认来源为 `patsnap-plugins`，点击 **＋ / Install**，按提示完成安装。
6. 完成 MCP 连接提示后，在 **Code** 页新建会话。

出现 `Network access to "git.patsnap.com" is blocked by egress settings.` 时，表示同步请求被出站网络策略拦截，市场尚未添加成功。需要由管理该同步环境的管理员核查域名访问策略；不要反复点击 Sync。可选择本机 CLI 安装，或在允许上传插件的账号中上传单插件 ZIP。

### CLI：从 GitLab 安装插件

由本机 Git 拉取仓库。本机需能访问 `git.patsnap.com`，并已配置具有仓库读取权限的 SSH 凭据。此方式需要先登记 Marketplace，再安装插件：

```bash
branch=main # 中文版；英文版改为 release-en
claude plugin marketplace add "git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git#$branch"
claude plugin install patsnap-ip-plugin@patsnap-plugins --scope user
```

安装后打开 **Claude 桌面应用 → Code**，在同一系统用户下新建本地项目会话，按提示连接 MCP。

## ZIP 安装

### 界面：上传单插件 ZIP

在仓库根目录打包单插件，无需打包或添加 Marketplace。目标分支须已提交 `.claude-plugin/plugin.json`、Skills 和 MCP 配置；`git archive` 不包含未提交修改。

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

1. 打开 **Claude 桌面应用 → Customize → Plugins → Add → Upload plugin**；在 Cowork 布局中先选择 **Cowork**，再打开 **Customize**。
2. 选择 `patsnap-ip-main.zip`（中文）或 `patsnap-ip-release-en.zip`（英文），按提示完成上传并启用插件。
3. 在同一 Claude 账号下启动新的 Code 会话，确认插件已同步并可用，再按提示连接服务。

此入口将插件保存到 Claude 账号。同步到 Claude Code 需 v2.1.273 或更高版本、使用 Claude 账号登录，且组织允许插件同步。上传成功不等于已在 Code 中加载，需在目标会话确认。

### CLI：直接加载插件 ZIP（仅当前会话）

在仓库根目录打包单插件。目标分支须已提交 `.claude-plugin/plugin.json`、Skills 和 MCP 配置；`git archive` 不包含未提交修改。

```bash
cd /absolute/path/s-search-agent-plugins
branch=main # 中文版；英文版改为 release-en
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

将 ZIP 手动传到安装机器，在终端直接加载，无需解压或添加 Marketplace：

```bash
branch=main # 中文版；英文版改为 release-en
claude --plugin-dir "/absolute/path/packages/patsnap-ip-$branch.zip"
```

插件仅在本次终端会话生效，不会持久安装到桌面端。

# 验证与维护

## 验证

安装后检查插件、Skills 和 MCP 工具是否可用。

### 安装与能力加载

1. 在插件管理中确认`patsnap-ip-plugin` 已安装并启用，版本与仓库中的 `plugin.json` 一致；通过 Marketplace 安装时，来源为 `patsnap-plugins`。
2. 新建对话，确认上述七个 Skill 均可被发现，并确认本插件提供的 MCP 工具已加载。
3. 检查实际调用的工具来源、服务地址与连接状态，确认使用的是本插件提供的 MCP。

### MCP 与 Skill 联动

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

- **市场添加失败**：确认本地路径指向仓库根目录，或确认 Git 地址可访问、SSH 权限已配置且文件已推送。
- **Skill 未加载**：检查插件启用状态及 `plugin.json` 中的 `skills` 路径；刷新市场、更新插件后重新打开对话，仍未加载时重启客户端。
- **MCP 连接或调用失败**：检查 MCP 配置中的服务地址与网络连通性，依据实际错误定位问题。

## 维护

客户端适配在同一个分支内共存，不为 Codex 或 Claude Code 长期拆分发布分支。`main` / `release-en` 分别提供中文与英文默认语种和本地化文案，共用交付契约。

Skill 的目录组织、工具适配、文件清理和检查要求见 [Skill 维护说明](SKILL_MAINTENANCE.md)。

- **修改 MCP**：同步编辑 `plugins/patsnap-ip/mcp.json` 和 `.mcp.json`，保持服务名称、地址及连接参数一致。
- **修改 Skill**：编辑 `plugins/patsnap-ip/skills/<skill-name>/SKILL.md` 及其引用资源，更新工具使用流程和结果要求。
- **新增插件**：在 `plugins/` 下创建独立插件目录，并在 `.codebuddy-plugin/marketplace.json`、`.claude-plugin/marketplace.json` 和 `.agents/plugins/marketplace.json` 中同步登记。
- **发布更新**：同步更新标准清单和三份兼容清单的版本号。共同改动先进入 `main`，再同步到 `release-en` 并保留英文默认语种和本地化文案。两版 README 的安装说明和交付规则同步维护。提交并推送后，再让用户刷新市场、更新插件。

## 按发布标签打包

正式分发使用不可变的发布标签，避免分支后续提交导致同名 ZIP 内容变化。完成版本、RN 和文档的发布提交后，在该提交上创建标签，再从标签导出单插件：

```bash
release_tag=v0.10.5-cn
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
- [Codex / ChatGPT：插件上传权限](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)
- [Codex：CLI 命令](https://learn.chatgpt.com/docs/developer-commands)
- [Claude Code：桌面端插件安装](https://code.claude.com/docs/en/desktop#install-plugins)
- [Claude：上传插件与账号同步要求](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Claude Code：插件安装与私有市场](https://code.claude.com/docs/en/plugins/install)
- [Claude Code：托管插件市场](https://code.claude.com/docs/en/plugins/host-marketplace)
- [Claude Code：CLI 参考](https://code.claude.com/docs/en/plugins/cli-reference)
- [Git：git archive](https://git-scm.com/docs/git-archive)
