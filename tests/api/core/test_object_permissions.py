import pytest
from django.urls import reverse
from rest_framework import status

from georama.core.factories import GroupFactory
from tests.fixtures.layers import create_theme


def permissions_of(client, theme, entity: str) -> list[dict]:
    """The rows of the permissions of `theme` for the `entity` (users or groups)."""
    response = client.get(
        reverse("webgis:theme-manager-permissions", kwargs={"pk": theme.pk}),
        {"f": "json", "entity": entity},
    )
    assert response.status_code == status.HTTP_200_OK
    return response.json()["results"]


@pytest.mark.django_db
def test_groups_have_no_inherited_permissions(client_as, project_global_organisation):
    theme = create_theme(project_global_organisation, public=True)
    GroupFactory.create()
    rows = permissions_of(client_as("superuser"), theme, "groups")
    assert rows
    assert all("inherited_permissions" not in row for row in rows)


@pytest.mark.django_db
def test_users_have_inherited_permissions(client_as, persona, project_global_organisation):
    theme = create_theme(project_global_organisation, public=True)
    persona("member")
    rows = permissions_of(client_as("superuser"), theme, "users")
    assert rows
    assert all(row["inherited_permissions"] == {"can_view": False} for row in rows)
