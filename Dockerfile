FROM ubuntu:24.04 AS base

USER 0
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    apt-get update && \
    apt-get install -y \
      python3-venv \
      python3-gdal \
      python3-psycopg \
      unixodbc \
      odbc-mdbtools \
      gdal-bin \
      git \
      make \
      curl \
      tini

#########################
#  DEV
#########################
FROM base AS dev

LABEL org.opengisch.author="Clemens Rudert <clemens@opengis.ch>"
LABEL org.opengisch.image.title="georama"
USER 0

WORKDIR /opt/georama/
ADD setup.py .
ADD pyproject.toml .
ADD Makefile .

ENV VENV_PATH=/opt/georama/venv

WORKDIR /app

COPY ./ .

RUN VENV_PATH=${VENV_PATH} VENV_OPTIONS=--system-site-packages make install-dev

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/bin/tini", "--", "make"]

CMD ["serve-dev-outbound"]

#########################
#  PROD
#########################
FROM base AS prod

LABEL org.opengisch.author="Clemens Rudert <clemens@opengis.ch>"
LABEL org.opengisch.image.title="georama"
# TODO: USER should not be root for prod
USER 0

WORKDIR /opt/georama/
ADD setup.py .
ADD pyproject.toml .
ADD Makefile .

ENV VENV_PATH=/opt/georama/venv

WORKDIR /app

COPY ./ .

RUN VENV_PATH=${VENV_PATH} VENV_OPTIONS=--system-site-packages make install

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/bin/tini", "--", "make"]

CMD ["serve-outbound"]
