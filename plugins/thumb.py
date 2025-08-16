import os
from pyrogram import Client, filters
from config import Config

# -------------------------------
# Save custom thumbnail
# -------------------------------
@Client.on_message(filters.photo)
async def save_thumb(client, message):
    user_id = message.from_user.id
    thumb_path = f"{Config.DOWNLOAD_LOCATION}/{user_id}.jpg"
    os.makedirs(Config.DOWNLOAD_LOCATION, exist_ok=True)

    await client.download_media(message, file_name=thumb_path)
    await message.reply_text("✅ Custom thumbnail saved!")


# -------------------------------
# Delete custom thumbnail
# -------------------------------
@Client.on_message(filters.command("delthumb"))
async def delete_thumb(client, message):
    user_id = message.from_user.id
    thumb_path = f"{Config.DOWNLOAD_LOCATION}/{user_id}.jpg"

    if os.path.exists(thumb_path):
        os.remove(thumb_path)
        await message.reply_text("❌ Thumbnail deleted!")
    else:
        await message.reply_text("⚠️ No thumbnail found")


# -------------------------------
# Process video (remove/add thumbnail)
# -------------------------------
@Client.on_message(filters.video)
async def process_video(client, message):
    user_id = message.from_user.id
    video_path = f"{Config.DOWNLOAD_LOCATION}/{user_id}_video.mp4"
    thumb_path = f"{Config.DOWNLOAD_LOCATION}/{user_id}.jpg"

    # Download user video
    await client.download_media(message, file_name=video_path)

    # Check thumbnail
    if os.path.exists(thumb_path):
        # Add custom thumbnail
        await message.reply_video(
            video=video_path,
            thumb=thumb_path,
            caption="🎬 Video with your custom thumbnail"
        )
    else:
        # Remove thumbnail (by not giving thumb argument)
        await message.reply_video(
            video=video_path,
            caption="🎬 Video without thumbnail"
        )

    # Clean up
    os.remove(video_path)
