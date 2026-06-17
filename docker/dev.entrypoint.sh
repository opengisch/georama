#!/bin/bash

uv sync --group dev
exec uv run uvicorn --host 0.0.0.0 --port 4242 --reload georama.asgi:application
