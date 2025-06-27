#!/bin/bash

# Run Ruff linter; continue even if issues are found
ruff check || true

# Run unit tests
pytest -q
