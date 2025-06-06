# GEORAMA

A GDI (geospatial data infrastructure) like application to publish your geodata
via QGIS projects.

## Features

1. A GDI like django application (geodata cms)
1. Split into combinable [django](https://www.djangoproject.com) apps
1. [QGIS](https://qgis.org) backed data integration app
1. pygeoapi backed feature server (WFS and OGC API Features)
1. [QGIS](https://qgis.org) backed WMS
1. [GeoGirafe](https://gitlab.com/geogirafe/gg-viewer) Frontend

## Docs

For a detailed description, please consult our [documentation](https://docs.georama.io)

## Quickstart docker compose

Create your own `.env` file by copying the example.
```shell
cp .env.example .env
```

Set the path to the QGIS projects directory:
`GEORAMA_LOCAL_DATA=<path-to-your-qgis-projects>`

And adapt additional values of `.env` as needed.

Then, start the services.
```shell
docker compose build
docker compose up -d
```

Wait for services to be up and running. That might last a moment since the test
data has to be
fetched (about 5GB).

If everything runs, you can prepare the Django DB.

```shell
docker compose exec georama make migrate
docker compose exec georama make create-superuser
```

Admin interface (user: admin password: whatever-you-chose): http://localhost:4242/admin/
