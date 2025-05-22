# Quick-start

See the also the
<a href="https://github.com/opengisch/georama?tab=readme-ov-file#quickstart" target="_blank">
README.md</a>



## Quickstart docker compose

### Prerequisites
- Docker
- Docker Compose


### Setup
```shell
git clone git@github.com:opengisch/georama.git
cd georama
```
#### Configuring the environment
Create your own `.env` file by copying the example.
```shell
cp .env.example .env
```

Set the path to the QGIS projects directory:
`GEORAMA_LOCAL_DATA=<path-to-your-qgis-projects>`

And adapt additional values of `.env` as needed.

#### Starting the services
Then, start the services.
```shell
docker compose build
docker compose up -d
```

Wait for services to be up and running. That might last a moment since the test
data has to be
fetched (about 5GB).

#### Preparing the DB
If everything runs, you can prepare the Django DB.

```shell
docker compose exec georama make migrate
docker compose exec georama make create-superuser
```

#### Accessing the services
Admin interface (user: admin password: whatever-you-chose): http://localhost:8080/admin/


## Next Steps
See the [Workflow](workflow.md)

