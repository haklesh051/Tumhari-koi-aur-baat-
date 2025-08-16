from pyrogram import filters
from pyrogram.types import Message
from bot import bot   # 👈 bot.py se bot object import

@bot.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.first_name}!\n\n"
        "✅ Bot is alive and running...\n"
        "Use /help to see available commands."
    )
