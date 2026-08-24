from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from . import __version__
from .owner_map import load_and_validate
from .resources import find_root, prompt_files, skill_directories
from .validation import read_frontmatter, validate_repository


def _add_json_flag(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help="emit machine-readable JSON")


def _print(payload: Any, *, json_mode: bool, lines: list[str] | None = None) -> None:
    if json_mode:
        print(json.dumps(payload, indent=2, default=str))
    elif lines is not None:
        print("\n".join(lines))
    elif isinstance(payload, str):
        print(payload)
    else:
        print(json.dumps(payload, indent=2, default=str))


def _root(args: argparse.Namespace) -> Path:
    return find_root(getattr(args, "root", None))


def cmd_doctor(args: argparse.Namespace) -> int:
    root = _root(args)
    validation = validate_repository(root)
    optional = {
        name: importlib.util.find_spec(module) is not None
        for name, module in {
            "requests": "requests",
            "beautifulsoup4": "bs4",
            "lxml": "lxml",
            "reportlab": "reportlab",
        }.items()
    }
    payload = {
        "ok": validation["ok"] and sys.version_info >= (3, 10),
        "version": __version__,
        "python": sys.version.split()[0],
        "root": str(root),
        "skills": validation["skill_count"],
        "prompts": validation["prompt_count"],
        "optional_dependencies": optional,
        "validation_errors": validation["errors"],
        "external_mutations": "none",
    }
    lines = [
        f"geoskills {__version__}",
        f"root: {root}",
        f"skills: {payload['skills']} | prompts: {payload['prompts']}",
        f"validation: {'PASS' if payload['ok'] else 'FAIL'}",
        "external mutations: none",
        "optional: " + ", ".join(f"{name}={'yes' if present else 'no'}" for name, present in optional.items()),
    ]
    _print(payload, json_mode=getattr(args, "json", False), lines=lines)
    return 0 if payload["ok"] else 1


def cmd_validate(args: argparse.Namespace) -> int:
    payload = validate_repository(_root(args))
    lines = [
        f"validation: {'PASS' if payload['ok'] else 'FAIL'}",
        f"skills: {payload['skill_count']} | prompts: {payload['prompt_count']}",
        f"errors: {len(payload['errors'])} | warnings: {len(payload['warnings'])}",
    ]
    lines.extend(f"ERROR: {item}" for item in payload["errors"])
    lines.extend(f"WARN: {item}" for item in payload["warnings"])
    _print(payload, json_mode=getattr(args, "json", False), lines=lines)
    return 0 if payload["ok"] else 1


def cmd_skills_list(args: argparse.Namespace) -> int:
    items = []
    for directory in skill_directories(_root(args)):
        metadata, _ = read_frontmatter(directory / "SKILL.md")
        items.append({"name": metadata.get("name"), "description": metadata.get("description")})
    _print(
        {"count": len(items), "skills": items},
        json_mode=getattr(args, "json", False),
        lines=[f"{item['name']}: {item['description']}" for item in items],
    )
    return 0


def cmd_skills_show(args: argparse.Namespace) -> int:
    path = _root(args) / "skills" / args.name / "SKILL.md"
    if not path.exists():
        _print({"ok": False, "error": f"unknown skill: {args.name}"}, json_mode=getattr(args, "json", False))
        return 1
    raw = path.read_text(encoding="utf-8")
    _print({"ok": True, "name": args.name, "path": str(path), "content": raw}, json_mode=getattr(args, "json", False), lines=[raw])
    return 0


def _prompt_items(root: Path) -> list[dict[str, str]]:
    items = []
    for path in prompt_files(root):
        if path.name in {"README.md", "EXAMPLES.md"} or path.name.startswith("00-"):
            continue
        raw = path.read_text(encoding="utf-8")
        title = next((line.removeprefix("# ") for line in raw.splitlines() if line.startswith("# ")), path.stem)
        items.append({"name": path.stem, "title": title, "path": str(path.relative_to(root))})
    return items


def cmd_prompts_list(args: argparse.Namespace) -> int:
    items = _prompt_items(_root(args))
    _print(
        {"count": len(items), "prompts": items},
        json_mode=getattr(args, "json", False),
        lines=[f"{item['name']}: {item['title']}" for item in items],
    )
    return 0


def cmd_prompts_show(args: argparse.Namespace) -> int:
    root = _root(args)
    hit = next((item for item in _prompt_items(root) if item["name"] == args.name), None)
    if hit is None:
        _print({"ok": False, "error": f"unknown prompt: {args.name}"}, json_mode=getattr(args, "json", False))
        return 1
    path = root / hit["path"]
    raw = path.read_text(encoding="utf-8")
    _print({"ok": True, **hit, "content": raw}, json_mode=getattr(args, "json", False), lines=[raw])
    return 0


def cmd_owner_map_validate(args: argparse.Namespace) -> int:
    path = Path(args.path).expanduser().resolve()
    payload, errors = load_and_validate(path)
    result = {"ok": not errors, "path": str(path), "errors": errors, "owner_count": len((payload or {}).get("owners", []))}
    lines = [f"owner map: {'PASS' if result['ok'] else 'FAIL'}", f"path: {path}", f"owners: {result['owner_count']}"]
    lines.extend(f"ERROR: {error}" for error in errors)
    _print(result, json_mode=getattr(args, "json", False), lines=lines)
    return 0 if result["ok"] else 1


def _run_bundled_script(args: argparse.Namespace, relative: str, script_args: list[str]) -> int:
    script = _root(args) / relative
    result = subprocess.run([sys.executable, str(script), *script_args], capture_output=True, text=True, check=False)
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError:
        payload = {"ok": False, "returncode": result.returncode, "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}
    if isinstance(payload, dict) and "ok" not in payload:
        payload["ok"] = result.returncode == 0 and not payload.get("error") and not payload.get("errors")
    _print(payload, json_mode=getattr(args, "json", False))
    return 0 if result.returncode == 0 and payload.get("ok", True) else 1


def cmd_inspect(args: argparse.Namespace) -> int:
    return _run_bundled_script(args, "skills/geo/scripts/fetch_page.py", [args.url, args.mode])


def cmd_citability(args: argparse.Namespace) -> int:
    return _run_bundled_script(args, "skills/geo/scripts/citability_scorer.py", [args.url])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="geoskills", description="Agent-native CLI for GEO skill discovery and deterministic checks")
    parser.add_argument("--version", action="version", version=f"geoskills {__version__}")
    parser.add_argument("--root", help="explicit geo-skills resource root")
    _add_json_flag(parser)
    sub = parser.add_subparsers(dest="command", required=True)

    doctor = sub.add_parser("doctor", help="verify installation, resources, and skill contracts")
    _add_json_flag(doctor)
    doctor.set_defaults(func=cmd_doctor)

    validate = sub.add_parser("validate", help="validate every skill and bundled prompt contract")
    _add_json_flag(validate)
    validate.set_defaults(func=cmd_validate)

    skills = sub.add_parser("skills", help="discover bundled Agent Skills")
    skills_sub = skills.add_subparsers(dest="skills_command", required=True)
    skills_list = skills_sub.add_parser("list", help="list skills")
    _add_json_flag(skills_list)
    skills_list.set_defaults(func=cmd_skills_list)
    skills_show = skills_sub.add_parser("show", help="show one SKILL.md")
    skills_show.add_argument("name")
    _add_json_flag(skills_show)
    skills_show.set_defaults(func=cmd_skills_show)

    prompts = sub.add_parser("prompts", help="discover paste-ready prompt packs")
    prompt_sub = prompts.add_subparsers(dest="prompts_command", required=True)
    prompt_list = prompt_sub.add_parser("list", help="list prompts")
    _add_json_flag(prompt_list)
    prompt_list.set_defaults(func=cmd_prompts_list)
    prompt_show = prompt_sub.add_parser("show", help="show one prompt")
    prompt_show.add_argument("name")
    _add_json_flag(prompt_show)
    prompt_show.set_defaults(func=cmd_prompts_show)

    owner_map = sub.add_parser("owner-map", help="validate the GEO-to-TokenMax owner-intent handoff")
    owner_sub = owner_map.add_subparsers(dest="owner_command", required=True)
    owner_validate = owner_sub.add_parser("validate", help="validate an owner-intent JSON file")
    owner_validate.add_argument("path")
    _add_json_flag(owner_validate)
    owner_validate.set_defaults(func=cmd_owner_map_validate)

    inspect = sub.add_parser("inspect", help="run deterministic read-only page inspection")
    inspect.add_argument("url")
    inspect.add_argument("--mode", choices=["page", "robots", "llms", "sitemap", "blocks", "full"], default="page")
    _add_json_flag(inspect)
    inspect.set_defaults(func=cmd_inspect)

    citability = sub.add_parser("citability", help="score page passages for extractability")
    citability.add_argument("url")
    _add_json_flag(citability)
    citability.set_defaults(func=cmd_citability)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    raise SystemExit(args.func(args))
