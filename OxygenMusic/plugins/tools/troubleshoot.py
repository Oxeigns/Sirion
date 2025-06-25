from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message

from OxygenMusic import app
from OxygenMusic.core.call import Aviax
from OxygenMusic.misc import db
from config import BANNED_USERS, adminlist, lyrical


MENU = [
    [InlineKeyboardButton("🔁 Restart playback loop", callback_data="tb_restart")],
    [InlineKeyboardButton("🧼 Clear group queue", callback_data="tb_clear")],
    [InlineKeyboardButton("🔄 Refresh download engine", callback_data="tb_refresh")],
    [InlineKeyboardButton("🧠 Rebuild user cache", callback_data="tb_cache")],
]


@app.on_message(filters.command(["troubleshoot", "trouble"]) & filters.group & ~BANNED_USERS)
async def troubleshoot_cmd(_, message: Message):
    await message.reply_text(
        "Troubleshooting Menu",
        reply_markup=InlineKeyboardMarkup(MENU),
    )


@app.on_callback_query(filters.regex("^tb_restart") & ~BANNED_USERS)
async def cb_restart(_, cb: CallbackQuery):
    try:
        await Aviax.stop_stream_force(cb.message.chat.id)
        await cb.answer("Playback loop restarted", show_alert=True)
    except Exception as e:
        await cb.answer(f"Failed: {e}", show_alert=True)


@app.on_callback_query(filters.regex("^tb_clear") & ~BANNED_USERS)
async def cb_clear(_, cb: CallbackQuery):
    db[cb.message.chat.id] = []
    await cb.answer("Queue cleared", show_alert=True)


@app.on_callback_query(filters.regex("^tb_refresh") & ~BANNED_USERS)
async def cb_refresh(_, cb: CallbackQuery):
    lyrical.clear()
    await cb.answer("Downloader refreshed", show_alert=True)


@app.on_callback_query(filters.regex("^tb_cache") & ~BANNED_USERS)
async def cb_cache(_, cb: CallbackQuery):
    adminlist[cb.message.chat.id] = []
    await cb.answer("User cache rebuilt", show_alert=True)

