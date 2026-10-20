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
to be set explicitly in production, while `Dev` provides defaults for many of them.

Each setting reads an environment variable named `<PREFIX>_<SETTING>`. The prefix is
`DJANGO` for standard Django settings (e.g. `DJANGO_SECRET_KEY`) and `GEORAMA` for
Georama settings (e.g. `GEORAMA_DB_NAME`).

### Environment Files

| File        | Purpose                                                                  |
| ----------- | ------------------------------------------------------------------------ |
| `.env.dev`  | Template for local development                                           |
| `.env.prod` | Template for production                                                  |
| `.env`      | Your actual configuration, read by Docker Compose (not committed to git) |

## Required Variables

### Django

`DJANGO_CONFIGURATION`
: Selects the configuration class (`Dev` or `Prod`).

    - **Dev**: `Dev`. Set it explicitly: the ASGI server defaults to `Dev`, but the
      `manage` command defaults to `Prod`, so `uv run manage …` would fail without it.
      The `create_dev_content_*` commands also only run when it is `Dev`.
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

The connection to the PostgreSQL / PostGIS database. In development, `compose.yml` also
uses `GEORAMA_DB_USER`, `GEORAMA_DB_PW` and `GEORAMA_DB_NAME` to initialise the
`georama-db` service, and refuses to start if they are missing.

| Variable          | Purpose           | Dev (`.env.dev`)                    | Prod               |
| ----------------- | ----------------- | ----------------------------------- | ------------------ |
| `GEORAMA_DB_NAME` | Database name     | `postgres`                          | Your database name |
| `GEORAMA_DB_USER` | Database user     | `postgres`                          | Your database user |
| `GEORAMA_DB_PW`   | Database password | `test`                              | A strong password  |
| `GEORAMA_DB_HOST` | Database host     | `georama-db` (the compose service)  | Your database host |
| `GEORAMA_DB_PORT` | Database port     | `5432` (inside the compose network) | Usually `5432`     |

!!! warning

    The values of `.env.prod` are placeholders copied from development: replace them,
    in particular the password, before deploying.

### QGIS-Server-Light

`GEORAMA_QSL_EXPORTER_URL`
: Full URL of the QSL exporter endpoint. Georama `POST`s the path of a QGIS project to
it when a project is imported, and receives the project description back.

    - **Dev**: set by `compose.yml` to `http://qsl-exporter:8000/export`, no need to
      put it in `.env`.
    - **Prod**: required. Use the full endpoint, including the `/export` path, e.g.
      `http://qsl-exporter:8000/export`.

`QSL_REDIS_URL`
: URL of the Redis instance used as job queue between Georama and the QSL rendering
workers (`qsl`). Note that this variable has **no** `GEORAMA_` prefix: it is shared
with QSL, which reads the same name.

    - **Dev**: defaults to `redis://qsl-redis:6379`, also set by `compose.yml`.
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

    - **Dev**: defaults to `http://localhost:9308`, the `geogirafe` compose service.
    - **Prod**: required, e.g. `https://map.example.com`.

`GEORAMA_CORS_ALLOWED_ORIGINS`
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

    - **Dev**: defaults to `tests/resources/projects`, which is also mounted as `/io/data`
      in the QSL services.
    - **Prod**: required, but already set to `/io` by the production image: mount your
      projects volume there, or override the variable.

## Optional Variables

### Georama

| Variable                                                   | Default                | Purpose                                                                                                                              |
| ---------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `GEORAMA_SITE_TITLE`                                       | `Georama`              | Title displayed in the templates.                                                                                                    |
| `GEORAMA_ORGANISATION_GLOBAL_PUBLIC_ACCESS`                | `true`                 | Whether the global organisation (the bare `GEORAMA_ORGANISATION_DOMAIN`) is accessible without being logged in.                      |
| `GEORAMA_ORGANISATION_NOT_AUTHENTICATED_TARGET`            | `core:login`           | Name of the view anonymous users are redirected to when they access a non public organisation.                                       |
| `GEORAMA_ORGANISATION_GLOBAL_PUBLIC_ACCESS_BYPASS_TARGETS` | _empty_                | Space separated view names skipped by the organisation middleware. **Use with caution**, it may expose data.                         |
| `GEORAMA_DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER`      | `global`               | Name of the global organisation folder inside `GEORAMA_DATA_INTEGRATION_ROOT`.                                                       |
| `GEORAMA_JOB_TIMEOUT`                                      | `1000`                 | Timeout of the rendering jobs sent to QSL through Redis, **_in seconds_**.                                                           |
| `GEORAMA_WEBGIS_OGC_SERVER_NAME`                           | `georama.webgis`       | Name of the Georama OGC server in the `themes.json` served to GeoGirafe.                                                             |
| `GEORAMA_LIST_PAGE_SIZES`                                  | `10 25 50 100 200 500` | Page sizes proposed in the lists of the user interface.                                                                              |

### Database Tuning

| Variable                                 | Default                                  | Purpose                                                                                                                                                                            |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GEORAMA_DB_OPTIONS`                     | `{"pool": False}`                        | Driver [`OPTIONS`](https://docs.djangoproject.com/en/6.0/ref/databases/#postgresql-notes), e.g. `{"pool": True}` to enable psycopg connection pooling. `.env.dev` sets it to `{}`. |
| `GEORAMA_DB_CONN_MAX_AGE`                | `0`                                      | Lifetime of a database connection in seconds (`0` closes it after each request).                                                                                                   |
| `GEORAMA_DB_CONN_HEALTH_CHECKS`          | `true`                                   | Check persistent connections before reusing them.                                                                                                                                  |
| `GEORAMA_DB_DISABLE_SERVER_SIDE_CURSORS` | `true`                                   | Disable server side cursors, needed behind a transaction pooler such as PgBouncer.                                                                                                 |
| `GEORAMA_DB_ENGINE`                      | `django.contrib.gis.db.backends.postgis` | Django database backend. PostGIS is required, there is normally no reason to change it.                                                                                            |

### Security and CORS

| Variable                         | Default                                      | Purpose                                                                                                                                                                                                                                                 |
| -------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DJANGO_SECURE_PROXY_SSL_HEADER` | _unset_                                      | **Prod**, behind a reverse proxy terminating TLS: set it to `HTTP_X_FORWARDED_PROTO,https` (comma separated) so that Django knows the original request was HTTPS ([docs](https://docs.djangoproject.com/en/6.0/ref/settings/#secure-proxy-ssl-header)). |
| `GEORAMA_CORS_ALLOW_CREDENTIALS` | `true`                                       | Allow cookies in cross-origin requests.                                                                                                                                                                                                                 |
| `GEORAMA_CORS_ALLOW_METHODS`     | `DELETE HEAD GET OPTIONS PATCH POST PUT`     | HTTP methods allowed in cross-origin requests.                                                                                                                                                                                                          |
| `GEORAMA_CORS_ALLOW_HEADERS`     | django-cors-headers defaults + `content-crs` | Headers allowed in cross-origin requests.                                                                                                                                                                                                               |

### Authentication with OpenID Connect

Georama can delegate the login to an OpenID Connect provider (e.g. Keycloak) through
[django-allauth](https://docs.allauth.org/en/dev/socialaccount/providers/openid_connect.html).

| Variable                          | Default        | Purpose                                                                                              |
| --------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| `GEORAMA_OIDC_SERVER_URL`         | _unset_        | URL of the provider, e.g. `https://sso.example.com/realms/<realm>/.well-known/openid-configuration`. |
| `GEORAMA_OIDC_CLIENT_ID`          | `georama-oidc` | Client id registered at the provider.                                                                |
| `GEORAMA_OIDC_SECRET`             | `secret`       | Client secret. **Prod**: always set it to the real secret.                                           |
| `GEORAMA_OIDC_NAME`               | `Keycloak`     | Name of the provider displayed on the login page.                                                    |
| `GEORAMA_OIDC_PROVIDER_ID`        | `keycloak`     | Internal identifier of the provider, used in the callback URLs.                                      |
| `GEORAMA_OIDC_OAUTH_PKCE_ENABLED` | `true`         | Use PKCE for the authorization code flow.                                                            |

!!! note

    The development stack does not include an identity provider. To test OIDC locally,
    run one (e.g. Keycloak) and point `GEORAMA_OIDC_SERVER_URL` to it.

### QGIS-Server-Light

`QSL_LOG_LEVEL`
: Log level of the QSL services (`debug`, `info`, …). Georama does not read it: in
development it reaches the `qsl` and `qsl-exporter` services through the shared
`.env`. In production, set it on the QSL containers.

### Docker Compose (Development Only)

These variables are only used by Docker Compose, when building the development image or
starting the stack. They have no effect on the production image.

| Variable               | Default  | Purpose                                                                                                                                                                                                                    |
| ---------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `UID`                  | `1000`   | **Required on Linux** when your ids differ from the default: user id (`id -u`) of the container user, so that files created in the mounted repository belong to you.                                                       |
| `GID`                  | `1000`   | **Required on Linux**, as above: group id (`id -g`) of the container user.                                                                                                                                                 |
| `QSL_SOURCE_BRANCH`    | `master` | Branch of [qgis-server-light](https://github.com/opengisch/qgis-server-light) downloaded into the `georama` image (`/qsl`), which provides the `qgis-server-light` Python dependency. Rebuild the image after changing it. |
| `QSL_IMAGE_TAG_SUFFIX` | _empty_  | Suffix appended to the `qsl` (`latest`) and `qsl-exporter` (`latest-exporter`) image tags, to run images built for a QSL pull request, e.g. `-pr-66`.                                                                      |
| `QSL_SOURCE_ROOT`      | _unset_  | Path (absolute or relative) to a local clone of qgis-server-light, to develop it alongside Georama. Only used by `compose.override.yml.with_qsl_sources`, which you need to copy to `compose.override.yml`.                |
| `PY_VERSION`           | `3.12`   | Python version of the development images.                                                                                                                                                                                  |

## Summary: Dev vs Prod

| Variable                              | Dev                                              | Prod                                    |
| ------------------------------------- | ------------------------------------------------ | --------------------------------------- |
| `DJANGO_CONFIGURATION`                | `Dev`                                            | `Prod` (mandatory)                      |
| `DJANGO_SECRET_KEY`                   | ignored                                          | **required**, secret                    |
| `DJANGO_ALLOWED_HOSTS`                | default                                          | **required** in practice                |
| `DJANGO_CSRF_TRUSTED_ORIGINS`         | default                                          | **required**                            |
| `GEORAMA_CORS_ALLOWED_ORIGINS`        | default                                          | **required**                            |
| `GEORAMA_DB_*`                        | **required** (`.env.dev` values)                 | **required**                            |
| `GEORAMA_QSL_EXPORTER_URL`            | set by `compose.yml`                             | **required**                            |
| `QSL_REDIS_URL`                       | default / `compose.yml`                          | **required**                            |
| `GEORAMA_ORGANISATION_DOMAIN`         | ignored (`localhost`)                            | **required**                            |
| `GEORAMA_WEBGISURL`                   | default                                          | **required**                            |
| `GEORAMA_DATA_INTEGRATION_ROOT`       | default                                          | **required**, set to `/io` by the image |
| `UID`, `GID`, `QSL_*` build variables | Linux / optional                                 | not used                                |

### Production Example

```shell title=".env.prod"
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
GEORAMA_CORS_ALLOWED_ORIGINS=https://map.example.com

GEORAMA_QSL_EXPORTER_URL=http://qsl-exporter:8000/export
QSL_REDIS_URL=redis://qsl-redis:6379
```
