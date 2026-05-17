---
name: command-source
description: "Source deals — discover companies and draft founder outreach"
---

# /source Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[sector or criteria, e.g. 'industrial services in Texas $10-50M']`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `deal-sourcing` skill and run the sourcing pipeline: discover target companies, check CRM for existing relationships, and draft personalized founder outreach emails.

If criteria are provided, use them. Otherwise ask the user for sector, size, geography, and deal parameters.
