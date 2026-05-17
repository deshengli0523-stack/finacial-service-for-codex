---
name: command-client-review
description: "Prep for a client review meeting"
---

# /client-review Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[client name]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `client-review` skill and prepare a client meeting package with performance, allocation, and talking points.

If a client name is provided, use it. Otherwise ask who the meeting is with.
