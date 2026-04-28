from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"
TEMP_DIR = BASE_DIR / "tmp"

BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = -1001234567890

DEFAULT_CAPTION_EMOJI = "🎵"
DEFAULT_ARTIST = "Unknown Artist"
DEFAULT_CHANNEL_TITLE = "My Channel"
DEFAULT_COVER_PATH = ASSETS_DIR / "default.jpg"
SUPPORTED_AUDIO_EXTENSIONS = {".mp3", ".m4a"}
