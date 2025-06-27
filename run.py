import asyncio
import OxygenMusic
from OxygenMusic.bootstrap import bootstrap


if __name__ == "__main__":
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

    from OxygenMusic.__main__ import init

    asyncio.run(init())
