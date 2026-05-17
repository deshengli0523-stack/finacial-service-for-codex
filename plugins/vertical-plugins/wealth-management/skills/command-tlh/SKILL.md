---
name: command-tlh
description: "Identify tax-loss harvesting opportunities"
---

# /tlh Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[client name or account]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `tax-loss-harvesting` skill to scan taxable accounts for harvestable losses, suggest replacement securities, and manage wash sale windows.

If a client or account is provided, use it. Otherwise ask for the portfolio to scan.
