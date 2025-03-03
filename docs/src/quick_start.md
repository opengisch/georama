# Quick-start

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
docker compose exec georama make migrate
docker compose exec georama make create-superuser
```

The last command asks you for a password. Choose one and remember it. You will need it
to login to the admin interface.

Admin interface (user: admin password: whatever-you-chose): http://localhost:8080/admin/
