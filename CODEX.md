# Codex Repository Guide

This repository has been converted for Codex plugin discovery.

- Start with `.agents/plugins/marketplace.json`.
- Each plugin has a `.codex-plugin/plugin.json` manifest.
- Use `skills/**/SKILL.md` files as the active Codex workflows.
- `skills/agent-*` files replace upstream named agent prompts.
- `skills/command-*` files replace upstream Claude slash commands.
- `managed-agent-cookbooks/` and `upstream-docs/` are retained as reference
  material, not direct Codex runtime entrypoints.

Run `tools/validate_codex_port.py` after structural changes.
