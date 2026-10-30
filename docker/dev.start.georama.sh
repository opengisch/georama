#!/bin/bash

reload_dirs=(--reload-dir /app/src)

# watches mounted qsl sources too (see compose.dev_with_qsl.yml)
if [ -n "${DEV_QSL_SOURCES:-}" ]; then
  reload_dirs+=(
    --reload-dir "${DEV_QSL_SOURCES}/src/qgis_server_light/interface"
    --reload-dir "${DEV_QSL_SOURCES}/src/qgis_server_light/dispatcher"
  )
fi

exec uv run uvicorn \
  --host 0.0.0.0 \
  --port 4242 \
  "${reload_dirs[@]}" \
  --reload georama.asgi:application
