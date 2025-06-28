"""Simple service helpers."""

import datetime

async def ping() -> dict[str, str]:
    """Return a simple ping response with current UTC time."""
    return {"status": "ok", "timestamp": datetime.datetime.utcnow().isoformat()}
