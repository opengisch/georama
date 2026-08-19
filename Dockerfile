FROM ubuntu:24.04 AS base

USER 0
RUN apt-get update && \
    apt-get install -y \
      python3-venv \
      python3-dev \
      unixodbc \
      odbc-mdbtools \
      gdal-bin \
      libgdal-dev \
      libpq-dev \
      build-essential \
      make \
      git \
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

RUN VENV_PATH=${VENV_PATH} make install-dev

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

RUN VENV_PATH=${VENV_PATH} make install

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["/usr/bin/tini", "--", "make"]

CMD ["serve-outbound"]
