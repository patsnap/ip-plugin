# Install Patsnap IP Plugin

The English edition uses the `release-en` branch. The Chinese edition uses `main`. The marketplace ID is `patsnap-plugins` and the plugin ID is `patsnap-ip-plugin`. [中文安装指南](https://github.com/patsnap/ip-plugin/blob/main/INSTALL.md)

## Install and verify with an agent

Send this prompt to an agent that can manage plugins and follow the authorization prompts in your client.

```text
Please install the English plugin from the release-en branch of https://github.com/patsnap/ip-plugin, connect to its MCP server, and verify the connection.
```

After installation, start a new session and verify the plugin and MCP connection.

```text
Please confirm that patsnap-ip-plugin is enabled and its skills are loaded, then call one of its read-only MCP tools to verify the connection. If authorization is required, prompt me and resume verification afterward.
```

Searches use your organization’s API credits. Available tools depend on organization and member permissions.

## Claude Code

```bash
claude plugin marketplace add 'https://github.com/patsnap/ip-plugin.git#release-en'
claude plugin install patsnap-ip-plugin@patsnap-plugins
```

You can also use `/plugin` in Claude Code to manage marketplaces and install the plugin. To load the plugin from a local checkout, check out `release-en` and run `claude --plugin-dir ./plugins/patsnap-ip` from the repository root.

## Codex

```bash
codex plugin marketplace add https://github.com/patsnap/ip-plugin.git --ref release-en
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

In the Codex desktop app, open **Plugins → Add marketplace**, enter `https://github.com/patsnap/ip-plugin.git`, set **Git ref** to `release-en`, and install **Patsnap IP Plugin**.

## WorkBuddy AI / CodeBuddy

```bash
git clone --branch release-en https://github.com/patsnap/ip-plugin.git
cd ip-plugin
pwd
```

In the client, add a local marketplace using the directory printed by `pwd` and install **Patsnap IP Plugin**. If your client supports a Git marketplace with a branch selector, use the same GitHub URL and select `release-en`.

## ChatGPT, Claude.ai, and other MCP clients

Use this Streamable HTTP endpoint in clients that support custom remote MCP servers:

```text
https://connect.patsnap.com/2b0355/logic-mcp
```

In ChatGPT on the web, authorized workspace users can open **Plugins → Add custom MCP server**. Availability depends on your plan, role, and workspace policy. See [OpenAI’s custom MCP guide](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt).

A custom MCP connection exposes the service tools. To load this repository’s skills and report templates, install the plugin in a supported plugin host.

## Authorize your Patsnap account

When your client prompts you to connect, open its authorization flow, sign in to your Patsnap account, and finish OAuth. Return to the client and check the connection status. The marketplace already supplies the server configuration for plugin hosts.

## Verify and troubleshoot

1. Check the installed version and Git branch.
2. Make sure the plugin and the `patsnap-ip` service are enabled. After authorization, start a new session and check that the skills and tools load.
3. If marketplace sync fails, check whether your client can reach GitHub. If the MCP connection fails, check the workspace permissions and server URL, then follow your client’s reauthorization steps.
4. If the problem persists, file a [GitHub issue](https://github.com/patsnap/ip-plugin/issues) with the client and plugin versions, branch, and a redacted error message.
