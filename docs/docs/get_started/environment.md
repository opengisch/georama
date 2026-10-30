---
icon: lucide/settings
---

# Environment Variables

Georama is configured through environment variables. This page lists them, first the
**required** ones and then the **optional** ones, and explains what each one does in
**development** and in **production**.

## How the Configuration Works

The Django settings (`src/georama/settings.py`) are built with
[django-configurations](https://django-configurations.readthedocs.io/). They define
several configuration classes, and `DJANGO_CONFIGURATION` selects which one is active:

| Configuration | Used for                                                                 |
| ------------- | ------------------------------------------------------------------------ |
| `Dev`         | Local development (`DEBUG` on, permissive defaults, profiling with Silk) |
| `Prod`        | Production (`DEBUG` off, static files served by ServeStatic)             |
| `Test`        | The test suite (selected by `pytest` through `--dc=Test`)                |
| `Static`      | Only used while building the production image, to run `collectstatic`    |

`Base` holds the restrictive defaults shared by all configurations, so most values have
to be set explicitly in production. `Dev` provides defaults for the values which are the
same on every developer machine (e.g. allowed hosts and origins), the values which
depend on the services of the stack (e.g. the QSL and database addresses) are set by
`compose.yml`.

Each setting reads an environment variable named `<PREFIX>_<SETTING>`. The prefix is
`DJANGO` for settings of Django and Django apps (e.g. `DJANGO_SECRET_KEY`,
`DJANGO_CORS_ALLOWED_ORIGINS` for django-cors-headers) and `GEORAMA` for Georama
settings (e.g. `GEORAMA_DB_NAME`). Settings shared with other applications are read
without prefix (e.g. `QSL_REDIS_URL`, also read by QSL).

### Environment Files

| File           | Purpose                                                                         |
| -------------- | ------------------------------------------------------------------------------- |
| `.env.example` | Template for the Docker Compose stack, prod like (default) or dev variants      |
| `.env`         | Your actual configuration, read by Docker Compose (not committed to git)        |

Docker Compose only passes the variables to the containers which the compose files
reference. The values of the stack (e.g. `GEORAMA_QSL_EXPORTER_URL`) are set directly in
`compose.yml`, `.env` provides the secrets and the variant specific values. For
production, see the [example](#production-example) below.

## Required Variables

### Django

`DJANGO_CONFIGURATION`
: Selects the configuration class (`Dev` or `Prod`).

    - **Dev**: `Dev`, set by `compose.dev.yml` (`compose.yml` sets `Prod` for the prod
      like stack). Outside of the stack set it explicitly: the ASGI server defaults to
      `Dev`, but the `manage` command defaults to `Prod`, so `uv run manage …` would fail
      without it. The `create_dev_content_*` commands also only run when it is `Dev`.
    - **Prod**: `Prod`. **Mandatory**: the production image starts Gunicorn on the ASGI
      application, which falls back to `Dev` (with `DEBUG` enabled) when this variable
      is missing.

`DJANGO_SECRET_KEY`
: Django's [`SECRET_KEY`](https://docs.djangoproject.com/en/6.0/ref/settings/#secret-key),
used for signing sessions, CSRF tokens, password reset links, etc.

    - **Dev**: ignored, `Dev` uses a hard-coded insecure key.
    - **Prod**: required and must not be empty. Use a long random value and keep it
      secret, e.g. generated with
      `python -c "import secrets; print(secrets.token_urlsafe(64))"`.

`DJANGO_ALLOWED_HOSTS`
: Host names Georama answers to
([`ALLOWED_HOSTS`](https://docs.djangoproject.com/en/6.0/ref/settings/#allowed-hosts)),
space separated. A leading dot matches all subdomains, e.g. `.georama.example.com`.

    - **Dev**: not needed, defaults to `.localhost georama.local`.
    - **Prod**: required in practice, e.g. `.georama.example.com`.

    !!! warning "Set it in production, including the subdomains"

        Georama starts without this variable, but the list is then empty and, as `DEBUG`
        is off, Django answers **every** request with a `400 Bad Request`.

        Organisations are served on subdomains of `GEORAMA_ORGANISATION_DOMAIN`
        (e.g. `acme.georama.example.com`), and the host is checked before the
        organisation is resolved: use a leading dot (`.georama.example.com`) so that
        they are accepted too.

`DJANGO_CSRF_TRUSTED_ORIGINS`
: Origins trusted for unsafe requests (POST, PUT, …)
([`CSRF_TRUSTED_ORIGINS`](https://docs.djangoproject.com/en/6.0/ref/settings/#csrf-trusted-origins)),
space separated, with scheme, e.g. `https://georama.example.com`.

    - **Dev**: optional, defaults to the local Georama and GeoGirafe addresses
      (`http://localhost:4242`, `http://localhost:9308`, `https://localhost:9309`, …).
    - **Prod**: required (may be empty, but then cross-origin forms are rejected).

### Database

The connection to the PostgreSQL / PostGIS database. In the stack, `compose.yml` also
uses `GEORAMA_DB_USER`, `GEORAMA_DB_PW` and `GEORAMA_DB_NAME` to initialise the
`georama-db` service, and refuses to start if they (or `GEORAMA_DB_OPTIONS`) are missing.

| Variable          | Purpose           | Stack                                                 | Prod               |
| ----------------- | ----------------- | ----------------------------------------------------- | ------------------ |
| `GEORAMA_DB_NAME` | Database name     | `postgres` (`.env.example`)                           | Your database name |
| `GEORAMA_DB_USER` | Database user     | `postgres` (`.env.example`)                           | Your database user |
| `GEORAMA_DB_PW`   | Database password | `test` (`.env.example`)                               | A strong password  |
| `GEORAMA_DB_HOST` | Database host     | `georama-db`, the compose service (`compose.yml`)     | Your database host |
| `GEORAMA_DB_PORT` | Database port     | `5432`, inside the compose network (`compose.yml`)    | Usually `5432`     |

!!! warning

    The values of `.env.example` are placeholders for development: don't use them, in
    particular the password, for a deployment.

### QGIS-Server-Light

`GEORAMA_QSL_EXPORTER_URL`
: Full URL of the QSL exporter endpoint. Georama `POST`s the path of a QGIS project to
it when a project is imported, and receives the project description back.

    - **Dev**: set by `compose.yml` to `http://qsl-exporter:5000/export`, no need to
      put it in `.env`.
    - **Prod**: required. Use the full endpoint, including the `/export` path, e.g.
      `http://qsl-exporter:5000/export`.

`QSL_REDIS_URL`
: URL of the Redis instance used as job queue between Georama and the QSL rendering
workers (`qsl-worker`). Note that this variable has **no** `GEORAMA_` prefix: it is
shared with QSL, which reads the same name.

    - **Dev**: set by `compose.yml` to `redis://qsl-redis:6379`, for Georama and the
      QSL workers.
    - **Prod**: required, e.g. `redis://qsl-redis:6379`. It must point to the same Redis
      as the QSL workers.

### Georama

`GEORAMA_ORGANISATION_DOMAIN`
: The domain Georama runs on. The organisation middleware compares the requested host
with it to find the organisation: a request to `<org>.georama.example.com` is served
for the organisation whose domain is `<org>`, a request to the domain itself is
served for the global organisation. If Georama already runs under a subdomain,
include it, e.g. `sub.example.com`.

    - **Dev**: ignored, hard-coded to `localhost` (use `<org>.localhost:4242`).
    - **Prod**: required.

`GEORAMA_WEBGISURL`
: Public URL of the GeoGirafe viewer. It is used for the link on the home page, to
build the theme URLs, and to validate URLs given to the WebGIS API (they must start
with it).

    - **Dev**: set by `compose.yml` to `https://localhost:9309`, the `geogirafe` compose
      service.
    - **Prod**: required, e.g. `https://map.example.com`.

`DJANGO_CORS_ALLOWED_ORIGINS`
: Origins allowed to call the API from a browser
([django-cors-headers](https://github.com/adamchainz/django-cors-headers#cors_allowed_origins-sequencestr)),
space separated. Typically the GeoGirafe URL.

    - **Dev**: optional, defaults to the local GeoGirafe addresses.
    - **Prod**: required (may be empty, but then browsers block cross-origin calls,
      e.g. from GeoGirafe).

`GEORAMA_DATA_INTEGRATION_ROOT`
: Directory containing the QGIS projects and their data, with one sub-folder per
organisation (the global organisation folder is created at startup). QSL must see the
same files.

    - **Dev**: set by `compose.yml` to `/io/data`, where `LOCAL_PROJECTS` (default
      `./tests/resources/projects`) is mounted in Georama and the QSL services.
    - **Prod**: required, but already set to `/io` by the production image: mount your
      projects volume there, or override the variable.

## Optional Variables

### Georama

| Variable                                                   | Default                | Purpose                                                                                                                              |
| ---------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `GEORAMA_LOG_LEVEL`                                        | `INFO` (Dev: `DEBUG`)  | Log level of Georama (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`, case insensitive).                                            |
| `GEORAMA_SITE_TITLE`                                       | `Georama`              | Title displayed in the templates.                                                                                                    |
| `GEORAMA_ORGANISATION_GLOBAL_PUBLIC_ACCESS`                | `true`                 | Whether the global organisation (the bare `GEORAMA_ORGANISATION_DOMAIN`) is accessible without being logged in.                      |
| `GEORAMA_ORGANISATION_NOT_AUTHENTICATED_TARGET`            | `core:login`           | Name of the view anonymous users are redirected to when they access a non public organisation.                                       |
| `GEORAMA_ORGANISATION_GLOBAL_PUBLIC_ACCESS_BYPASS_TARGETS` | _empty_                | Space separated view names skipped by the organisation middleware. **Use with caution**, it may expose data.                         |
| `GEORAMA_DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER`      | `global`               | Name of the global organisation folder inside `GEORAMA_DATA_INTEGRATION_ROOT`.                                                       |
| `GEORAMA_JOB_TIMEOUT`                                      | `1000`                 | Timeout of the rendering jobs sent to QSL through Redis, **_in seconds_**.                                                           |
| `GEORAMA_WEBGIS_OGC_SERVER_NAME`                           | `georama.webgis`       | Name of the Georama OGC server in the `themes.json` served to GeoGirafe.                                                             |
| `GEORAMA_LIST_PAGE_SIZES`                                  | `10 25 50 100 200 500` | Page sizes proposed in the lists of the user interface.                                                                              |
| `GEORAMA_MAPS_OGC_OTHER_CRS`                               | `EPSG:3857 EPSG:4326`  | Space separated crs (e.g. EPSG codes) offered by the WFS of the maps app besides the layer crs (OtherCRS), resolved by QSL.          |
| `GEORAMA_WEBGIS_OGC_OTHER_CRS`                             | `EPSG:3857 EPSG:4326`  | Same as `GEORAMA_MAPS_OGC_OTHER_CRS` for the WFS of the webgis app.                                                                  |

### Database Tuning

| Variable                                 | Default                                  | Purpose                                                                                                                                                                                |
| ---------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GEORAMA_DB_OPTIONS`                     | `{"pool": False}`                        | Driver [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes), e.g. `{"pool": True}` to enable psycopg connection pooling. `.env.example` sets it to `{}`. |
| `GEORAMA_DB_CONN_MAX_AGE`                | `0`                                      | Lifetime of a database connection in seconds (`0` closes it after each request).                                                                                                       |
| `GEORAMA_DB_CONN_HEALTH_CHECKS`          | `true`                                   | Check persistent connections before reusing them.                                                                                                                                      |
| `GEORAMA_DB_DISABLE_SERVER_SIDE_CURSORS` | `true`                                   | Disable server side cursors, needed behind a transaction pooler such as PgBouncer.                                                                                                     |
| `GEORAMA_DB_ENGINE`                      | `django.contrib.gis.db.backends.postgis` | Django database backend. PostGIS is required, there is normally no reason to change it.                                                                                                |

### Security and CORS

| Variable                         | Default                                      | Purpose                                                                                                                                                                                                                                                 |
| -------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DJANGO_SECURE_PROXY_SSL_HEADER` | _unset_                                      | **Prod**, behind a reverse proxy terminating TLS: set it to `HTTP_X_FORWARDED_PROTO,https` (comma separated) so that Django knows the original request was HTTPS ([docs](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-proxy-ssl-header)). |
| `DJANGO_CORS_ALLOW_CREDENTIALS`  | `true`                                       | Allow cookies in cross-origin requests.                                                                                                                                                                                                                 |
| `DJANGO_CORS_ALLOW_METHODS`      | `DELETE HEAD GET OPTIONS PATCH POST PUT`     | HTTP methods allowed in cross-origin requests.                                                                                                                                                                                                          |
| `DJANGO_CORS_ALLOW_HEADERS`      | django-cors-headers defaults + `content-crs` | Headers allowed in cross-origin requests.                                                                                                                                                                                                               |

### Authentication with OpenID Connect

Georama can delegate the login to an OpenID Connect provider (e.g. Keycloak) through
[django-allauth](https://docs.allauth.org/en/dev/socialaccount/providers/openid_connect.html).

| Variable                          | Default        | Purpose                                                                                                                                              |
| --------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GEORAMA_OIDC_SERVER_URL`         | _unset_        | URL of the provider, e.g. `https://sso.example.com/realms/<realm>/.well-known/openid-configuration`. Set by `compose.yml` to the `keycloak` service. |
| `GEORAMA_OIDC_CLIENT_ID`          | `georama-oidc` | Client id registered at the provider.                                                                                                                |
| `GEORAMA_OIDC_SECRET`             | `secret`       | Client secret. **Prod**: always set it to the real secret.                                                                                           |
| `GEORAMA_OIDC_NAME`               | `Keycloak`     | Name of the provider displayed on the login page.                                                                                                    |
| `GEORAMA_OIDC_PROVIDER_ID`        | `keycloak`     | Internal identifier of the provider, used in the callback URLs.                                                                                      |
| `GEORAMA_OIDC_OAUTH_PKCE_ENABLED` | `true`         | Use PKCE for the authorization code flow.                                                                                                            |

!!! note

    The stack includes a Keycloak instance and `compose.yml` points
    `GEORAMA_OIDC_SERVER_URL` to it, see
    [Authentication](local_development/authentication.md).

### QGIS-Server-Light

`QSL_LOG_LEVEL`
: Log level of the QSL services (`debug`, `info`, …). Georama does not read it: in the
stack, `compose.yml` passes it to the `qsl-worker` and `qsl-exporter` services (default
`info`, `debug` for the worker of `compose.dev_with_qsl.yml`). In production, set it on
the QSL containers.

### Docker Compose

These variables are only used by Docker Compose, when building the images or starting
the stack. They have no effect on the production image itself.

| Variable                | Default                        | Purpose                                                                                                                                                                       |
| ----------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `COMPOSE_FILE`          | `compose.yml`                  | Variant of the stack: prod like (unset), dev (`compose.yml:compose.dev.yml`) or dev with local QSL sources (`compose.yml:compose.dev.yml:compose.dev_with_qsl.yml`).          |
| `PLATFORM`              | `linux/amd64`                  | Platform of the services.                                                                                                                                                     |
| `LOCAL_PROJECTS`        | `./tests/resources/projects`   | Directory with the QGIS projects, mounted as `/io/data` in Georama and the QSL services.                                                                                      |
| `PG_SERVICE_CONF`       | `./docker/pg_service.conf`     | PostgreSQL service file, mounted in Georama and the QSL services (`PGSERVICEFILE`).                                                                                           |
| `QSL_REPLICAS`          | `4`                            | Number of QSL workers (`compose.dev_with_qsl.yml` always runs 1).                                                                                                             |
| `UID`                   | `1000`                         | **Dev**, **required on Linux** when your ids differ from the default: user id (`id -u`) of the container user, so that files created in the mounted repository belong to you. |
| `GID`                   | `1000`                         | **Dev**, **required on Linux**, as above: group id (`id -g`) of the container user.                                                                                           |
| `PYTHON_VERSION`        | `3.12`                         | **Dev**: Python version of the development image.                                                                                                                             |
| `GEORAMA_DEV_AUTOSTART` | `1`                            | **Dev**: start Georama in the container (`1`) or let it idle (`0`), e.g. to start it yourself for debugging or in a devcontainer.                                             |
| `LOCAL_QSL_SOURCES`     | _unset_                        | **Dev with local QSL sources**, mandatory: absolute path to your local qgis-server-light checkout.                                                                            |
| `QSL_DEV_AUTOSTART`     | `1`                            | **Dev with local QSL sources**: same as `GEORAMA_DEV_AUTOSTART` for the QSL worker.                                                                                           |

## Summary: Dev vs Prod

| Variable                              | Dev                                              | Prod                                    |
| ------------------------------------- | ------------------------------------------------ | --------------------------------------- |
| `DJANGO_CONFIGURATION`                | `Dev`, set by `compose.dev.yml`                  | `Prod` (mandatory)                      |
| `DJANGO_SECRET_KEY`                   | ignored                                          | **required**, secret                    |
| `DJANGO_ALLOWED_HOSTS`                | default                                          | **required** in practice                |
| `DJANGO_CSRF_TRUSTED_ORIGINS`         | default                                          | **required**                            |
| `DJANGO_CORS_ALLOWED_ORIGINS`         | default                                          | **required**                            |
| `GEORAMA_DB_*`                        | **required** (`.env.example` values)             | **required**                            |
| `GEORAMA_QSL_EXPORTER_URL`            | set by `compose.yml`                             | **required**                            |
| `QSL_REDIS_URL`                       | set by `compose.yml`                             | **required**                            |
| `GEORAMA_ORGANISATION_DOMAIN`         | ignored (`localhost`)                            | **required**                            |
| `GEORAMA_WEBGISURL`                   | set by `compose.yml`                             | **required**                            |
| `GEORAMA_DATA_INTEGRATION_ROOT`       | set by `compose.yml`                             | **required**, set to `/io` by the image |
| Docker Compose variables              | Linux (`UID`, `GID`) / optional                  | not used                                |

### Production Example

```shell title=".env"
DJANGO_CONFIGURATION=Prod
DJANGO_SECRET_KEY=<long-random-secret>
DJANGO_ALLOWED_HOSTS=.georama.example.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://georama.example.com https://map.example.com
DJANGO_SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https

GEORAMA_DB_NAME=georama
GEORAMA_DB_USER=georama
GEORAMA_DB_PW=<strong-password>
GEORAMA_DB_HOST=db.example.com
GEORAMA_DB_PORT=5432

GEORAMA_ORGANISATION_DOMAIN=georama.example.com
GEORAMA_WEBGISURL=https://map.example.com
DJANGO_CORS_ALLOWED_ORIGINS=https://map.example.com

GEORAMA_QSL_EXPORTER_URL=http://qsl-exporter:5000/export
QSL_REDIS_URL=redis://qsl-redis:6379
```
