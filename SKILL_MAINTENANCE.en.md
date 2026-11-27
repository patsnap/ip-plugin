# Skill Maintenance

This guide is for maintainers of the repository’s plugin skills. See [installation guide](INSTALL.en.md) for installation and client verification. Skills do not need to load this guide during business execution.

## Scope of changes

- Identify whether a change concerns business behavior, tool adaptation, structure or presentation.
- Tool adaptation changes tool selection, handoffs, essential parameter rules, result interpretation and missing-capability handling. Preserve capabilities, scenarios, business steps, confirmation points, methods and deliverables.
- When a tool cannot provide evidence, disclose the gap and affected conclusions. Do not silently remove report sections or substitute samples, abstracts or model judgments for complete evidence.
- Change capability descriptions, triggers and workflows only when the business scope actually changes.

## Directory and file responsibilities

Skills live in `plugins/<plugin-name>/skills/<skill-name>/`. The directory and `SKILL.md` name must match, using lowercase letters, digits and hyphens.

Prefer names describing business capabilities and explain responsibilities through concrete execution steps. Each skill is self-contained: its business steps, runtime references, templates and scripts live in its own directory. Its instructions and cases neither name another skill nor require delegation to or loading another skill. Describe compound-task steps and boundaries within the same workflow.

| File/directory | Responsibility | Retention rule |
| --- | --- | --- |
| `SKILL.md` | Name, triggers, inputs, workflow, key rules and deliverables | Required |
| `references/` | Longer methods, output specifications or tool guidance | Link from relevant steps and explain when to read |
| `assets/` | Report templates, styles and delivery resources | Keep when actually used |
| `scripts/` | Local conversion or repeatable processing | State purpose, dependencies and invocation |
| `agents/openai.yaml` | Client display name and optional invocation policy | Use the branch-language business name in `interface.display_name`; preserve policies and the invocation identifier in `SKILL.md` |
| `evals/` | Business review and behavior cases | Keep useful cases; not routine business inputs |

Maintain plugin configuration centrally:

- [Standard manifest](plugins/patsnap-ip/plugin.json) uses Agent Plugins 1.0 and discovers `skills/` and `mcp.json`. Keep version, description and display metadata aligned with compatibility manifests. The Codex compatibility format also remains supported; this repository packages both formats.
- [WorkBuddy/CodeBuddy](plugins/patsnap-ip/.codebuddy-plugin/plugin.json), [Claude Code](plugins/patsnap-ip/.claude-plugin/plugin.json) and [Codex](plugins/patsnap-ip/.codex-plugin/plugin.json) manifests declare the same version, skills and MCP paths. Use `patsnap-ip-plugin` in the standard manifest, all three compatibility manifests and their marketplace entries. Client adapters coexist without duplicating business content.
- [Standard MCP configuration](plugins/patsnap-ip/mcp.json) and [compatibility configuration](plugins/patsnap-ip/.mcp.json) use `streamable-http` and `http` respectively. Synchronize service names, endpoints and authentication policy. Default to host-managed OAuth; do not distribute API-key forms, static authentication headers or real credentials. For client-specific configurations, verify manifest precedence and same-name service merging. OAuth metadata must have a real source; do not guess endpoints or client IDs.
- [WorkBuddy/CodeBuddy](.codebuddy-plugin/marketplace.json), [Claude Code](.claude-plugin/marketplace.json) and [Codex](.agents/plugins/marketplace.json) marketplace files register the same plugin directory and description in each client’s format.

## Writing descriptions

Plugin `description` states the audience, main capabilities and workflows. Keep manifests, marketplace entries and README consistent in scope; a low-level tool capability is not automatically a complete skill workflow.

Skill `description` explains what it does and when to use it. Put detailed methods and tool rules in the body or references. Tool adaptation should not incidentally change business positioning.

Configure display names through each Skill’s `agents/openai.yaml`: Chinese names in the Chinese branch and English names in the English branch. README shows business names/descriptions only in its branch language, with invocation identifiers where useful. Display names do not replace directories or `name`.

Avoid repeatedly stating the plugin name, service endpoint, MCP compatibility or “only use this MCP.” Describe the tools actually available; explain dependencies or limitations at the affected step.

### Language branches and delivery contract

Use “智慧芽” for Chinese brand text and “Patsnap” for English brand text. In bilingual documents, follow the language of each passage; in reports, follow the output language. Preserve plugin identifiers, directory names, tool names, URLs and connection parameters such as `APP_ID`.

Official plugin display names and developer identity: “智慧芽 IP 专家套件” in Chinese, “Patsnap IP Plugin” as the English short name, and “Patsnap” for the developer/author. Keep marketplace names localized by branch and retain current plugin identifiers rather than adopting candidate identifiers.

`main` defaults to Chinese and `release-en` defaults to English. An explicit output-language request takes precedence. Use the adopted output language for dialogue, prose, templates, headers, chart labels and HTML `lang`. Determine search languages and jurisdictions independently. Preserve source originals and locations, with labeled translations where needed.

Keep capabilities, business rules, delivery formats, chapters, fields, template structure, styling, tool configuration and versions aligned. Branch differences concern default language, translation, localized copy and the MCP endpoint. Within each branch, the standard and compatibility configurations use the same endpoint. Apply shared changes to `main` and synchronize them to `release-en`. Verify both locales against the same evidence and review the complete branch diff before release. Maintain equivalent guidance in the README and maintenance notes with localized prose.

## Tool guidance depth

Before changing tool calls, inspect the target MCP’s current tool list and relevant definitions, including inputs, outputs and limits. Keep execution rules in each skill’s own references and synchronize affected embedded guidance when routing changes; execution must not depend on shared files outside that skill directory. Do not infer current capabilities from old tool names, historical receipts or another service. Execute a scoped search only when needed to validate specific behavior.

Keep three types of guidance:

1. Handoffs: when and in what order to call tools, and how results feed the next step.
2. Essential parameter rules: combinations affecting results or prone to misuse, such as Boolean versus other strategies and publication versus family counting.
3. Necessary field meanings: totals versus returned-page counts, company versus applicant identities, and reference expressions versus executable queries.

Full parameter lists, types, defaults, pagination limits, language enums and result structures are governed by runtime definitions. Do not copy interface snapshots, obsolete fields or historical aliases into skills.

Distinguish tool results, user materials and locally calculated report fields. Missing is not zero; a link is not proof of reading; tool success does not establish a conclusion.

## Separate tool reference files

A separate reference file is optional:

- Put short rules in the relevant `SKILL.md` step.
- Put longer, independently useful rules spanning phases in `references/tool-usage.md`, linked as “Tool usage”.
- Maintain a rule once where practical; keep the call purpose in the workflow and link to details.
- Do not create identical files solely for uniformity or require every reference to be read at startup.

For example, the [competitor report](plugins/patsnap-ip/skills/competitive-patent-analysis/SKILL.md) embeds tool rules in company confirmation and area searches; [report review tool guidance](plugins/patsnap-ip/skills/patent-search-report-reviewer/references/tool-usage.md) separately covers query verification and evidence handling.

## Adding, deleting and organizing

Check business scope and resource purpose before adding a skill directory containing `SKILL.md`. Inspect imported `.skill` archives before extraction, avoid extra directory nesting, and remove caches, temporary outputs and unused attachments.

Before deleting files, check Markdown links, prose paths, script dependencies, template references and evaluation inputs. Remove duplicate installation instructions, connection configurations or obsolete interface snapshots only after their purpose is covered elsewhere. Do not delete useful methods, templates, scripts or cases just because the main workflow does not link them directly.

When renaming/deleting a skill, update README structure, descriptions, verification examples and other references. Directory-based discovery does not require a separate per-skill registry.

Document current capabilities, usage and maintenance rules. Keep change histories, test execution logs and temporary troubleshooting notes in version control or task records.

## Confirmation points and evaluation

User confirmation, human selection and professional review are business steps. Do not remove, move or replace them with agent self-checks to improve automated test pass rates, increase tool calls or finish in one turn. Changing these points requires an explicit business requirement.

Evaluate routing, awaiting confirmation, awaiting material, tool execution and final delivery separately. Waiting at a required user checkpoint after selecting the correct workflow is a valid stage result; lack of tool calls at that point is not itself failure. Tests of later tool calls must provide actual applicable prior confirmation or multiple turns. Do not fabricate approval, treat a general request as approval of every checkpoint, or treat silence/timeouts as consent. Record quotas, tool faults and business waiting separately.

## Checks after changes

- Structure/references: parse YAML frontmatter with `name` and `description`; verify directory names, JSON, links, paths and resources.
- Business scope: preserve scenarios, steps, confirmation points, methods and deliverables; never invent capabilities or evidence to fill tool gaps.
- Tool usage: check names, handoffs and key combinations; distinguish hits, samples, families and local calculations.
- Resources: run representative script inputs; inspect generated templates; use relevant business cases for rule changes.
- Localization: check every distributed text file and DOCX XML. Classify remaining non-English text by purpose, verify English output defaults, and test English heading recognition, navigation, references and document layout.
- Client verification: before release, verify discovery, tool loading and affected workflows per README. Documentation and format checks are not live business integration tests.

Use available skill validators where appropriate and run `git diff --check`. Match verification to the changes; description/link edits alone do not require complete business searches.

Update plugin versions for publication, verify marketplace/README/package agreement, then commit and distribute according to the release process. Routine local document edits do not require a version bump. Never commit real credentials or personal client configuration.
