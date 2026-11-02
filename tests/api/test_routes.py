"""Route inventory and permission matrix: every route of Georama is in `ROUTES`, and every
route x method x persona answers the status declared there.
"""

from typing import NamedTuple

import pytest
from django.db.models import Model

from georama.core.models.user import GeoramaUser
from georama.features.models import FeatureLayer
from georama.integration.models import Vector
from georama.maps.models import WmsLayer
from georama.webgis.models import Theme
from tests.api.addressed import create_addressed, module_transaction
from tests.api.routes import ROUTES, expected
from tests.api.routing import application_routes, call, url_kwargs
from tests.fixtures.gis import Gis
from tests.fixtures.personas import PERSONAS, create_editor_group, create_persona, persona_client


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
        name: {"declared": sorted(ROUTES[name].methods), "view": sorted(route.methods)}
        for name, route in application_routes().items()
        if name in ROUTES
        and route.methods is not None
        and set(ROUTES[name].methods) != route.methods
    }
    assert not mismatches


def test_every_method_has_a_status_for_every_persona():
    incomplete = [
        f"{name} {method}"
        for name, declaration in ROUTES.items()
        for method, statuses in declaration.methods.items()
        if statuses.keys() != set(PERSONAS)
    ]
    assert not incomplete


def matrix():
    """Yields a test case per route x method x persona, a strict xfail for the known bugs."""
    for name, declaration in ROUTES.items():
        for method, statuses in declaration.methods.items():
            for persona, status in statuses.items():
                status, marks = expected(status)
                yield pytest.param(
                    name, method, persona, status, marks=marks, id=f"{name}-{method}-{persona}"
                )


class MatrixData(NamedTuple):
    # the object of each model addressed by the routes
    addressed: dict[type[Model], Model]
    users: dict[str, GeoramaUser | None]
    # id of a feature of the table of the addressed FeatureLayer
    feature_id: str


@pytest.fixture(scope="module")
def matrix_data(django_db_setup, django_db_blocker, tmp_path_factory, gis: Gis) -> MatrixData:
    with module_transaction(django_db_blocker, tmp_path_factory):
        addressed = create_addressed(gis)
        editor_group = create_editor_group()
        view_objects = [addressed[WmsLayer], addressed[Theme], addressed[FeatureLayer]]
        users = {
            name: create_persona(
                name, editor_group, objects=view_objects if name == "viewer" else ()
            )
            for name in PERSONAS
        }
        yield MatrixData(addressed, users, gis.first_feature_id(addressed[Vector]))


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("name, method, persona, status", matrix())
def test_status(matrix_data, name, method, persona, status):
    route = application_routes()[name]
    client = persona_client(matrix_data.users[persona])
    response = call(
        client, name, method, url_kwargs(route, matrix_data.addressed, matrix_data.feature_id)
    )
    assert response.status_code == status
