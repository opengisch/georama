# GEORAMA

A SDI like application to publish your geodata via QGIS projects.

## Features

1. A SDI like django application (geodata cms)
1. Split into combinable [django](https://www.djangoproject.com) apps
1. [QGIS](https://qgis.org) backed dataintegration app
1. pygeoapi backed feature server (wfs AND OGC API Features)
1. [QGIS](https://qgis.org) backed WMS
1. [GeoGirafe](https://gitlab.com/geogirafe/gg-viewer) Frontend

## Docs

Currently, the docs are not poblished on github pages.

You can read them in the markdown format [docs](docs/src).

You can run a local server to read them in your browser locally by:

```shell
make docs-serve
```

Once server started you can reach the docs [here](http://127.0.0.1:8000/georama/).

## Quickstart docker compose

```shell
cp .env.example .env
```

Adapt content of `.env` as you need (usually nothing need to be changes)

```shell
docker compose build
docker compose up -d
```

Wait for services to be up and running. That might last a moment since the test data (about 5GB) has to be
fetched.

If everything runs, you can prepare the Django DB

```shell
docker compose exec georama make migrate
docker compose exec georama make create-superuser
```

Admin interface (user: admin password: whatever-you-chose): http://localhost:8080/admin/
