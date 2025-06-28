"""Utility conversion helpers."""

from __future__ import annotations

def time_to_seconds(time: str) -> int:
    """Convert a time string (``HH:MM`` or ``MM:SS``) to seconds."""
    parts = [int(part) for part in time.split(":")]
    seconds = 0
    for idx, part in enumerate(reversed(parts)):
        seconds += part * 60**idx
    return seconds

def seconds_to_min(seconds: int | None) -> str:
    """Convert seconds to a ``HH:MM:SS`` style string."""
    if seconds is None:
        return "-"
    seconds = int(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    parts: list[str] = []
    if days:
        parts.append(f"{days:02d}")
    if days or hours:
        parts.append(f"{hours:02d}")
    parts.append(f"{minutes:02d}")
    parts.append(f"{seconds:02d}")
    return ":".join(parts)
