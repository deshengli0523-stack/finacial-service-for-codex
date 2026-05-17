#!/usr/bin/env python3
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
