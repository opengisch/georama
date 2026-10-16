---
icon: lucide/laptop
---

# Local Development

The development stack is defined in `compose.yml` and runs Georama with live reload,
alongside its database, QGIS-Server-Light and GeoGirafe.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)

Python and `uv` are provided in the container runtime: dependencies, `manage` commands
and tests all run inside the `georama` service, so there is no need to install them
locally to run the stack.

Some tools still run on your host:

- [pre-commit](https://pre-commit.com/#installation): it checks every commit before it
  is created, so that the code is consistently linted and formatted and no Django
  migration is forgotten, catching these issues before the CI does. The git hooks are
  triggered by your local `git commit`. The hooks themselves (`ruff`, `ruff format`, missing
  migrations check) run inside the container through `docker compose run`.

  ```shell
  pre-commit install
  ```

- [uv](https://docs.astral.sh/uv/) (optional): only needed to preview this
  documentation locally, as [Zensical](https://zensical.org/) is not installed in the
  development image.

  ```shell
  cd docs
  uv run --frozen --only-group docs zensical serve
  ```

## Clone the Repository

```shell
git clone git@github.com:opengisch/georama.git
cd georama
```

## Environment Configuration

Copy the example environment file and customize it:

```shell
cp .env.dev .env
```

On Linux, set `UID` and `GID` to your host user and group ids, so that files created in
the container have the right permissions outside of it:

```shell
UID=1000  # output of `id -u`
GID=1000  # output of `id -g`
```

Optionally, adjust the other variables (database credentials, `QSL_SOURCE_BRANCH`, …)
in the `.env` file to match your environment.

!!! note "QGIS projects"

    The QGIS projects served by QGIS-Server-Light are read from
    `./tests/resources/projects`, which is mounted into the `qsl` and `qsl-exporter`
    services as `/io/data`. Put your own projects there (or adapt the volumes in
    `compose.yml`).

## Start the Services

Build and launch all containers:

```shell
docker compose build
docker compose up -d
```

During development, you can also let Compose rebuild the image when `uv.lock` or the
`Dockerfile` change:

```shell
docker compose up --watch --remove-orphans
```

The stack contains the following services:

| Service        | Description                        | Local address           |
| -------------- | ---------------------------------- | ----------------------- |
| `georama`      | Django application (uvicorn)       | <http://localhost:4242> |
| `georama-db`   | PostgreSQL / PostGIS database      | `localhost:5433`        |
| `qsl`          | QGIS-Server-Light rendering worker | –                       |
| `qsl-exporter` | QGIS-Server-Light project exporter | <http://localhost:5000> |
| `qsl-redis`    | Redis queue used by QSL            | –                       |
| `geogirafe`    | GeoGirafe web viewer               | <http://localhost:9308> |

## Prepare the Django Database

Once services are running, apply the migrations and create a superuser:

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage migrate"
docker compose run --rm --entrypoint bash georama -c "uv run manage createsuperuser"
```

## Create Example Content (optional)

Georama ships bulk creation commands which fill the database with fake datasets.

!!! danger

    These commands **delete the content of their related tables** before inserting
    random data. Never run them against a database whose content you want to keep.

```shell
# users, groups, organisations and memberships (also creates the admin user admin/admin)
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_core"
# projects, raster, custom and vector layers (vector layers are backed by PostGIS tables in the `dummy` schema)
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_integration"
# publishes vector layers as OGC API - Features
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_features"
# publishes vector datasources as WMS
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_maps"
# publishes projects as WebGIS themes
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_webgis"
```

Users created by `create_dev_content_core` can log in with `<username>:<username>`.

## Access the Admin Interface

Admin panel: <http://localhost:4242/admin/>

Log in with the superuser credentials you chose (or `admin/admin` if you created the
core example content).

## Remote Development

The `georama` service exposes an SSH server on `localhost:4222` which can be used for
remote development (or use the in-container development capabilities of your IDE).

- Credentials: `appuser:secret`
- Python interpreter: `/home/appuser/.venv/bin/python`

## Run the Tests

```shell
docker compose run --rm --entrypoint bash georama -c "uv run pytest"
```
