---
name: command-screen-deal
description: "Screen an inbound deal (CIM or teaser)"
---

# /screen-deal Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[path to CIM/teaser file]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `deal-screening` skill and quickly evaluate an inbound deal against the fund's investment criteria.

If a file path is provided, use it. Otherwise ask the user for the deal materials or description.
