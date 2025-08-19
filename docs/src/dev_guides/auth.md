# Authentication using OIDC with Keycloak

How to test / develop OIDC authentication locally using Keycloak.
Add the `docker-compose.keycloak.yml` to the `COMPOSE_FILE` variable in your .env file:
```sh
COMPOSE_FILE="docker-compose.yml:docker-compose.keycloak.yml"
```

## Overview

Local development of OIDC + Keycloak is currently supported for the following
scenario:

- Running Georama backend (Django) from filesystem (not docker) at `localhost:4242`
- Running GeoGirafe frontend from filesystem (not docker) at `app.localhost:8080`

Other scenarios will require some config tweaks.

Currently, this requires GeoGirafe from our fork until exposing `oauth4webapi`'s
`allowInsecureRequests` in the GeoGirafe config has made it upstream.

Therefore, you need to use GeoGirafe from this branch for now:
https://gitlab.com/opengisch/gg-viewer/-/tree/oidc-allow-insecure-connections

## Starting the stack

- Boot the stack with `docker-compose up`
- Stop georama and geogirafe services with `docker-compose stop georama geogirafe`

## Testing authentication

Check that Keycloak is running:

 - Visit http://localhost:7080/ (incognito tab recommended)
 - Log in with the user `admin` and password `admin`
 - In the top left, select the "ninjas" instead of the "master" realm
 - Under users, there should be 1 user, `fred.flintstone`
 - Under clients, there should be a `georama-oidc` client
 - On that client is where you would configure additional allowed redirect URIs and CORS origins

### Backend

- Visit http://localhost:4242
- Attempt to log into the admin panel
- You should see an alternative option "Keycloak" at the bottom
- Click on it, you should be redirected to the Keycloak "Ninjas" Realm
- Log in with the user `fred.flintstone` and password `fred`
- You should be redirected back to Django, and see a message that you are logged in as `fred.flintstone`, but don't have access to the admin panel

### Frontend

First, copy over the `geogirafe/config.json` from the `georama` repo to your standalone GeoGirafe local development instance (or its `"oauth"` section at least).

- Visit https://app.localhost:8080
- Click "Login"
- You should be redirected to the Keycloak "Ninjas" Realm
- Log in with the user `fred.flintstone` and password `fred`
- You should be redirected back to GeoGirafe, and in the top right see your user
- If you refresh the page however, auth will break
- To work around that, set `"loginRequired": true` in the GeoGirafe `config.json`


## Local development HTTPS setup

The provided configuration should work as-is for local development, because
it sets `"allowInsecureRequests": true` in the GeoGirafe `config.json`. This
allows GeoGirafe's OIDC library to make requests to a non-HTTPS Keycloak server.

If you need to test authentication locally with HTTPS though, you'll need some
additional setup steps:

The Keycloak instance for local development already has HTTPS enabled, and comes
with pregenerated throwaway self-signed certificates. However, these certificates
need to be put into the trust store once (either system wide, or per browser)
for HTTPS to work.

Accepting the in-browser warning dialog exception is not sufficient, as
GeoGirafe will do XHRs from service workers, and those whitelisted exceptions
don't apply for those requests.

You therefore have to import the self-signed certificate into either your
system wide trust store, or your browser's trust store.

The certificates for local development are in the repo at `/keycloak/certs/`.
You will need to import and trust both the `keycloak.crt` and `rootCA.crt`
certificates.

After that, you should be able to switch the OIDC configuration to Keycloak's
HTTPS URL (`https://localhost:7443/`) in both Georama's `settings.py` and
GeoGirafe's `config.json`.