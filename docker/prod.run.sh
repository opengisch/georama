#!/usr/bin/env bash

set -e

uvicorn georama.asgi:application --host 0.0.0.0 --port 4242
