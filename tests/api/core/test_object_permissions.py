import pytest
from rest_framework import status
from rest_framework.test import APIClient

from georama.core.factories import GroupFactory


@pytest.fixture
def group():
    group = GroupFactory.create()
    yield group
    group.delete()


@pytest.fixture
def admin_client(admin_user, admin_user_name, admin_password):
    client = APIClient()
    client.login(username=admin_user_name, password=admin_password)
    yield client


def permissions_path(theme):
    return f"/webgis/manage/themes/{theme.pk}/permissions/"


class TestPermissionsJsonRepresentation:
    @pytest.mark.django_db
    def test_groups_have_no_inherited_permissions(
        self, admin_client, global_webgis_theme_public, group
    ):
        response = admin_client.get(
            permissions_path(global_webgis_theme_public),
            {"f": "json", "entity": "groups"},
            SERVER_NAME="localhost",
        )
        assert response.status_code == status.HTTP_200_OK
        rows = response.json()["results"]
        assert rows
        assert all("inherited_permissions" not in row for row in rows)

    @pytest.mark.django_db
    def test_users_have_inherited_permissions(
        self, admin_client, global_webgis_theme_public, user_with_membership_global
    ):
        response = admin_client.get(
            permissions_path(global_webgis_theme_public),
            {"f": "json", "entity": "users"},
            SERVER_NAME="localhost",
        )
        assert response.status_code == status.HTTP_200_OK
        rows = response.json()["results"]
        assert rows
        assert all(row["inherited_permissions"] == {"can_view": False} for row in rows)
