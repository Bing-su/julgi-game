from __future__ import annotations


def stat(value: int, value_max: int = 0xFFFF, low: int = 1000, high: int = 3000) -> int:
    if not (0 <= value <= value_max):
        raise ValueError("Value out of range")
    v = value / value_max
    return round(low + (high - low) * v)
