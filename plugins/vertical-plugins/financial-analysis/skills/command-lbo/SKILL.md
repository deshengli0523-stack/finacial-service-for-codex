---
name: command-lbo
description: "Build an LBO model for a PE acquisition"
---

# /lbo Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[company name or deal details]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `lbo-model` skill and build a leveraged buyout model for the specified company or deal.

If a company name is provided as an argument, use it. Otherwise ask the user for the target company and deal parameters.
