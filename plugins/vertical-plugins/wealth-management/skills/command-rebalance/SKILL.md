---
name: command-rebalance
description: "Analyze drift and generate rebalancing trades"
---

# /rebalance Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[client name or account]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `portfolio-rebalance` skill to analyze allocation drift and recommend tax-aware rebalancing trades.

If a client or account is provided, use it. Otherwise ask for the portfolio to analyze.
