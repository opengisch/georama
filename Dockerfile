ARG PYTHON_VERSION=3.12
FROM python:$PYTHON_VERSION AS base
LABEL org.opencontainers.image.authors="Clemens Rudert <clemens@opengis.ch>"
LABEL org.opencontainers.image.vendor="opengis.ch"
LABEL org.opencontainers.image.title="Georama Base Image"

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev \
    gettext \
    openssh-server \
    sudo

COPY --from=ghcr.io/astral-sh/uv:0.11.19 /uv /uvx /bin/

FROM base AS dev

ARG UID=1000
ARG GID=1000
ARG USERPWD=secret
ARG USER=appuser
ARG UV_CACHE_DIR_BUILD_TIME=/home/$USER/.cache/uv-build-time
ARG UV_CACHE_DIR_RUN_TIME=/home/$USER/.cache/uv
#https://docs.astral.sh/uv/reference/environment/#uv_override
ENV UV_PROJECT_ENVIRONMENT=/home/$USER/.venv
ARG QSL_SOURCE_DIR=/qsl
ARG QSL_SOURCE_BRANCH=master

# Setup a non-root user
RUN groupadd --system --gid $GID nonroot \
 && useradd --system --gid $GID --uid $UID --create-home $USER \
 && echo "$USER:$USERPWD" | chpasswd

# We allow the non root user sudo access on decent actions
RUN echo "$USER ALL=(root) NOPASSWD: /usr/sbin/sshd, /etc/ssh/ssh_keygen, /bin/chown, /bin/chmod, /bin/mkdir" >> /etc/sudoers.d/$USER && \
    chmod 0440 /etc/sudoers.d/$USER

ARG STATIC_DIR="/georama/static"
# we create a non project content static dir to avoid backfire
#   of mounted content to the host
WORKDIR $STATIC_DIR
WORKDIR /app

ADD --unpack https://github.com/opengisch/qgis-server-light/archive/refs/heads/$QSL_SOURCE_BRANCH.tar.gz $QSL_SOURCE_DIR
RUN mv $QSL_SOURCE_DIR/qgis-server-light-$QSL_SOURCE_BRANCH/* $QSL_SOURCE_DIR
RUN chown -R $UID:$GID /app \
 && chown -R $UID:$GID $STATIC_DIR \
 && mkdir -p $UV_CACHE_DIR_RUN_TIME \
 && chown -R $UID:$GID $UV_CACHE_DIR_RUN_TIME
RUN chown -R $UID:$GID $QSL_SOURCE_DIR

# https://docs.astral.sh/uv/reference/environment/#uv_python_cache_dir
ENV UV_PYTHON_CACHE_DIR=/home/$USER/.cache/uv/python
# https://docs.astral.sh/uv/reference/environment/#uv_link_mode
ENV UV_LINK_MODE=copy

# setting path to the static folder
ENV GEORAMA_STATIC_ROOT=$STATIC_DIR

# We install only the deps at build time,
#   not the project itself
USER $USER


RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=cache,target=$UV_CACHE_DIR_BUILD_TIME,uid=$UID,gid=$GID \
    python -c "import platform; print(platform.python_version())" > .python-version \
 && uv sync --frozen --no-install-project --group dev \
 && cp -r $UV_CACHE_DIR_BUILD_TIME/. $UV_CACHE_DIR_RUN_TIME

COPY docker/dev.entrypoint.sh /bin/dev.entrypoint.sh

ENTRYPOINT ["/bin/dev.entrypoint.sh"]
