import logging

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.services.media_service import publish_audio

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        "Salom! Menga MP3 yoki M4A audio yuboring. "
        "Men uni kanalga sarlavha va rasm bilan joylayman."
    )


@router.message(F.audio)
async def handle_audio(message: Message) -> None:
    try:
        await publish_audio(message.bot, message, message.audio)
    except Exception:
        logger.exception("Unexpected error while processing audio.")
        await message.answer("⚠️ Kutilmagan xatolik yuz berdi.")


@router.message()
async def handle_invalid_content(message: Message) -> None:
    await message.answer("❌ Faqat audio fayl yuborishingiz mumkin.")
