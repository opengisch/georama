FROM ghcr.io/osgeo/gdal:ubuntu-full-3.9.1 AS base

USER 0
RUN apt-get update && \
    apt-get install -y \
      python3-pip \
      python3-setuptools

ARG TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

#########################
#  DEV
#########################
FROM base AS dev

LABEL org.opengisch.author="Clemens Rudert <clemens.rudert@bl.ch>"
LABEL org.opengisch.image.title="georama"
USER 0

RUN apt-get install -y \
      libpq-dev \
      python3-gdal \
      python3-numpy \
      python3-venv \
      git \
      make

WORKDIR /opt/georama/
ADD setup.py .
ADD pyproject.toml .
ADD Makefile .

ENV VENV_PATH=/opt/georama/venv

WORKDIR /app

COPY ./ .

RUN VENV_PATH=${VENV_PATH} make dev

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=core.settings

ENTRYPOINT ["/tini", "--", "make"]

CMD ["serve"]
