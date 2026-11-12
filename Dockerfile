# the OSGeo alpine-normal image brings GDAL, PROJ, GEOS, python and the
# matching GDAL python binding (osgeo). The tag pins all of them together:
# GDAL 3.13 is built on alpine 3.23 which ships python 3.12, newer tags
# (alpine 3.24) come with python 3.14
# the digest anchors the tag, OSGeo could rebuild it on another alpine version
ARG GDAL_IMAGE=ghcr.io/osgeo/gdal:alpine-normal-3.13.3@sha256:102f7f57fea5ce2cb4cb5a1deb060b78ab1f5a77232663a84641d4b7bf2e1aa3

FROM ${GDAL_IMAGE} AS base
LABEL org.opencontainers.image.authors="OPENGIS.ch <info@opengis.ch>"
LABEL org.opencontainers.image.vendor="opengis.ch"

# the OSGeo release images are not rebuilt, the security fixes of alpine are
# pulled in here (GDAL itself is built from source and not an apk package)
RUN apk upgrade --no-cache

# alpine comes without the time zone database, python's zoneinfo (django's
# TIME_ZONE) reads it from /usr/share/zoneinfo
RUN apk add --no-cache tzdata

# the venvs are created with access to the system site-packages to use the
# osgeo binding of the image, the gdal dependency group of the pyproject.toml
# is only for usage outside of the image and has to follow the tag above
ENV UV_PYTHON=/usr/bin/python3
ENV UV_PYTHON_DOWNLOADS=never
ENV UV_LINK_MODE=copy

FROM base AS builder

COPY --from=ghcr.io/astral-sh/uv:0.11.19 /uv /uvx /bin/

# build-base and python3-dev: rasterio has no musl wheel and is compiled
# against the GDAL of the image
# git: qgis-server-light is a git dependency
# gettext: compiles the translation catalogs
RUN apk add --no-cache \
      build-base \
      python3-dev \
      git \
      gettext

FROM builder AS prod-builder

ENV UV_COMPILE_BYTECODE=1

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv venv --system-site-packages /app/.venv \
 && uv sync --frozen --no-install-project --no-dev --group prod

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
# at run time anymore, the translation sources neither
RUN uv sync --frozen --no-dev --no-editable --group prod \
 && find /app/.venv -path "*/georama/locale/*" -name "*.po" -delete

# the venv script is called directly, `uv run` would sync the default group
#   (dev) into the venv again and install georama editable on top
RUN DJANGO_CONFIGURATION=Static \
    DJANGO_STATIC_ROOT=/static \
    /app/.venv/bin/manage collectstatic --noinput

FROM base AS prod
ARG UID=1001
ARG USER=app
LABEL org.opencontainers.image.title="Georama"

ENV GEORAMA_DATA_INTEGRATION_ROOT=/io
# georama serves the static files itself (ServeStatic) from here
ENV DJANGO_STATIC_ROOT=/static
# python and the libraries resolve the home of arbitrary uids (OpenShift)
# through HOME, so no entry in /etc/passwd is needed
ENV HOME=/tmp
# native crashes (GDAL/GEOS) print a python traceback instead of a silent
# dying worker
ENV PYTHONFAULTHANDLER=1
ENV PATH="/app/.venv/bin:$PATH"

# app files belong to root and are read only for the app user,
# only the data integration root is writable (group 0 for arbitrary uids)
COPY --from=prod-builder /app/.venv /app/.venv
COPY --from=prod-builder /static /static
COPY docker/prod.run.sh /usr/local/bin/

RUN adduser \
      -S \
      -D \
      -H \
      -u $UID \
      -G root \
      -s /bin/bash \
      $USER \
 && mkdir -p $GEORAMA_DATA_INTEGRATION_ROOT \
 && chown $UID:0 $GEORAMA_DATA_INTEGRATION_ROOT \
 && chmod g=u $GEORAMA_DATA_INTEGRATION_ROOT

WORKDIR /app

CMD [ "/usr/local/bin/prod.run.sh" ]

USER $UID:0

# only for emergencies of ops in client infrastructures, published as
# <version>-debug and never as latest
FROM prod AS debug
ARG UID=1001
LABEL org.opencontainers.image.title="Georama (debug)"

USER root
RUN apk add --no-cache \
      curl \
      iputils-ping \
      jq \
      postgresql-client
USER $UID:0

# dev builds on top of prod and adds the tooling for development, the sources
# are mounted to /app and the venv lives outside of it
FROM prod AS dev
ARG UID=1000
ARG GID=1000
ARG USERPWD=secret
ARG USER=appuser
ARG UV_CACHE_DIR_BUILD_TIME=/home/$USER/.cache/uv-build-time
ARG UV_CACHE_DIR_RUN_TIME=/home/$USER/.cache/uv
LABEL org.opencontainers.image.title="Georama (dev)"

USER root

COPY --from=ghcr.io/astral-sh/uv:0.11.19 /uv /uvx /bin/

# same build tooling as the builder: rasterio is compiled on sync, the
# entrypoint compiles the translation catalogs of the mounted sources
RUN apk add --no-cache \
      build-base \
      python3-dev \
      git \
      gettext

#https://docs.astral.sh/uv/reference/environment/#uv_override
ENV UV_PROJECT_ENVIRONMENT=/home/$USER/.venv
ENV PATH="/home/$USER/.venv/bin:$PATH"
# prod points HOME to /tmp, the dev user has a real one
ENV HOME=/home/$USER

# Setup a non-root user, the OSGeo image already has accounts in the range of
# host uids (e.g. 1000), they give way so the dev user matches the host user
RUN existing_user=$(awk -F: -v uid=$UID '$3 == uid { print $1 }' /etc/passwd) \
 && if [ -n "$existing_user" ]; then deluser "$existing_user"; fi \
 && existing_group=$(awk -F: -v gid=$GID '$3 == gid { print $1 }' /etc/group) \
 && if [ -n "$existing_group" ]; then delgroup "$existing_group"; fi \
 && addgroup -S -g $GID nonroot \
 && adduser -S -D -u $UID -G nonroot -s /bin/bash $USER \
 && echo "$USER:$USERPWD" | chpasswd

ARG STATIC_DIR="/georama/static"
# we create a non project content static dir to avoid backfire
# of mounted content to the host
WORKDIR $STATIC_DIR
WORKDIR /app

RUN chown -R $UID:$GID /app \
 && chown -R $UID:$GID $STATIC_DIR \
 && mkdir -p $UV_CACHE_DIR_RUN_TIME \
 && chown -R $UID:$GID $UV_CACHE_DIR_RUN_TIME

# https://docs.astral.sh/uv/reference/environment/#uv_python_cache_dir
ENV UV_PYTHON_CACHE_DIR=/home/$USER/.cache/uv/python

# setting path to the static folder
ENV DJANGO_STATIC_ROOT=$STATIC_DIR

# We install only the deps at build time,
# not the project itself
USER $USER

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=cache,target=$UV_CACHE_DIR_BUILD_TIME,uid=$UID,gid=$GID \
    python -c "import platform; print(platform.python_version())" > .python-version \
 && uv venv --system-site-packages $UV_PROJECT_ENVIRONMENT \
 && uv sync --frozen --no-install-project --group dev \
 && cp -r $UV_CACHE_DIR_BUILD_TIME/. $UV_CACHE_DIR_RUN_TIME

COPY ./docker/dev.debug.entrypoint.sh /usr/local/bin/dev.debug.entrypoint.sh
COPY ./docker/dev.start.georama.sh /usr/local/bin/dev.start.georama.sh

ENTRYPOINT [ "/usr/local/bin/dev.debug.entrypoint.sh" ]

CMD [ "/usr/local/bin/dev.start.georama.sh" ]

# prod stays the default, a build without --target results in it
FROM prod
