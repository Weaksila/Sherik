import html
import logging
from pathlib import Path
from typing import Optional

from aiogram import Bot
from aiogram.types import Audio, FSInputFile, Message

from app.config import CHANNEL_ID, DEFAULT_CAPTION_EMOJI
from app.services.channel_service import get_channel_info
from app.utils.metadata import extract_artist, is_supported_audio

logger = logging.getLogger(__name__)


async def publish_audio(bot: Bot, message: Message, audio: Audio) -> bool:
    if not is_supported_audio(audio):
        await message.answer("❌ Faqat MP3 yoki M4A audio yuboring.")
        return False

    temp_cover_path: Optional[Path] = None

    try:
        channel_title, cover_file, temp_cover_path = await get_channel_info(bot)
        artist = extract_artist(audio)
        title = f"{channel_title} - {artist}"
        caption = f"{html.escape(channel_title)} {DEFAULT_CAPTION_EMOJI}"

        await bot.send_audio(
            chat_id=CHANNEL_ID,
            audio=audio.file_id,
            caption=caption,
            title=title,
            thumbnail=cover_file,
        )

        await message.answer("✅ Audio kanalga muvaffaqiyatli yuborildi.")
        logger.info(
            "Audio published. user_id=%s message_id=%s channel_id=%s title=%s",
            message.from_user.id if message.from_user else "unknown",
            message.message_id,
            CHANNEL_ID,
            title,
        )
        return True
    except Exception:
        logger.exception("Failed to publish audio.")
        await message.answer("⚠️ Audio yuborishda xatolik yuz berdi. Keyinroq urinib ko‘ring.")
        return False
    finally:
        if temp_cover_path and temp_cover_path.exists():
            temp_cover_path.unlink(missing_ok=True)
