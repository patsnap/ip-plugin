# Patsnap Plugins

A plugin marketplace for R&D and intellectual property teams, providing patent search, analysis and reporting workflows.

## Repository structure

```text
s-search-agent-plugins/
├── .codebuddy-plugin/marketplace.json # WorkBuddy / CodeBuddy marketplace
├── .claude-plugin/marketplace.json    # Claude Code marketplace
├── .agents/plugins/marketplace.json   # Codex marketplace
├── plugins/
│   └── patsnap-ip/
│       ├── plugin.json                  # Standard plugin manifest
│       ├── mcp.json                     # Standard MCP configuration
│       ├── .codebuddy-plugin/plugin.json
│       ├── .claude-plugin/plugin.json
│       ├── .codex-plugin/plugin.json
│       ├── .mcp.json                    # Compatibility MCP configuration
│       └── skills/
│           ├── competitive-patent-analysis/  # Competitive Patent Analysis
│           ├── patent-search-report-reviewer/  # Patent Search Report Reviewer
│           ├── ip-novelty-search/  # Novelty Search
│           ├── ip-portfolio-analysis/  # Patent Portfolio Analysis
│           ├── ip-innovation-harvesting/  # Innovation Harvesting
│           ├── ip-fto-search/  # FTO Search
│           └── ip-eou-investigation/  # EOU Investigation
├── .gitignore
├── SKILL_MAINTENANCE.md
└── README.md
```

The plugin ID in the `patsnap-plugins` marketplace is `patsnap-ip-plugin` for all clients.

## MCP service

`plugins/patsnap-ip/mcp.json` and `.mcp.json` define the same `patsnap-ip` service using the `streamable-http` and `http` transport labels respectively, with the same endpoint:

```text
https://connect.patsnap.com/2b0355/logic-mcp
```

The client network must reach this service. Skills organize patent search, literature, full-text, legal-record and aggregation tools into workflows. Actual parameters follow the runtime tool schemas.

## Skills

MCP supplies tools; skills define workflows. The manifest distributes both together.

Current plugin version: **0.10.7**. Chinese edition: `main`; English edition: `release-en`.

### ip-novelty-search: Novelty Search

File: [SKILL.md](plugins/patsnap-ip/skills/ip-novelty-search/SKILL.md)

Use when checking whether an invention or technical proposal is new. Compare its features with the closest patents, verify the decisive evidence, and report novelty and inventive step separately in a traceable HTML report. Can continue an existing search.

### ip-portfolio-analysis: Patent Portfolio Analysis

File: [SKILL.md](plugins/patsnap-ip/skills/ip-portfolio-analysis/SKILL.md)

Use when planning patent protection for a project or company. Combine your own coverage with competitor activity across set dates and countries to recommend technical directions, patent groups, filing priorities and target countries in an HTML report.

### competitive-patent-analysis: Competitive Patent Analysis

File: [SKILL.md](plugins/patsnap-ip/skills/competitive-patent-analysis/SKILL.md)

Use when analyzing one company's strongest technology directions and representative patents. Confirm the company and its subsidiaries, verify patent families where data permits, explain each selected patent, and deliver an HTML report. Does not replace FTO research.

### ip-innovation-harvesting: Innovation Harvesting

File: [SKILL.md](plugins/patsnap-ip/skills/ip-innovation-harvesting/SKILL.md)

Use when turning real R&D problems, proposals or invention disclosures into patentable ideas. Keep the supplied facts, compare them with prior art, and list differences, experiments still needed and next steps. Supports quick and deep modes. Does not invent results or guarantee a grant.

### ip-fto-search: FTO Search

File: [SKILL.md](plugins/patsnap-ip/skills/ip-fto-search/SKILL.md)

Use for freedom-to-operate research on a confirmed product and its target countries. Screen candidate patents, let the user choose which ones go into claim analysis, build claim charts, and produce a risk report with sources and coverage gaps. Does not guarantee non-infringement.

### ip-eou-investigation: EOU Investigation

File: [SKILL.md](plugins/patsnap-ip/skills/ip-eou-investigation/SKILL.md)

Use when looking for third-party products that may use your own patents. Find relevant patents, explain their key claim features, research competing products, and map the evidence into a comparison matrix in an HTML report with sources, evidence gaps and next steps.

### patent-search-report-reviewer: Patent Search Report Reviewer

File: [SKILL.md](plugins/patsnap-ip/skills/patent-search-report-reviewer/SKILL.md)

Use to review an existing patent search, novelty, FTO, evidence-of-use or invalidity report. Check the search strategy, cited documents, quoted source text and counts, and return located issues, coverage and missing evidence as written comments. Does not run a new search from scratch.

### File responsibilities

- The plugin’s root `plugin.json` uses Agent Plugins 1.0 and discovers `skills/` and `mcp.json`. Three hidden compatibility manifests declare `./skills/` and `./.mcp.json`, sharing the same skills and service.
- `SKILL.md` defines scenarios, inputs, workflow, tool choice and deliverables. Short rules stay in the relevant step; longer rules may live in `references/tool-usage.md`. Runtime declarations govern full interfaces.
- `references/` holds methods/specifications, `assets/` templates, and `scripts/` local conversion programs.
- Skill directory names match `SKILL.md` names and remain invocation identifiers. `interface.display_name` in `agents/openai.yaml` supplies the business name in this branch’s language, preserving invocation policies where present. `evals/` contains review cases and is not used for routine report generation.

Novelty scripts organize report data and receipts; HTML rendering requires Python 3, `markdown-it-py` and `Pillow`. Keep raw responses separate from local analysis fields.

### Delivery formats

| Skill | Deliverables |
|---|---|
| `competitive-patent-analysis` | Standalone offline HTML using the packaged template. Keep valuation and jurisdictional coverage in the representative patent table. |
| `ip-fto-search` | A self-contained HTML preview first; after content confirmation, deliver the selected HTML, Word, PDF, Markdown or combination. The main claim comparison table has four columns. |
| `ip-eou-investigation` | Standalone HTML report with a product model by claim point evidence matrix, supporting evidence, and open questions. |
| `ip-novelty-search` | Novelty conclusions and single-file HTML with actual retrieval, per-feature evidence, Agent verification, separate novelty/inventive-step assessments and unresolved issues. |
| `ip-portfolio-analysis` | Thirteen-chapter HTML with an eight-column portfolio matrix. Include an action plan only when requested. |
| `ip-innovation-harvesting` | Markdown in dialogue and light HTML for full reports, retaining six CP-0 fields and a six-month roadmap. |
| `patent-search-report-reviewer` | Three-part Markdown by default. Preserve the three-part structure when another format is requested. |

## Installation

[Install directly with an agent](#install-directly-with-an-agent) · [WorkBuddy domestic edition](#workbuddy-domestic-edition) · [WorkBuddy AI international edition](#workbuddy-ai-international-edition) · [Codex](#codex-chatgpt-desktop) · [Claude Code](#claude-code-cc)

Plugin version **0.10.7** is available in English (`release-en`) and Chinese (`main`). Install one edition per client. Both use the plugin ID `patsnap-ip-plugin`. For local installation, replace `/absolute/path/s-search-agent-plugins` with the path to your clone.

Searches use your organization's API credits. The tools you can access depend on your organization and member permissions.

### Install directly with an agent

Copy the prompt for your preferred edition into your agent. Follow any authorization prompts in your client. Depending on the model’s capabilities, the agent may need help completing installation or connecting to MCP. If a step fails, follow the instructions for your client below.

**English**

```text
Please install the English plugin from the release-en branch of https://github.com/patsnap/ip-plugin, connect to its MCP server, and verify the connection.
```

**中文**

```text
请从 https://github.com/patsnap/ip-plugin 安装中文版插件，连接其 MCP 服务并确认连接成功。
```

#### Verify after installation

After installation, start a new chat and send the verification prompt to your agent.

**English**

```text
Please confirm that patsnap-ip-plugin is enabled and its skills are loaded, then call one of its read-only MCP tools to verify the connection. If authorization is required, prompt me and resume verification afterward.
```

**中文**

```text
请确认 patsnap-ip-plugin 已启用、插件技能已加载，并调用一个只读 MCP 工具验证连接；如果需要授权，请提示我，授权后继续验证。
```

# WorkBuddy domestic edition

## GitHub marketplace installation

1. Open **专家·技能·连接器 → 技能 → 套件 → 添加市场** (Add Marketplace).
2. Enter `patsnap/ip-plugin` in **市场源** (Marketplace Source) and click **提交** (Submit). This installs the Chinese edition by default.
3. Open `patsnap-plugins`, find `patsnap-ip-plugin`, click **安装** (Install) and enable the plugin.

## Local installation

In a terminal, open your existing clone and select the language branch.

```bash
cd /absolute/path/s-search-agent-plugins
git switch release-en  # Use git switch main for Chinese
pwd
```

1. Open **专家·技能·连接器 → 技能 → 套件 → 添加市场** (Add Marketplace).
2. Enter the repository root printed by `pwd` in **市场源** (Marketplace Source) and click **提交** (Submit).
3. Open `patsnap-plugins`, install `patsnap-ip-plugin` and enable it.

## Connect to Patsnap MCP

Open **专家·技能·连接器 → 连接器 → 自定义连接器 → 我的 MCP** and find the `patsnap-ip` service from `patsnap-ip-plugin`. If it shows **需要认证** (Needs authentication), click **连接** (Connect), sign in to the Patsnap Open Platform in your browser and allow access. Return to WorkBuddy. A green indicator and an enabled tool count mean you can start a new task.

# WorkBuddy AI international edition

## GitHub marketplace installation

1. Open **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**.
2. Enter `patsnap/ip-plugin` in **Marketplace Source** and click **Submit**. This installs the Chinese edition by default.
3. Open `patsnap-plugins`, find `patsnap-ip-plugin`, click **Install** and enable the plugin.

## Local installation

In a terminal, open your existing clone and select the language branch.

```bash
cd /absolute/path/s-search-agent-plugins
git switch release-en  # Use git switch main for Chinese
pwd
```

1. Open **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**.
2. Enter the repository root printed by `pwd` in **Marketplace Source** and click **Submit**.
3. Open `patsnap-plugins`, install `patsnap-ip-plugin` and enable it.

## Connect to Patsnap MCP

Open **Experts · Skills · Connectors → Connectors → Custom connectors → My MCP** and find `patsnap-ip` labeled **From plugin patsnap-ip-plugin**. If it shows **Needs authentication**, click **Connect**, sign in and allow access in your browser. Return to WorkBuddy AI. A green indicator and an enabled tool count mean you can start a new task.

# Codex ChatGPT desktop

The English marketplace and plugin appear as **Patsnap Plugins** and **Patsnap IP Plugin**. The Chinese edition appears as **智慧芽插件市场** and **智慧芽 IP 专家套件**.

## GitHub marketplace installation

1. Open **Plugins → Add → Add a marketplace**.
2. Enter `patsnap/ip-plugin` in **Source**. Set **Git ref** to `release-en` for English or `main` for Chinese. Leave **Sparse paths** blank and click **Add marketplace**.
3. Open the marketplace for your edition, select the plugin and click **Install**.

To install from GitHub using the CLI, run these commands in a terminal.

```bash
branch=release-en  # Use main for Chinese
codex plugin marketplace add patsnap/ip-plugin --ref "$branch"
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

## Local installation

In a terminal, open your existing clone and select the language branch.

```bash
cd /absolute/path/s-search-agent-plugins
git switch release-en  # Use git switch main for Chinese
pwd
```

1. Open **Plugins → Add → Add a marketplace**.
2. Enter the repository root printed by `pwd` in **Source**. This directory contains `.agents/plugins/marketplace.json`. Click **Add marketplace**.
3. Open the marketplace for your edition, select the plugin and click **Install**.

To install using the CLI, run these commands from the same repository root. Restart the desktop app and start a new chat.

```bash
codex plugin marketplace add "$(pwd)"
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

## Connect to Patsnap MCP

After installation, sign in and allow access when the browser opens. If it does not open automatically, find **MCP servers → patsnap-ip** on the plugin details page and click the settings gear. Under **From plugins**, click **Authenticate** for `patsnap-ip`. When the browser shows **Authentication complete**, return to Codex. Confirm that the service no longer shows the **Authenticate** button, then start a new chat.

# Claude Code CC

## GitHub marketplace installation

1. In the Claude desktop app, open **Customize → Plugins → Discover**. Click **＋ (Add marketplace) → Add from a repository**.
2. Enter `patsnap/ip-plugin#release-en` for English or `patsnap/ip-plugin#main` for Chinese in **URL**, then click **Sync**.
3. Under **Personal → patsnap-plugins**, find the plugin published by **Patsnap** and click **Install**.

To install from GitHub using the CLI, run these commands in a terminal.

```bash
branch=release-en  # Use main for Chinese
claude plugin marketplace add "patsnap/ip-plugin#$branch"
claude plugin install patsnap-ip-plugin@patsnap-plugins --scope user
```

## Local installation

In a terminal, open your existing clone and select the language branch.

```bash
cd /absolute/path/s-search-agent-plugins
git switch release-en  # Use git switch main for Chinese
```

### Install for subsequent local sessions

Register the local marketplace and install the plugin from the repository root.

```bash
claude plugin marketplace add "$(pwd)"
claude plugin install patsnap-ip-plugin@patsnap-plugins --scope user
```

Open **Claude desktop → Code** under the same system user and start a local project session.

### Load from source for the current session

To test the plugin during development, run this command from the repository root.

```bash
claude --plugin-dir "$(pwd)/plugins/patsnap-ip"
```

## Connect to Patsnap MCP

In the Claude desktop app, open the plugin details and select **Connectors → patsnap-ip**. If it shows **Not connected**, click **Connect**, sign in and allow access in your browser. Return to the connector details. When the status reads **Connected**, start a new Code session.

# Verification and maintenance

## Check the installation

Confirm that the version on the plugin details page matches the release or marketplace source you selected. Marketplace installations should list `patsnap-plugins` as the source. Start a new task or chat, check that all seven skills are available, and run a query with one of the plugin’s read-only MCP tools to confirm it returns a result.

### Verify skill and MCP workflows for maintenance

Try the seven workflows individually:

> Use competitive-patent-analysis from the Patsnap IP Plugin to create a technology and patent report for a specified company. Confirm the technology areas as required before searching and reporting.

> Use patent-search-report-reviewer from the Patsnap IP Plugin to review my patent report, focusing on queries and original cited patent text.

> Use ip-novelty-search on my technical disclosure. Search and compare complete technical relationships, verify decisive evidence, assess novelty and inventive step separately, and generate traceable HTML with unresolved issues.

> Use ip-portfolio-analysis to analyze an R&D patent portfolio for a specified topic and company, preserving all ten phases and 13 report chapters.

> Use ip-innovation-harvesting in quick mode for my technical proposal. Produce the CP-0 card, then proceed through four blocks and ten steps after confirmation.

> Use ip-fto-search for my proposal. Resolve actual countries and search languages; after screening, confirm CC scope and full-text strategy, then compare in batches and report.

> Use ip-eou-investigation to investigate a third-party product using patents we own. Confirm the company scope, patent portfolio, claim points, and retained leads, then deliver an HTML report with model-specific evidence and open questions.

Check skill loading, calls/parameters and evidence traceability. Competitor reports must disclose pagination, family and valuation limits; reviews collect evidence according to the issue. Record source, time and actual read coverage for supplementary web materials.

### Troubleshooting

- **Marketplace addition fails:** for a GitHub marketplace, check that the client can reach the public repository and that the branch matches your edition. For a local marketplace, check that the selected directory is the repository root. [Public repository](https://github.com/patsnap/ip-plugin)
- **Skill missing:** check plugin enablement and the `skills` path; refresh the marketplace, update the plugin and open a new chat, then restart the client if needed.
- **MCP connection/call fails:** check the MCP endpoint and network connectivity; diagnose the actual error.

## Maintenance

Client adapters coexist within each branch. `main` and `release-en` share the delivery contract and use branch-specific default languages, localized wording and MCP endpoints. See [Skill Maintenance](SKILL_MAINTENANCE.md) for structure, tool adaptation, cleanup and checks.

- **MCP changes:** synchronize `mcp.json` and `.mcp.json` service names, endpoints and parameters.
- **Skill changes:** update `SKILL.md`, referenced resources, tool handoffs and expected results.
- **New plugins:** create a directory under `plugins/` and register it in all three marketplace files.
- **Releases:** synchronize versions in the standard and three compatibility manifests. Merge shared changes into `main`, then synchronize/localize `release-en`. Preserve English content and output defaults. Commit and push before asking users to refresh/update.

### Package a local development build

From the repository root, export the latest commit on the selected branch to a single-plugin ZIP for local testing. The archive contains the plugin manifests, MCP configuration and `skills/` at its root.

```bash
branch=release-en  # Use main for Chinese
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

## Package from release tags

Use immutable release tags for distribution so later branch commits do not change a named ZIP. After the release commit and tag exist, export the plugin directory:

```bash
release_tag=v0.10.7-en
mkdir -p outputs/releases
git archive --format=zip --output="outputs/releases/patsnap-ip-$release_tag.zip" "$release_tag:plugins/patsnap-ip"
(cd outputs/releases && shasum -a 256 "patsnap-ip-$release_tag.zip" > "patsnap-ip-$release_tag.zip.sha256")
unzip -t "outputs/releases/patsnap-ip-$release_tag.zip"
```

The ZIP root contains the standard manifest, three hidden client manifests, both MCP configurations and seven Skills. Exclude repository marketplace files, release documents and temporary work. Distribute the ZIP with its `.sha256` file. Branch-based packaging above is for local development; use tag packages for formal distribution.

## References

- [WorkBuddy plugins](https://www.workbuddy.cn/docs/workbuddy/Plugins)
- [WorkBuddy AI quickstart](https://www.workbuddy.ai/docs/workbuddy/Quickstart)
- [Codex plugin structure and local marketplaces](https://developers.openai.com/plugins/build/plugins)
- [Codex plugin UI](https://learn.chatgpt.com/docs/plugins)
- [Codex CLI commands](https://learn.chatgpt.com/docs/developer-commands)
- [Claude Code desktop plugin installation](https://code.claude.com/docs/en/desktop#install-plugins)
- [Claude Code installation and private marketplaces](https://code.claude.com/docs/en/plugins/install)
- [Claude Code marketplace hosting](https://code.claude.com/docs/en/plugins/host-marketplace)
- [Claude Code plugin CLI](https://code.claude.com/docs/en/plugins/cli-reference)
- [Git archive](https://git-scm.com/docs/git-archive)
