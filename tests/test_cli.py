import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _cli() -> list[str]:
    installed = shutil.which("geoskills")
    if installed:
        return [installed]
    if os.environ.get("GEOSKILLS_FORCE_INSTALLED") == "1":
        raise RuntimeError("geoskills is not installed on PATH")
    return [sys.executable, "-m", "geoskills"]


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(_cli() + list(args), cwd=ROOT, capture_output=True, text=True, check=False)


def test_help_and_version():
    assert run_cli("--help").returncode == 0
    version = run_cli("--version")
    assert version.returncode == 0
    assert "geoskills 0.1.1" in version.stdout


def test_doctor_json():
    result = run_cli("--json", "doctor")
    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["external_mutations"] == "none"


def test_skill_and_prompt_discovery_json():
    skills = run_cli("skills", "list", "--json")
    prompts = run_cli("prompts", "list", "--json")
    assert skills.returncode == 0
    assert prompts.returncode == 0
    assert json.loads(skills.stdout)["count"] >= 28
    assert json.loads(prompts.stdout)["count"] == 7


def test_owner_map_validation_command():
    fixture = ROOT / "tests" / "fixtures" / "owner-map.valid.json"
    result = run_cli("owner-map", "validate", str(fixture), "--json")
    assert result.returncode == 0, result.stdout + result.stderr
    assert json.loads(result.stdout)["ok"] is True
