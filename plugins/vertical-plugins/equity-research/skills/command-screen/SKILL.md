---
name: command-screen
description: "Run a stock screen or generate investment ideas"
---

# /screen Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[screen criteria, e.g. 'undervalued midcap tech']`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `idea-generation` skill and run quantitative screens or thematic sweeps to surface new investment ideas.

If criteria are provided, use them. Otherwise ask the user what they're looking for (long/short, sector, style, theme).
