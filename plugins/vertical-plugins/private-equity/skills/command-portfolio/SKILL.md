---
name: command-portfolio
description: "Review portfolio company performance"
---

# /portfolio Command Workflow

Use this skill when a user asks for the original slash command behavior. Codex does not load Claude slash commands directly, so follow the command workflow below as normal skill instructions.

Original argument hint: `[company name or path to financial package]`


> Codex port note: This skill was adapted from Anthropic's financial-services repository. Use Codex-native tools and available MCP servers in this environment; when the original instructions mention Claude, Claude Code, Cowork, or Claude-specific tool names, interpret that as the corresponding Codex workflow or connector if available.

Load the `portfolio-monitoring` skill and analyze a portfolio company's performance against plan — KPIs, variances, and red flags.

If a company name or file is provided, use it. Otherwise ask the user for the portfolio company and financial data.
