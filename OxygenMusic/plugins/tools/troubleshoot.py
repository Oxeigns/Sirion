from pyrogram import filters
from pyrogram.types import Message

from OxygenMusic import app
from config import BANNED_USERS

TROUBLE_TEXT = (
    "If you experience issues during playback:\n"
    "- Ensure the bot has required permissions.\n"
    "- Try /restart if the bot is unresponsive.\n"
    "- Check your server or Heroku logs for errors.\n"
    "- Update to the latest version of OxygenMusic."
)

@app.on_message(filters.command(["troubleshoot", "trouble"]) & ~BANNED_USERS)
async def troubleshoot_cmd(client: app, message: Message):
    await message.reply_text(TROUBLE_TEXT)
