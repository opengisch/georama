# DEV

## Prerequisites

Tools used:

- `uv` https://docs.astral.sh/uv/
- `docker` + `docker compose` https://docs.docker.com/engine/install/
- `git` https://git-scm.com/install/
- `pre-commit` https://pre-commit.com/#installation

they are provided in the container runtime, no need to have them locally

## DEV with the stack

Service georama exposes an ssh server on localhost:4222 which can be used for remote
development.

Credentials: `appuser:secret`

The interpreter is located in the container under: `/home/appuser/.venv/bin/python`

It might be uses also directly with in-container-dev capabilities of your IDE.

The composition is synced with your local user (GID/UID) to ensure, created files in the
container have the right permissions also outside the container.

## Commands

```shell
# Add a new dependency for georama
docker compose run --rm --entrypoint bash georama -c "uv add <package-name>"
# Add a new dev dependency for georama
docker compose run --rm --entrypoint bash georama -c "uv add --group dev <package-name>"
```

```shell
docker compose up --watch --remove-orphans
```

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage"
```

```shell
docker compose run --rm --entrypoint bash georama -c "uv run pytest"
```

## Local editable qgis-server-light (optional)

The shared dependency lock uses the Git source for `qgis-server-light` so `uv lock`
is portable on host and CI.

If you need to iterate on a local checkout, install it editable into your local env
after syncing dependencies:

```shell
uv sync --group dev
uv pip install --editable /absolute/path/to/qgis-server-light[interface]
```

## System GDAL

GDAL bindings need to be compatible with the gdal binaries that are installed.
The default way is that Georama expects gdal bindings to be installed from the system,
on ubuntu this can be done with:

```shell
apt install python3-gdal
```

This requires the app to be run with system python too. If you want to run the app with
another python interpreter than system python or have other specific needs, you will
need to have gdal development dependencies to be installed and can install the `gdal`
group

```
uv sync --group gdal
```


### Create DEV content

⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️

The following commands are bulk creation tools! They are intended to be used whenever
you as a DEV need random and more or less functional content in Georama to try things.
NOTE: FOR CONSISTENCY REASON THESE COMMANDS ARE ALL DELETING THE CONTENT OF THEIR
RELATED
TABLES BEFORE THEY INSERT THE RANDOM STUFF!

⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️

#### Core content

Create users, groups, admin user, memberships, organisations, assigns users randomly to
organisations (memberships) and to groups.

Adminuser: `admin/admin`

User: `<username>:<username>`

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_core"
```

#### Integration content

Creates projects, raster, custom and vector layers (with fields) and binds projects
randomly to organisations which might exist.

NOTE: Raster and Custom layers are non-functional random layers, Vector is PostGIS only!

For each vector layer, a corresponding postgis table is created and populated with
random data.
The tables can be found in the georama db in the schema `dummy`.

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_integration"
```

#### Features content

Randomly publishes vector layers assigns them to users or groups.

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_features"
```

#### Maps content

Randomly publishes vector datasources as WMS and assigns them to users or groups.

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_maps"
```

#### WebGis content

Randomly publishes Projects as WebGis Themes. Be aware, that only the automatic vector
datasources
are working currently. Raster and Custom are generated but have no working
content/source definition
yet.

Also, the themes_json is empty currently and so a bound GeoGirafe instance won't work
currently.

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_webgis"
```

# pygeoapi

- oapif write only on postgis layers
- ogr provider does not support layers without fields beside pk & geom

# Problems

- Inheritance of templates not working for django
  partials: https://code.djangoproject.com/ticket/37038
