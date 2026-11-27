<div align="center">
  <img src="assets/open-platform-logo.png" alt="Open Platform by Patsnap" width="260">
</div>

# Patsnap IP Plugin

Search patents and scientific literature, run novelty and freedom-to-operate (FTO) workflows, and produce reports with traceable evidence in your AI assistant.

[简体中文](https://github.com/patsnap/ip-plugin/tree/main) · [v0.10.5-en](https://github.com/patsnap/ip-plugin/tree/v0.10.5-en) · [Installation](#installation) · [Choose a skill](#choose-a-skill) · [Changelog](CHANGELOG.en.md)

| When you need to | What you get |
| --- | --- |
| Assess a technical proposal before filing | The closest prior art, a feature-by-feature comparison, and separate novelty and inventive-step assessments |
| Screen a product before launch | Potential patent risks in the target jurisdictions and claim charts for the patents you select |
| Research competitors or plan a portfolio | Representative patents, technology directions, filing priorities, and target jurisdictions |

## How it works

Describe your technical proposal, product configuration, or company in plain language. The relevant skill defines the scope, uses Patsnap MCP tools to search and compare evidence, and produces results with citations and gaps you can review.

```mermaid
flowchart LR
    A[Describe the task] --> B[Select the skill]
    B --> C[Search and compare evidence]
    C --> D[Produce a cited report]
```

## See it in action

> Run a novelty search for this technical proposal. Break it into searchable features, find the closest prior art, and show which features each reference discloses and which are still uncertain.

Include the technical disclosure, any relevant dates, and the jurisdictions you want to cover. The novelty report includes the search strategy, a feature-by-feature evidence comparison, and separate assessments of novelty and inventive step.

## Installation

### Claude Code

```bash
claude plugin marketplace add 'https://github.com/patsnap/ip-plugin.git#release-en'
claude plugin install patsnap-ip-plugin@patsnap-plugins
```

### Codex

```bash
codex plugin marketplace add https://github.com/patsnap/ip-plugin.git --ref release-en
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

See the [installation guide](INSTALL.en.md) for WorkBuddy AI, CodeBuddy, custom MCP connections in ChatGPT, account authorization, and troubleshooting.

## Choose a skill

| When you need to | Skill | Deliverable |
| --- | --- | --- |
| Check novelty before filing | `ip-novelty-search` | Feature-by-feature evidence and novelty and inventive-step assessments |
| Screen for FTO risks before launch | `ip-fto-search` | Screening results, claim charts, and a risk report |
| Understand a competitor’s technology | `competitive-patent-analysis` | A report on technology directions and representative patents |
| Plan a patent portfolio | `ip-portfolio-analysis` | Technology directions, filing priorities, and target jurisdictions |
| Identify invention candidates | `ip-innovation-harvesting` | Candidate inventions, prior-art differences, and validation suggestions |
| Investigate evidence of use | `ip-eou-investigation` | A patent-to-product evidence matrix and report |
| Review an existing search report | `patent-search-report-reviewer` | Written review of the search strategy, documents, facts, and citations |

### MCP tools

<details>
<summary>15 tools in five groups</summary>

| Group | Tools |
| --- | --- |
| Search and query preparation | `describe_search_capability`, `search_patent`, `search_literature`, `build_patent_boolean_query`, `expand_patent_search_terms` |
| Document retrieval | `fetch_patent`, `fetch_literature`, `fetch_patent_lifecycle` |
| Assignee and field analysis | `get_standard_assignee_name`, `get_corptree_hierarchy`, `field_analysis` |
| Novelty evidence | `extract_technical_features`, `assess_feature_disclosure` |
| FTO analysis | `screen_patents_for_FTO`, `build_claim_chart` |

</details>

## Data and limitations

Specify the relevant product model, company scope, jurisdictions, and dates. Review patent publication numbers, passages, legal status, and evidence gaps before relying on a report. The reports support research and review. Consult a qualified professional for legal conclusions. [Data coverage](https://open.patsnap.com/data-coverage) · [Patsnap Trust Center](https://trust.patsnap.com/)

## Troubleshooting and migration

If the plugin is enabled but its tools are unavailable, complete account authorization and start a new session. If you used Patent & Literature Search MCP, check the endpoint and available tools in the [installation guide](INSTALL.en.md). Use `search_patent` and `search_literature` for search and `fetch_patent` and `fetch_literature` for document retrieval.

## Pricing

See [Patsnap Open Platform pricing](https://open.patsnap.com/pricing) for current pricing and account allowances.

## Support

Open a [GitHub issue](https://github.com/patsnap/ip-plugin/issues) for usage questions or feedback. See [SECURITY.md](SECURITY.md) for security reports.
