"""CRUD of the manage endpoints: the writes of a real payload reach the database as expected.

The matrix (`test_routes.py`) checks the status of every route with an empty payload. Here,
the superuser writes on the objects of alpha from its host, and the database is read after
each request. The data is `api_data`, see `tests/api/data.py`.

The routes written on are deduced from `ROUTES`: the creations, updates (PATCH), form updates
and deletions of the viewsets, and their `permissions` actions, but the ones a rule forbids
(405). The payloads of the creations and updates are declared in `declarations.py`, the deletions
and the object permissions need none:

- creation: only the objects of core and the short urls are created through the API, in the
  organisation of the host for the organisational ones;
- update: the published layers and themes, and the objects of core, are edited through PATCH
  and through the form of their page. An invalid PATCH changes nothing;
- deletion: the object is gone;
- object permissions: the `permissions` action grants and revokes the guardian permissions of
  the members of the host and of the groups.

The status of a write is the usual one of its kind (201, 200, 302, 400, 204). A rule or a bug
of the matrix on its route x method is reused when it expects the same status, with the ones
its payload declares in `declarations.py`.
"""

import pytest
from django.contrib.auth.models import Group
from django.db.models import Model
from django.urls import reverse
from guardian.shortcuts import assign_perm, get_perms
from rest_framework.test import APIClient

from georama.core.models.membership import Membership
from georama.core.models.user import GeoramaUser
from tests.api.crud.declarations import (
    CREATIONS,
    FORM_UPDATES,
    INVALID_UPDATES,
    NOT_EDITED,
    UPDATES,
    Creation,
    Invalid,
    Payload,
    Update,
)
from tests.api.data import ALPHA, ApiData
from tests.api.routes.declarations import ROUTES, Bug, Rule, expected, xfail
from tests.api.routing import application_routes, call, route_model

# the actions of the viewsets written on, by method
CREATE = ("post", {"create", "acreate"})
PATCH = ("patch", {"partial_update", "partial_aupdate"})
FORM = ("post", {"aform_update"})
DELETE = ("delete", {"destroy", "adestroy"})
PERMISSIONS = ("post", {"permissions"})


def matrix_status(name: str, method: str):
    return ROUTES[name][method]["superuser"]


def routes_of(kind: tuple[str, set[str]]) -> list[str]:
    """The routes whose `kind` of write the superuser can make: the ones a rule forbids (405)
    are left out.
    """
    method, actions = kind
    return [
        name
        for name, methods in ROUTES.items()
        if method in methods
        and getattr(application_routes()[name].view, "actions", {}).get(method) in actions
        and expected(matrix_status(name, method))[0] != 405
    ]


def model_of(name: str) -> type[Model]:
    return route_model(application_routes()[name])


def expected_write(
    name: str, kind: tuple[str, set[str]], status: int, known: tuple[Rule | Bug, ...] = ()
) -> tuple[int, list]:
    """The status of a write on the route `name` and the marks of its test case: the rules
    and bugs its payload hits, and the one of the matrix when it expects the same status.
    """
    matrix = matrix_status(name, kind[0])
    if isinstance(matrix, Rule | Bug) and matrix.status == status:
        known = (*known, matrix)
    return (known[0].status if known else status), xfail(known)


def cases(declarations: dict, kind: tuple[str, set[str]], status: int):
    """A test case per write declared on each route, labelled when a route has several."""
    for name, writes in declarations.items():
        labelled = writes.items() if isinstance(writes, dict) else [("", writes)]
        for label, write in labelled:
            write_status, marks = expected_write(name, kind, status, write.known)
            yield pytest.param(
                name, write, write_status, marks=marks, id="-".join(filter(None, [name, label]))
            )


def deduced(kind: tuple[str, set[str]], status: int):
    """A test case per route of `kind`, which needs no payload."""
    for name in routes_of(kind):
        write_status, marks = expected_write(name, kind, status)
        yield pytest.param(name, write_status, marks=marks, id=name)


# the payloads declared in `declarations.py`, the kind of write they make, and the routes exempted
DECLARED = [
    pytest.param(CREATIONS, CREATE, {}, id="creations"),
    pytest.param(UPDATES, PATCH, NOT_EDITED, id="updates"),
    pytest.param(INVALID_UPDATES, PATCH, NOT_EDITED, id="invalid-updates"),
    pytest.param(FORM_UPDATES, FORM, {}, id="form-updates"),
]


def client(api_data: ApiData) -> APIClient:
    """A client of the superuser on the host of alpha."""
    return api_data.client("superuser", ALPHA)


def alpha_object(api_data: ApiData, name: str) -> Model:
    """The object of alpha, or the shared one, addressed by the route `name`."""
    return api_data.addressed(ALPHA)[model_of(name)]


def alpha_member(api_data: ApiData) -> GeoramaUser:
    """A member of alpha, the host of the requests."""
    return api_data.objects[ALPHA][Membership].user


def payload_of(payload: Payload, obj: Model) -> dict:
    return payload(obj) if callable(payload) else payload


def reload(obj: Model) -> Model:
    return type(obj).objects.get(pk=obj.pk)


@pytest.mark.parametrize("declarations, kind, exempted", DECLARED)
def test_every_write_has_a_payload(declarations, kind, exempted):
    """A route listed here needs its payloads in `declarations.py`."""
    assert sorted(set(routes_of(kind)) - declarations.keys() - exempted.keys()) == []


@pytest.mark.parametrize("declarations, kind, exempted", DECLARED)
def test_every_payload_has_a_write(declarations, kind, exempted):
    """A route listed here is not written on any more, or is forbidden by a rule: its
    payloads are removed from `declarations.py`.
    """
    assert sorted((declarations.keys() | exempted.keys()) - set(routes_of(kind))) == []


@pytest.mark.django_db
@pytest.mark.parametrize("name, creation, status", list(cases(CREATIONS, CREATE, 201)))
def test_creation_writes_the_object_in_the_organisation_of_the_host(
    api_data, name, creation: Creation, status
):
    model = model_of(name)
    response = call(client(api_data), name, "post", {}, creation.payload(api_data))
    assert response.status_code == status
    created = model.objects.get(**creation.lookup(api_data))
    if field := getattr(model, "ORGANISATION_FIELD_NAME", None):
        alpha = api_data.organisations[ALPHA]
        assert model.objects.filter(pk=created.pk, **{field: alpha}).exists()


@pytest.mark.django_db
@pytest.mark.parametrize("name, update, status", list(cases(UPDATES, PATCH, 200)))
def test_patch_writes_the_payload(api_data, name, update: Update, status):
    obj = alpha_object(api_data, name)
    response = call(
        client(api_data), name, "patch", {"pk": obj.pk}, payload_of(update.payload, obj)
    )
    assert response.status_code == status
    assert update.read(reload(obj)) == update.written


@pytest.mark.django_db
@pytest.mark.parametrize("name, invalid, status", list(cases(INVALID_UPDATES, PATCH, 400)))
def test_invalid_patch_changes_nothing(api_data, name, invalid: Invalid, status):
    obj = alpha_object(api_data, name)
    before = invalid.read(obj)
    response = call(
        client(api_data), name, "patch", {"pk": obj.pk}, payload_of(invalid.payload, obj)
    )
    assert response.status_code == status
    assert invalid.read(reload(obj)) == before


@pytest.mark.django_db
@pytest.mark.parametrize("name, update, status", list(cases(FORM_UPDATES, FORM, 302)))
def test_form_writes_the_fields(api_data, name, update: Update, status):
    obj = alpha_object(api_data, name)
    response = client(api_data).post(
        reverse(name, kwargs={"pk": obj.pk}), payload_of(update.payload, obj)
    )
    assert response.status_code == status
    assert update.read(reload(obj)) == update.written


@pytest.mark.django_db
@pytest.mark.usefixtures("backends")
@pytest.mark.parametrize("name, status", list(deduced(DELETE, 204)))
def test_delete_removes_the_object(api_data, name, status):
    obj = alpha_object(api_data, name)
    response = call(client(api_data), name, "delete", {"pk": obj.pk})
    assert response.status_code == status
    assert not type(obj).objects.filter(pk=obj.pk).exists()


def permission_actions():
    """A test case per action of the `ACTION_MAP` of the model of each `permissions` route."""
    for param in deduced(PERMISSIONS, 200):
        name, status = param.values
        for action in model_of(name).ACTION_MAP:
            yield pytest.param(name, action, status, marks=param.marks, id=f"{name}-{action}")


def grant_all(model: type[Model], entities, obj: Model):
    for entity in entities:
        for codename in model.PERMISSIONS.values():
            assign_perm(f"{model._meta.app_label}.{codename}", entity, obj)


@pytest.mark.django_db
@pytest.mark.parametrize("name, action, status", list(permission_actions()))
def test_permission_action_grants_or_revokes(api_data, name, action, status):
    """Each action of `ACTION_MAP` grants its permissions, or revokes them from an entity
    holding them all, to a member of the host and to a group.
    """
    model = model_of(name)
    obj = alpha_object(api_data, name)
    grant, codenames, _label = model.ACTION_MAP[action]
    member, group = alpha_member(api_data), api_data.shared[Group]
    entities = [member, group]
    if not grant:
        grant_all(model, entities, obj)
    response = call(
        client(api_data),
        name,
        "post",
        {"pk": obj.pk},
        {"action": action, "users": [str(member.pk)], "groups": [group.pk]},
    )
    assert response.status_code == status
    assert (response.json()["users"], response.json()["groups"]) == (
        [str(member.pk)],
        [str(group.pk)],
    )
    for entity in entities:
        held = set(get_perms(entity, obj))
        assert set(codenames) <= held if grant else not set(codenames) & held


@pytest.mark.django_db
@pytest.mark.parametrize("name, status", list(deduced(PERMISSIONS, 200)))
def test_permission_action_ignores_the_users_of_other_organisations(api_data, name, status):
    obj = alpha_object(api_data, name)
    response = call(
        client(api_data),
        name,
        "post",
        {"pk": obj.pk},
        {"action": "grant", "users": [str(api_data.beta_member.pk)]},
    )
    assert response.status_code == status
    assert response.json()["users"] == []
    assert get_perms(api_data.beta_member, obj) == []


@pytest.mark.django_db
@pytest.mark.parametrize("name, status", list(deduced(PERMISSIONS, 400)))
def test_invalid_permission_action_changes_nothing(api_data, name, status):
    obj = alpha_object(api_data, name)
    member = alpha_member(api_data)
    response = call(
        client(api_data),
        name,
        "post",
        {"pk": obj.pk},
        {"action": "unknown", "users": [str(member.pk)]},
    )
    assert response.status_code == status
    assert get_perms(member, obj) == []
