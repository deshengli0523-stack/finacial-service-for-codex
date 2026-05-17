---
name: command-dd-prep
description: "Prep for a diligence meeting or expert call"
---

# /dd-prep Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[company name] [meeting type]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `dd-meeting-prep` skill and generate targeted questions, benchmarks, and red flags to probe.

If details are provided, use them. Otherwise ask for the company, meeting type (management presentation, expert call, customer reference), and topic focus.
