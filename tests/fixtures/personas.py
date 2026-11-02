"""Personas: the users the API tests make their requests as."""

from collections.abc import Callable, Iterable

import pytest
from django.apps import apps
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model, Q
from guardian.shortcuts import assign_perm
from rest_framework.test import APIClient

from georama.core.factories import GroupFactory, MembershipFactory, UserFactory
from georama.core.models.organisation import Organisation
from georama.core.models.user import GeoramaUser
from georama.features.models import FeatureLayer
from georama.maps.models.wms_layer import WmsLayer
from georama.webgis.models import Theme

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


def create_editor_group() -> Group:
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


def create_persona(
    name: str,
    editor_group: Group,
    organisation: Organisation | None = None,
    objects: Iterable[Model] = (),
) -> GeoramaUser | None:
    """Creates the user of a persona, member of `organisation` (None for the global one).

    Personas:

    - anonymous: no user;
    - member: a membership, nothing else;
    - viewer: a member with the view permission on each of `objects`;
    - editor: a member of `editor_group`;
    - staff: a member with `is_staff`;
    - superuser: a member with `is_superuser`.
    """
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


def persona_client(user: GeoramaUser | None, organisation: Organisation | None = None) -> APIClient:
    """Creates a client logged in as `user` (anonymous for None), whose requests target the
    host of `organisation`. The user is available as `client.persona`.
    """
    domain = settings.ORGANISATION_DOMAIN
    client = APIClient(SERVER_NAME=f"{organisation.domain}.{domain}" if organisation else domain)
    client.persona = user
    if user is not None:
        client.force_login(user)
    return client


@pytest.fixture
def editor_group(db) -> Group:
    return create_editor_group()


@pytest.fixture
def persona(editor_group) -> Callable[..., GeoramaUser | None]:
    """Creates the user of a persona, see `create_persona`."""

    def create(
        name: str, organisation: Organisation | None = None, objects: Iterable[Model] = ()
    ) -> GeoramaUser | None:
        return create_persona(name, editor_group, organisation, objects)

    return create


@pytest.fixture
def client_as(persona) -> Callable[..., APIClient]:
    """Creates a client logged in as a persona, see `create_persona` and `persona_client`."""

    def create(
        name: str, organisation: Organisation | None = None, objects: Iterable[Model] = ()
    ) -> APIClient:
        return persona_client(persona(name, organisation, objects), organisation)

    return create
