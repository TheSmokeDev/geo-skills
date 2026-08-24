from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

import yaml

from .resources import prompt_files, skill_directories


ALLOWED_FRONTMATTER_KEYS = {"allowed-tools", "description", "license", "metadata", "name"}
TEXT_SUFFIXES = {".json", ".md", ".py", ".yaml", ".yml"}
SKIP_PARTS = {".artifacts", ".git", ".pytest_cache", ".venv", "__pycache__", "build", "dist"}
PROMPT_REQUIRED_TERMS = (
    "Output contract",
    "OBSERVED",
    "CALCULATED",
    "INFERRED",
    "PROPOSED",
    "coverage",
)


def read_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", raw, re.S)
    if not match:
        raise ValueError("missing YAML frontmatter")
    payload = yaml.safe_load(match.group(1)) or {}
    if not isinstance(payload, dict):
        raise ValueError("frontmatter must be a mapping")
    return payload, raw[match.end() :]


def validate_skill(path: Path) -> tuple[list[str], list[str], dict[str, Any]]:
    errors: list[str] = []
    warnings: list[str] = []
    metadata: dict[str, Any] = {}
    skill_file = path / "SKILL.md"
    try:
        metadata, body = read_frontmatter(skill_file)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        return [f"{path.name}: {exc}"], warnings, metadata

    unknown = sorted(set(metadata) - ALLOWED_FRONTMATTER_KEYS)
    if unknown:
        errors.append(f"{path.name}: unexpected frontmatter keys: {', '.join(unknown)}")
    name = metadata.get("name")
    description = metadata.get("description")
    if name != path.name:
        errors.append(f"{path.name}: frontmatter name must match directory")
    if not isinstance(description, str) or not description.strip():
        errors.append(f"{path.name}: description must be a non-empty string")
    elif "<" in description or ">" in description:
        errors.append(f"{path.name}: description cannot contain angle brackets")
    if not body.strip():
        errors.append(f"{path.name}: SKILL.md body is empty")
    if metadata.get("metadata") is not None and not isinstance(metadata["metadata"], dict):
        errors.append(f"{path.name}: metadata must be a mapping")

    openai_yaml = path / "agents" / "openai.yaml"
    if openai_yaml.exists():
        try:
            agent_data = yaml.safe_load(openai_yaml.read_text(encoding="utf-8")) or {}
            interface = agent_data.get("interface") or {}
            default_prompt = interface.get("default_prompt") or ""
            short = interface.get("short_description") or ""
            if not isinstance(default_prompt, str) or f"${path.name}" not in default_prompt:
                errors.append(f"{path.name}: agents/openai.yaml default_prompt must mention ${path.name}")
            if not isinstance(short, str) or not 25 <= len(short) <= 64:
                errors.append(f"{path.name}: agents/openai.yaml short_description must be 25-64 characters")
        except (OSError, UnicodeError, yaml.YAMLError, AttributeError) as exc:
            errors.append(f"{path.name}: invalid agents/openai.yaml: {exc}")
    else:
        warnings.append(f"{path.name}: agents/openai.yaml is not present")
    return errors, warnings, metadata


def validate_repository(root: Path) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    names: set[str] = set()
    skills = skill_directories(root)

    for directory in skills:
        skill_errors, skill_warnings, metadata = validate_skill(directory)
        errors.extend(skill_errors)
        warnings.extend(skill_warnings)
        name = metadata.get("name")
        if isinstance(name, str):
            if name in names:
                errors.append(f"duplicate skill name: {name}")
            names.add(name)

    prompts = [path for path in prompt_files(root) if re.match(r"0[1-7]-", path.name)]
    for path in prompts:
        try:
            raw = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
            continue
        for term in PROMPT_REQUIRED_TERMS:
            if term not in raw:
                errors.append(f"{path.relative_to(root)}: missing prompt contract term {term!r}")

    for path in root.rglob("*"):
        if (
            not path.is_file()
            or any(part in SKIP_PARTS or part.endswith(".egg-info") for part in path.parts)
            or path.suffix.lower() not in TEXT_SUFFIXES
        ):
            continue
        try:
            raw = path.read_text(encoding="utf-8")
            if path.suffix.lower() == ".json":
                json.loads(raw)
            elif path.suffix.lower() in {".yaml", ".yml"}:
                yaml.safe_load(raw)
        except (OSError, UnicodeError, json.JSONDecodeError, yaml.YAMLError) as exc:
            errors.append(f"{path.relative_to(root)}: invalid UTF-8 or structured data: {exc}")

    citation = root / "CITATION.cff"
    try:
        citation_data = yaml.safe_load(citation.read_text(encoding="utf-8")) or {}
        for field in ("cff-version", "message", "title", "authors"):
            if not citation_data.get(field):
                errors.append(f"CITATION.cff: missing {field}")
    except (OSError, UnicodeError, yaml.YAMLError) as exc:
        errors.append(f"CITATION.cff: invalid: {exc}")

    return {
        "ok": not errors,
        "root": str(root),
        "skill_count": len(skills),
        "prompt_count": len(prompts),
        "errors": errors,
        "warnings": warnings,
    }
