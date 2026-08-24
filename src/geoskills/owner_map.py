from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


ACTIONS = {"upgrade", "create", "consolidate", "hold"}
STATUSES = {"ready", "partial", "blocked"}
REQUIRED_TOP_LEVEL = {
    "schema_version",
    "status",
    "evidence_collected_at",
    "market",
    "owners",
    "collisions",
    "gold_page",
    "pilot",
    "held",
    "quality_gates",
    "measurement_plan",
    "coverage_receipt",
}


def validate_owner_map(payload: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(payload, dict):
        return ["owner map must be a JSON object"]
    missing = sorted(REQUIRED_TOP_LEVEL - set(payload))
    if missing:
        errors.append(f"missing top-level fields: {', '.join(missing)}")
    unknown = sorted(set(payload) - REQUIRED_TOP_LEVEL)
    if unknown:
        errors.append(f"unknown top-level fields: {', '.join(unknown)}")
    if payload.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    if payload.get("status") not in STATUSES:
        errors.append("status must be ready, partial, or blocked")
    try:
        datetime.fromisoformat(str(payload.get("evidence_collected_at") or "").replace("Z", "+00:00"))
    except ValueError:
        errors.append("evidence_collected_at must be an ISO-8601 timestamp")
    market = payload.get("market")
    if not isinstance(market, dict) or not str(market.get("location") or "").strip() or not str(
        market.get("language") or ""
    ).strip():
        errors.append("market requires non-empty location and language")

    owners = payload.get("owners")
    owner_ids: set[str] = set()
    if not isinstance(owners, list):
        errors.append("owners must be a list")
        owners = []
    for index, owner in enumerate(owners):
        prefix = f"owners[{index}]"
        if not isinstance(owner, dict):
            errors.append(f"{prefix} must be an object")
            continue
        owner_id = str(owner.get("intent_id") or "").strip()
        action = owner.get("action")
        if not owner_id:
            errors.append(f"{prefix}.intent_id is required")
        elif owner_id in owner_ids:
            errors.append(f"{prefix}.intent_id is duplicated: {owner_id}")
        owner_ids.add(owner_id)
        if action not in ACTIONS:
            errors.append(f"{prefix}.action must be upgrade, create, consolidate, or hold")
        if not str(owner.get("primary_query") or "").strip():
            errors.append(f"{prefix}.primary_query is required")
        if action in {"upgrade", "create", "consolidate"} and not str(owner.get("route_owner") or "").strip():
            errors.append(f"{prefix}.route_owner is required for action {action}")
        evidence = owner.get("evidence_sources")
        if not isinstance(evidence, list):
            errors.append(f"{prefix}.evidence_sources must be a list")
        elif action != "hold" and not evidence:
            errors.append(f"{prefix}.evidence_sources cannot be empty for action {action}")

    pilot = payload.get("pilot")
    if not isinstance(pilot, list):
        errors.append("pilot must be a list")
        pilot = []
    if len(pilot) > 10:
        errors.append("pilot cannot contain more than 10 routes")
    for index, item in enumerate(pilot):
        prefix = f"pilot[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{prefix} must be an object")
            continue
        if item.get("owner_id") not in owner_ids:
            errors.append(f"{prefix}.owner_id must reference an owners[].intent_id")
        for field in ("entity", "route", "reason"):
            if not str(item.get(field) or "").strip():
                errors.append(f"{prefix}.{field} is required")
    for field in ("collisions", "held", "quality_gates"):
        if not isinstance(payload.get(field), list):
            errors.append(f"{field} must be a list")
    for field in ("measurement_plan", "coverage_receipt"):
        if not isinstance(payload.get(field), dict):
            errors.append(f"{field} must be an object")
    gold_page = payload.get("gold_page")
    if gold_page is not None and not isinstance(gold_page, dict):
        errors.append("gold_page must be an object or null")
    elif isinstance(gold_page, dict) and gold_page.get("owner_id") not in owner_ids:
        errors.append("gold_page.owner_id must reference an owners[].intent_id")
    return errors


def load_and_validate(path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return None, [f"cannot read owner map: {exc}"]
    return payload, validate_owner_map(payload)
