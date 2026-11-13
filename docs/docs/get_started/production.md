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

## Security Settings

The settings below decide who gets in and how and if at all. Their defaults are the safe
choice for a
deployment on the internet; each table shows when to deviate. All variables are listed
in [Environment Variables](environment.md).

### HTTP Basic authentication

`GEORAMA_BASIC_AUTH_ENABLED` lets clients send username and password with every request,
without a session. QGIS does this for WMS, WFS and OGC API Features when a layer is
added with a username and password.

| Situation                                                   | Setting                                                                       |
|-------------------------------------------------------------|-------------------------------------------------------------------------------|
| Everyone uses the browser or GeoGirafe                      | `false` (default)                                                             |
| QGIS users load protected layers with username and password | `true`                                                                        |
| Reachable from the internet with `true`                     | additionally a rate limit per ip address in front of Georama (ingress, proxy) |

Superusers can't use HTTP Basic, they get the same answer as for a wrong password. They
use a separate account without superuser rights in QGIS. A refused superuser is logged
as
a warning.

### Failed password logins

Every way a password reaches Georama (login page, admin login, HTTP Basic) counts failed
logins per username. Once `GEORAMA_LOGIN_ATTEMPTS_LIMIT` failures fall within
`GEORAMA_LOGIN_ATTEMPTS_BLOCKED_MINUTES`, the username is refused with HTTP 429 until
the
oldest failure is older than that, even with the right password. Successful logins don't
count.

| Situation                                           | Setting                                                    |
|-----------------------------------------------------|------------------------------------------------------------|
| Default                                             | `5` failures in `5` minutes                                |
| Users complain about being blocked by typos         | raise the limit, e.g. `10`                                 |
| Accounts with valuable rights, public internet      | lower the limit or raise the minutes                       |
| Protection against one source trying many usernames | not in Georama: a rate limit per ip address in front of it |

Georama doesn't limit per ip address on purpose: behind a proxy all clients share its
address and would block each other. The counters live in the memory of each worker
process, so with several workers the effective limit is the limit times the number of
workers, and a restart resets them.

When a username gets blocked, Georama logs a warning with the username, the remote
address and the `X-Forwarded-For` header as received. These are personal data: keep the
logs only as long as needed and mention the logging in the privacy notice (legitimate
interest in network and information security).

### Cookies and HTTPS

| Situation                                                          | Setting                                                                         |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Browsers reach Georama with HTTPS, also with TLS ending at a proxy | `DJANGO_SESSION_COOKIE_SECURE=true`, `DJANGO_CSRF_COOKIE_SECURE=true` (default) |
| Plain HTTP, e.g. the stack on `http://localhost:4242`              | both `false` (`compose.yml` does this)                                          |
| Behind a proxy terminating TLS                                     | `DJANGO_SECURE_PROXY_SSL_HEADER=HTTP_X_FORWARDED_PROTO,https`                   |
| The proxy doesn't send HSTS itself                                 | `DJANGO_SECURE_HSTS_SECONDS`, e.g. `31536000`, together with the line above     |
| Shorter sessions, e.g. shared workstations                         | `DJANGO_SESSION_COOKIE_AGE` in seconds, e.g. `28800` (a working day)            |

The secure flag is about the connection between the browser and the first server it
talks to. The hop from a proxy to Georama may be plain HTTP.

### Identity provider

#### `GEORAMA_OIDC_CLIENT_ID` and `GEORAMA_OIDC_SECRET`

| Situation                | Setting                                                                |
|--------------------------|------------------------------------------------------------------------|
| A provider is configured | `GEORAMA_OIDC_CLIENT_ID` is required, Georama doesn't start without it |
| Public client with PKCE  | `GEORAMA_OIDC_SECRET` empty (default)                                  |
| Confidential client      | `GEORAMA_OIDC_SECRET` set to the client's secret                       |

#### `GEORAMA_OIDC_EMAIL_AUTHENTICATION`

| Situation                                                                                         | Setting           |
|---------------------------------------------------------------------------------------------------|-------------------|
| The provider can't be trusted to verify emails, or people register there themselves               | `false` (default) |
| The provider verifies emails and accounts are created by an administrator (e.g. company Keycloak) | `true`            |

#### `GEORAMA_OIDC_USERNAME_CONFLICT`

| Situation                                                                          | Setting            |
|------------------------------------------------------------------------------------|--------------------|
| Usernames at the provider can be chosen freely                                     | `suffix` (default) |
| The provider's usernames are the same people as the local ones and can't be chosen | `connect`          |

#### `GEORAMA_GEOGIRAFE_SUPERUSER_ENABLED`

| Situation                                                     | Setting              |
|---------------------------------------------------------------|----------------------|
| Production                                                    | `false` (default)    |
| Development, administrators test GeoGirafe with their account | `true` (Dev default) |

#### `GEORAMA_OIDC_TIMEOUT_SECONDS` and `GEORAMA_OIDC_RETRY_SECONDS`

| Situation                    | Setting                                             |
|------------------------------|-----------------------------------------------------|
| Provider in the same network | timeout `5` (default) or less, retry `30` (default) |
| Slow or remote provider      | timeout a few seconds more                          |

With `GEORAMA_OIDC_EMAIL_AUTHENTICATION=false`, a person with a local account who signs
in
through the provider for the first time, with the same email, gets a form to complete
the
signup with another email. Georama logs a warning in that case. The user list of the
admin has the filter "provider account: not linked" which shows the local accounts
concerned. Once linked, later logins find the account by the provider's user id.

Logging out of Georama ends Georama's session only, not the one at the provider. The
lifetime of the provider's session is configured there (in Keycloak the realm's session
timeouts).

### Upgrading

These defaults changed and need a look when an existing installation is upgraded:

- HTTP Basic is off. Installations where QGIS uses username and password set
  `GEORAMA_BASIC_AUTH_ENABLED=true`.
- The cookies are sent over HTTPS only. Installations on plain HTTP set both
  `DJANGO_*_COOKIE_SECURE=false`.
- `GEORAMA_OIDC_CLIENT_ID` has no default anymore, and `GEORAMA_OIDC_SECRET` defaults to
  empty. Installations with a provider set both explicitly.
- Signing in by email is off (`GEORAMA_OIDC_EMAIL_AUTHENTICATION`). Check the admin
  filter
  "provider account: not linked" for local accounts which would be affected.
- Superusers can't use GeoGirafe with their token
  (`GEORAMA_GEOGIRAFE_SUPERUSER_ENABLED`).
- GeoGirafe tokens no longer open a session in Georama.
