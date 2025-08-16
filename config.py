import os

class Config:
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # Extra Config
    BANNED_USERS = []  # Agar aapko kuch IDs block karni hain to yaha list me dal do
    DOWNLOAD_LOCATION = "./downloads"  # Thumbnails save karne ka folder
