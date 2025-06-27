from pyrogram import filters
from pyrogram.types import Message

from OxygenMusic import app
from OxygenMusic.misc import SUDOERS_FILTER
from OxygenMusic.utils.database import add_off, add_on, get_lang, is_on_off
from strings import get_string

VCNOTIFY_ID = 3


@app.on_message(filters.command(["vcnotify"]) & SUDOERS_FILTER)
async def vcnotify_toggle(client, message: Message):
    language = await get_lang(message.chat.id)
    _ = get_string(language)
    usage = _["vc_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].lower()
    if state == "enable":
        await add_on(VCNOTIFY_ID)
        await message.reply_text(_["vc_2"])
    elif state == "disable":
        await add_off(VCNOTIFY_ID)
        await message.reply_text(_["vc_3"])
    else:
        await message.reply_text(usage)


# ``video_chat_joined`` filter was removed from newer versions of
# Pyrogram. ``video_chat_participants_invited`` provides a similar
# behaviour by triggering when users join an ongoing voice chat via an
# invite link. Use this filter to avoid AttributeError on import.
@app.on_message(filters.video_chat_participants_invited)
async def vc_joined(client, message: Message):
    if not await is_on_off(VCNOTIFY_ID):
        return
    language = await get_lang(message.chat.id)
    _ = get_string(language)
    if message.from_user:
        await message.reply_text(_["vc_4"].format(message.from_user.mention))
