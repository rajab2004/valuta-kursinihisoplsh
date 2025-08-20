import os
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is missing. Create a .env file from .env.example and set BOT_TOKEN.")
