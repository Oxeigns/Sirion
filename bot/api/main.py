"""FastAPI application entry point."""

from fastapi import FastAPI

from ..config.settings import get_settings
from ..services.telegram_bot import TelegramBot

app = FastAPI(title="Telegram Music Bot")


@app.on_event("startup")
async def on_startup() -> None:
    """Initialize services on startup."""
    get_settings()
    bot = TelegramBot()
    app.state.bot = bot
    # Start bot polling in background task
    import asyncio
    asyncio.create_task(bot.run_polling())


@app.get("/ping")
async def ping() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
