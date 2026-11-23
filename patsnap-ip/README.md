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
│       ├── plugin.json                  # Standard manifest for ZIP upload and compatible clients
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
│           └── ip-EOU-investigation/  # EOU Investigation
├── .gitignore
├── SKILL_MAINTENANCE.md
└── README.md
```

The marketplace is `patsnap-plugins`; its plugin is `patsnap-ip`.

## MCP service

`plugins/patsnap-ip/mcp.json` and `.mcp.json` define the same `patsnap-ip` service using the `streamable-http` and `http` transport labels respectively, with the same endpoint:

```text
https://ai-fabric.patsnap.com/logic-mcp/patsnap-ip?APP_ID=Patsnap
```

The client network must reach this service. Skills organize patent search, literature, full-text, legal-record and aggregation tools into workflows. Actual parameters follow the runtime tool schemas.

## Skills

MCP supplies tools; skills define workflows. The manifest distributes both together.

Current plugin version: **0.10.0**. Chinese edition: `main`; English edition: `release-en`.

### ip-novelty-search: Novelty Search

File: [SKILL.md](plugins/patsnap-ip/skills/ip-novelty-search/SKILL.md)

Assess a complete technical disclosure against prior patents, compare its features, verify decisive evidence, and report novelty and inventive step separately in a traceable HTML report. Supports continuation of an existing search.

### ip-portfolio-analysis: Patent Portfolio Analysis

File: [SKILL.md](plugins/patsnap-ip/skills/ip-portfolio-analysis/SKILL.md)

Use when planning patent protection for a defined project. Analyze portfolios, competitors and technical spaces using explicit dates and jurisdictions; produce a layout matrix and evidence-backed recommendations. Proposed workflow; apply the local MC/Skill/ip-portfolio-analysis execution contract. Runtime binding and channel availability remain unverified.

### competitive-patent-analysis: Competitive Patent Analysis

File: [SKILL.md](plugins/patsnap-ip/skills/competitive-patent-analysis/SKILL.md)

Use when analyzing one company’s strongest technology directions and representative patents. Confirm directions and assignee scope, verify family identities where data permits, explain selected patents and disclose missing valuation or legal data. This does not replace FTO research. Proposed workflow; apply the local MC/Skill/competitive-patent-analysis execution contract. Runtime binding and channel availability remain unverified.

### ip-innovation-harvesting: Innovation Harvesting

File: [SKILL.md](plugins/patsnap-ip/skills/ip-innovation-harvesting/SKILL.md)

Use when organizing real R&D results into potential invention ideas. Preserve supplied facts, support quick or deep exploration, compare prior art and identify differences, experiments and next actions. Do not invent technical achievements or guarantee patent grant. Proposed workflow; apply the local MC/Skill/ip-innovation-harvesting execution contract. Runtime binding and channel availability remain unverified.

### ip-fto-search: FTO Search

File: [SKILL.md](plugins/patsnap-ip/skills/ip-fto-search/SKILL.md)

Use for FTO research on a single confirmed product configuration and specified manufacturing, sales or use countries. Bind the separate fto-search service, run official screening, preserve client-selected claim-analysis scope and produce the actual official report plus evidence review. Disclose coverage and product gaps; do not guarantee non-infringement or exhaustive retrieval. Proposed workflow; apply the local MC/Skill/ip-fto-search execution contract. Runtime binding and channel availability remain unverified.

### ip-EOU-investigation: EOU Investigation

File: [SKILL.md](plugins/patsnap-ip/skills/ip-EOU-investigation/SKILL.md)

EoU Investigation helps companies identify potential patent infringement leads by matching their own patents with evidence from third-party products. It discovers relevant patents, explains key claim features, researches competing products, and maps supporting evidence into a clear comparison matrix. Findings are delivered in a standalone HTML report with traceable sources, evidence gaps, and recommended next steps to support further review.

### patent-search-report-reviewer: Patent Search Report Reviewer

File: [SKILL.md](plugins/patsnap-ip/skills/patent-search-report-reviewer/SKILL.md)

Use to independently review an existing report, citations and process records. Check document identity, quoted source text, evidence support and scope/count consistency. Return located issues, coverage and missing evidence. Unavailable sources do not prove fabrication. Additional retrieval or independent FTO searching requires a separately defined scope. Proposed workflow; apply the local MC/Skill/patent-search-report-reviewer execution contract. Runtime binding and channel availability remain unverified.

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
| `ip-EOU-investigation` | Standalone HTML report with a product model by claim point evidence matrix, supporting evidence, and open questions. |
| `ip-novelty-search` | Novelty conclusions and single-file HTML with actual retrieval, per-feature evidence, Agent verification, separate novelty/inventive-step assessments and unresolved issues. |
| `ip-portfolio-analysis` | Thirteen-chapter HTML with an eight-column portfolio matrix. Include an action plan only when requested. |
| `ip-innovation-harvesting` | Markdown in dialogue and light HTML for full reports, retaining six CP-0 fields and a six-month roadmap. |
| `patent-search-report-reviewer` | Three-part Markdown by default. Preserve the three-part structure when another format is requested. |

## Installation

[WorkBuddy](#workbuddy-domestic-edition) · [WorkBuddy AI](#workbuddy-ai-international-edition) · [Codex](#codex-chatgpt-desktop) · [Claude Code](#claude-code-cc)

- Chinese edition: `main`; English edition: `release-en`. Both editions share delivery formats, required sections and fields, template structure and styling. Dialogue and deliverables default to Chinese in `main` and English in `release-en`. An explicit output-language request takes precedence. Preserve original evidence and determine search languages and jurisdictions separately.
- Install one language edition per client; marketplace/plugin identifiers are shared.
- Replace `/absolute/path/...` with actual paths. GitLab access requires the company network and SSH credentials.
- Run commands in a terminal; examples target macOS, Linux or Git Bash. Obtain release packages from [Plugin versions and packages](https://xa3hdkuita.feishu.cn/docx/Wc5Dd2mDqoQ3C2xSgYucxWninwb); local development packaging is described below.

# WorkBuddy domestic edition

## Local installation

Select the language branch in an existing clone:

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git switch "$branch"
pwd
```

1. Open **Experts · Skills · Connectors → Skills → Suites → Add Marketplace** (domestic UI: **专家·技能·连接器 → 技能 → 套件 → 添加市场**).
2. Enter the repository root printed by `pwd` in **Marketplace Source / 市场源**, then click **Submit / 提交**.
3. Select **patsnap-plugins → patsnap-ip → Install / 安装**, enable it and start a new task.

## GitLab installation

Use the same marketplace UI, entering this source instead of a local path:

```text
git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git
```

Install `patsnap-ip`, enable it and start a new task. This method uses the repository’s default branch. For a specific language edition, switch branches locally and add the directory.

# WorkBuddy AI international edition

## Local installation

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git switch "$branch"
pwd
```

1. Open **Experts · Skills · Connectors → Skills → Plugins → Add Marketplace**.
2. Enter the repository root printed by `pwd` in **Marketplace Source**, then click **Submit**.
3. Select **patsnap-plugins → patsnap-ip → Install**, enable it and start a new task.

## GitLab installation

Use the same UI with this marketplace source:

```text
git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git
```

Install `patsnap-ip`, enable it and start a new task. This uses the default branch; use a local directory after switching branches to select a particular language edition.

# Codex ChatGPT desktop

## Local installation

### Marketplace UI

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git switch "$branch"
pwd
```

1. Open **Plugins → Add → Add a marketplace**.
2. Enter the absolute repository root in **Source**. It must contain `.agents/plugins/marketplace.json`.
3. Set **Git ref** to `release-en` for English or `main` for Chinese, matching the local branch.
4. Click **Add marketplace** and wait for loading.
5. Select **Patsnap Plugins → Patsnap IP → ＋ / Install**.
6. Complete connection prompts, confirm it is installed and enabled, and start a new chat.

### Marketplace CLI

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git switch "$branch"
codex plugin marketplace add "$(pwd)"
codex plugin add patsnap-ip@patsnap-plugins
```

Restart the desktop app and start a new chat.

## GitLab installation

### Marketplace UI

The machine requires company GitLab access and SSH credentials. Open **Plugins → Add → Add a marketplace**, enter the following **Source**, set **Git ref** to `release-en` or `main`, and click **Add marketplace**. Then select **Patsnap Plugins → Patsnap IP → ＋ / Install**, complete connection prompts and start a new chat.

```text
git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git
```

### Marketplace CLI

```bash
branch=release-en # English; use main for Chinese
codex plugin marketplace add 'git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git' --ref "$branch"
codex plugin add patsnap-ip@patsnap-plugins
```

Restart the desktop app and start a new chat.

## ZIP installation

Package one plugin from the repository root. The target branch must already contain committed manifests and MCP configuration; `git archive` excludes staged and uncommitted changes.

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

The repository maintains two supported formats. Agent Plugins uses root `plugin.json` with the Agent Plugins 1.0 schema, `mcp.json` and `skills/`. Codex compatibility uses `.codex-plugin/plugin.json` pointing to `skills/` and `.mcp.json`, without requiring an additional root manifest. Package the complete plugin directory; repository marketplace files and manual extraction are unnecessary.

1. Open **Plugins → Add → Upload plugin archive**.
2. Select `patsnap-ip-release-en.zip` (English) or `patsnap-ip-main.zip` (Chinese), then **Add plugin**.
3. Install or confirm installation on the plugin detail page, connect MCP and start a new chat.

The workspace must permit plugin uploads and plugins with custom MCP services.

# Claude Code CC

## Local installation

### Load directly for development

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git switch "$branch"
claude --plugin-dir "$(pwd)/plugins/patsnap-ip"
```

This applies only to the current terminal session and does not persistently install the desktop plugin.

### Install for subsequent local sessions

Register the local marketplace, then install:

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git switch "$branch"
claude plugin marketplace add "$(pwd)"
claude plugin install patsnap-ip@patsnap-plugins --scope user
```

Open **Claude desktop → Code**, start a local project session under the same system user and complete MCP connection prompts.

## GitLab installation

### Repository UI

This first synchronizes the marketplace, then installs a selected plugin. The synchronization environment must allow outbound access to `git.patsnap.com`; local-machine access alone is insufficient. It uses the default branch, which installs Chinese when that branch is `main`.

1. Open **Claude desktop → Code → ＋ → Add plugins → Directory → Plugins**.
2. Click **＋ / Add marketplace** beside **Filter by**, then **Add from a repository**.
3. Expand **URL / Select a repository**, paste this into **Search GitHub or paste a repository URL**, and select it:

   ```text
   https://git.patsnap.com/search-engine/search-service/s-search-agent-plugins.git
   ```

4. Click **Sync**. This page has no separate branch selector.
5. Search for `patsnap-ip`, verify the `patsnap-plugins` source and click **＋ / Install**.
6. Complete MCP connection prompts and start a new **Code** session.

`Network access to "git.patsnap.com" is blocked by egress settings.` means synchronization was blocked and the marketplace was not added. Ask the environment administrator to check domain access policy instead of repeatedly syncing. Alternatives are local CLI installation or a single-plugin ZIP upload where permitted.

### GitLab CLI

Local Git requires access to `git.patsnap.com` and SSH credentials with repository read permission.

```bash
branch=release-en # English; use main for Chinese
claude plugin marketplace add "git@git.patsnap.com:search-engine/search-service/s-search-agent-plugins.git#$branch"
claude plugin install patsnap-ip@patsnap-plugins --scope user
```

Open **Claude desktop → Code**, start a local project session under the same system user and connect MCP.

## ZIP installation

### Upload through the UI

Package one plugin; no marketplace archive is required. Commit `.claude-plugin/plugin.json`, skills and MCP configuration first because `git archive` excludes uncommitted changes.

```bash
cd /absolute/path/s-search-agent-plugins
branch=release-en # English; use main for Chinese
git archive --format=zip --output="../patsnap-ip-$branch.zip" "$branch:plugins/patsnap-ip"
```

1. Open **Claude desktop → Customize → Plugins → Add → Upload plugin**. In the Cowork layout, select **Cowork** first, then **Customize**.
2. Select the English or Chinese ZIP, upload and enable it.
3. Start a new Code session under the same Claude account, confirm synchronization and availability, then connect the service.

This saves the plugin to the Claude account. Claude Code synchronization requires v2.1.273 or newer, Claude-account sign-in and organizational permission for plugin synchronization. A successful upload does not prove loading in Code; verify in the target session.

### Load a ZIP for the current CLI session

Use the packaging command above, manually transfer the ZIP to the installation machine, then load it without extracting or adding a marketplace:

```bash
branch=release-en # English; use main for Chinese
claude --plugin-dir "/absolute/path/packages/patsnap-ip-$branch.zip"
```

This affects only the current terminal session and does not persistently install the desktop plugin.

# Verification and maintenance

## Verification

1. Confirm `patsnap-ip` is installed/enabled and its version matches `plugin.json`. Marketplace installations should show `patsnap-plugins` as the source.
2. Start a new chat and verify discovery of all seven skills and loading of this plugin’s MCP tools.
3. If the same MCP was configured separately, check actual tool attribution; an existing connection’s success does not prove the plugin connection loaded.

Try the seven workflows individually:

> Use competitive-patent-analysis from patsnap-ip to create a technology and patent report for a specified company. Confirm the technology areas as required before searching and reporting.

> Use patent-search-report-reviewer from patsnap-ip to review my patent report, focusing on queries and original cited patent text.

> Use ip-novelty-search on my technical disclosure. Search and compare complete technical relationships, verify decisive evidence, assess novelty and inventive step separately, and generate traceable HTML with unresolved issues.

> Use ip-portfolio-analysis to analyze an R&D patent portfolio for a specified topic and company, preserving all ten phases and 13 report chapters.

> Use ip-innovation-harvesting in quick mode for my technical proposal. Produce the CP-0 card, then proceed through four blocks and ten steps after confirmation.

> Use ip-fto-search for my proposal. Resolve actual countries and search languages; after screening, confirm CC scope and full-text strategy, then compare in batches and report.

> Use ip-EOU-investigation to investigate a third-party product using patents we own. Confirm the company scope, patent portfolio, claim points, and retained leads, then deliver an HTML report with model-specific evidence and open questions.

Check skill loading, calls/parameters and evidence traceability. Competitor reports must disclose pagination, family and valuation limits; reviews collect evidence according to the issue. Record source, time and actual read coverage for supplementary web materials.

### Troubleshooting

- **Marketplace addition fails:** check the local repository-root path or reachable Git URL, SSH permissions and pushed files.
- **Skill missing:** check plugin enablement and the `skills` path; refresh the marketplace, update the plugin and open a new chat, then restart the client if needed.
- **MCP connection/call fails:** check the MCP endpoint and network connectivity; diagnose the actual error.

## Maintenance

Client adapters coexist within each branch. `main` and `release-en` share the delivery contract and use branch-specific default languages, localized wording and MCP endpoints. See [Skill Maintenance](SKILL_MAINTENANCE.md) for structure, tool adaptation, cleanup and checks.

- **MCP changes:** synchronize `mcp.json` and `.mcp.json` service names, endpoints and parameters.
- **Skill changes:** update `SKILL.md`, referenced resources, tool handoffs and expected results.
- **New plugins:** create a directory under `plugins/` and register it in all three marketplace files.
- **Releases:** synchronize versions in the standard and three compatibility manifests. Merge shared changes into `main`, then synchronize/localize `release-en`. Preserve English content and output defaults. Commit and push before asking users to refresh/update.

## Package from release tags

Use immutable release tags for distribution so later branch commits do not change a named ZIP. After the release commit and tag exist, export the plugin directory:

```bash
release_tag=v0.10.0-en
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
- [Codex and ChatGPT upload permissions](https://learn.chatgpt.com/docs/enterprise/apps-and-connectors)
- [Codex CLI commands](https://learn.chatgpt.com/docs/developer-commands)
- [Claude Code desktop plugin installation](https://code.claude.com/docs/en/desktop#install-plugins)
- [Claude uploads and account synchronization](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)
- [Claude Code installation and private marketplaces](https://code.claude.com/docs/en/plugins/install)
- [Claude Code marketplace hosting](https://code.claude.com/docs/en/plugins/host-marketplace)
- [Claude Code plugin CLI](https://code.claude.com/docs/en/plugins/cli-reference)
- [Git archive](https://git-scm.com/docs/git-archive)
