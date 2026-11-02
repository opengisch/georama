"""The routes of Georama as resolved by Django, and the requests made to them by the tests."""

from collections.abc import Callable
from functools import cache
from typing import NamedTuple

from django.db.models import Model
from django.http import HttpResponse
from django.urls import URLResolver, get_resolver, reverse
from rest_framework.renderers import JSONRenderer
from rest_framework.test import APIClient

from georama.core.common.managers import OrganisationalManager
from georama.features.models import FeatureLayer

# routes of third party apps, not tested here
EXCLUDED_PREFIXES = ("admin/", "accounts/", "silk/")
# answered by every view
IMPLICIT_METHODS = {"head", "options"}


class Route(NamedTuple):
    path: str
    view: Callable
    # None when the view dispatches requests itself
    methods: set[str] | None
    params: set[str]


def walk(patterns, prefix="", namespace=None, params=frozenset()):
    """Yields the path, namespaced name, view and URL parameters of each route."""
    for pattern in patterns:
        path = prefix + str(pattern.pattern)
        route_params = params | set(pattern.pattern.regex.groupindex)
        if isinstance(pattern, URLResolver):
            yield from walk(
                pattern.url_patterns,
                path,
                ":".join(filter(None, [namespace, pattern.namespace])) or None,
                route_params,
            )
        else:
            name = pattern.name and ":".join(filter(None, [namespace, pattern.name]))
            yield path, name, pattern.callback, route_params


def view_methods(callback) -> set[str] | None:
    """Returns the methods a view answers, None when it dispatches requests itself."""
    view = getattr(callback, "cls", None) or callback.view_class
    allowed = set(view.http_method_names) - IMPLICIT_METHODS
    actions = getattr(callback, "actions", None)
    if actions is not None:
        # a viewset maps the methods to its actions, `http_method_names` can disable some
        return set(actions) & allowed
    return {method for method in allowed if hasattr(view, method)} or None


@cache
def application_routes() -> dict[str, Route]:
    """Returns the routes by name, unnamed routes under their path."""
    routes = {}
    for path, name, callback, params in walk(get_resolver().url_patterns):
        if not path.startswith(EXCLUDED_PREFIXES):
            # the variants with a format suffix come after their route, and share its methods
            routes.setdefault(
                name or path, Route(path, callback, view_methods(callback), params - {"format"})
            )
    return routes


def route_model(route: Route) -> type[Model] | None:
    """The model of the objects a route addresses, None for the views without queryset."""
    if "collection_id" in route.params:
        return FeatureLayer
    queryset = getattr(getattr(route.view, "cls", None), "queryset", None)
    return None if queryset is None else queryset.model


def is_organisational(model: type[Model] | None) -> bool:
    return isinstance(getattr(model, "objects", None), OrganisationalManager) and hasattr(
        model, "ORGANISATION_FIELD_NAME"
    )


def url_kwargs(route: Route, addressed: dict[type[Model], Model], feature_id: str) -> dict:
    """The URL parameters of `route` addressing the objects of `addressed`."""
    values = {
        "lang": "en",
        "collection_id": addressed[FeatureLayer].identifier,
        "item_id": feature_id,
    }
    if "pk" in route.params:
        values["pk"] = addressed[route_model(route)].pk
    return {param: values[param] for param in route.params}


def accept_json(view) -> bool:
    """The DRF views able to answer JSON are asked for it, the others answer their only format."""
    renderers = getattr(view, "initkwargs", {}).get(
        "renderer_classes", getattr(getattr(view, "cls", None), "renderer_classes", [])
    )
    return any(issubclass(renderer, JSONRenderer) for renderer in renderers)


def call(
    client: APIClient,
    name: str,
    method: str,
    kwargs: dict,
    payload: dict | None = None,
    query: dict | None = None,
) -> HttpResponse:
    """Requests the route `name`, in JSON when it answers JSON. The writes send `payload` in
    JSON, empty by default.
    """
    route = application_routes()[name]
    url = reverse(name, kwargs=kwargs)
    headers = {"HTTP_ACCEPT": "application/json"} if accept_json(route.view) else {}
    if method == "get":
        return client.get(url, query, **headers)
    return getattr(client, method)(url, payload or {}, format="json", **headers)
