import os

class Config:
    API_ID = 123456            # Apna API ID yahan
    API_HASH = "your_api_hash" # Apna API HASH yahan
    BOT_TOKEN = "your_bot_token_here"
    DOWNLOAD_LOCATION = os.path.join(os.getcwd(), "downloads")
    BANNED_USERS = []          # Agar koi banned user hai, id list me dalen

# Ensure download folder exists
if not os.path.exists(Config.DOWNLOAD_LOCATION):
    os.makedirs(Config.DOWNLOAD_LOCATION)
