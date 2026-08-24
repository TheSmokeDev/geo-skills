import json

import yaml

from geoskills import __version__
from geoskills.resources import find_root
from geoskills.validation import validate_repository


def test_public_repository_contract_is_valid():
    result = validate_repository(find_root())
    assert result["ok"], result["errors"]
    assert result["skill_count"] >= 28
    assert result["prompt_count"] == 7


def test_citation_and_owner_schema_are_machine_readable():
    root = find_root()
    citation = yaml.safe_load((root / "CITATION.cff").read_text(encoding="utf-8"))
    schema = json.loads((root / "schemas" / "owner-intent-map.schema.json").read_text(encoding="utf-8"))
    assert citation["version"] == __version__
    assert schema["properties"]["schema_version"]["const"] == 1
