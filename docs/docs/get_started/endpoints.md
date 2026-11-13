---
icon: lucide/link
---

# User Endpoints

Georama publishes its content through three endpoints. The URLs below use the local
development stack on `http://localhost:4242`.

| Endpoint     | Service                   | URL                                      | Trailing slash |
| ------------ | ------------------------- | ---------------------------------------- | -------------- |
| Maps         | WMS 1.3.0                 | <http://localhost:4242/maps/ows>         | **optional**   |
| WebGIS       | WMS 1.3.0 (for GeoGirafe) | <http://localhost:4242/webgis/ows>       | **optional**   |
| Features     | OGC API - Features        | <http://localhost:4242/features/api>     | **none**       |

!!! warning "Trailing slash"

    `APPEND_SLASH` is disabled, Georama does not redirect between both forms. A URL with
    the wrong trailing slash answers with `404`. This also applies to the paths below
    `features/api`, e.g. `features/api/collections/<collection_id>/items`.

Requests to `<org>.localhost:4242` are served for the organisation `<org>`, see
[Environment Variables](environment.md#georama).

## Health

<http://localhost:4242/health/> tells whether Georama, its database, the QSL queue and
at least one QSL worker are up. It needs no login and works on every organisation
subdomain. It answers `200` when everything is up and `503` otherwise, as JSON
(`?f=json`, the default) or as an HTML page (`?f=html`). The alive workers are listed
with their id and the time of their last heartbeat, nothing more.
