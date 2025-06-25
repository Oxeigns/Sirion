import asyncio

from OxygenMusic.__main__ import init

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
