from pathlib import Path

from setuptools import setup


ROOT = Path(__file__).resolve().parent
RESOURCE_DIRS = ("agents", "docs", "prompt-packs", "schemas", "skills")
ROOT_FILES = ("CITATION.cff", "CONTRIBUTING.md", "INSTALL.md", "LICENSE", "README.md")


def bundled_data_files() -> list[tuple[str, list[str]]]:
    grouped: dict[str, list[str]] = {}
    for directory in RESOURCE_DIRS:
        base = ROOT / directory
        if not base.exists():
            continue
        for path in sorted(base.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
                continue
            relative = path.relative_to(ROOT)
            destination = str(Path("share/geoskills") / relative.parent)
            grouped.setdefault(destination, []).append(relative.as_posix())
    grouped.setdefault("share/geoskills", []).extend(
        name for name in ROOT_FILES if (ROOT / name).exists()
    )
    return sorted(grouped.items())


setup(data_files=bundled_data_files())
