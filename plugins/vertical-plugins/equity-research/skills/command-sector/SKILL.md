---
name: command-sector
description: "Create a sector overview report"
---

# /sector Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[sector or industry]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `sector-overview` skill and create an industry landscape report covering market sizing, competitive dynamics, and investment implications.

If a sector is provided, use it. Otherwise ask the user which industry to cover.
