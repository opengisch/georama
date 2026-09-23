#!/usr/bin/env bash

set -e

exec /app/.venv/bin/gunicorn georama.asgi:application \
  --bind 0.0.0.0:4242 \
  --workers 3 \
  --worker-class uvicorn_worker.UvicornWorker \
  --access-logfile - \
  --error-logfile - \
  --timeout 120 \
  --graceful-timeout 30 \
  --keep-alive 5
