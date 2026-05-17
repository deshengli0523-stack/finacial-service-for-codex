#!/usr/bin/env python3
"""Convert Anthropic's financial-services Claude plugin repo into Codex plugins.

The source repository is intentionally file based, which makes the conversion
mostly structural:

- .claude-plugin/plugin.json -> .codex-plugin/plugin.json
- .claude-plugin/marketplace.json -> .agents/plugins/marketplace.json
- agents/*.md -> skills/agent-*/SKILL.md
- commands/*.md -> skills/command-*/SKILL.md
- SKILL.md front matter is normalized to Codex's name/description pair
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any


PLUGIN_ROOTS = (
    "plugins/agent-plugins",
    "plugins/vertical-plugins",
    "plugins/partner-built",
)

SKIP_NAMES = {
    ".git",
    ".github",
    ".claude-plugin",
    "__pycache__",
}

PORT_NOTE = (
    "\n\n> Codex port note: This skill was adapted from Anthropic's "
    "financial-services repository. Use Codex-native tools and available MCP "
    "servers in this environment; when the original instructions mention Claude, "
    "Claude Code, Cowork, or Claude-specific tool names, interpret that as the "
    "corresponding Codex workflow or connector if available.\n"
)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:64].strip("-") or "codex-skill"


def display_name(slug: str) -> str:
    known = {
        "dcf": "DCF",
        "lbo": "LBO",
        "kyc": "KYC",
        "gl": "GL",
        "nav": "NAV",
        "lp": "LP",
        "sp": "S&P",
        "lseg": "LSEG",
        "xlsx": "XLSX",
        "pptx": "PPTX",
        "xls": "XLS",
        "ib": "IB",
        "fx": "FX",
        "ai": "AI",
    }
    words = []
    for part in slug.replace("_", "-").split("-"):
        words.append(known.get(part, part.capitalize()))
    return " ".join(words)


def remove_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + len("\n---") :]
    if body.startswith("\n"):
        body = body[1:]

    meta: dict[str, Any] = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value in {"|", ">"}:
            block: list[str] = []
            i += 1
            while i < len(lines) and (
                not lines[i].strip() or lines[i].startswith((" ", "\t"))
            ):
                block.append(lines[i].strip())
                i += 1
            meta[key] = "\n".join(block).strip()
            continue
        meta[key] = value.strip('"').strip("'")
        i += 1
    return meta, body


def yaml_scalar(value: str) -> str:
    value = " ".join(value.replace("\r", "\n").split())
    value = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{value}"'


def skill_frontmatter(name: str, description: str) -> str:
    return f"---\nname: {name}\ndescription: {yaml_scalar(description)}\n---\n\n"


def normalize_skill(skill_path: Path) -> None:
    text = skill_path.read_text(encoding="utf-8")
    meta, body = remove_frontmatter(text)
    name = slugify(str(meta.get("name") or skill_path.parent.name))
    description = str(meta.get("description") or f"Use for {display_name(name)} financial-services workflows.")
    if "Codex port note:" not in body:
        body = PORT_NOTE + "\n" + body.lstrip()
    skill_path.write_text(skill_frontmatter(name, description) + body.rstrip() + "\n", encoding="utf-8")


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    for item in src.iterdir():
        if item.name in SKIP_NAMES:
            continue
        target = dst / item.name
        if item.is_dir():
            shutil.copytree(
                item,
                target,
                ignore=shutil.ignore_patterns(".git", ".github", ".claude-plugin", "__pycache__"),
            )
        else:
            shutil.copy2(item, target)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def plugin_manifest(source_manifest: dict[str, Any], plugin_dir: Path, repo_url: str) -> dict[str, Any]:
    name = slugify(source_manifest["name"])
    description = source_manifest.get("description", f"Codex financial-services plugin for {display_name(name)}.")
    manifest: dict[str, Any] = {
        "name": name,
        "version": source_manifest.get("version", "0.1.0"),
        "description": description,
        "author": {
            "name": source_manifest.get("author", {}).get("name", "Anthropic FSI, ported for Codex"),
            "url": "https://github.com/anthropics/financial-services",
        },
        "homepage": repo_url,
        "repository": repo_url,
        "license": "Apache-2.0",
        "keywords": ["finance", "financial-services", "codex", "skills", "mcp"],
        "skills": "./skills/",
        "interface": {
            "displayName": display_name(name),
            "shortDescription": description[:120],
            "longDescription": (
                description
                + " Ported from Anthropic's financial-services Claude plugin format into "
                "Codex plugin and skill conventions."
            ),
            "developerName": "Anthropic FSI / Codex port",
            "category": "Finance",
            "capabilities": ["Interactive", "Write"],
            "websiteURL": "https://github.com/anthropics/financial-services",
            "privacyPolicyURL": "https://openai.com/policies/row-privacy-policy/",
            "termsOfServiceURL": "https://openai.com/policies/row-terms-of-use/",
            "defaultPrompt": [
                f"Use {display_name(name)} workflows for a finance task.",
                f"Run a {display_name(name)} analysis with citations.",
            ],
            "brandColor": "#2563EB",
            "screenshots": [],
        },
    }
    if (plugin_dir / ".mcp.json").exists():
        manifest["mcpServers"] = "./.mcp.json"
    if (plugin_dir / "hooks" / "hooks.json").exists():
        manifest["hooks"] = "./hooks/hooks.json"
    return manifest


def create_agent_skill(agent_file: Path, skills_dir: Path) -> None:
    text = agent_file.read_text(encoding="utf-8")
    meta, body = remove_frontmatter(text)
    base = slugify(str(meta.get("name") or agent_file.stem))
    name = slugify(f"agent-{base}")
    description = str(
        meta.get("description")
        or f"Run the {display_name(base)} end-to-end financial-services agent workflow in Codex."
    )
    out_dir = skills_dir / name
    out_dir.mkdir(parents=True, exist_ok=True)
    body = (
        f"# {display_name(base)} Agent Workflow\n\n"
        "Use this as a Codex skill that emulates the original named agent. "
        "Codex does not install custom Claude Managed Agents directly, so keep "
        "the orchestration inside the current Codex session and delegate only "
        "when the active Codex environment supports it.\n"
        + PORT_NOTE
        + "\n"
        + body.lstrip()
    )
    (out_dir / "SKILL.md").write_text(skill_frontmatter(name, description) + body.rstrip() + "\n", encoding="utf-8")


def create_command_skill(command_file: Path, skills_dir: Path) -> None:
    text = command_file.read_text(encoding="utf-8")
    meta, body = remove_frontmatter(text)
    base = slugify(command_file.stem)
    name = slugify(f"command-{base}")
    description = str(meta.get("description") or f"Codex replacement for the /{base} financial-services command.")
    argument_hint = meta.get("argument-hint")
    out_dir = skills_dir / name
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = (
        f"# /{base} Command Workflow\n\n"
        "Use this skill when a user asks for the original slash command behavior. "
        "Codex does not load Claude slash commands directly, so follow the command "
        "workflow below as normal skill instructions.\n"
    )
    if argument_hint:
        prefix += f"\nOriginal argument hint: `{argument_hint}`\n"
    body = prefix + PORT_NOTE + "\n" + body.lstrip()
    (out_dir / "SKILL.md").write_text(skill_frontmatter(name, description) + body.rstrip() + "\n", encoding="utf-8")


def write_root_docs(dst: Path, repo_url: str, plugin_entries: list[dict[str, Any]]) -> None:
    plugins = "\n".join(
        f"- `{entry['name']}` -> `{entry['source']['path']}`" for entry in plugin_entries
    )
    readme = f"""# Financial Services For Codex

This repository is a Codex-ready port of Anthropic's Apache-2.0
[`financial-services`](https://github.com/anthropics/financial-services) reference
agents, plugins, skills, commands, and MCP connector definitions.

## What Changed

- Claude plugin manifests were converted from `.claude-plugin/plugin.json` to
  `.codex-plugin/plugin.json`.
- Claude marketplace metadata was converted to `.agents/plugins/marketplace.json`.
- Claude slash commands were converted into `command-*` Codex skills.
- Claude named agent prompts were converted into `agent-*` Codex skills.
- Existing `SKILL.md` files were normalized to Codex-readable front matter.
- Claude Managed Agent cookbooks are preserved as reference material in
  `managed-agent-cookbooks/`, but Codex uses the plugin and skill layout.

## Install / Use In Codex

Use this repository as a local/plugin marketplace source in Codex. The marketplace
file is at:

```text
.agents/plugins/marketplace.json
```

Available ported plugins:

{plugins}

MCP connectors are preserved where the original repo provided `.mcp.json` files.
Most financial data connectors require separate provider subscriptions, credentials,
and network access.

## Safety

These workflows draft analyst work product for qualified human review. They do not
provide investment, legal, tax, or accounting advice, and they must not execute
transactions, approve onboarding, post to ledgers, or bind risk without your own
controls.

## Provenance

- Upstream: https://github.com/anthropics/financial-services
- Codex port repository: {repo_url}
- License: Apache-2.0; see `LICENSE`.
"""
    notes = """# Codex Porting Notes

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
"""
    codex = """# Codex Repository Guide

This repository has been converted for Codex plugin discovery.

- Start with `.agents/plugins/marketplace.json`.
- Each plugin has a `.codex-plugin/plugin.json` manifest.
- Use `skills/**/SKILL.md` files as the active Codex workflows.
- `skills/agent-*` files replace upstream named agent prompts.
- `skills/command-*` files replace upstream Claude slash commands.
- `managed-agent-cookbooks/` and `upstream-docs/` are retained as reference
  material, not direct Codex runtime entrypoints.

Run `tools/validate_codex_port.py` after structural changes.
"""
    dst.joinpath("README.md").write_text(readme, encoding="utf-8")
    dst.joinpath("CODEX_PORTING_NOTES.md").write_text(notes, encoding="utf-8")
    dst.joinpath("CODEX.md").write_text(codex, encoding="utf-8")


def write_validation_script(dst: Path) -> None:
    script = r'''#!/usr/bin/env python3
"""Lightweight validation for the Codex financial-services port."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    sys.exit(1)


def main() -> None:
    marketplace = ROOT / ".agents" / "plugins" / "marketplace.json"
    if not marketplace.exists():
        fail("missing .agents/plugins/marketplace.json")
    data = json.loads(marketplace.read_text(encoding="utf-8"))
    entries = data.get("plugins", [])
    if not entries:
        fail("marketplace has no plugins")
    for entry in entries:
        name = entry.get("name", "")
        if not NAME_RE.match(name):
            fail(f"invalid plugin name {name!r}")
        source = entry.get("source", {})
        path = source.get("path")
        if not path:
            fail(f"plugin {name} missing source.path")
        plugin_dir = ROOT / path.replace("./", "", 1)
        manifest = plugin_dir / ".codex-plugin" / "plugin.json"
        if not manifest.exists():
            fail(f"plugin {name} missing {manifest.relative_to(ROOT)}")
        manifest_data = json.loads(manifest.read_text(encoding="utf-8"))
        if manifest_data.get("name") != name:
            fail(f"plugin {name} manifest name mismatch")
        skills_dir = plugin_dir / "skills"
        if not skills_dir.exists():
            fail(f"plugin {name} missing skills directory")
        skill_files = list(skills_dir.rglob("SKILL.md"))
        if not skill_files:
            fail(f"plugin {name} has no SKILL.md files")
        for skill_file in skill_files:
            text = skill_file.read_text(encoding="utf-8")
            if not text.startswith("---\n"):
                fail(f"{skill_file.relative_to(ROOT)} missing YAML front matter")
            head = text.split("---", 2)[1]
            if "name:" not in head or "description:" not in head:
                fail(f"{skill_file.relative_to(ROOT)} missing name or description")
    print(f"OK: validated {len(entries)} plugins")


if __name__ == "__main__":
    main()
'''
    tools = dst / "tools"
    tools.mkdir(exist_ok=True)
    tools.joinpath("validate_codex_port.py").write_text(script, encoding="utf-8")


def convert(source: Path, dst: Path, repo_url: str) -> None:
    plugin_entries: list[dict[str, Any]] = []

    if (dst / "CLAUDE.md").exists():
        (dst / "CLAUDE.md").unlink()

    if (source / "LICENSE").exists():
        shutil.copy2(source / "LICENSE", dst / "LICENSE")

    upstream_docs = dst / "upstream-docs"
    upstream_docs.mkdir(exist_ok=True)
    for rel in ("README.md", "CLAUDE.md"):
        src = source / rel
        if src.exists():
            shutil.copy2(src, upstream_docs / rel)

    if (source / "scripts").exists():
        copy_tree(source / "scripts", dst / "upstream-scripts")
    if (source / "managed-agent-cookbooks").exists():
        copy_tree(source / "managed-agent-cookbooks", dst / "managed-agent-cookbooks")
    if (source / "claude-for-msft-365-install").exists():
        copy_tree(source / "claude-for-msft-365-install", dst / "claude-for-msft-365-install")

    for root_rel in PLUGIN_ROOTS:
        root = source / root_rel
        if not root.exists():
            continue
        for src_plugin in sorted(p for p in root.iterdir() if p.is_dir()):
            source_manifest_path = src_plugin / ".claude-plugin" / "plugin.json"
            if not source_manifest_path.exists():
                continue
            dest_plugin = dst / root_rel / src_plugin.name
            copy_tree(src_plugin, dest_plugin)

            skills_dir = dest_plugin / "skills"
            skills_dir.mkdir(parents=True, exist_ok=True)

            for skill_file in skills_dir.rglob("SKILL.md"):
                normalize_skill(skill_file)

            agents_dir = dest_plugin / "agents"
            if agents_dir.exists():
                for agent_file in sorted(agents_dir.glob("*.md")):
                    create_agent_skill(agent_file, skills_dir)

            commands_dir = dest_plugin / "commands"
            if commands_dir.exists():
                for command_file in sorted(commands_dir.glob("*.md")):
                    create_command_skill(command_file, skills_dir)

            source_manifest = read_json(source_manifest_path)
            manifest = plugin_manifest(source_manifest, dest_plugin, repo_url)
            codex_dir = dest_plugin / ".codex-plugin"
            codex_dir.mkdir(exist_ok=True)
            codex_dir.joinpath("plugin.json").write_text(
                json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )

            plugin_entries.append(
                {
                    "name": manifest["name"],
                    "source": {
                        "source": "local",
                        "path": f"./{root_rel}/{src_plugin.name}",
                    },
                    "policy": {
                        "installation": "AVAILABLE",
                        "authentication": "ON_INSTALL",
                    },
                    "category": "Finance",
                }
            )

    marketplace = {
        "name": "financial-services-for-codex",
        "interface": {
            "displayName": "Financial Services For Codex",
        },
        "plugins": plugin_entries,
    }
    market_dir = dst / ".agents" / "plugins"
    market_dir.mkdir(parents=True, exist_ok=True)
    market_dir.joinpath("marketplace.json").write_text(
        json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    gitignore = """# Local conversion workspace
__source_financial_services/

# Python/cache output
__pycache__/
*.pyc

# OS/editor noise
.DS_Store
Thumbs.db
"""
    dst.joinpath(".gitignore").write_text(gitignore, encoding="utf-8")
    write_root_docs(dst, repo_url, plugin_entries)
    write_validation_script(dst)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--dest", required=True, type=Path)
    parser.add_argument("--repo-url", required=True)
    args = parser.parse_args()

    convert(args.source.resolve(), args.dest.resolve(), args.repo_url)


if __name__ == "__main__":
    main()
