"""The payloads of the CRUD tests, by route: what each write sends, and what it changes in the
database.

Everything else is deduced from `ROUTES` by `test_crud.py`: the routes to write on, the model
of their objects, the deletions, the object permissions, and the rules and bugs of the matrix
expecting the status of the write. `test_every_write_has_a_payload` fails until a payload is
declared here for each write route of `ROUTES`, but the ones a rule forbids (405).

A payload declares in `known` only the rules and bugs it hits beyond the ones of the matrix,
e.g. the nested metadata of a map layer, which the empty payload of the matrix does not write.
"""

import json
from collections.abc import Callable
from operator import attrgetter
from typing import NamedTuple

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model

from georama.features.models import FeatureLayer
from georama.integration.models import Project
from tests.api.data import ApiData
from tests.api.routes.declarations import (
    FENCE_ASAVE,
    HOST_ORGANISATION,
    MEMBERSHIP_FIELDS,
    NESTED_METADATA,
    QUERYABLE_READ_ONLY,
    Bug,
    Rule,
)

# the payload of a write, from the object written for the payloads naming its content
Payload = dict | Callable[[Model], dict]


class Creation(NamedTuple):
    """A POST on a list route, answering 201."""

    payload: Callable[[ApiData], dict]
    # identifies the object created
    lookup: Callable[[ApiData], dict]
    # the rules and bugs the payload hits beyond the ones of the matrix
    known: tuple[Rule | Bug, ...] = ()


class Update(NamedTuple):
    """A PATCH on a detail route answering 200, or the post of the form of the page of the
    object answering 302.
    """

    payload: Payload
    # the values written, read on the object
    read: Callable[[Model], object]
    written: object
    known: tuple[Rule | Bug, ...] = ()


class Invalid(NamedTuple):
    """A PATCH with an invalid payload, answering 400 and changing nothing."""

    payload: Payload
    # the values the payload tries to write, read on the object
    read: Callable[[Model], object]
    known: tuple[Rule | Bug, ...] = ()


SQUARE = [[[[0, 0], [0, 1], [1, 1], [0, 0]]]]
SHORTENED = f"{settings.WEBGISURL}?theme=created"

# by list route; only the objects of core and the short urls are created through the API, see
# `CREATION` in `routes/declarations.py`
CREATIONS = {
    "core:georamauser-list": Creation(
        lambda data: {
            "username": "created",
            "groups": [data.shared[Group].pk],
            "user_permissions": [],
            "memberships": [],
        },
        lambda data: {"username": "created", "groups": data.shared[Group]},
    ),
    "core:group-list": Creation(
        lambda data: {"name": "Created", "permissions": [data.shared[Permission].pk]},
        lambda data: {"name": "Created", "permissions": data.shared[Permission]},
    ),
    "core:permission-list": Creation(
        lambda data: {
            "name": "Can create",
            "codename": "created",
            "content_type": ContentType.objects.get_for_model(Project).pk,
        },
        lambda data: {"codename": "created", "content_type__model": "project"},
    ),
    "core:organisation-list": Creation(
        lambda data: {"name": "Created", "domain": "created", "fences": [], "memberships": []},
        lambda data: {"name": "Created", "domain": "created"},
    ),
    "core:fence-list": Creation(
        lambda data: {
            "type": "Feature",
            "geometry": {"type": "MultiPolygon", "coordinates": SQUARE},
            "properties": {"name": "Created"},
        },
        lambda data: {"name": "Created"},
        (Bug(201, FENCE_ASAVE), Rule(201, HOST_ORGANISATION)),
    ),
    "core:membership-list": Creation(
        lambda data: {"user_id": str(data.newcomer.pk)},
        lambda data: {"user": data.newcomer},
        (Bug(201, MEMBERSHIP_FIELDS), Rule(201, HOST_ORGANISATION)),
    ),
    "webgis:short-list": Creation(
        lambda data: {"url": SHORTENED},
        lambda data: {"url": SHORTENED},
    ),
}


def fence(name: str) -> dict:
    return {"type": "Feature", "properties": {"name": name}}


def first_field(layer: FeatureLayer):
    return layer.fields.order_by("name").first()


# the detail routes on which nothing is edited, with the reason
NOT_EDITED = {
    "core:membership-detail": "a membership has no field to edit: its user and its "
    "organisation are set at its creation",
}

# by detail route, then by what is written. The integrated objects are not edited, see
# `INTEGRATED` in `routes/declarations.py`. The title of a theme is not editable for now
UPDATES = {
    "core:georamauser-detail": {
        "attributes": Update(
            {"first_name": "Patched", "is_active": False},
            attrgetter("first_name", "is_active"),
            ("Patched", False),
        ),
    },
    "core:group-detail": {
        "attributes": Update({"name": "Patched"}, attrgetter("name"), "Patched"),
    },
    "core:permission-detail": {
        "attributes": Update({"name": "Patched"}, attrgetter("name"), "Patched"),
    },
    "core:organisation-detail": {
        "attributes": Update({"name": "Patched"}, attrgetter("name"), "Patched"),
    },
    "core:fence-detail": {
        "attributes": Update(fence("Patched"), attrgetter("name"), "Patched"),
    },
    "maps:maplayer-manager-detail": {
        "attributes": Update(
            {"public": True, "is_queryable": False, "extent": "0,0,1,1"},
            attrgetter("public", "is_queryable", "extent"),
            (True, False, "0,0,1,1"),
            (Bug(200, QUERYABLE_READ_ONLY),),
        ),
        "metadata": Update(
            {"metadata": {"title": "Patched", "description": "Patched"}},
            attrgetter("metadata.title", "metadata.description"),
            ("Patched", "Patched"),
        ),
    },
    "features:feature-manager-detail": {
        "attributes": Update(
            {"public": True, "max_items": 7, "on_exceed": "THROTTLE"},
            attrgetter("public", "max_items", "on_exceed"),
            (True, 7, "THROTTLE"),
        ),
        "metadata": Update(
            {"metadata": {"title": "Patched", "description": "Patched"}},
            attrgetter("metadata.title", "metadata.description"),
            ("Patched", "Patched"),
        ),
        "fields": Update(
            lambda layer: {"fields": [{"name": first_field(layer).name, "visible": False}]},
            lambda layer: first_field(layer).visible,
            False,
        ),
    },
    "webgis:theme-manager-detail": {
        "attributes": Update(
            {"public": True, "ordering": 5}, attrgetter("public", "ordering"), (True, 5)
        ),
    },
}

# by detail route, then by what is invalid
INVALID_UPDATES = {
    "core:georamauser-detail": {
        "email": Invalid({"email": "not-an-email"}, attrgetter("email")),
    },
    "core:group-detail": {"name": Invalid({"name": ""}, attrgetter("name"))},
    "core:permission-detail": {"name": Invalid({"name": ""}, attrgetter("name"))},
    "core:organisation-detail": {"name": Invalid({"name": ""}, attrgetter("name"))},
    "core:fence-detail": {"name": Invalid(fence(""), attrgetter("name"))},
    "maps:maplayer-manager-detail": {
        "public": Invalid({"public": "maybe"}, attrgetter("public")),
    },
    "features:feature-manager-detail": {
        "max_items": Invalid({"max_items": "many"}, attrgetter("max_items")),
        "fields": Invalid(
            {"fields": [{"name": "unknown", "visible": False}]},
            lambda layer: sorted(layer.fields.values_list("name", "visible")),
        ),
    },
    "webgis:theme-manager-detail": {
        "ordering": Invalid({"ordering": "first"}, attrgetter("ordering")),
    },
}

# by form route: the form of the page of an object posts all its fields, the unchecked boxes
# are left out
FORM_UPDATES = {
    "maps:maplayer-manager-aform-update": Update(
        {"public": "true", "extent": "0,0,1,1", "metadata.title": "Patched"},
        attrgetter("public", "is_queryable", "extent", "metadata.title"),
        (True, False, "0,0,1,1", "Patched"),
        (Bug(302, NESTED_METADATA),),
    ),
    "features:feature-manager-aform-update": Update(
        {"public": "true", "max_items": "7", "metadata.title": "Patched"},
        attrgetter("public", "max_items", "metadata.title"),
        (True, 7, "Patched"),
    ),
    "webgis:theme-manager-aform-update": Update(
        lambda theme: {
            "public": "true",
            "ordering": "5",
            "theme_json": json.dumps(theme.theme_json),
            "background_layers": "[]",
        },
        attrgetter("public", "ordering"),
        (True, 5),
    ),
}
