#!/bin/bash
set -e
uvicorn bot.api.main:app --host 0.0.0.0 --port 8080
