from __future__ import annotations

from typing import Any

from yaml import safe_load


def stat(value: int, value_max: int = 0xFFFF, low: int = 1000, high: int = 3000) -> int:
    if not (0 <= value <= value_max):
        raise ValueError("Value out of range")
    v = value / value_max
    return round(low + (high - low) * v)


def get_skill_info(file_path: str = "julgi/skill/skill_ko.yml") -> dict[str, Any]:
    with open(file_path, encoding="utf-8") as f:
        data = safe_load(f)
    return data
