# API tests

Most of the API tests are driven by declarations: a test module reads a table of routes and
generates one test case per route, method and persona. Consistency tests fail as soon as a
route of Django is missing from these tables, so they guide you through what to declare.

## Test groups

| Folder            | What it checks                                                                                       |
|-------------------|------------------------------------------------------------------------------------------------------|
| `routes/`         | Every route is declared, and each route x method x persona answers its declared status             |
| `isolation/`      | From the host of an organisation, a route reaches only its objects, and the middleware guards it    |
| `crud/`           | Real payloads written by the superuser reach the database as expected                               |
| `public_content/` | The public listings show the public objects, and the permitted ones to the viewer                   |
| `core/`, `webgis/`, `integration/` | Hand-written tests of a specific behaviour                                         |

## Structure

```
api/
  conftest.py       fixtures `api_data` (the shared data, see data.py) and `backends` (QSL, pygeoapi)
  data.py           the shared data: organisations global, alpha and beta, their objects, the personas
  routing.py        reads the URL configuration of Django, and makes the requests (`call`)
  <group>/
    declarations.py the data of the group: what to expect, payloads, checks
    test_<group>.py the tests, and the generation of their cases
```

`routes/declarations.py` (`ROUTES`) is the reference: the other groups reuse its statuses and its
known bugs (`Bug`) and domain rules (`Rule`), which are strict xfails.

## Adding a route

1. Run `pytest tests/api`: `test_every_route_is_declared` lists the route with its methods.
2. Declare the status of each persona per method in `routes/declarations.py`. A status that
   is wrong today is declared as `Bug(expected, reason)` or `Rule(expected, reason)`. A new
   URL parameter (other than `pk`, `lang`, `collection_id`, `item_id`) needs its value in
   `url_kwargs` (`routing.py`).
3. If `test_every_route_has_an_isolation` fails, declare how to check it in `ISOLATION`
   (`isolation/declarations.py`). Viewsets on an organisational model need nothing.
4. If the route writes (create, PATCH, form update), `test_every_write_has_a_payload` asks for
   its payload in `crud/declarations.py`.
5. If the route lists public objects, add it to `ENDPOINTS` in `public_content/declarations.py`.
6. A behaviour specific to the route goes in a hand-written test in `<app>/test_*.py`, using
   `client_as` or `api_data.client()`, and the objects of `api_data` when it only reads them.

## Adding a Django app

1. Declare its routes as above, in a `# <app>` section of `ROUTES`.
2. If editors manage its models, add its label to `EDITOR_APPS` (`tests/fixtures/personas.py`).
3. If its models are organisational, add an object of each to `create_organisation_objects`
   (`data.py`), else to `create_shared_objects`: the routes with a `pk` address these objects.
4. If its objects carry a view permission, add it to `VIEW_PERMISSIONS`
   (`tests/fixtures/personas.py`) and give it to the viewer in `create_api_data` (`data.py`).
5. Put its hand-written tests in a new `api/<app>/` folder.

## Data in tests

A fixture provides infrastructure (`gis`, `posted_jobs`, `client_as`) or the shared data
(`api_data`). An object specific to a test is created in the test, with the `create_*`
functions of `tests/fixtures/layers.py` or the factories.
