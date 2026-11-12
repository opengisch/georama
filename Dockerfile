ARG PYTHON_VERSION=3.12
# trixie is pinned in all stages, the python binding gdal==3.10.3 has to match
#   libgdal of debian trixie (3.10.3) at build and at run time
FROM python:${PYTHON_VERSION}-trixie AS base
LABEL org.opencontainers.image.authors="OPENGIS.ch <info@opengis.ch>"
LABEL org.opencontainers.image.vendor="opengis.ch"
LABEL org.opencontainers.image.title="Georama Base Image"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    gdal-bin \
    gettext

FROM base AS builder-base

COPY --from=ghcr.io/astral-sh/uv:0.11.19 /uv /uvx /bin/

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    libgdal-dev

FROM builder-base AS dev

ARG UID=1000
ARG GID=1000
ARG USERPWD=secret
ARG USER=appuser
ARG UV_CACHE_DIR_BUILD_TIME=/home/$USER/.cache/uv-build-time
ARG UV_CACHE_DIR_RUN_TIME=/home/$USER/.cache/uv
#https://docs.astral.sh/uv/reference/environment/#uv_override
ENV UV_PROJECT_ENVIRONMENT=/home/$USER/.venv

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    libgdal-dev

# Setup a non-root user
RUN groupadd --system --gid $GID nonroot \
 && useradd --system --gid $GID --uid $UID --create-home $USER \
 && echo "$USER:$USERPWD" | chpasswd

ARG STATIC_DIR="/georama/static"
# we create a non project content static dir to avoid backfire
#   of mounted content to the host
WORKDIR $STATIC_DIR
WORKDIR /app

RUN chown -R $UID:$GID /app \
 && chown -R $UID:$GID $STATIC_DIR \
 && mkdir -p $UV_CACHE_DIR_RUN_TIME \
 && chown -R $UID:$GID $UV_CACHE_DIR_RUN_TIME

# https://docs.astral.sh/uv/reference/environment/#uv_python_cache_dir
ENV UV_PYTHON_CACHE_DIR=/home/$USER/.cache/uv/python
# https://docs.astral.sh/uv/reference/environment/#uv_link_mode
ENV UV_LINK_MODE=copy

# setting path to the static folder
ENV DJANGO_STATIC_ROOT=$STATIC_DIR

# We install only the deps at build time,
#   not the project itself
USER $USER

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=cache,target=$UV_CACHE_DIR_BUILD_TIME,uid=$UID,gid=$GID \
    python -c "import platform; print(platform.python_version())" > .python-version \
 && uv sync --frozen --no-install-project --group dev \
 && cp -r $UV_CACHE_DIR_BUILD_TIME/. $UV_CACHE_DIR_RUN_TIME

COPY ./docker/dev.debug.entrypoint.sh /usr/local/bin/dev.debug.entrypoint.sh
COPY ./docker/dev.start.georama.sh /usr/local/bin/dev.start.georama.sh

ENTRYPOINT [ "/usr/local/bin/dev.debug.entrypoint.sh" ]

CMD [ "/usr/local/bin/dev.start.georama.sh" ]

FROM builder-base AS prod-builder

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
# the venv must point to /usr/local/bin/python of the official image,
#   the slim runtime has the very same path, a uv managed python is not there
ENV UV_PYTHON_DOWNLOADS=never

WORKDIR /app/tests/resources/projects
WORKDIR /static
WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev --group prod

COPY ./src ./src
COPY ./README.md ./

# compiles the translation catalogs (*.po -> *.mo) before the project is installed
RUN for po in src/georama/locale/*/LC_MESSAGES/django.po; do \
      msgfmt --check-format -o "${po%.po}.mo" "$po" || exit 1; \
    done

ARG BUILD_BRANCH=
ARG BUILD_COMMIT=

COPY docker/generate-build-info.py /usr/local/bin/generate-build-info.py
RUN python3 /usr/local/bin/generate-build-info.py \
    --output "./src/georama/core/static/core/build-info.json" \
    --branch "$BUILD_BRANCH" \
    --commit "$BUILD_COMMIT"

# georama lands as a regular package in the venv, the sources are not needed
#   at run time anymore, the translation sources neither
RUN uv sync --frozen --no-dev --no-editable --group prod \
 && find /app/.venv -path "*/georama/locale/*" -name "*.po" -delete

# the venv script is called directly, `uv run` would sync the default group
#   (dev) into the venv again and install georama editable on top
RUN DJANGO_CONFIGURATION=Static \
    DJANGO_STATIC_ROOT=/static \
    /app/.venv/bin/manage collectstatic --noinput

# the runtime is slim on purpose: python and bash for debugging, the shared
#   libraries the venv really loads and nothing else
FROM python:${PYTHON_VERSION}-slim-trixie AS prod-base
ARG PYTHON_VERSION
ARG UID=1001
ARG USER=app
LABEL org.opencontainers.image.authors="OPENGIS.ch <info@opengis.ch>"
LABEL org.opencontainers.image.vendor="opengis.ch"
LABEL org.opencontainers.image.title="Georama"

# libgdal36: python binding gdal (osgeo) and GeoDjango
# libgeos-c1t64: GeoDjango (loaded via ctypes)
# libproj25: GeoDjango / GDAL coordinate transformations, brings proj.db
# pip and the bundled wheels of ensurepip are not used by the venv
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      libgdal36 \
      libgeos-c1t64 \
      libproj25 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && python -m pip uninstall --yes pip \
 && rm -rf /usr/local/lib/python${PYTHON_VERSION}/ensurepip/_bundled

ENV GEORAMA_DATA_INTEGRATION_ROOT=/io
# georama serves the static files itself (ServeStatic) from here
ENV DJANGO_STATIC_ROOT=/static
# python and the libraries resolve the home of arbitrary uids (OpenShift)
#   through HOME, so no entry in /etc/passwd is needed
ENV HOME=/tmp
# native crashes (GDAL/GEOS) print a python traceback instead of a silent
#   dying worker
ENV PYTHONFAULTHANDLER=1
ENV PATH="/app/.venv/bin:$PATH"

# app files belong to root and are read only for the app user,
#   only the data integration root is writable (group 0 for arbitrary uids)
COPY --from=prod-builder /app/.venv /app/.venv
COPY --from=prod-builder /static /static
COPY docker/prod.run.sh /usr/local/bin/

RUN useradd \
      --system \
      --uid $UID \
      --gid 0 \
      --shell /bin/bash \
      --no-create-home \
      --no-user-group \
      --password '*' \
      $USER \
 && mkdir -p $GEORAMA_DATA_INTEGRATION_ROOT \
 && chown $UID:0 $GEORAMA_DATA_INTEGRATION_ROOT \
 && chmod g=u $GEORAMA_DATA_INTEGRATION_ROOT \
 && rm -rf /tmp/*

WORKDIR /app

CMD [ "/usr/local/bin/prod.run.sh" ]

USER $UID:0

# only for emergencies of ops in client infrastructures, published as
#   <version>-debug and never as latest
FROM prod-base AS debug
ARG UID=1001

USER root
RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      curl \
      iputils-ping \
      jq \
      postgresql-client \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
USER $UID:0

# the prod image stays the last stage, so a build without --target results in it
FROM prod-base AS prod
