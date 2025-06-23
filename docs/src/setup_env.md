---
tags:
  - Setup
  - Environment
---

# Setting up the environment variables for different environments

We use the package `django-configurations` to switch between different configuration classes. The most important
environment variable for this is `DJANGO_CONFIGURATION` which can be set to either `Prod`, `Dev` or `Test`

Depending on the enviroment you choose, the `.env` file needs different values provided.

## Development
Copy the provided example file
```bash
cp .env.dev.example .env
```

The content of the file looks now like this:

```text
############################################################################
# Georama development settings
############################################################################

DJANGO_CONFIGURATION=Dev

QSL_LOG_LEVEL=debug
QSL_REPLICAS=1
QSL_REDIS_URL=redis://qsl-redis
QSL_DATA_ROOT=/io/data

GEORAMA_DATA_INTEGRATION_ROOT=/io/data

GEORAMA_DB_PW=test
GEORAMA_DB_USER=postgres
GEORAMA_DB_PORT=5432
GEORAMA_DB_HOST=georama-db
GEORAMA_DB_NAME=postgres

GEORAMA_LOCAL_DATA=<path-to-your-qgis-projects>
```

You only need to provide `GEORAMA_LOCAL_DATA` to spin up the stack on your local machine


## Production
Copy the provided example file
```bash
cp .env.prod.example .env
```

The content of the file looks now like this:

```text
############################################################################
# Georama production settings
############################################################################

DJANGO_CONFIGURATION=Prod

# Set this to a long, random string unique for this deployment.
DJANGO_SECRET_KEY=<your-secret-key>

QSL_LOG_LEVEL=info
QSL_REPLICAS=1
QSL_REDIS_URL=redis://qsl-redis
QSL_DATA_ROOT=/io/data

GEORAMA_DATA_INTEGRATION_ROOT=/io/data

GEORAMA_DB_PW=<your-db-password>
GEORAMA_DB_USER=<your-db-user>
GEORAMA_DB_PORT=5432
GEORAMA_DB_HOST=georama-db
GEORAMA_DB_NAME=postgres

GEORAMA_LOCAL_DATA=<path-to-your-qgis-projects>

# In the settings below, replace georama.example.org and geogirafe.example.org
# with the public hostnames of your Georama backend and the frontend, respectively.

# space separated list of allowed hosts
GEORAMA_ALLOWED_HOSTS="localhost georama.example.org"

# space separated list of allowed CORS origins
GEORAMA_CORS_ALLOWED_ORIGINS="https://geogirafe.example.org"

# space separated list of CSRF trusted origins
GEORAMA_CSRF_TRUSTED_ORIGINS="https://geogirafe.example.org"

```

You now need to provide values for all the variables.