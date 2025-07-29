---
tags:
  - Setup
  - Development
---

There are reasons why you want to develop QGIS-Server-Light and Georama in parallel. To offer a straight
forward solution Georama local setup offers a modified setup to link the `.venv` to a path on your local file
system where QGIS-Server-Light is situated.

# How to develop QGIS-Server-Light and Georama in parallel

## Setting up QGIS-Server-Light

The following steps have to be done outside the Georama project path on your file system:

1. Clone [QGIS-Server-Light repository](https://github.com/opengisch/qgis-server-light) to some place on your system
2. Follow the steps of [QGIS-Server-Light local setup](https://opengisch.github.io/qgis-server-light/usage.worker.local/)

## Align Georama with QGIS-Server-Light

The following steps have to be done inside the Georama project path on your file system:

1. `LOCAL_QGIS_SERVER_LIGHT_PATH=<absolute-local-filesystem-path-to-qsl> make install-dev-local-qsl`
2. Now you can proceed as described in [local setup](local.md)

After this, your setup is ready for development.

# A word about the workflow

## Review process

The reviewer of your changes needs access to them on both, the QGIS-Server-Light and the Georama repository.
So you might assist in setting up as described here.

## Release process

Once you finished development and review is finished, you first should release QGIS-Server-Light as a new
version. This includes the package (github@master or pypi) and the corresponding docker image (docker hub). You then should
reconfigure the Georama `pyproject.toml` to link to that versions and provide the Pullrequest for your changes.
