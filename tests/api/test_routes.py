"""Route inventory and permission matrix: every route of Georama is in `ROUTES`, and every
route x method x persona answers the status declared there.
"""

import random
from collections.abc import Callable
from functools import cache
from typing import NamedTuple

import factory.random
import psycopg
import pytest
from django.contrib.auth.models import Group, Permission
from django.contrib.gis.geos import MultiPolygon, Polygon
from django.db import transaction
from django.db.models import Model
from django.test import override_settings
from django.urls import URLResolver, get_resolver, reverse
from rest_framework.renderers import JSONRenderer

from georama.core.factories import GroupFactory, MembershipFactory, OrganisationFactory, UserFactory
from georama.core.models.fence import Fence
from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser
from georama.features.models import FeatureLayer
from georama.integration.factories import CustomFactory, RasterFactory
from georama.integration.models import Custom, Datasource, Project, Raster, Vector, VectorField
from georama.maps.models import WmsLayer
from georama.webgis.models import Theme, UrlShortener
from tests.api.routes import ROUTES, Bug
from tests.conftest import (
    PERSONAS,
    create_editor_group,
    create_global_project,
    create_persona,
    persona_client,
)
from tests.fixtures import SEED
from tests.fixtures.gis import GIS_SCHEMA, create_global_vector
from tests.fixtures.layers import (
    create_global_feature_layer,
    create_global_theme,
    create_global_wms_layer,
)

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
                marks = []
                if isinstance(status, Bug):
                    marks.append(pytest.mark.xfail(strict=True, reason=status.reason))
                    status = status.status
                yield pytest.param(
                    name, method, persona, status, marks=marks, id=f"{name}-{method}-{persona}"
                )


class MatrixData(NamedTuple):
    # the object of each model addressed by the routes
    addressed: dict[type[Model], Model]
    users: dict[str, GeoramaUser | None]
    # id of a feature of the table of the addressed FeatureLayer
    feature_id: str


def create_addressed(gis_dataset, gis_db_settings, gis_faker) -> dict[type[Model], Model]:
    """Creates the objects addressed by the routes, of the global organisation, not public."""
    project = create_global_project()
    vector = create_global_vector(project, gis_dataset, gis_db_settings, gis_faker)
    user = UserFactory.create(username="addressed", groups=[])
    return {
        GeoramaUser: user,
        Group: GroupFactory.create(name="Addressed"),
        Permission: Permission.objects.get(codename="view_project"),
        Organisation: OrganisationFactory.create(),
        Fence: Fence.objects.create(
            name="Addressed", geometry=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0))))
        ),
        Membership: MembershipFactory.create(user=user, organisation=None),
        Project: project,
        Datasource: vector,
        Vector: vector,
        VectorField: vector.fields.first(),
        Raster: RasterFactory.create(project=project),
        Custom: CustomFactory.create(project=project),
        WmsLayer: create_global_wms_layer(vector, public=False, queryable=True),
        FeatureLayer: create_global_feature_layer(vector, public=False),
        Theme: create_global_theme(project, public=False),
        UrlShortener: UrlShortener.objects.create(id="addressed", url="https://example.org"),
    }


@pytest.fixture(scope="module")
def matrix_data(
    django_db_setup, django_db_blocker, tmp_path_factory, gis_dataset, gis_db_settings, gis_faker
) -> MatrixData:
    """The data of the matrix, created once in a transaction rolled back after the module.

    Each test runs in a savepoint of this transaction, like `TestCase.setUpTestData`: the
    writes of a route are rolled back after its test.
    """
    with (
        django_db_blocker.unblock(),
        override_settings(DATA_INTEGRATION_ROOT=tmp_path_factory.mktemp("projects")),
        transaction.atomic(),
    ):
        # module fixtures run before the autouse seeding fixture
        random.seed(SEED)
        factory.random.reseed_random(SEED)
        addressed = create_addressed(gis_dataset, gis_db_settings, gis_faker)
        editor_group = create_editor_group()
        view_objects = [addressed[WmsLayer], addressed[Theme], addressed[FeatureLayer]]
        users = {
            name: create_persona(
                name, editor_group, objects=view_objects if name == "viewer" else ()
            )
            for name in PERSONAS
        }
        table = addressed[Vector].source["postgres"]["table"]
        with psycopg.connect(**gis_db_settings) as conn:
            feature_id = conn.execute(f"SELECT id FROM {GIS_SCHEMA}.{table} LIMIT 1").fetchone()[0]
        yield MatrixData(addressed, users, str(feature_id))
        transaction.set_rollback(True)


@pytest.fixture
def backends(monkeypatch, posted_jobs, render_job_result):
    """QSL renders, and the item writes of pygeoapi answer without touching the shared table."""
    posted_jobs.answer = render_job_result
    monkeypatch.setattr(
        "pygeoapi.api.itemtypes.manage_collection_item",
        lambda *args, **kwargs: ({}, 200, "application/json"),
    )


def url_kwargs(route: Route, data: MatrixData) -> dict[str, str]:
    values = {
        "lang": "en",
        "collection_id": data.addressed[FeatureLayer].identifier,
        "item_id": data.feature_id,
    }
    if "pk" in route.params:
        values["pk"] = data.addressed[route.view.cls.queryset.model].pk
    return {param: values[param] for param in route.params}


def accept_json(view) -> bool:
    """The DRF views able to answer JSON are asked for it, the others answer their only format."""
    renderers = getattr(view, "initkwargs", {}).get(
        "renderer_classes", getattr(getattr(view, "cls", None), "renderer_classes", [])
    )
    return any(issubclass(renderer, JSONRenderer) for renderer in renderers)


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("name, method, persona, status", matrix())
def test_status(matrix_data, name, method, persona, status):
    route = application_routes()[name]
    client = persona_client(matrix_data.users[persona])
    url = reverse(name, kwargs=url_kwargs(route, matrix_data))
    headers = {"HTTP_ACCEPT": "application/json"} if accept_json(route.view) else {}
    if method == "get":
        response = client.get(url, **headers)
    else:
        response = getattr(client, method)(url, {}, format="json", **headers)
    assert response.status_code == status
