---
name: command-proposal
description: "Create an investment proposal for a prospect"
---

# /proposal Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[prospect name]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `investment-proposal` skill to create a personalized investment proposal for a prospective client.

If a prospect name is provided, use it. Otherwise ask for prospect details.
