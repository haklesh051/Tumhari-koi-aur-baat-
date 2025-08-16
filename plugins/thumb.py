import os
from pyrogram import filters, Client
from translation import Translation
from database.database import df_thumb, del_thumb, thumb
from config import Config

@Client.on_message(filters.photo)
async def save_photo(client, message):
    if message.from_user.id in Config.BANNED_USERS:
        await client.delete_messages(message.chat.id, message.id, revoke=True)
        return

    download_location = f"{Config.DOWNLOAD_LOCATION}/{message.from_user.id}.jpg"
    os.makedirs(Config.DOWNLOAD_LOCATION, exist_ok=True)

    # First download photo
    await client.download_media(message, file_name=download_location)
    # Then save in DB
    await df_thumb(message.from_user.id, message.id)

    await message.reply_text(Translation.SAVED_CUSTOM_THUMB_NAIL)


@Client.on_message(filters.command(["delthumb"]))
async def delete_thumbnail(client, message):
    thumb_image_path = f"{Config.DOWNLOAD_LOCATION}/{message.from_user.id}.jpg"
    try:
        await del_thumb(message.from_user.id)
    except Exception as e:
        print(f"DB delete error: {e}")
    try:
        os.remove(thumb_image_path)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"File delete error: {e}")

    await message.reply_text(Translation.DEL_ETED_CUSTOM_THUMB_NAIL)


@Client.on_message(filters.command(["showthumb"]))
async def show_thumb(client, message):
    thumb_image_path = f"{Config.DOWNLOAD_LOCATION}/{message.from_user.id}.jpg"

    if not os.path.exists(thumb_image_path):
        try:
            mes = await thumb(message.from_user.id)
            if mes:
                m = await client.get_messages(message.chat.id, mes.msg_id)
                await m.download(file_name=thumb_image_path)
        except Exception as e:
            print(f"Thumb restore error: {e}")
            thumb_image_path = None

    if thumb_image_path and os.path.exists(thumb_image_path):
        await client.send_photo(message.chat.id, thumb_image_path, reply_to_message_id=message.id)
    else:
        await message.reply_text(Translation.NO_THUMB_FOUND)
