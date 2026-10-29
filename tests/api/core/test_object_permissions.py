import pytest
from rest_framework import status

from georama.core.factories import GroupFactory


@pytest.fixture
def group(db):
    return GroupFactory.create()


@pytest.fixture
def superuser_client(client_as):
    return client_as("superuser")


def permissions_path(theme):
    return f"/webgis/manage/themes/{theme.pk}/permissions/"


class TestPermissionsJsonRepresentation:
    @pytest.mark.django_db
    def test_groups_have_no_inherited_permissions(
        self, superuser_client, global_webgis_theme_public, group
    ):
        response = superuser_client.get(
            permissions_path(global_webgis_theme_public),
            {"f": "json", "entity": "groups"},
        )
        assert response.status_code == status.HTTP_200_OK
        rows = response.json()["results"]
        assert rows
        assert all("inherited_permissions" not in row for row in rows)

    @pytest.mark.django_db
    def test_users_have_inherited_permissions(
        self, superuser_client, global_webgis_theme_public, user_with_membership_global
    ):
        response = superuser_client.get(
            permissions_path(global_webgis_theme_public),
            {"f": "json", "entity": "users"},
        )
        assert response.status_code == status.HTTP_200_OK
        rows = response.json()["results"]
        assert rows
        assert all(row["inherited_permissions"] == {"can_view": False} for row in rows)
