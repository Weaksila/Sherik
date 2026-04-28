import logging
import tempfile
from pathlib import Path
from typing import Optional, Tuple

from aiogram import Bot
from aiogram.types import FSInputFile

from app.config import CHANNEL_ID, DEFAULT_CHANNEL_TITLE, DEFAULT_COVER_PATH, TEMP_DIR

logger = logging.getLogger(__name__)


async def get_channel_info(bot: Bot) -> Tuple[str, FSInputFile, Optional[Path]]:
    chat = await bot.get_chat(CHANNEL_ID)
    title = (chat.title or DEFAULT_CHANNEL_TITLE).strip()

    if not chat.photo:
        logger.info("Channel photo not found. Using default cover.")
        return title, FSInputFile(DEFAULT_COVER_PATH), None

    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=TEMP_DIR, suffix=".jpg", delete=False) as temp_file:
        temp_path = Path(temp_file.name)

    try:
        telegram_file = await bot.get_file(chat.photo.big_file_id)
        await bot.download_file(telegram_file.file_path, destination=temp_path)
        logger.info("Channel cover downloaded successfully: %s", temp_path.name)
        return title, FSInputFile(temp_path), temp_path
    except Exception:
        logger.exception("Failed to download channel cover. Using default image.")
        if temp_path.exists():
            temp_path.unlink(missing_ok=True)
        return title, FSInputFile(DEFAULT_COVER_PATH), None
