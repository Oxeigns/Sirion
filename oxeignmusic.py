from ShrutiMusic.__main__ import init
import asyncio

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
