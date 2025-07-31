---
tags:
  - Setup
  - Development
---

## Development in a standalone Docker container

### Start the services Georama relies on

#### Start a database (for georama admin configuration)

```shell
docker run --rm -d --name georama-db -e POSTGRES_PASSWORD=test -p 54321:5432 postgis/postgis:latest
```

#### Start a redis instance

For integration with QGIS-Server-Light we need to have a redis instance available:

```shell
docker run --rm -d -p 1234:6379 --name qsl-redis redis
```

#### Start QGIS-Server-Light worker

The QGIS-Server-Light worker can be started with:

```shell
docker run -d --rm --net host --name qsl -v $(pwd)/tests/resources/projects:/io/data opengisch/qgis-server-light:latest
```

### Build Georama container

```shell
docker build -t georama:dev --target dev .
```

### Start Georama container

```shell
docker run -d -p 4242 --rm --net host --name georama -v $(pwd)/tests/resources/projects:/io/data georama:dev
```

### Prepare Django DB and admin user

```shell
docker exec georama make migrate
```

```shell
docker exec -ti georama make create-superuser
```

!!! success
    Admin interface (user: admin password: whatever-you-chose): http://localhost:4242/admin/

!!! info
    You might want to connect to the python interpreter inside the container for debugging reasons. You can
    find it here: `/opt/georama/venv/bin/python`

!!! info
    To force reinstall GitHub dep qgis_server_light interface without complete rebuild:
    ```shell
    docker exec georama bash -c '/opt/georama/venv/bin/pip install --force-reinstall --no-deps "git+ssh://git@github.com/opengisch/qgis-server-light.git@master#qgis_server_light"'
    ```
