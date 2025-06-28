import asyncio
from dotenv import load_dotenv
import OxygenMusic
from OxygenMusic.bootstrap import bootstrap
from OxygenMusic.logging import LOGGER

load_dotenv()


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
