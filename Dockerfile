ARG PYTHON_VERSION=3.12
FROM python:$PYTHON_VERSION AS base
LABEL org.opencontainers.image.authors="Clemens Rudert <clemens@opengis.ch>"
LABEL org.opencontainers.image.vendor="opengis.ch"
LABEL org.opencontainers.image.title="Georama Base Image"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin libgdal-dev gettext

COPY --from=ghcr.io/astral-sh/uv:0.11.19 /uv /uvx /bin/

FROM base AS dev

ARG UID=1000
ARG GID=1000
ARG UV_CACHE_DIR_BUILD_TIME=/home/appuser/.cache/uv-build-time
ARG UV_CACHE_DIR_RUN_TIME=/home/appuser/.cache/uv

# Setup a non-root user
RUN groupadd --system --gid $GID nonroot \
 && useradd --system --gid $GID --uid $UID --create-home appuser

ARG STATIC_DIR="/georama/static"
# we create a non project content static dir to avoid backfire
#   of mounted content to the host
WORKDIR $STATIC_DIR
WORKDIR /app

RUN chown -R $GID:$UID /app
RUN chown -R $GID:$UID $STATIC_DIR
RUN mkdir -p $UV_CACHE_DIR_RUN_TIME
RUN chown -R $GID:$UID $UV_CACHE_DIR_RUN_TIME

# https://docs.astral.sh/uv/reference/environment/#uv_python_cache_dir
ENV UV_PYTHON_CACHE_DIR=/home/appuser/.cache/uv/python
# https://docs.astral.sh/uv/reference/environment/#uv_link_mode
ENV UV_LINK_MODE=copy
#https://docs.astral.sh/uv/reference/environment/#uv_override
ENV UV_PROJECT_ENVIRONMENT=/home/appuser/.venv

# setting path to the static folder
ENV GEORAMA_STATIC_ROOT=$STATIC_DIR

# We install only the deps at build time,
#   not the project itself
USER appuser

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=cache,target=$UV_CACHE_DIR_BUILD_TIME,uid=$UID,gid=$GID \
    python -c "import platform; print(platform.python_version())" > .python-version \
 && uv sync --frozen --no-install-project --group dev \
 && cp -r $UV_CACHE_DIR_BUILD_TIME/. $UV_CACHE_DIR_RUN_TIME
