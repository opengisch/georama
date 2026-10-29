import random
from collections.abc import Callable, Iterable
from pathlib import Path

import factory.random
import pytest
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, Q
from guardian.shortcuts import assign_perm
from rest_framework.test import APIClient

from georama.core.factories import (
    AdminUserFactory,
    GroupFactory,
    MembershipFactory,
    OrganisationFactory,
    UserFactory,
)
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser
from georama.features.models import FeatureLayer
from georama.integration.factories import ProjectFactory
from georama.maps.models.wms_layer import WmsLayer
from georama.webgis.models import Theme
from tests.fixtures import SEED

pytest_plugins = [
    "tests.fixtures.gis",
    "tests.fixtures.layers",
    "tests.fixtures.qsl",
    "tests.fixtures.testmandant",
]


@pytest.fixture(autouse=True)
def seed():
    """Factories draw from `random` directly, factory_boy and Faker share another generator."""
    random.seed(SEED)
    factory.random.reseed_random(SEED)


@pytest.fixture(autouse=True)
def data_integration_root(settings, tmp_path) -> Path:
    """Keeps the folders created by the code (organisations, projects) out of the repository."""
    root = tmp_path / "projects"
    (root / settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER).mkdir(parents=True)
    settings.DATA_INTEGRATION_ROOT = root
    return root


@pytest.fixture
def admin_user_name():
    yield "admin"


@pytest.fixture
def admin_password():
    yield "admin"


@pytest.fixture
def admin_email():
    yield "admin@example.org"


@pytest.fixture
def admin_user(admin_user_name, admin_password, admin_email):
    return AdminUserFactory.create(
        username=admin_user_name,
        email=admin_email,
        is_staff=True,
        is_superuser=True,
        password=admin_password,
    )


@pytest.fixture
def organisation():
    return OrganisationFactory.create()


@pytest.fixture
def organisation_public_access():
    return OrganisationFactory.create(public_access=True)


@pytest.fixture
def organisation_non_public_access():
    return OrganisationFactory.create(public_access=False)


@pytest.fixture
def project_global_organisation(db):
    return ProjectFactory.create(organisation=None, path="Global/GlobalProject.qgz")


@pytest.fixture
def membership(organisation):
    return MembershipFactory.create(organisation=organisation)


@pytest.fixture
def membership_public_organisation(organisation_public_access):
    return MembershipFactory.create(organisation=organisation_public_access)


@pytest.fixture
def membership_global(db):
    return MembershipFactory.create(organisation=None)


@pytest.fixture
def membership_non_public_organisation(organisation_non_public_access):
    return MembershipFactory.create(organisation=organisation_non_public_access)


@pytest.fixture
def user_user_name():
    yield "limu"


@pytest.fixture
def user_first_name():
    yield "Lieschen"


@pytest.fixture
def user_last_name():
    yield "Müller"


@pytest.fixture
def user_password():
    yield "oh-my-secret"


@pytest.fixture
def user_email(user_user_name):
    yield f"{user_user_name}@example.org"


@pytest.fixture
def user(user_user_name, user_first_name, user_last_name, user_email, user_password):
    return UserFactory.create(
        username=user_user_name,
        password=user_password,
        first_name=user_first_name,
        last_name=user_last_name,
        email=user_email,
        is_staff=False,
        is_superuser=False,
        groups=[],
    )


@pytest.fixture
def user_with_membership_global(user, membership_global):
    user.memberships.add(membership_global)
    user.save()
    yield user


@pytest.fixture
def user_with_dedicated_membership_non_public(user, membership_non_public_organisation):
    user.memberships.add(membership_non_public_organisation)
    user.save()
    yield user


PERSONAS = ["anonymous", "member", "viewer", "editor", "staff", "superuser"]
PERSONA_PASSWORD = "persona-secret"
# apps whose models the editor manages
EDITOR_APPS = ["integration", "maps", "webgis", "features"]
# permission a viewer gets on each object given to `persona`
VIEW_PERMISSIONS = {
    WmsLayer: "view_published_wms_layer",
    Theme: "view_published_theme",
    FeatureLayer: "view_objects_on_published_layer",
}


@pytest.fixture
def editor_group(db) -> Group:
    """Group with the view, add, change and delete permissions on the models of `EDITOR_APPS`."""
    query = Q()
    for app_label in EDITOR_APPS:
        for model in apps.get_app_config(app_label).get_models():
            query |= Q(
                content_type=ContentType.objects.get_for_model(model),
                codename__in=[
                    f"{action}_{model._meta.model_name}"
                    for action in ("view", "add", "change", "delete")
                ],
            )
    group = GroupFactory.create(name="Editor")
    group.permissions.set(Permission.objects.filter(query))
    return group


@pytest.fixture
def persona(editor_group) -> Callable[..., GeoramaUser | None]:
    """Creates the user of a persona, member of `organisation` (None for the global one).

    Personas:

    - anonymous: no user;
    - member: a membership, nothing else;
    - viewer: a member with the view permission on each of `objects`;
    - editor: a member of `editor_group`;
    - staff: a member with `is_staff`;
    - superuser: a member with `is_superuser`.
    """

    def create(
        name: str, organisation: Organisation | None = None, objects: Iterable[Model] = ()
    ) -> GeoramaUser | None:
        if name not in PERSONAS:
            raise ValueError(f"Unknown persona {name}, expected one of {PERSONAS}")
        if name == "anonymous":
            return None
        if (name == "viewer") != bool(objects):
            raise ValueError("Objects are given to the viewer, and only to the viewer")
        user = UserFactory.create(
            username=f"{name}-{organisation.domain if organisation else 'global'}",
            password=PERSONA_PASSWORD,
            is_staff=name in ("staff", "superuser"),
            is_superuser=name == "superuser",
            groups=[editor_group] if name == "editor" else [],
        )
        MembershipFactory.create(user=user, organisation=organisation)
        for obj in objects:
            assign_perm(VIEW_PERMISSIONS[type(obj)], user, obj)
        return user

    return create


@pytest.fixture
def client_as(persona) -> Callable[..., APIClient]:
    """Creates a client logged in as a persona (see `persona`), whose requests target the
    host of `organisation`. The user is available as `client.persona`.
    """

    def create(
        name: str, organisation: Organisation | None = None, objects: Iterable[Model] = ()
    ) -> APIClient:
        domain = settings.ORGANISATION_DOMAIN
        client = APIClient(
            SERVER_NAME=f"{organisation.domain}.{domain}" if organisation else domain
        )
        client.persona = persona(name, organisation, objects)
        if client.persona is not None:
            client.force_login(client.persona)
        return client

    return create
