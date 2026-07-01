#!/usr/bin/env python3
"""Validate plugin and Skill metadata without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
MANIFEST_PATH_KEYS = {
    "file",
    "files",
    "path",
    "paths",
    "resource",
    "resources",
    "skill",
    "skills",
    "skillPath",
    "skillPaths",
    "skill_path",
    "skill_paths",
}


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_semver(value: object, label: str) -> None:
    if not isinstance(value, str) or not SEMVER_RE.fullmatch(value):
        fail(f"{label} must be SemVer")


def load_plugin_json() -> dict:
    path = ROOT / ".codex-plugin" / "plugin.json"
    if not path.is_file():
        fail("missing .codex-plugin/plugin.json")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json is invalid JSON: {exc}")
    if not isinstance(payload, dict):
        fail("plugin.json must contain an object")
    return payload


def validate_plugin_json(payload: dict) -> None:
    for key in ("name", "version", "description", "author", "interface"):
        if key not in payload:
            fail(f"plugin.json missing {key}")
    require_semver(payload["version"], "plugin.json version")
    if payload.get("license") != "MIT":
        fail("plugin.json license must be MIT")
    if not (ROOT / "LICENSE").is_file():
        fail("missing LICENSE")
    for value in walk_strings(payload):
        if value.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", value):
            fail(f"plugin.json contains absolute path: {value}")
    validate_manifest_paths(payload)


def walk_strings(value: object):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_strings(item)


def validate_manifest_paths(value: object, is_path_field: bool = False, label: str = "plugin.json") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            validate_manifest_paths(item, key in MANIFEST_PATH_KEYS, f"{label}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            validate_manifest_paths(item, is_path_field, f"{label}[{index}]")
    elif is_path_field and isinstance(value, str):
        validate_manifest_path(value, label)


def validate_manifest_path(value: str, label: str) -> None:
    if not value:
        fail(f"{label} must not be empty")
    if "://" in value:
        fail(f"{label} must be a repository-relative path: {value}")
    candidate = (ROOT / value).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        fail(f"{label} points outside repository: {value}")
    if not candidate.exists():
        fail(f"{label} points to missing path: {value}")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} missing frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail(f"{path.relative_to(ROOT)} frontmatter is not closed")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            fail(f"{path.relative_to(ROOT)} has unsupported frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields


def validate_skills() -> None:
    skills_root = ROOT / "skills"
    if not skills_root.exists():
        return
    if not skills_root.is_dir():
        fail("skills must be a directory")
    for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
        if skill_dir.name.startswith("."):
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            fail(f"{skill_dir.relative_to(ROOT)} missing SKILL.md")
        fields = parse_frontmatter(skill_md)
        for key in ("name", "description", "version"):
            if not fields.get(key):
                fail(f"{skill_md.relative_to(ROOT)} missing frontmatter field {key}")
        if fields["name"] != skill_dir.name:
            fail(f"{skill_md.relative_to(ROOT)} name must match directory name")
        require_semver(fields["version"], f"{skill_md.relative_to(ROOT)} version")


def main() -> None:
    validate_plugin_json(load_plugin_json())
    validate_skills()
    print("validation passed")


if __name__ == "__main__":
    main()
