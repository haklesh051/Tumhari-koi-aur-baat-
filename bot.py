import os
import asyncio
from pyrogram import Client, filters
from translation import Translation
from database.database import df_thumb, del_thumb, thumb, init_db
from config import Config

bot = Client(
    "thumb_bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

# ---------- Commands ----------
@bot.on_message(filters.photo)
async def save_photo(bot, update):
    if update.from_user.id in Config.BANNED_USERS:
        await bot.delete_messages(update.chat.id, update.message_id, revoke=True)
        return

    download_location = f"{Config.DOWNLOAD_LOCATION}/{update.from_user.id}.jpg"
    await df_thumb(update.from_user.id, update.message_id)
    await bot.download_media(update, file_name=download_location)
    await bot.send_message(update.chat.id, Translation.SAVED_CUSTOM_THUMB_NAIL, reply_to_message_id=update.message_id)

@bot.on_message(filters.command(["delthumb"]))
async def delete_thumbnail(bot, update):
    thumb_image_path = f"{Config.DOWNLOAD_LOCATION}/{update.from_user.id}.jpg"
    try:
        await del_thumb(update.from_user.id)
    except: pass
    try:
        os.remove(thumb_image_path)
    except: pass
    await bot.send_message(update.chat.id, Translation.DEL_ETED_CUSTOM_THUMB_NAIL, reply_to_message_id=update.message_id)

@bot.on_message(filters.command(["showthumb"]))
async def show_thumb(bot, update):
    thumb_image_path = f"{Config.DOWNLOAD_LOCATION}/{update.from_user.id}.jpg"
    if not os.path.exists(thumb_image_path):
        mes = await thumb(update.from_user.id)
        if mes is not None:
            m = await bot.get_messages(update.chat.id, mes.msg_id)
            await m.download(file_name=thumb_image_path)
        else:
            thumb_image_path = None
    if thumb_image_path is not None:
        try:
            await bot.send_photo(update.chat.id, thumb_image_path, reply_to_message_id=update.message_id)
        except: pass
    else:
        await bot.send_message(update.chat.id, Translation.NO_THUMB_FOUND, reply_to_message_id=update.message_id)

# ---------- Main runner ----------
async def main():
    await init_db()    # Initialize database
    await bot.start()  # Start bot
    print("✅ Bot is running...")
    await bot.idle()   # Keep bot alive

if __name__ == "__main__":
    asyncio.run(main())
