---
name: command-ai-readiness
description: "Scan the portfolio for the highest-leverage AI opportunities"
---

# /ai-readiness Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[path to quarterly materials folder, or company names]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `ai-readiness` skill and scan portfolio companies for AI leverage — per-company go / no-go gate, quick wins ranked by EBITDA impact across the portfolio, and replays that hit multiple companies at once.

If a folder or company list is provided, use it. Otherwise ask which companies to include and for their latest quarterly materials.
