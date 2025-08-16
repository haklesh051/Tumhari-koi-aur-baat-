from pyrogram import Client
from config import Config

bot = Client(
    "my_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")  # 👈 sab plugins load karega
)

print("✅ Bot started...")
bot.run()
