---
name: command-catalysts
description: "View or update the catalyst calendar"
---

# /catalysts Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[timeframe, e.g. 'next 2 weeks']`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `catalyst-calendar` skill to build or review upcoming catalysts across the coverage universe.

If a timeframe is provided, use it. Otherwise default to the next 2 weeks.
