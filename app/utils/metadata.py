from pathlib import Path

from aiogram.types import Audio

from app.config import DEFAULT_ARTIST


def extract_artist(audio: Audio) -> str:
    if audio.performer:
        return audio.performer.strip()

    if audio.file_name:
        stem = Path(audio.file_name).stem.strip()
        if " - " in stem:
            parts = [part.strip() for part in stem.split(" - ", maxsplit=1)]
            if parts[0]:
                return parts[0]

    return DEFAULT_ARTIST


def is_supported_audio(audio: Audio) -> bool:
    if audio.mime_type and not audio.mime_type.startswith("audio/"):
        return False

    if not audio.file_name:
        return True

    suffix = Path(audio.file_name).suffix.lower()
    return suffix in {".mp3", ".m4a"}
