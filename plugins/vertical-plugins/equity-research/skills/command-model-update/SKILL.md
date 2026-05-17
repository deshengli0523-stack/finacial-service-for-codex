---
name: command-model-update
description: "Update a financial model with new data"
---

# /model-update Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[company ticker]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `model-update` skill and plug in new earnings, guidance, or revised assumptions.

If a ticker is provided, use it. Otherwise ask the user which model to update and what changed.
