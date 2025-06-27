import asyncio
from dotenv import load_dotenv

load_dotenv()

import OxygenMusic
from OxygenMusic.bootstrap import bootstrap
from OxygenMusic.logging import LOGGER


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

    asyncio.run(init())
