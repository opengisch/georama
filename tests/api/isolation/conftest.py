"""The data of the isolation tests.

The organisational objects addressed by the routes are created three times: in the global
organisation and in the non public organisations alpha and beta.
"""

from typing import NamedTuple

import pytest
from django.db.models import Model
from rest_framework.test import APIClient

from georama.core.factories import OrganisationFactory
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser
from georama.integration.models import Vector
from tests.api.addressed import create_organisation_objects, first_feature_id, module_transaction
from tests.api.routing import application_routes, url_kwargs
from tests.conftest import create_editor_group, create_persona, persona_client

GLOBAL, ALPHA, BETA = "global", "alpha", "beta"
# host and the organisation of an object the host must not reach
FOREIGN = [(ALPHA, BETA), (ALPHA, GLOBAL), (GLOBAL, ALPHA)]
HOSTS = [GLOBAL, ALPHA]


class IsolationData(NamedTuple):
    organisations: dict[str, Organisation | None]
    # the organisational objects of each organisation
    objects: dict[str, dict[type[Model], Model]]
    superuser: GeoramaUser
    # member of beta only
    member: GeoramaUser
    # id of a feature of the table shared by the Vectors
    feature_id: str

    def client(self, host: str) -> APIClient:
        """A client of the superuser on `host`, answering the server errors as a response."""
        client = persona_client(self.superuser, self.organisations[host])
        client.raise_request_exception = False
        return client

    def kwargs(self, name: str, owner: str) -> dict:
        """The URL parameters of the route `name` addressing the objects of `owner`."""
        return url_kwargs(application_routes()[name], self.objects[owner], self.feature_id)

    def others(self, model: type[Model], key: str) -> set[str]:
        """The ids of the objects of `model` in the organisations other than `key`."""
        return {str(objects[model].pk) for other, objects in self.objects.items() if other != key}


@pytest.fixture(scope="module")
def isolation_data(
    django_db_setup, django_db_blocker, tmp_path_factory, gis_dataset, gis_db_settings, gis_faker
) -> IsolationData:
    with module_transaction(django_db_blocker, tmp_path_factory):
        organisations = {
            GLOBAL: None,
            **{
                key: OrganisationFactory.create(
                    name=key.capitalize(), domain=key, public_access=False
                )
                for key in (ALPHA, BETA)
            },
        }
        objects = {
            key: create_organisation_objects(organisation, gis_dataset, gis_db_settings, gis_faker)
            for key, organisation in organisations.items()
        }
        editor_group = create_editor_group()
        yield IsolationData(
            organisations,
            objects,
            create_persona("superuser", editor_group),
            create_persona("member", editor_group, organisations[BETA]),
            first_feature_id(objects[GLOBAL][Vector], gis_db_settings),
        )
