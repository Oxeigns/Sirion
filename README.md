# Telegram Music Bot

A modern asynchronous music bot built with Python 3.11+. The project uses a clean layered architecture with FastAPI for the web interface and [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot) for Telegram integration.

## Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp sample.env .env  # fill in the required values
uvicorn bot.api.main:app --reload
```

Run `bash fast_check.sh` to lint the code with Ruff and execute the tests.

## Deployment

The bot can run on any platform that supports Docker. Use the provided `Dockerfile` to build an image:

```bash
docker build -t telegram-music-bot .
docker run --env-file .env -p 8080:8080 telegram-music-bot
```

It can also be deployed to Heroku using the `Procfile` or to Render using `render.yaml`.
