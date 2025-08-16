import os
from pyrogram import Client

# Render ke environment variables se values lena
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Pyrogram Client
bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message()
async def start_handler(client, message):
    await message.reply_text("✅ Bot chal raha hai!")

if __name__ == "__main__":
    bot.run()
