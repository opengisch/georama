# Development

## In a container

Follow the [quick start](quick_start). Check if everything is running.

The setup is mounting the project code into the container of the `georama` service. So hot reload is enabled
if you change code while the docker composition is running.

In case you are using an IDE you can point it to the interpreter inside the container of the `georama`
service. The correct path inside the container is: `/opt/georama/venv`

## Locally

| :exclamation:  This can be used with python 3.10 or lower! |
|------------------------------------------------------------|

*Dependencies*

- gdal 3.9.1 (incl headers have to be available)
- make has to be installed on your system
- general pip and virtualenv has to be available

### Virtual environment

To prepare a local virtual environment (in the folder `.venv`) run the following command:

```shell
make dev
```

In case you are using an IDE you can point it to that venv to have code completion and code inspection.

### Running the test

To run the tests locally execute the following command:

```shell
make tests
```

### Running test server

Georama needs a postgres database to store its stuff in. Unless you have a running database already somewhere
you can easily start one via docker.

Spin up a database (for georama admin configuration):
```shell
docker run --rm -d --name georama -e POSTGRES_PASSWORD=test -p 54321:5432 postgis/postgis:latest
```

The maps ([qgis-server-light](https://github.com/opengisch/qgis-server-light)) part of georama needs a redis
instance to put jobs in.

Start a redis instance (for qsl integration):
```shell
docker run --rm -d -p 1234:6379 --name georama-redis redis
```

You can spin up a self reloading DEV server which detects code changes automatically with:

```shell
make serve
```

Once the server is running, open another terminal to create the database structure for Georama.

```shell
make migrate
```

Create a superuser which can be used to log into Georama:

```shell
make create-superuser
```
