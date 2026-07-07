# DEV

## Prerequisites

- `uv` https://docs.astral.sh/uv/
- `docker` + `docker compose` https://docs.docker.com/engine/install/
- `git` https://git-scm.com/install/
- `pre-commit` https://pre-commit.com/#installation

## Commands

```shell
# Add a new dependency for georama
uv add <package-name>
# Add a new dev dependency for georama
uv add --group dev <package-name>
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
### Create DEV content

⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️

The following commands are bulk creation tools! They are intended to be used whenever
you as a DEV need random and more or less functional content in Georama to try things.
NOTE: FOR CONSISTENCY REASON THESE COMMANDS ARE ALL DELETING THE CONTENT OF THEIR RELATED
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

For each vector layer, a corresponding postgis table is created and populated with random data.
The tables can be found in the georama db in the schema `dummy`.

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_integration"
```
#### Features content

Randomly publishes vector layers assigns them to users or groups.

```shell
docker compose run --rm --entrypoint bash georama -c "uv run manage create_dev_content_features"
```

# pygeoapi

- oapif write only on postgis layers
- ogr provider does not support layers without fields beside pk & geom

# Problems

- we depend on GDAL, uv always just installs the newest package or the locked on,
  however, this
  rarely matches the exact version available installed in random systems, so we remove
  it as a dep
  from pyproject.toml and make it a dep assumed to be available in the system via (
  python3-gdal, or similar)
