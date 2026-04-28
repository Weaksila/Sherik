# Telegram Audio Publisher Bot

Production-ready Telegram bot built with **Python** and **aiogram 3**.

## Overview
This bot accepts only audio files from users and publishes them to a Telegram channel.

### Features
- accepts only `audio` messages
- rejects invalid content with a clear error message
- reposts music to a target channel
- uses the channel profile photo as audio thumbnail when available
- falls back to `assets/default.jpg` when the channel has no photo
- generates music title in this format:
  - `CHANNEL_NAME - ARTIST`
- adds caption in this format:
  - `Channel Name 🎵`
- async/await architecture
- structured logging
- defensive `try/except` handling
- Render-ready deployment

## Project Structure
```text
/project-root
├── main.py
├── requirements.txt
├── Procfile
├── README.md
├── .gitignore
├── LICENSE
├── runtime.txt
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── handlers/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── channel_service.py
│   │   └── media_service.py
│   └── utils/
│       ├── __init__.py
│       ├── logging.py
│       └── metadata.py
└── assets/
    └── default.jpg
```

## Configuration
Edit `app/config.py` and set your values directly in code:

```python
BOT_TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"
CHANNEL_ID = -1001234567890
```

### Important
- add the bot to your channel
- promote the bot as an admin so it can post messages
- use a valid channel ID such as `-100xxxxxxxxxx`

## Install
```bash
git clone <your-repository-url>
cd project-root
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run locally
```bash
python main.py
```

## Deploy on Render
1. Push this project to GitHub.
2. Open Render dashboard.
3. Create a **Background Worker** service.
4. Connect your GitHub repository.
5. Render will detect:
   - `requirements.txt`
   - `runtime.txt`
   - `Procfile`
6. Start command will be:
   ```bash
   worker: python main.py
   ```
7. Deploy.

## How to test
1. Open the bot in Telegram.
2. Send `/start`.
3. Send a valid `MP3` or `M4A` audio file.
4. Verify that:
   - the bot accepts the file
   - the audio appears in the channel
   - the title is `CHANNEL_NAME - ARTIST`
   - the caption contains the channel name and emoji
   - the thumbnail is the channel profile photo or default image
5. Send a non-audio file or text message.
6. Verify the error response is returned.

## Notes
- If performer metadata exists, it is used as the artist name.
- If performer metadata is missing, the bot tries to derive the artist from the filename.
- If both are missing, it falls back to `Unknown Artist`.

## Production Recommendations
- keep the bot as channel admin
- avoid deleting `assets/default.jpg`
- if you change accepted formats, update `SUPPORTED_AUDIO_EXTENSIONS`
- monitor logs in Render for troubleshooting

## License
MIT
