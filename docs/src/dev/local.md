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

### 🌍 Running the test server

Georama needs a postgres database to store its stuff in. Unless you have a running database already somewhere
you can easily start one via docker.

#### Spin up a database (for georama admin configuration)

```shell
docker run --rm -d --name georama -e POSTGRES_PASSWORD=test -p 54321:5432 postgis/postgis:latest
```

The maps ([qgis-server-light](https://github.com/opengisch/qgis-server-light)) part of georama needs a redis
instance to put jobs in.

#### Start a redis instance (for qsl integration)

    ```shell
    docker run --rm -d -p 1234:6379 --name georama-redis redis
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

---

### ✅  Running the tests

To run the tests locally execute the following command:

```shell
make tests
```
