# Financial Services For Codex

[中文](README.zh-CN.md)

This repository is a Codex-ready port of Anthropic's Apache-2.0
[`financial-services`](https://github.com/anthropics/financial-services) reference
agents, plugins, skills, commands, and MCP connector definitions.

## What Changed

- Claude plugin manifests were converted from `.claude-plugin/plugin.json` to
  `.codex-plugin/plugin.json`.
- Claude marketplace metadata was converted to `.agents/plugins/marketplace.json`.
- Claude slash commands were converted into `command-*` Codex skills.
- Claude named agent prompts were converted into `agent-*` Codex skills.
- Existing `SKILL.md` files were normalized to Codex-readable front matter.
- Claude Managed Agent cookbooks are preserved as reference material in
  `managed-agent-cookbooks/`, but Codex uses the plugin and skill layout.

## Install / Use In Codex

Use this repository as a local/plugin marketplace source in Codex. The marketplace
file is at:

```text
.agents/plugins/marketplace.json
```

Available ported plugins:

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

MCP connectors are preserved where the original repo provided `.mcp.json` files.
Most financial data connectors require separate provider subscriptions, credentials,
and network access.

## Safety

These workflows draft analyst work product for qualified human review. They do not
provide investment, legal, tax, or accounting advice, and they must not execute
transactions, approve onboarding, post to ledgers, or bind risk without your own
controls.

## Provenance

- Upstream: https://github.com/anthropics/financial-services
- Codex port repository: https://github.com/deshengli0523-stack/finacial-service-for-codex
- License: Apache-2.0; see `LICENSE`.
