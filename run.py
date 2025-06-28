import asyncio
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env before importing any project modules
load_dotenv(Path(__file__).resolve().parent / ".env")

import OxygenMusic  # noqa: E402
from OxygenMusic.bootstrap import bootstrap  # noqa: E402
from OxygenMusic.logging import LOGGER  # noqa: E402


if __name__ == "__main__":
    try:
        (
            OxygenMusic.app,
            OxygenMusic.userbot,
            OxygenMusic.Apple,
            OxygenMusic.Carbon,
            OxygenMusic.SoundCloud,
            OxygenMusic.Spotify,
            OxygenMusic.Resso,
            OxygenMusic.YouTube,
            OxygenMusic.Telegram,
        ) = bootstrap()
    except Exception:
        LOGGER(__name__).exception("Failed during bootstrap")
        raise

    from OxygenMusic.__main__ import init

    try:
        asyncio.run(init())
    except KeyboardInterrupt:
        LOGGER(__name__).info("Bot stopped by user")
