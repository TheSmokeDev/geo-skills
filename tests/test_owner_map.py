import json
from pathlib import Path

from geoskills.owner_map import validate_owner_map


FIXTURE = Path(__file__).parent / "fixtures" / "owner-map.valid.json"


def test_valid_owner_map_passes():
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert validate_owner_map(payload) == []


def test_owner_map_fails_closed_for_missing_source_and_unknown_owner():
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload["owners"][0]["evidence_sources"] = []
    payload["pilot"][0]["owner_id"] = "missing"
    payload["gold_page"]["owner_id"] = "missing"
    payload["evidence_collected_at"] = "not-a-date"
    payload["surprise"] = True
    errors = validate_owner_map(payload)
    assert any("evidence_sources cannot be empty" in error for error in errors)
    assert any("must reference" in error for error in errors)
    assert any("ISO-8601" in error for error in errors)
    assert any("unknown top-level" in error for error in errors)


def test_owner_map_caps_pilot_at_ten():
    payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
    payload["pilot"] = payload["pilot"] * 11
    assert "pilot cannot contain more than 10 routes" in validate_owner_map(payload)
