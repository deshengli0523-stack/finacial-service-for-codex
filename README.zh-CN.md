# Financial Services For Codex

[English](README.md)

本仓库是 Anthropic Apache-2.0 许可的
[`financial-services`](https://github.com/anthropics/financial-services) 参考仓库的
Codex 可用移植版，包含面向金融服务工作流的 agents、plugins、skills、commands
以及 MCP connector 定义。

## 主要变更

- 将 Claude 插件清单从 `.claude-plugin/plugin.json` 转换为
  `.codex-plugin/plugin.json`。
- 将 Claude marketplace 元数据转换为 `.agents/plugins/marketplace.json`。
- 将 Claude slash commands 转换为 `command-*` Codex skills。
- 将 Claude named agent prompts 转换为 `agent-*` Codex skills。
- 将现有 `SKILL.md` 文件规范化为 Codex 可读取的 front matter。
- 保留 Claude Managed Agent cookbooks 作为参考资料，路径为
  `managed-agent-cookbooks/`；Codex 运行时使用 plugin 和 skill 布局。

## 在 Codex 中安装 / 使用

将本仓库作为 Codex 的本地 plugin marketplace 来源使用。marketplace 文件位于：

```text
.agents/plugins/marketplace.json
```

已移植的 plugins：

- `earnings-reviewer` -> `./plugins/agent-plugins/earnings-reviewer`
- `gl-reconciler` -> `./plugins/agent-plugins/gl-reconciler`
- `kyc-screener` -> `./plugins/agent-plugins/kyc-screener`
- `market-researcher` -> `./plugins/agent-plugins/market-researcher`
- `meeting-prep-agent` -> `./plugins/agent-plugins/meeting-prep-agent`
- `model-builder` -> `./plugins/agent-plugins/model-builder`
- `month-end-closer` -> `./plugins/agent-plugins/month-end-closer`
- `pitch-agent` -> `./plugins/agent-plugins/pitch-agent`
- `statement-auditor` -> `./plugins/agent-plugins/statement-auditor`
- `valuation-reviewer` -> `./plugins/agent-plugins/valuation-reviewer`
- `equity-research` -> `./plugins/vertical-plugins/equity-research`
- `financial-analysis` -> `./plugins/vertical-plugins/financial-analysis`
- `fund-admin` -> `./plugins/vertical-plugins/fund-admin`
- `investment-banking` -> `./plugins/vertical-plugins/investment-banking`
- `operations` -> `./plugins/vertical-plugins/operations`
- `private-equity` -> `./plugins/vertical-plugins/private-equity`
- `wealth-management` -> `./plugins/vertical-plugins/wealth-management`
- `lseg` -> `./plugins/partner-built/lseg`
- `sp-global` -> `./plugins/partner-built/spglobal`

如果上游仓库提供了 `.mcp.json` 文件，本移植版会保留对应的 MCP connectors。
多数金融数据 connectors 需要单独的服务商订阅、凭证和网络访问权限。

## 安全说明

这些工作流用于起草供合格专业人士审核的分析师工作成果。它们不构成投资、
法律、税务或会计建议，也不应在缺少你方控制流程的情况下执行交易、批准入职、
登记账务或承担风险。

## 来源

- 上游仓库：https://github.com/anthropics/financial-services
- Codex 移植仓库：https://github.com/deshengli0523-stack/finacial-service-for-codex
- 许可证：Apache-2.0；见 `LICENSE`。
