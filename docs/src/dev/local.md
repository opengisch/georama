---
tags:
  - Setup
  - Development
---

## Development on the Host (Local Machine)

!!! info
    Local development requires **Python 3.10 or higher** due to package compatibility.

### 📦 Dependencies

Make sure these are available on your system:

- GDAL (incl headers have to be available)
- `make`
- general `pip` and `virtualenv` has to be available

#### ✅ Install on Ubuntu:

```bash
sudo apt-get update && sudo apt-get install gdal make
```

#### ✅ Install on Arch:

```bash
sudo pacman -Syy && sudo pacman -S gdal make
```

### 🧪 Set Up Virtual Environment

To prepare a local virtual environment (in the folder `.venv`) run the following command:

```shell
make install-dev
```

In case you are using an IDE you can point it to that venv to have code completion and code inspection.

---

### 🌍 Running the server

Georama needs a postgres database to store its stuff in. Unless you have a running database already somewhere
you can easily start one via docker.

#### Spin up a database (for georama admin configuration)

```shell
docker run --rm -d --name georama-db -e POSTGRES_PASSWORD=test -p 54321:5432 postgis/postgis:latest
```

The maps ([qgis-server-light](https://github.com/opengisch/qgis-server-light)) part of georama needs a redis
instance to put jobs in.

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

#### Launch the Auto-Reloading Dev Server

You can spin up a self reloading DEV server which detects code changes automatically with:

```shell
make serve-dev
```

4. Initialize the Database:
Once the server is running, open another terminal to create the database structure for Georama.

```shell
make migrate
```

5. Create a Superuser:
Create a superuser which can be used to log into Georama:

```shell
make create-superuser
```

6. Create example content (like demo users):

```shell
make create-example-content
```

You may now navigate to [http://localhost:4242/admin/](http://localhost:4242/admin/) with your favorite
browser.

!!! info
    To force reinstall GitHub dependency qgis_server_light interface without rebuilding everything:
    ```shell
    .venv/bin/pip install --force-reinstall --no-deps "git+ssh://git@github.com/opengisch/qgis-server-light.git@master#qgis_server_light"
    ```

---

### ✅  Running the tests

To run the tests locally execute the following command:

```shell
make tests
```
