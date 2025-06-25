from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from OxygenMusic import app
from OxygenMusic.utils.database import get_vip_user, is_vip_user


@app.on_message(filters.command("myrewards") & ~BANNED_USERS)
async def myrewards(_, message: Message):
    user_id = message.from_user.id
    vip = await get_vip_user(user_id)
    if not vip:
        return await message.reply_text("You are not a VIP user.")
    perks = ", ".join(vip.get("perks", []))
    xp = vip.get("global_xp", 0)
    text = f"🌟 <b>VIP Rewards</b> 🌟\nXP: <code>{xp}</code>\nPerks: {perks}"
    await message.reply_text(text)


@app.on_message(filters.command("vipqueue") & filters.group & ~BANNED_USERS)
async def vipqueue(_, message: Message):
    if not await is_vip_user(message.from_user.id):
        return await message.reply_text("Only VIP users can use this command.")
    if len(message.command) < 2 and not message.reply_to_message:
        return await message.reply_text("Provide a song name or reply to a media.")
    cmd = message.text.split(maxsplit=1)
    query = cmd[1] if len(cmd) > 1 else ""
    reply_id = message.reply_to_message.id if message.reply_to_message else message.id
    await app.send_message(
        message.chat.id, f"/playforce {query}", reply_to_message_id=reply_id
    )
