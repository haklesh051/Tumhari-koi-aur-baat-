from pyrogram import filters
from pyrogram.types import Message

from bot import bot   # ❌ isko hatao (yehi error ki wajah thi)

# ✅ Correct way: sirf decorator @Client.on_message use karo
# Client ka instance (bot) already inject ho jata hai by pyrogram

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.first_name}!\n\n"
        "✅ Bot is alive and running..."
    )
