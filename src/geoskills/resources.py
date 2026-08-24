from __future__ import annotations

import os
import sysconfig
from pathlib import Path


def _is_root(path: Path) -> bool:
    return (path / "skills").is_dir() and (path / "README.md").is_file()


def find_root(explicit: str | Path | None = None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    if os.environ.get("GEOSKILLS_ROOT"):
        candidates.append(Path(os.environ["GEOSKILLS_ROOT"]))

    cwd = Path.cwd().resolve()
    candidates.extend([cwd, *cwd.parents])
    candidates.append(Path(__file__).resolve().parents[2])
    candidates.append(Path(sysconfig.get_path("data")) / "share" / "geoskills")

    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.expanduser().resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if _is_root(resolved):
            return resolved
    raise RuntimeError(
        "geo-skills resources not found; install the package or set GEOSKILLS_ROOT to a geo-skills checkout"
    )


def skill_directories(root: Path) -> list[Path]:
    return sorted(path for path in (root / "skills").iterdir() if (path / "SKILL.md").is_file())


def prompt_files(root: Path) -> list[Path]:
    prompt_root = root / "prompt-packs"
    return sorted(prompt_root.rglob("*.md")) if prompt_root.exists() else []
