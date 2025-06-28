"""YouTube audio fetching utilities using yt-dlp."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Optional

from yt_dlp import YoutubeDL


@dataclass
class YouTubeAudio:
    """Represent fetched YouTube audio information."""

    title: str
    url: str
    duration: int | None
    file_path: str


async def fetch_audio(url: str) -> YouTubeAudio:
    """Fetch audio information and download the file."""

    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "outtmpl": "%(id)s.%(ext)s",
    }
    loop = asyncio.get_event_loop()

    def _download() -> tuple[str, Optional[int], str, str]:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "unknown")
            duration = info.get("duration")
            file_path = ydl.prepare_filename(info)
            return title, duration, info["webpage_url"], file_path

    title, duration, page_url, file_path = await loop.run_in_executor(None, _download)
    return YouTubeAudio(title=title, url=page_url, duration=duration, file_path=file_path)
