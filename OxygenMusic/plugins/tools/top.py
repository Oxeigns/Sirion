from pyrogram import filters
from pyrogram.types import Message

from OxygenMusic import app
from OxygenMusic.utils.database import get_top_users, get_top_chats
from config import BANNED_USERS

@app.on_message(filters.command(["top", "toptracks"]) & ~BANNED_USERS)
async def top_cmd(_, message: Message):
    top_users = get_top_users()
    top_chats = get_top_chats()
    text = "<b>Top Users:</b>\n"
    for i, (uid, count) in enumerate(top_users, start=1):
        text += f"{i}. <a href='tg://user?id={uid}'>User</a> - {count}\n"
    text += "\n<b>Top Chats:</b>\n"
    for i, (cid, count) in enumerate(top_chats, start=1):
        text += f"{i}. <code>{cid}</code> - {count}\n"
    await message.reply_text(text, disable_web_page_preview=True)
