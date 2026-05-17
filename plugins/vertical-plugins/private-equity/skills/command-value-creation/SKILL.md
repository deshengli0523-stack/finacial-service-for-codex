---
name: command-value-creation
description: "Build a post-acquisition value creation plan"
---

# /value-creation Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[company name]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `value-creation-plan` skill and structure a value creation roadmap with EBITDA bridge, 100-day plan, and KPI dashboard.

If a company name is provided, use it. Otherwise ask the user for the target company details.
