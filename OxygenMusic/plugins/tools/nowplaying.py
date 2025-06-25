from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

import config
from config import BANNED_USERS
from OxygenMusic import app
from OxygenMusic.misc import db
from OxygenMusic.utils import seconds_to_min
from OxygenMusic.utils.database import get_cmode, is_active_chat
from OxygenMusic.utils.decorators.language import language
from OxygenMusic.utils.inline import stream_markup_timer
from OxygenMusic.utils.thumbnails import gen_thumb


@app.on_message(
    filters.command(["nowplaying", "cnowplaying"]) & filters.group & ~BANNED_USERS
)
@language
async def now_playing(client, message: Message, _):
    if message.command[0].startswith("c"):
        chat_id = await get_cmode(message.chat.id)
        if chat_id is None:
            return await message.reply_text(_["setting_7"])
    else:
        chat_id = message.chat.id

    if not await is_active_chat(chat_id):
        return await message.reply_text(_["general_5"])

    playing = db.get(chat_id)
    if not playing:
        return await message.reply_text(_["queue_2"])

    song = playing[0]
    file_path = song["file"]
    videoid = song["vidid"]
    title = song["title"].title()
    streamtype = song["streamtype"].title()
    requested_by = song["by"]
    played = seconds_to_min(song["played"])
    duration = song["dur"]

    if "live_" in file_path or "index_" in file_path:
        image = config.STREAM_IMG_URL
    elif "vid_" in file_path:
        image = await gen_thumb(videoid)
    else:
        if videoid == "telegram":
            image = (
                config.TELEGRAM_VIDEO_URL
                if streamtype == "Video"
                else config.TELEGRAM_AUDIO_URL
            )
        elif videoid == "soundcloud":
            image = config.SOUNCLOUD_IMG_URL
        else:
            image = await gen_thumb(videoid)

    buttons = stream_markup_timer(_, chat_id, played, duration)
    send = _["queue_6"] if duration == "Unknown" else _["queue_7"]
    caption = _["queue_8"].format(app.mention, title, streamtype, requested_by, send)
    await message.reply_photo(
        image, caption=caption, reply_markup=InlineKeyboardMarkup(buttons)
    )
