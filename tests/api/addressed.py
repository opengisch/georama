"""The objects addressed by the routes, created once per test module."""

from contextlib import contextmanager

from django.contrib.auth.models import Group, Permission
from django.contrib.gis.geos import MultiPolygon, Polygon
from django.db import transaction
from django.db.models import Model
from django.test import override_settings

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
from georama.webgis.models import WmsLayer as WebGisWmsLayer
from tests.fixtures import reseed
from tests.fixtures.gis import Gis, create_project
from tests.fixtures.layers import (
    create_feature_layer,
    create_theme,
    create_webgis_wms_layer,
    create_wms_layer,
    with_geogirafe_json,
)


@contextmanager
def module_transaction(django_db_blocker, tmp_path_factory):
    """Creates the data of a module fixture in a transaction rolled back after the module.

    Each test runs in a savepoint of this transaction, like `TestCase.setUpTestData`: the
    writes of a request are rolled back after its test.
    """
    with (
        django_db_blocker.unblock(),
        override_settings(DATA_INTEGRATION_ROOT=tmp_path_factory.mktemp("projects")),
        transaction.atomic(),
    ):
        # module fixtures run before the autouse seeding fixture
        reseed()
        yield
        transaction.set_rollback(True)


def create_organisation(key: str) -> Organisation:
    """A non public organisation, whose domain is `key`."""
    return OrganisationFactory.create(name=key.capitalize(), domain=key, public_access=False)


def create_organisation_objects(
    organisation: Organisation | None, gis: Gis
) -> dict[type[Model], Model]:
    """Creates an object of each organisational model in `organisation` (None for the global
    one), not public. The Vector reads the table of `gis`.
    """
    name = organisation.domain if organisation else "global"
    project = create_project(organisation)
    vector = gis.create_vector(project)
    theme = with_geogirafe_json(create_theme(project, public=False))
    return {
        Fence: Fence.objects.create(
            name=f"Addressed {name}",
            organisation=organisation,
            geometry=MultiPolygon(Polygon(((0, 0), (0, 1), (1, 1), (0, 0)))),
        ),
        Membership: MembershipFactory.create(
            user=UserFactory.create(username=f"addressed-{name}", groups=[]),
            organisation=organisation,
        ),
        Project: project,
        Datasource: vector,
        Vector: vector,
        VectorField: vector.fields.first(),
        Raster: RasterFactory.create(project=project),
        Custom: CustomFactory.create(project=project),
        WmsLayer: create_wms_layer(vector, public=False, queryable=True),
        FeatureLayer: create_feature_layer(vector, public=False),
        Theme: theme,
        WebGisWmsLayer: create_webgis_wms_layer(vector, theme),
    }


def create_shared_objects() -> dict[type[Model], Model]:
    """Creates an object of each model shared by the organisations, except the users."""
    return {
        Group: GroupFactory.create(name="Addressed"),
        Permission: Permission.objects.get(codename="view_project"),
        Organisation: OrganisationFactory.create(),
    }


def create_addressed(gis: Gis) -> dict[type[Model], Model]:
    """Creates the objects addressed by the routes: the organisational ones in the global
    organisation, not public, and the others.
    """
    objects = create_organisation_objects(None, gis)
    return (
        objects
        | {GeoramaUser: objects[Membership].user}
        | create_shared_objects()
        | {UrlShortener: UrlShortener.objects.create(id="addressed", url="https://example.org")}
    )
