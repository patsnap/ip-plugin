# 仓库使用说明 / Repository guide

智慧芽 IP 专家套件提供专利与文献检索、查新、FTO 和专利分析工作流。GitHub `main` 提供默认中文版，`release-en` 提供英文版。先读本分支的安装指南，确认插件与 `patsnap-ip` MCP 已连接，再选择与用户目标最吻合的 Skill。

- 按 `plugins/patsnap-ip/skills/<skill-name>/SKILL.md` 中的业务范围和确认节点执行。FTO 核对产品配置和法域，查新核对技术方案，其他场景按对应 Skill 确认输入。
- 以宿主实际提供的工具和参数为准。抓取证据后核对公开号、文献或法律记录、文本位置和覆盖范围，并保留报告里的来源。
- 工具不可用、授权失败、查询受限或返回不全时，告诉用户具体失败点及对报告的影响。避免把缺失数据当作零，用摘要代替全文，或编造公开号和引用。
- 将报告用于研究与人工复核。法律结论由合格专业人员判断。请勿将凭据或客户敏感数据写入仓库、Issue 或演示文件。

Install the edition that matches the user’s language and select the skill documented in its `SKILL.md`. Confirm the scope, use the host’s actual tool definitions, verify citations against their sources, and explain any limits caused by failed authorization, retrieval, or coverage. Follow the selected skill’s required user decisions and review steps.
