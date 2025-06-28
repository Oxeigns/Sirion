"""Simple audio track queue management."""

from __future__ import annotations

import asyncio
from collections import deque
from dataclasses import dataclass
from typing import Deque, Optional


@dataclass
class Track:
    """Represent an audio track."""

    title: str
    url: str
    duration: int | None = None


class TrackQueue:
    """Asynchronous queue for tracks."""

    def __init__(self) -> None:
        self._queue: Deque[Track] = deque()
        self._event = asyncio.Event()

    def put(self, track: Track) -> None:
        """Add a track to the queue."""
        self._queue.append(track)
        self._event.set()

    async def get(self) -> Track:
        """Wait for and return the next track."""
        while not self._queue:
            self._event.clear()
            await self._event.wait()
        return self._queue.popleft()

    def get_nowait(self) -> Optional[Track]:
        """Return the next track if available."""
        if self._queue:
            return self._queue.popleft()
        return None

    def peek(self) -> Optional[Track]:
        """Return the next track without removing it."""
        return self._queue[0] if self._queue else None

    def __len__(self) -> int:
        return len(self._queue)
