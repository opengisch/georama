---
icon: lucide/link
---

# User Endpoints

Georama publishes its content through four endpoints. The URLs below use the local
development stack on `http://localhost:4242`.

| Endpoint | Service                            | URL                                  | Trailing slash |
|----------|------------------------------------|--------------------------------------|----------------|
| Maps     | WMS 1.3.0                          | <http://localhost:4242/maps/ows>     | **optional**   |
| WebGIS   | WMS 1.3.0 (for GeoGirafe)          | <http://localhost:4242/webgis/ows>   | **optional**   |
| Features | OGC API - Features                 | <http://localhost:4242/features/api> | **none**       |
| WebGIS   | OGC API - Features (for GeoGirafe) | <http://localhost:4242/webgis/api>   | **none**       |

!!! warning "Trailing slash"

    `APPEND_SLASH` is disabled, Georama does not redirect between both forms. A URL with
    the wrong trailing slash answers with `404`. This also applies to the paths below
    `features/api` and `webgis/api`, e.g. `features/api/collections/<collection_id>/items`.

## WebGIS OGC API - Features

GeoGirafe edits the features of a theme through `webgis/api`. Every layer of a theme
which is based on a vector datasource is a collection there, including datasources
without geometry, which are used as lookup tables. Raster layers are not.

The collection id is the name GeoGirafe knows the layer by from the WMS and WFS of the
WebGIS, the layer identifier prefixed with an underscore (`_<layer id>`). The plain
layer identifier is accepted as well.

Reading follows the view permission of the theme, like the WMS does. Writing needs the
create, update or delete permission on the theme. A public theme can be read by
everybody, but it never allows anybody to write (same as for features endpoints).

Requests to `<org>.localhost:4242` are served for the organisation `<org>`, see
[Environment Variables](environment.md#georama).

## Health

<http://localhost:4242/health/> tells whether Georama, its database, the QSL queue and
at least one QSL worker are up. It needs no login and works on every organisation
subdomain. It answers `200` when everything is up and `503` otherwise, as JSON
(`?f=json`, the default) or as an HTML page (`?f=html`). The alive workers are listed
with their id and the time of their last heartbeat, nothing more.
