---
name: command-process-letter
description: "Draft a process letter or bid instructions"
---

# /process-letter Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[IOI or final bid]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `process-letter` skill and draft process correspondence.

If a letter type is specified (IOI, final bid, management meeting invite), use it. Otherwise ask the user what stage the process is in.
