"""The data of the CRUD tests.

The organisational objects addressed by the routes are created in the non public organisation
alpha, the host of the requests. Beta holds a user outside of alpha.
"""

from typing import NamedTuple

import pytest
from django.contrib.auth.models import Group
from django.db.models import Model
from rest_framework.test import APIClient

from georama.core.factories import GroupFactory, UserFactory
from georama.core.models.membership import Membership
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser
from tests.api.addressed import (
    create_organisation,
    create_organisation_objects,
    create_shared_objects,
    module_transaction,
)
from tests.fixtures.gis import Gis
from tests.fixtures.personas import create_editor_group, create_persona, persona_client


class CrudData(NamedTuple):
    organisation: Organisation
    # the organisational objects of alpha, and an object of each model shared by the
    # organisations
    objects: dict[type[Model], Model]
    superuser: GeoramaUser
    # member of alpha
    member: GeoramaUser
    # member of beta only
    outsider: GeoramaUser
    # member of no organisation
    newcomer: GeoramaUser
    group: Group

    def client(self) -> APIClient:
        """A client of the superuser on the host of alpha."""
        return persona_client(self.superuser, self.organisation)


@pytest.fixture(scope="module")
def crud_data(django_db_setup, django_db_blocker, tmp_path_factory, gis: Gis) -> CrudData:
    with module_transaction(django_db_blocker, tmp_path_factory):
        alpha, beta = create_organisation("alpha"), create_organisation("beta")
        objects = create_organisation_objects(alpha, gis)
        editor_group = create_editor_group()
        yield CrudData(
            alpha,
            objects
            | {GeoramaUser: UserFactory.create(username="addressed", groups=[])}
            | create_shared_objects(),
            create_persona("superuser", editor_group, alpha),
            objects[Membership].user,
            create_persona("member", editor_group, beta),
            UserFactory.create(username="newcomer", groups=[]),
            GroupFactory.create(name="Readers"),
        )
