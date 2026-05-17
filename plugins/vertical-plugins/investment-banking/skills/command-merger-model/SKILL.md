---
name: command-merger-model
description: "Build an accretion/dilution merger model"
---

# /merger-model Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[acquirer] acquiring [target]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `merger-model` skill and build a merger consequences analysis.

If acquirer and target are provided, use them. Otherwise ask the user for deal details.
