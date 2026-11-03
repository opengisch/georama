"""Isolation of the organisations: from the host of an organisation, the routes reach only its
objects, and the middleware keeps the non members out of a non public organisation.

The superuser makes the requests: it passes the middleware and every permission check, the
organisational filter is the only thing left between it and the objects of the other
organisations. The data is `api_data`, see `tests/api/data.py`. The check of each route is
deduced from its viewset, or declared in `ISOLATION`, see `declarations.py`.
"""

import pytest
from django.conf import settings
from django.urls import reverse
from rest_framework.test import APIClient

from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation
from tests.api.data import ALPHA, ApiData
from tests.api.isolation.declarations import (
    CAPABILITIES,
    FOREIGN,
    GUARDS,
    HOSTS,
    ISOLATION,
    LAYER_REQUESTS,
    UNGUARDED,
    Creation,
    Form,
    Global,
    Isolation,
    Listing,
    Object,
    Ogc,
    Payload,
    layer_request,
)
from tests.api.routes.declarations import ROUTES, expected
from tests.api.routing import application_routes, call, is_organisational, route_model
from tests.fixtures.personas import persona_client


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


def isolation(name: str, method: str) -> Isolation | None:
    """How the isolation of a route x method is checked: declared in `ISOLATION`, else deduced
    from the viewset. None when it is neither.
    """
    return ISOLATION[name] if name in ISOLATION else deduce(name, method)


def routes_of(kind: type) -> list[tuple[str, str, Isolation]]:
    """The name, method and isolation of each route x method whose isolation is a `kind`."""
    return [
        (name, method, check)
        for name, methods in ROUTES.items()
        for method in methods
        if isinstance(check := isolation(name, method), kind)
    ]


def client(api_data: ApiData, host: str) -> APIClient:
    """A client of the superuser on `host`, answering the server errors as a response."""
    return api_data.client("superuser", host, raise_request_exception=False)


def test_every_route_has_an_isolation():
    """A route listed here declares its check in `ISOLATION`, see `declarations.py`."""
    assert [
        f"{name} {method}"
        for name, methods in ROUTES.items()
        for method in methods
        if isolation(name, method) is None
    ] == []


def test_every_declared_isolation_is_a_route():
    assert sorted(ISOLATION.keys() - ROUTES.keys()) == []


def test_global_routes_address_no_organisational_model():
    assert [
        name
        for name, check in ISOLATION.items()
        if isinstance(check, Global) and is_organisational(route_model(application_routes()[name]))
    ] == []


def object_cases():
    for name, method, _ in routes_of(Object):
        for host, owner in FOREIGN:
            yield pytest.param(
                name, method, host, owner, 404, id=f"{name}-{method}-{host}-on-{owner}"
            )
        # the object of the organisation of the host is reached
        status, marks = expected(ROUTES[name][method]["superuser"])
        yield pytest.param(
            name,
            method,
            ALPHA,
            ALPHA,
            status,
            marks=marks,
            id=f"{name}-{method}-{ALPHA}-on-{ALPHA}",
        )


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("name, method, host, owner, status", list(object_cases()))
def test_object_is_reached_from_its_organisation_only(api_data, name, method, host, owner, status):
    response = call(client(api_data, host), name, method, api_data.kwargs(name, owner))
    assert response.status_code == status


def listing_cases():
    for name, method, listing in routes_of(Listing):
        for host in HOSTS:
            _, marks = expected(ROUTES[name][method]["superuser"])
            yield pytest.param(name, listing.model, host, marks=marks, id=f"{name}-{host}")


@pytest.mark.django_db
@pytest.mark.parametrize("name, model, host", list(listing_cases()))
def test_listing_holds_the_objects_of_its_organisation_only(api_data, name, model, host):
    """The ids of the organisational objects are UUIDs: searched in the answer, whatever its
    format.
    """
    response = call(
        client(api_data, host),
        name,
        "get",
        api_data.kwargs(name, host),
        # every object on one page, the JSON of the OGC API
        query={"limit": 100, "f": "json"},
    )
    assert response.status_code == 200
    content = response.content.decode()
    assert str(api_data.objects[host][model].pk) in content
    assert [pk for pk in api_data.others(model, host) if pk in content] == []


def payload_cases():
    for name, _, payload in routes_of(Payload):
        for host, owner in [*FOREIGN, (ALPHA, ALPHA)]:
            yield pytest.param(name, payload, host, owner, id=f"{name}-{host}-on-{owner}")


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("name, payload, host, owner", list(payload_cases()))
def test_payload_reaches_the_objects_of_its_organisation_only(api_data, name, payload, host, owner):
    """The status is not checked: the requests on another organisation fail in many ways."""
    target = api_data.objects[owner][payload.model]
    before = payload.effect(target)
    call(client(api_data, host), name, "post", {}, payload.data(target))
    assert (payload.effect(target) != before) == (host == owner)


@pytest.mark.django_db
@pytest.mark.parametrize("host", HOSTS)
def test_users_are_not_filtered_by_organisation(api_data, host):
    client_ = client(api_data, host)
    users = {key: objects[Membership].user for key, objects in api_data.objects.items()}
    content = call(client_, "core:georamauser-list", "get", {}, query={"limit": 100}).content
    assert [user for user in users.values() if str(user.pk) not in content.decode()] == []
    for user in users.values():
        assert call(client_, "core:georamauser-detail", "get", {"pk": user.pk}).status_code == 200


def test_every_unguarded_route_is_a_route():
    assert sorted(UNGUARDED.keys() - ROUTES.keys()) == []


def middleware_cases():
    for name, methods in ROUTES.items():
        if name not in UNGUARDED:
            for method in methods:
                for guard in GUARDS:
                    yield pytest.param(name, method, guard, id=f"{name}-{method}-{guard}")


@pytest.mark.django_db
@pytest.mark.parametrize("name, method, guard", list(middleware_cases()))
def test_middleware_guards_every_route(api_data, name, method, guard):
    """The middleware answers before the view: the URL parameters address no object."""
    guard = GUARDS[guard]
    organisation = api_data.organisations.get(guard.host) or Organisation(domain=guard.host)
    client_ = persona_client(api_data.beta_member if guard.member else None, organisation)
    kwargs = {param: "0" for param in application_routes()[name].params}
    response = call(client_, name, method, kwargs)
    assert response.status_code == guard.status
    if guard.status == 302:
        assert response.url == reverse(settings.ORGANISATION_NOT_AUTHENTICATED_TARGET)
    else:
        assert response.content.decode() == str(guard.body)


# the OGC services, with the model of their layers
OGC = {name: check.model for name, check in ISOLATION.items() if isinstance(check, Ogc)}


@pytest.mark.django_db
@pytest.mark.parametrize("host", HOSTS)
@pytest.mark.parametrize("service", CAPABILITIES)
@pytest.mark.parametrize("name", OGC)
def test_capabilities_hold_the_layers_of_their_organisation_only(api_data, name, service, host):
    content = client(api_data, host).get(reverse(name), CAPABILITIES[service]).content
    layers = {
        key: objects[OGC[name]].identifier.encode() for key, objects in api_data.objects.items()
    }
    assert layers.pop(host) in content
    assert [layer for layer in layers.values() if layer in content] == []


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("host, owner", [*FOREIGN, (ALPHA, ALPHA)])
@pytest.mark.parametrize("operation", LAYER_REQUESTS)
@pytest.mark.parametrize("name", OGC)
def test_layer_is_reached_from_its_organisation_only(
    api_data, posted_jobs, name, operation, host, owner
):
    """The status is not checked: the requests on another organisation fail in many ways."""
    layer = api_data.objects[owner][OGC[name]]
    response = client(api_data, host).get(reverse(name), layer_request(operation, layer))
    rendered = LAYER_REQUESTS[operation].rendered
    reached = bool(posted_jobs) if rendered else response.status_code == 200
    assert reached == (host == owner)
