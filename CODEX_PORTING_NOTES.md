# Codex Porting Notes

This port is intentionally structural and conservative.

## Directly Ported

- Plugin folders under `plugins/agent-plugins`, `plugins/vertical-plugins`, and
  `plugins/partner-built`.
- All `skills/**/SKILL.md` files and their bundled resources.
- Hook files, command source files, references, scripts, requirements, and docs.
- MCP server configuration files such as `.mcp.json`.
- Managed-agent cookbook files as reference artifacts.

## Converted

- `.claude-plugin/plugin.json` -> `.codex-plugin/plugin.json`.
- `.claude-plugin/marketplace.json` -> `.agents/plugins/marketplace.json`.
- `agents/*.md` -> `skills/agent-*/SKILL.md`.
- `commands/*.md` -> `skills/command-*/SKILL.md`.
- Skill front matter was normalized to the Codex `name` and `description` fields.

## Runtime Differences

Codex does not directly execute Claude Cowork tiles, Claude slash commands, or
Claude Managed Agent API `agent.yaml` files. The converted `agent-*` and `command-*`
skills provide equivalent procedural instructions inside Codex. Where upstream
instructions mention Claude-specific tool names, use the available Codex tools,
installed plugins, or configured MCP servers instead.

## Connector Requirements

The source repo references financial-data MCP providers such as Daloopa,
Morningstar, S&P Global/Kensho, FactSet, Moody's, MT Newswires, Aiera, LSEG,
PitchBook, Chronograph, and Egnyte. Their `.mcp.json` entries are preserved, but
real use requires provider access and credentials.
