"""Route inventory and permission matrix: every route of Georama is in `ROUTES`, and every
route x method x persona answers the status declared there.
"""

import pytest

from tests.api.routes.declarations import ROUTES, expected
from tests.api.routing import application_routes, call
from tests.fixtures.personas import PERSONAS


def test_every_route_is_declared():
    missing = [
        f"{name} ({route.path}): {sorted(route.methods) if route.methods else 'to declare'}"
        for name, route in application_routes().items()
        if name not in ROUTES
    ]
    assert not missing, "Routes missing from ROUTES (unnamed ones need a name):\n" + "\n".join(
        missing
    )


def test_every_declared_route_exists():
    assert sorted(ROUTES.keys() - application_routes().keys()) == []


def test_declared_methods_are_the_methods_of_the_views():
    mismatches = {
        name: {"declared": sorted(ROUTES[name]), "view": sorted(route.methods)}
        for name, route in application_routes().items()
        if name in ROUTES and route.methods is not None and set(ROUTES[name]) != route.methods
    }
    assert not mismatches


def test_every_method_has_a_status_for_every_persona():
    incomplete = [
        f"{name} {method}"
        for name, methods in ROUTES.items()
        for method, statuses in methods.items()
        if statuses.keys() != set(PERSONAS)
    ]
    assert not incomplete


def matrix():
    """Yields a test case per route x method x persona, a strict xfail for the known bugs."""
    for name, methods in ROUTES.items():
        for method, statuses in methods.items():
            for persona, status in statuses.items():
                status, marks = expected(status)
                yield pytest.param(
                    name, method, persona, status, marks=marks, id=f"{name}-{method}-{persona}"
                )


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("name, method, persona, status", list(matrix()))
def test_status(api_data, name, method, persona, status):
    response = call(api_data.client(persona), name, method, api_data.kwargs(name))
    assert response.status_code == status
