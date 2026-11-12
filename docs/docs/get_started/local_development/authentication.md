---
icon: lucide/key-round
---

# Authentication (OIDC with Keycloak)

How to test / develop OIDC authentication locally using Keycloak.

## Overview

The development stack contains a Keycloak instance with the realm `ninjas`, the public
client `georama-oidc` and the user `fred.flintstone`. It is imported from
`keycloak/import/ninjas-realm.json` on the first start.

Local development of OIDC + Keycloak is currently supported for the following
scenarios:

- Georama backend from the stack at `http://localhost:4242`
- GeoGirafe frontend from the stack at `https://localhost:9309`
- GeoGirafe frontend from filesystem (not docker) at `http://app.localhost:8080` (aka
  dev environ as gg-viewer defines it)

Other scenarios require their address in the allowed redirect URIs and web origins of
the `georama-oidc` client (see [Testing authentication](#testing-authentication)) and in
`DJANGO_CORS_ALLOWED_ORIGINS` (see [Environment Variables](../environment.md)).

!!! warning "HTTPS for GeoGirafe"

    GeoGirafe requires HTTPS in two places, so the
    [development certificates](index.md#development-certificates) have to be trusted:

    - It handles authentication in a service worker, which browsers only register on
      HTTPS with a trusted certificate. Otherwise the login fails with
      `Cannot read properties of undefined (reading 'login')`.
    - Its OIDC library (`oauth4webapi`) only talks to an HTTPS issuer. Otherwise the
      login fails with `only requests to HTTPS are allowed`.

    A standalone GeoGirafe serves its own certificate, see its README. Keycloak is still
    served with the certificate of the stack.

## Login page

The login page (`/login/`) shows the local username/password form and below it one
button per configured OpenID Connect provider.

Setups where everyone signs in through the provider can hide the local form with
`GEORAMA_LOGIN_LOCAL_FORM_ENABLED=false`
(see [Environment Variables](../environment.md)).
The page then only shows the provider buttons and refuses a submitted local login (HTTP
405).

The setting covers every place in the browser where a password is entered:

- The admin login (`/admin/login/`) forwards to the login page and keeps the page that
  was requested. Administrators sign in through the provider as well.
- The login of django-allauth (`/accounts/login/`) refuses passwords. Its signup,
  password reset and email pages are gone.

If no provider is configured, both forms are shown anyway, so nobody is locked out.
Georama logs a warning at start about this combination. When the provider is down,
switch the setting back on for the time being or use `manage.py changepassword` /
`manage.py createsuperuser` in the container.

!!! note "HTTP Basic authentication"

    Clients like QGIS send username and password with every request (HTTP Basic
    authentication). This keeps working with the local form switched off, it does not
    open a session. Georama has no protection against guessing passwords there, so
    limit it in front of Georama (e.g. a rate limit on the ingress) if it is reachable
    from the internet.

    Superusers can't use HTTP Basic authentication.

### Signup

Nobody can create a local account themselves (`/accounts/signup/` shows a "closed"
page). Accounts are created by an administrator or by the first login through the
provider. To let people sign up, set `GEORAMA_LOGIN_LOCAL_SIGNUP_ENABLED=true` (see
[Environment Variables](../environment.md)). With the local form switched off there is
no signup at all.

## Starting the stack

- Boot the stack with `docker compose up -d`

Keycloak is reached with two different addresses:

- the browser uses `https://localhost:7443` (`KC_HOSTNAME` in `compose.yml`), this is
  also the issuer of the tokens
- Georama uses `http://keycloak:7080` from within the docker network
  (`GEORAMA_OIDC_SERVER_URL`)

`KC_HOSTNAME_BACKCHANNEL_DYNAMIC` makes Keycloak announce the endpoints for the server
to
server requests (token, userinfo, keys) with the address which was requested, so that
both sides can reach them.

## Testing authentication

Check that Keycloak is running:

- Visit https://localhost:7443/ (incognito tab recommended)
- Log in with the user `admin` and password `admin`
- In the top left, select the "ninjas" instead of the "master" realm
- Under users, there should be 1 user, `fred.flintstone`
- Under clients, there should be a `georama-oidc` client
- On that client is where you would configure additional allowed redirect URIs and CORS
  origins

### Keycloak login page

The realm uses the login theme `georama` from `keycloak/themes`, mounted into the
container. It only adds the Georama logo to the default Keycloak theme and an optional
hint under the login form. The hint is empty by default, add one in the admin console
under Realm settings > Localization > Realm overrides with the key `georamaLoginHint`.
With an existing `keycloak-db` volume the theme has to be selected once under Realm
settings > Themes > Login theme. How Keycloak themes work is described in the
[Keycloak theme documentation](https://www.keycloak.org/ui-customization/themes).

### Backend

- Visit http://localhost:4242/login/
- You should see a button "Keycloak" below the form
- Click on it, you should be redirected to the Keycloak "Ninjas" Realm
- Log in with the user `fred.flintstone` and password `fred`
- You should be redirected back to Georama and be logged in as `fred.flintstone`

### Frontend

The GeoGirafe of the stack uses `geogirafe/config.json`. For a standalone GeoGirafe
local
development instance, copy it over (or its `"oauth"` section at least).

- Visit https://localhost:9309 (stack) or https://app.localhost:8080 (standalone)
- Click "Login"
- You should be redirected to the Keycloak "Ninjas" Realm
- Log in with the user `fred.flintstone` and password `fred`
- You should be redirected back to GeoGirafe, and in the top right see your user
- If you refresh the page however, auth will break
- To work around that, set `"loginRequired": true` in the GeoGirafe `config.json`

!!! note "Existing Keycloak database"

    The realm is only imported when it does not exist yet. With an existing
    `keycloak-db` volume, add new redirect URIs and web origins in the admin console, or
    remove the volume (`docker compose down -v`) to import the realm again. This also
    removes the `dev-ca` volume, see [Development Certificates](index.md#development-certificates).
