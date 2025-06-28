"""Telegram bot service using python-telegram-bot."""

from __future__ import annotations

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from ..config.settings import get_settings
from ..core.queue import TrackQueue, Track
from .youtube import fetch_audio


class TelegramBot:
    """Encapsulate the Telegram bot logic."""

    def __init__(self) -> None:
        settings = get_settings()
        self._app = Application.builder().token(settings.bot_token).build()
        self._queue = TrackQueue()
        self._register_handlers()

    def _register_handlers(self) -> None:
        self._app.add_handler(CommandHandler("start", self.start))
        self._app.add_handler(CommandHandler("play", self.play))
        self._app.add_handler(CommandHandler("skip", self.skip))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Send a welcome message."""
        await update.message.reply_text("Welcome to the music bot!")

    async def play(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Queue a YouTube track by URL."""
        if not context.args:
            await update.message.reply_text("Usage: /play <youtube url>")
            return
        url = context.args[0]
        await update.message.reply_text("Downloading...")
        audio = await fetch_audio(url)
        track = Track(title=audio.title, url=audio.url, duration=audio.duration)
        self._queue.put(track)
        await update.message.reply_text(f"Queued {audio.title}")

    async def skip(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Skip the current track."""
        skipped = self._queue.get_nowait()
        if skipped:
            await update.message.reply_text("Skipped.")
        else:
            await update.message.reply_text("Queue is empty.")

    async def run_polling(self) -> None:
        """Start the bot using polling."""
        await self._app.initialize()
        await self._app.start()
        await self._app.updater.start_polling()
        await self._idle()

    async def _idle(self) -> None:
        """Block until the bot is stopped."""
        await self._app.updater.wait()
        await self._app.stop()
        await self._app.shutdown()
