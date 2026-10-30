---
icon: lucide/server
---

# Production Deployment

- pooling of DB connections from georama to its own DB has to be handled externally
  (suggestion: pg_bouncer)

Build prod image

```shell
docker build -t local/georama:prod .
```

Run prod image ([--init](https://docs.docker.com/reference/compose-file/services/#init)
replaces tini, it's now included in docker)

```shell
docker run --rm --env-file .env.prod --init docker.io/local/georama:prod
```
