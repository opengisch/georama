---
tags:
  - Setup
  - Environment
---

# Setting up the environment variables for different environments

Via the `DJANGO_CONFIGURATION` variable you select a configuration profile (one of the classes in settings.py).
These profiles provide base configurations (groups of settings) that are an appropriate starting point for the
respective environment.
By overriding settings via environment variables in the .env file, you can tune those configurations for your particular needs.
The `DJANGO_CONFIGURATION` variable can be set to either `Prod`, `Dev` or `Test`

Depending on the environment you choose, the `.env` file needs different values provided.

## Development
Copy the provided example file
```bash
cp .env.dev.example .env
```

You only need to provide `GEORAMA_LOCAL_DATA` to spin up the stack on your local machine


## Production
Copy the provided example file
```bash
cp .env.prod.example .env
```

For a production setup, you need to at least set or adapt the following variables:

```text
DJANGO_SECRET_KEY=<your-secret-key>

GEORAMA_DB_PW=<your-db-password>
GEORAMA_DB_USER=<your-db-user>
GEORAMA_DB_PORT=5432
GEORAMA_DB_HOST=georama-db
GEORAMA_DB_NAME=postgres

GEORAMA_LOCAL_DATA=<path-to-your-qgis-projects>

GEORAMA_ALLOWED_HOSTS="localhost georama.example.org"

GEORAMA_CORS_ALLOWED_ORIGINS="https://geogirafe.example.org"

GEORAMA_CSRF_TRUSTED_ORIGINS="https://geogirafe.example.org"
```
