# Telegram Music Bot

A modern asynchronous music bot built with Python 3.11+. The project uses a clean layered architecture with FastAPI for the web interface and `python-telegram-bot` for Telegram integration.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn bot.api.main:app --reload
```

## Deployment

The bot can run on platforms like Heroku or Render using the provided `Dockerfile` and `Procfile`.
