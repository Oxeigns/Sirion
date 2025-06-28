"""FastAPI application entry point."""

from fastapi import FastAPI

from .config import get_settings
from .services.ping import ping

app = FastAPI(title="Sirion")

@app.on_event("startup")
async def on_startup() -> None:
    get_settings()  # ensure settings are loaded

@app.get("/ping")
async def ping_endpoint() -> dict[str, str]:
    """Health check endpoint."""
    return await ping()
