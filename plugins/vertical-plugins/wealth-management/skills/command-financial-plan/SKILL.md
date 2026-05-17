---
name: command-financial-plan
description: "Build or update a financial plan"
---

# /financial-plan Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[client name]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `financial-plan` skill to create or update a comprehensive financial plan covering retirement, education, estate, and cash flow projections.

If a client name is provided, use it. Otherwise ask for client details.
