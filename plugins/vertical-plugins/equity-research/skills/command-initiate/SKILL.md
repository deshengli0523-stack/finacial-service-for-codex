---
name: command-initiate
description: "Create an initiating coverage report"
---

# /initiate Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[company ticker]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `initiating-coverage` skill and begin the 5-task workflow to create an institutional-quality initiation report.

If a ticker is provided, use it. Otherwise ask the user which company to initiate on.
