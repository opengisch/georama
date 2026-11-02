"""How the isolation of the organisations is checked on a route x method.

For each route, `test_isolation.py` must know how to check that the route does not reach the
objects of another organisation. The check depends on what the route does: it addresses an
object by its URL, lists objects, references an object in its payload...

Most routes are viewsets on an organisational model: their check is deduced from their URL
parameters and their actions (`Object`, `Listing`, `Creation`, `Form`, and `Global` for the
viewsets on a model shared by the organisations). Nothing is declared for them.

The other routes say nothing of what they reach: a view without queryset, an object referenced
by the payload, an OGC service. `test_every_route_has_an_isolation` fails on them until their
check is declared in `ROUTES` through `isolation=`, with one of the classes below:

    "core:index": route(Global("the home page"), get=allow(EVERYONE, 200)),

Whatever its check, every route is also guarded by the middleware, see
`test_middleware_guards_every_route`.
"""

from collections.abc import Callable
from typing import NamedTuple

from django.db.models import Model

from tests.api.routing import application_routes, is_organisational, route_model

# the checks declared in `ROUTES` through `isolation=`; `deduce` also returns `Global` and
# `Listing` for the viewsets, without declaration


class Global(NamedTuple):
    """The route reaches no organisational object: nothing can leak, nothing is checked.

    Examples: the home page (`core:index`), the authentication (`core:login`), the description
    of the API (`core:swagger`, `features:api-root`).

    `test_global_routes_address_no_organisational_model` checks that the view of the route
    has no organisational queryset.
    """

    # why the route reaches no organisational object
    reason: str


class Unchecked(NamedTuple):
    """The route reaches organisational objects, but cannot be checked by these tests.

    Example: `integration:manager-project-non-integrated` lists the files of the folder of the
    organisation, which are not objects of the database.

    Nothing is checked: the reason records the gap in the coverage.
    """

    # why the route cannot be checked
    reason: str


class Listing(NamedTuple):
    """The route answers a list of organisational objects of `model`.

    Example: `features:api-collections`, the collections of the OGC API, which are the
    FeatureLayers. Its view has no queryset: the model tells which objects to look for.

    Checked by `test_listing_holds_the_objects_of_its_organisation_only`: from the global
    organisation and from alpha, the answer holds the UUID of the object of the host, and none
    of the UUIDs of the objects of the other organisations.

    Deduced for a GET without `pk` on an organisational viewset (`maps:maplayer-list`,
    `webgis:theme-geogirafe`).
    """

    model: type[Model]


class Payload(NamedTuple):
    """The route writes on an organisational object referenced in its payload, not its URL.

    Example: `webgis:theme-manager-publish-from-project` posts `{"pk": <project id>}` and
    creates the themes of the project:

        Payload(
            Project,
            lambda project: {"pk": project.pk},
            lambda project: project.themes.count(),
        )

    Checked by `test_payload_reaches_the_objects_of_its_organisation_only`: from alpha, the
    payload references the object of another organisation, then of alpha. The status is not
    reliable, the requests on another organisation fail in many ways: the test measures the
    `effect` before and after the request, it changes on the object of alpha only.
    """

    # the model of the object referenced
    model: type[Model]
    # the payload referencing the object
    data: Callable[[Model], dict]
    # what the request changes on the object it references
    effect: Callable[[Model], object]


class Ogc(NamedTuple):
    """The route is an OGC service (WMS, WFS): one URL, the layers are named in its parameters
    (`?REQUEST=GetMap&LAYERS=<layer id>`).

    Examples: `maps:maps_ogc_entry` serves the maps WmsLayers, `webgis:ows_entry` the webgis
    ones.

    Checked through the operations of the service:

    - `test_capabilities_hold_the_layers_of_their_organisation_only`: the GetCapabilities
      list the layers of the organisation of the host only;
    - `test_layer_is_reached_from_its_organisation_only`: GetMap, GetFeature... on the layer
      of another organisation do not reach it.
    """

    # the model of the layers served
    model: type[Model]


# only deduced by `deduce`, never declared in routes


class Object(NamedTuple):
    """The route addresses an object by its URL: a `pk` or a `collection_id`.

    Examples: `integration:manager-project-detail`, `features:api-collection-items`.

    Checked by `test_object_is_reached_from_its_organisation_only`: from another
    organisation, the route answers 404; from the organisation of the object, the status of
    the superuser in the matrix.
    """


class Creation(NamedTuple):
    """The route creates an object: a `create` action.

    Example: POST on `integration:manager-project-list`.

    Checked by the CRUD tests, which check the organisation of the object created.
    """


class Form(NamedTuple):
    """The route answers the empty form creating an object: an `aadd` action.

    Example: `integration:manager-project-aadd`.

    The form reads no object: nothing is checked.
    """


Isolation = Global | Unchecked | Listing | Payload | Ogc | Object | Creation | Form


def deduce(name: str, method: str) -> Isolation | None:
    """The check of a route x method deduced from its viewset, None when it says nothing."""
    route = application_routes()[name]
    model = route_model(route)
    if model is None:
        # a view without queryset says nothing of what it reaches
        return None
    if not is_organisational(model):
        return Global("a viewset on a model shared by the organisations")
    actions = getattr(route.view, "actions", {})
    if route.params & {"pk", "collection_id"}:
        return Object()
    if actions.get(method) == "aadd":
        return Form()
    if method == "get":
        return Listing(model)
    if actions.get(method) in ("create", "acreate"):
        return Creation()
    return None
