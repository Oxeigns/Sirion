#!/usr/bin/env bash
set -e

# Check and install Python packages
required_pkgs=(pyrogram tgcrypto pymongo yt-dlp python-dotenv)
missing_pkgs=()

for pkg in "${required_pkgs[@]}"; do
    python - <<PY
import importlib, sys
try:
    importlib.import_module("${pkg//-/_}")
except Exception:
    sys.exit(1)
PY
    if [ $? -ne 0 ]; then
        missing_pkgs+=("$pkg")
    fi
done

if [ ${#missing_pkgs[@]} -ne 0 ]; then
    echo "Installing missing Python packages: ${missing_pkgs[@]}"
    pip install "${missing_pkgs[@]}"
else
    echo "All required Python packages are already installed."
fi

# Check ffmpeg
if ! command -v ffmpeg >/dev/null 2>&1; then
    echo "ffmpeg not found. Please install ffmpeg on your system."
else
    ffmpeg -version | head -n 1
fi
