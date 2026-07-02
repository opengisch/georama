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
docker compose exec georama uv run manage
```

```shell
docker compose exec georama uv run pytest
```

```shell
docker compose exec georama uv run manage create_dev_content_core
```

```shell
docker compose exec georama uv run manage create_dev_content_integration
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
