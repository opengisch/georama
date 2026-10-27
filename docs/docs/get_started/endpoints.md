---
icon: lucide/link
---

# User Endpoints

Georama publishes its content through three endpoints. The URLs below use the local
development stack on `http://localhost:4242`.

| Endpoint     | Service                   | URL                                      | Trailing slash |
| ------------ | ------------------------- | ---------------------------------------- | -------------- |
| Maps         | WMS 1.3.0                 | <http://localhost:4242/maps/ows/>        | **required**   |
| WebGIS       | WMS 1.3.0 (for GeoGirafe) | <http://localhost:4242/webgis/ows/>      | **required**   |
| Features     | OGC API - Features        | <http://localhost:4242/features/api>     | **none**       |

!!! warning "Trailing slash"

    `APPEND_SLASH` is disabled, Georama does not redirect between both forms. A URL with
    the wrong trailing slash answers with `404`. This also applies to the paths below
    `features/api`, e.g. `features/api/collections/<collection_id>/items`.

Requests to `<org>.localhost:4242` are served for the organisation `<org>`, see
[Environment Variables](environment.md#georama).
