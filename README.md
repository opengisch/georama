[![build](https://img.shields.io/github/workflow/status/opengisch/georama/Test%20Python%20Package/master?label=build&logo=github-actions&logoColor=%233392FF)](https://github.com/opengisch/georama/actions/workflows/test.yaml?query=branch%3Amaster)
[![release_version](https://img.shields.io/pypi/v/georama)](https://pypi.org/project/georama/)
[![wheel](https://img.shields.io/pypi/wheel/georama?color=green&label=wheel)](https://pypi.org/project/georama)
[![supported_versions](https://img.shields.io/pypi/pyversions/georama?color=blue&label=python&logo=python&logoColor=%23ccccff)](https://pypi.org/project/georama)
[![docs](https://img.shields.io/readthedocs/georama/master?logo=readthedocs&logoColor=lightblue)](https://georama.readthedocs.io/en/master/)
[![coverage](https://img.shields.io/codecov/c/github/opengisch/georama/master?logo=codecov)](https://app.codecov.io/gh/opengisch/georama)
[![maintainability](https://img.shields.io/codeclimate/maintainability/opengisch/georama)](https://codeclimate.com/github/opengisch/georama)
[![tech-debt](https://img.shields.io/codeclimate/tech-debt/opengisch/georama)](https://codeclimate.com/github/opengisch/georama)
[![ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://docs.astral.sh/ruff/)
[![gh-lic](https://img.shields.io/github/license/opengisch/georama)](https://github.com/opengisch/georama/blob/master/LICENSE)
[![commits_since_specific_tag_on_master](https://img.shields.io/github/commits-since/opengisch/georama/v0.0.1/master?color=blue&logo=github)](https://github.com/opengisch/georama/compare/v0.0.1..master)
[![commits_since_latest_github_release](https://img.shields.io/github/commits-since/opengisch/georama/latest?color=blue&logo=semver&sort=semver)]()

# GEORAMA

The habitat of geoanimals

- [**Code**](https://github.com/opengisch/georama)
- [**Docs**](https://georama.readthedocs.io/en/master/)
- [**PyPI**](https://pypi.org/project/georama/)
- [**CI**](https://github.com/opengisch/georama/actions/)

## Features

| :exclamation:  This can be used with python 3.10 or lower! |
|------------------------------------------------------------|

1. **georama** [python package](https://pypi.org/project/georama/)
   1. a gdi like django application
   1. split into combinable django apps
   1. qgis backed dataintegration app
   1. pygeoapi backed feature server (wfs AND OGC API Features)
   1. qgis backed WMS
   1. GeoGirafe Frontend
2. Tested against multiple platforms and python versions

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
docker compose exec app make migrate
docker compose exec app make create-superuser
```

Admin interface (user: admin password: admin): http://localhost:8080/admin/

After login you can use the Clogs integration interface: http://localhost:8080/clogs

Since GeoGirafe is not integrated completely yet, you need to change the following line:
https://github.com/opengisch/georama/blob/master/geogirafe/config.json#L17

The url set up is for the case where you integrated the mapbs themes.json:
`"http://localhost:8080/clogs/mapbs/themes.json"`

Change this to one of:

- "http://localhost:8080/clogs/mapnv/themes.json"
- "http://localhost:8080/clogs/cartoriviera/themes.json"
- "http://localhost:8080/clogs/sitn/themes.json"

Then you can reach your GeoGirafe at: https://localhost:8443/

This uses a custom certificate which you may need to allow. In addition, the themes.json is not the fastest
endpoint. So it may last a moment to load it (this is matter of current improvements).

You should now have a GeoGirafe instance providing the content of the integrated geoportal. You can configure
as you like in Django admin.

## Development


### Development Notes

Testing, Documentation Building, Scripts, CI/CD, Static Code Analysis for this project.

1. **Test Suite**, using `pytest`_, located in `tests` dir
1. **Parallel Execution** of Unit Tests, on multiple cpu's
1. **Documentation Pages**, hosted on `readthedocs` server, located in `docs` dir
1. **CI/CD Pipeline**, running on `Github Actions`_, defined in `.github/`
   1. **Test Job Matrix**, spanning different `platform`'s and `python version`'s
      1. Platforms: `ubuntu-latest`, `macos-latest`, `windows-latest`
      2. Python Interpreters: `3.8`, `3.9`, `3.10`, `3.11`
   1. **Continuous Deployment**

      `Production`
         1. **Python Distristribution** to `pypi.org`_, on `tags` **v***, pushed to `master` branch
         1. **Docker Image** to `Dockerhub`_, on every push, with automatic `Image Tagging`

      `Staging`

         1. **Python Distristribution** to `test.pypi.org`_, on "pre-release" `tags` **v*-rc**, pushed to `release` branch

   1. **Configurable Policies** for `Docker`, and `Static Code Analysis` Workflows
1. **Automation**, using `tox`_, driven by single `tox.ini` file

   1. **Code Coverage** measuring
   1. **Build Command**, using the `build`_ python package
   1. **Pypi Deploy Command**, supporting upload to both `pypi.org`_ and `test.pypi.org`_ servers
   1. **Type Check Command**, using `mypy`_
   1. **Lint** *Check* and `Apply` commands, using the fast `Ruff`_ linter, along with `isort`_ and `black`_

## Prerequisites

You need to have `Python` installed.

## Quickstart

Using `pip` is the approved way for installing `georama`.

```shell
python3 -m pip install georama
```

## DEV

NOTE: You need poetry to be installed on your system!

Install all deps:
```shell
poetry install
```

or (to run tests and build docs)

```shell
poetry install --all-extras
```

Spin up a database (for georama admin configuration):
```shell
docker run --rm -d --name georama -e POSTGRES_PASSWORD=test -p 54321:5432 postgis/postgis:latest
```

start a redis instance (for qsl integration):
```shell
docker run --rm -d -p 1234:6379 --name georama-redis redis
```

In case models changed and were not flushed into migrations:

```shell
python src/georama/manage.py makemigrations
```

Apply migrations:
```shell
python src/georama/manage.py migrate
```

Setup superuser:
```shell
DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_EMAIL=admin@xy.ch python src/georama/manage.py createsuperuser --noinput
```

You might want to prepare the test dataset as described in `georama.test_data` project.

Force reinstall GitHub dep qgis_server_light (in the poetry shell):
```shell
pip install --force-reinstall --no-deps "git+ssh://git@github.com/opengisch/qgis-server-light.git@master#qgis_server_light"
```

## Run tests

Run tests locally directly with pytest (example):

```shell
pytest -vv --cov-config .coveragerc.core -cov src/georama --cov-report term-missing:skip-covered tests
```

Run tests locally directly with tox (example):

```shell
tox -e py310 -vv -s false
```

## License

[![gh-lic](https://img.shields.io/github/license/opengisch/georama)](https://github.com/opengisch/georama/blob/master/LICENSE)

* `GNU Affero General Public License v3.0`

## License

* Free software: GNU Affero General Public License v3.0

## Links

- [tox](https://tox.wiki/en/latest/)
- [pytest](https://docs.pytest.org/en/7.1.x/)
- [build](https://github.com/pypa/build)
- [Dockerhub](https://hub.docker.com/)
- [pypi.org](https://pypi.org/)
- [test.pypi.org](https://test.pypi.org/)
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [Ruff](https://docs.astral.sh/ruff/)
- [isort](https://pycqa.github.io/isort/)
- [black](https://black.readthedocs.io/en/stable/)
- [GitHub Actions](https://github.com/opengisch/georama/actions)
- [GNU Affero General Public License v3.0](https://github.com/opengisch/georama/blob/master/LICENSE)
