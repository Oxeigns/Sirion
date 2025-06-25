import aiohttp
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from OxygenMusic import app

LYRICS_API = "https://api.lyrics.ovh/v1/{artist}/{title}"


@app.on_message(filters.command(["lyrics"]) & ~BANNED_USERS)
async def fetch_lyrics(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: /lyrics <artist> - <title>")

    query = " ".join(message.command[1:])
    if "-" not in query:
        return await message.reply_text("Please use format: artist - title")
    artist, title = map(str.strip, query.split("-", 1))

    msg = await message.reply_text("Searching lyrics...")
    async with aiohttp.ClientSession() as session:
        async with session.get(LYRICS_API.format(artist=artist, title=title)) as resp:
            if resp.status != 200:
                return await msg.edit_text("Lyrics not found.")
            data = await resp.json()

    lyrics = data.get("lyrics")
    if not lyrics:
        return await msg.edit_text("Lyrics not found.")

    if len(lyrics) > 4096:
        lyrics = lyrics[:4096]
    await msg.edit_text(f"<b>{artist} - {title}</b>\n\n{lyrics}")
