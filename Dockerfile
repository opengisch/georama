FROM ubuntu:24.04 AS base

USER 0
RUN apt-get update && \
    apt-get install -y \
      python3-pip \
      python3-setuptools \
      python3-venv \
      python3-psycopg2 \
      python3-gdal \
      make \
      git \
      curl

ARG TINI_VERSION=v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

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
ENV DJANGO_SETTINGS_MODULE=core.settings

ENTRYPOINT ["/tini", "--", "make"]

CMD ["serve-dev"]
