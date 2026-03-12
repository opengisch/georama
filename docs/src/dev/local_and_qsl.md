---
tags:
  - Setup
  - Development
---

# How to develop QGIS-Server-Light & Georama in parallel

There are reasons why you want to develop QGIS-Server-Light and Georama in parallel. To offer a straight
forward solution Georama local setup offers a modified path to link the `.venv` to a path on your local file
system where QGIS-Server-Light is situated.

## Setting up QGIS-Server-Light

The following steps have to be done outside the Georama project path on your file system:

1. Clone [QGIS-Server-Light repository](https://github.com/opengisch/qgis-server-light) to some place on your system
2. cd into the cloned directory and checkout your new branch you want to apply the changes on.
3. follow the steps for local development of QGIS-Server-Light as you prefer [locally](https://opengisch.github.io/qgis-server-light/usage.worker.local/) or with [docker](https://opengisch.github.io/qgis-server-light/usage.worker.docker/).

!!! hint
    Be sure to link QGIS-Server-Light to the **absolute** path of Georama's test data `tests/resources/projects`.
    This means to mount it with `-v <local-path-to-georama-repo>/tests/resources/projects:/io/data` in case of docker or
    to pass it as environment variable in case of local usage `QSL_DATA_ROOT=<local-path-to-georama-repo>/tests/resources/projects> make run`.

!!! success
    After these steps you should have a locally running redis instance and one worker of QGIS-Server-Light
    listening to that instance for jobs.

## Align Georama with QGIS-Server-Light

The following steps have to be done inside the Georama project path on your file system:

1. `docker run --rm -d --name georama-db -e POSTGRES_PASSWORD=test -p 5433:5432 postgis/postgis:latest`
2. `LOCAL_QGIS_SERVER_LIGHT_PATH=<absolute-local-filesystem-path-to-qsl> make install-dev-local-qsl`
3. `make serve-dev`
4. 2nd shell: `make migrate`
5. 2nd shell: `make create-superuser`
6. 2nd shell: `make create-example-content`

!!! success
    After this, your setup is ready for development in both, Georama & QGIS-Server-Light.

# A word about the workflow

## Review process

The reviewer of your changes needs access to them on both, the QGIS-Server-Light and the Georama repository.
So you might assist in setting up as described here.

## Release process

Once you finished development and review is finished, you first should release QGIS-Server-Light as a new
version. This includes the package (github@master or pypi) and the corresponding docker image (docker hub). You then should
reconfigure the Georama `pyproject.toml` to link to that versions and provide the Pullrequest for your changes.
