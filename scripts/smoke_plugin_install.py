#!/usr/bin/env python3
"""Smoke-test plugin discovery from a clean tracked-file install tree."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path(".codex-plugin/plugin.json")
PATH_KEYS = {
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
    "template",
    "templates",
    "templatePath",
    "templatePaths",
    "template_path",
    "template_paths",
}


def fail(area: str, message: str) -> None:
    print(f"error: {area}: {message}", file=sys.stderr)
    raise SystemExit(1)


def git_ls_files() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except FileNotFoundError:
        fail("environment", "git is not available")
    except subprocess.CalledProcessError as exc:
        fail("environment", f"git ls-files failed: {exc.stderr.decode().strip()}")
    files = [Path(item.decode()) for item in result.stdout.split(b"\0") if item]
    if not files:
        fail("environment", "no tracked files discovered")
    return files


def copy_clean_tree(target: Path) -> None:
    for rel_path in git_ls_files():
        source = ROOT / rel_path
        if not source.is_file():
            continue
        destination = target / rel_path
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def load_manifest(root: Path) -> dict:
    path = root / MANIFEST
    if not path.is_file():
        fail("manifest", "missing .codex-plugin/plugin.json")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail("manifest", f"plugin.json is invalid JSON: {exc}")
    if not isinstance(payload, dict):
        fail("manifest", "plugin.json must contain an object")
    return payload


def validate_relative_path(root: Path, value: object, label: str) -> Path:
    if not isinstance(value, str) or not value:
        fail("manifest", f"{label} must be a non-empty relative path")
    if "://" in value or value.startswith("/") or re.match(r"^[A-Za-z]:[\\/]", value):
        fail("manifest", f"{label} must be repository-relative: {value}")
    candidate = (root / value).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError:
        fail("manifest", f"{label} points outside repository: {value}")
    if not candidate.exists():
        fail("manifest", f"{label} points to missing path: {value}")
    return candidate


def walk_manifest_paths(value: object, is_path_field: bool = False, label: str = "plugin.json"):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from walk_manifest_paths(item, key in PATH_KEYS, f"{label}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk_manifest_paths(item, is_path_field, f"{label}[{index}]")
    elif is_path_field:
        yield label, value


def validate_manifest_paths(root: Path, manifest: dict) -> int:
    if "skills" not in manifest:
        fail("manifest", "plugin.json missing skills path")
    template_paths = 0
    for label, value in walk_manifest_paths(manifest):
        validate_relative_path(root, value, label)
        if "template" in label.lower():
            template_paths += 1
    return template_paths


def discover_skills(root: Path, manifest: dict) -> int:
    skills_root = validate_relative_path(root, manifest["skills"], "plugin.json.skills")
    if not skills_root.is_dir():
        fail("manifest", "plugin.json.skills must point to a directory")
    skill_dirs = sorted(path for path in skills_root.iterdir() if path.is_dir() and not path.name.startswith("."))
    if not skill_dirs:
        fail("Skill", f"{skills_root.relative_to(root)} contains no Skill directories")
    for skill_dir in skill_dirs:
        if not (skill_dir / "SKILL.md").is_file():
            fail("Skill", f"{skill_dir.relative_to(root)} missing SKILL.md")
    return len(skill_dirs)


def run_clean_validation(root: Path) -> None:
    validator = root / "scripts" / "validate_repo.py"
    if not validator.is_file():
        fail("environment", "clean tree missing scripts/validate_repo.py")
    result = subprocess.run(
        [sys.executable, str(validator)],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        fail("validation", f"clean validate_repo.py failed: {detail}")


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="desktop-taste-install-") as tmp:
        install_root = Path(tmp)
        copy_clean_tree(install_root)
        manifest = load_manifest(install_root)
        template_paths = validate_manifest_paths(install_root, manifest)
        skill_count = discover_skills(install_root, manifest)
        run_clean_validation(install_root)
    print(f"install smoke passed: manifest ok, skills={skill_count}, templates={template_paths}")


if __name__ == "__main__":
    main()
