#!/bin/bash

set -e

# convenience switch to prevent sync of the venv
if [ "${DEV_SYNC:-1}" = "1" ] && [ -f uv.lock ] && command -v uv >/dev/null; then
  uv sync --group dev
fi

# installs mounted qsl sources editable over the locked version
if [ -n "${DEV_QSL_SOURCES:-}" ]; then
  uv pip install -e "${DEV_QSL_SOURCES}[dispatcher]"
fi

# this just starts the container without a service in it
# useful for devcontainer usage where you start the service
# then inside the container itself => DEV_AUTOSTART=0
[ "${DEV_AUTOSTART:-1}" = "0" ] && exec sleep infinity

# calls the actual command
exec "$@"
