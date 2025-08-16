from pyrogram import filters
from pyrogram.types import Message

# 👇 Yaha 'client' instance Pyrogram khud pass karega
@Client.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(
        f"👋 Hello {message.from_user.first_name}!\n\n"
        "✅ Bot is alive and running...\n"
        "Use /help to see available commands."
    )
