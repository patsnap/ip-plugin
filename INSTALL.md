# 安装智慧芽 IP 专家套件

中文版使用 GitHub `main` 分支，英文版使用 `release-en`。市场标识为 `patsnap-plugins`，插件标识为 `patsnap-ip-plugin`。[English installation guide](https://github.com/patsnap/ip-plugin/blob/release-en/INSTALL.md)

## 让 Agent 安装与验证

将下面的指令发送给可以管理插件的 Agent，并按客户端提示完成授权。

```text
请从 https://github.com/patsnap/ip-plugin 安装中文版插件，连接其 MCP 服务并确认连接成功。
```

安装后新建会话，验证插件和 MCP 连通性。

```text
请确认 patsnap-ip-plugin 已启用、插件技能已加载，并调用一个只读 MCP 工具验证连接；如果需要授权，请提示我，授权后继续验证。
```

检索消耗所属企业的 API 积分，可用工具取决于企业和成员权限。

## Claude Code

```bash
claude plugin marketplace add patsnap/ip-plugin
claude plugin install patsnap-ip-plugin@patsnap-plugins
```

在 Claude Code 中也可以通过 `/plugin` 添加同一市场并安装插件。需要从本地加载时，先克隆对应分支，再运行 `claude --plugin-dir ./plugins/patsnap-ip`。

## Codex

```bash
codex plugin marketplace add https://github.com/patsnap/ip-plugin.git --ref main
codex plugin add patsnap-ip-plugin@patsnap-plugins
```

在 Codex 桌面端，打开 **插件 → 添加市场**，填入 `https://github.com/patsnap/ip-plugin.git`，将 **Git ref** 设为 `main`，然后安装 **智慧芽 IP 专家套件**。

## WorkBuddy / CodeBuddy

```bash
git clone --branch main https://github.com/patsnap/ip-plugin.git
cd ip-plugin
pwd
```

在客户端的插件市场中添加本地市场，使用 `pwd` 打印的目录作为市场源，再从 **智慧芽插件市场** 安装 **智慧芽 IP 专家套件**。如果客户端提供 Git 市场来源和分支选项，可以直接使用同一 GitHub 地址和 `main` 分支。

## ChatGPT、Claude.ai 和其他 MCP 客户端

如客户端允许添加自定义远程 MCP 服务，使用以下 Streamable HTTP 地址：

```text
https://connect.zhihuiya.com/2b0355/logic-mcp
```

在 ChatGPT 网页端，工作区授权用户可从 **插件 → 添加自定义 MCP 服务器** 设置连接。客户端的套餐、角色和工作区策略会决定此入口是否可用。详见 [OpenAI 自定义 MCP 指南](https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt)。

自定义 MCP 连接提供服务工具。仓库内的 Skill 和报告模板通过支持安装插件的客户端加载。

## 登录授权

启用插件或添加连接后，在客户端提示时打开授权入口，登录对应版本的智慧芽账号，并完成客户端的 OAuth 流程。返回客户端确认连接状态。支持插件安装的客户端会直接读取插件提供的连接配置。

## 验证与排错

1. 确认安装的版本、客户端和 Git 分支正确。
2. 确认插件和 `patsnap-ip` 服务均已启用。授权完成后，新开会话检查 Skill 与工具是否加载。
3. 市场同步失败时，检查客户端能否访问 GitHub。MCP 连接失败时，检查工作区权限和服务地址，再按客户端提示重新授权。
4. 问题持续时，在 [GitHub Issues](https://github.com/patsnap/ip-plugin/issues) 提供客户端版本、插件版本、分支及脱敏错误信息。
