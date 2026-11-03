"""The data shared by the API tests, created once per test module by the `api_data` fixture.

Three organisations: the global one, and the non public alpha and beta. Each holds a non public
object of each organisational model. The personas are members of the global organisation, the
viewer has the view permission on its layers and themes.

The tests only read this data: what a request writes is rolled back after its test.
"""

from contextlib import contextmanager
from typing import NamedTuple

from django.contrib.auth.models import Group, Permission
from django.contrib.gis.geos import MultiPolygon, Polygon
from django.db import transaction
from django.db.models import Model
from django.test import override_settings
from rest_framework.test import APIClient

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
from tests.api.routing import application_routes, url_kwargs
from tests.fixtures import reseed
from tests.fixtures.gis import Gis, create_project
from tests.fixtures.layers import (
    create_feature_layer,
    create_theme,
    create_webgis_wms_layer,
    create_wms_layer,
    with_geogirafe_json,
)
from tests.fixtures.personas import PERSONAS, create_editor_group, create_persona, persona_client

GLOBAL, ALPHA, BETA = "global", "alpha", "beta"


class ApiData(NamedTuple):
    # by key: GLOBAL (None), ALPHA, BETA
    organisations: dict[str, Organisation | None]
    # the organisational objects of each organisation
    objects: dict[str, dict[type[Model], Model]]
    # an object of each model shared by the organisations
    shared: dict[type[Model], Model]
    # the user of each persona, member of the global organisation
    personas: dict[str, GeoramaUser | None]
    # member of beta only
    beta_member: GeoramaUser
    # member of no organisation
    newcomer: GeoramaUser
    # id of a feature of the table read by the Vectors
    feature_id: str

    def addressed(self, key: str) -> dict[type[Model], Model]:
        """The object of each model addressed from the host of `key`: its organisational
        objects and the shared ones.
        """
        return self.objects[key] | self.shared

    def client(
        self, persona: str = "superuser", host: str = GLOBAL, raise_request_exception: bool = True
    ) -> APIClient:
        """A client of `persona` on the host of the organisation `host`. Without
        `raise_request_exception`, a server error is answered as a 500 response.
        """
        client = persona_client(self.personas[persona], self.organisations[host])
        client.raise_request_exception = raise_request_exception
        return client

    def kwargs(self, name: str, owner: str = GLOBAL) -> dict:
        """The URL parameters of the route `name` addressing the objects of `owner`."""
        return url_kwargs(application_routes()[name], self.addressed(owner), self.feature_id)

    def others(self, model: type[Model], key: str) -> set[str]:
        """The ids of the objects of `model` in the organisations other than `key`."""
        return {str(objects[model].pk) for other, objects in self.objects.items() if other != key}


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
    name = organisation.domain if organisation else GLOBAL
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
    """Creates an object of each model shared by the organisations."""
    return {
        GeoramaUser: UserFactory.create(username="addressed", groups=[]),
        Group: GroupFactory.create(name="Addressed"),
        Permission: Permission.objects.get(codename="view_project"),
        Organisation: OrganisationFactory.create(),
        UrlShortener: UrlShortener.objects.create(id="addressed", url="https://example.org"),
    }


def create_api_data(gis: Gis) -> ApiData:
    organisations = {GLOBAL: None, **{key: create_organisation(key) for key in (ALPHA, BETA)}}
    objects = {
        key: create_organisation_objects(organisation, gis)
        for key, organisation in organisations.items()
    }
    editor_group = create_editor_group()
    viewed = [objects[GLOBAL][model] for model in (WmsLayer, Theme, FeatureLayer)]
    return ApiData(
        organisations=organisations,
        objects=objects,
        shared=create_shared_objects(),
        personas={
            name: create_persona(name, editor_group, objects=viewed if name == "viewer" else ())
            for name in PERSONAS
        },
        beta_member=create_persona("member", editor_group, organisations[BETA]),
        newcomer=UserFactory.create(username="newcomer", groups=[]),
        feature_id=gis.first_feature_id(objects[GLOBAL][Vector]),
    )
