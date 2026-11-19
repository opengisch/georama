import pytest
from rest_framework import status
from rest_framework.test import APIClient

from georama.core.factories import GroupFactory, UserFactory


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
    return f"/webgis/manage/themes/{theme.pk}/permissions"


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
        # one entry per permission of the theme, the user is in no group which has any
        assert all(
            row["inherited_permissions"]
            == {"can_view": False, "can_create": False, "can_update": False, "can_delete": False}
            for row in rows
        )

    @pytest.mark.django_db
    def test_users_of_a_global_theme(
        self,
        admin_client,
        global_webgis_theme_public,
        user_with_membership_global,
        membership_non_public_organisation,
    ):
        # a user who is member of another organisation only
        other_user = UserFactory.create(username="otto", is_staff=False, is_superuser=False)
        other_user.memberships.add(membership_non_public_organisation)
        # a user who is member of no organisation, e.g. after the first login through an
        # identity provider
        UserFactory.create(username="nora", is_staff=False, is_superuser=False)
        response = admin_client.get(
            permissions_path(global_webgis_theme_public),
            {"f": "json", "entity": "users"},
            SERVER_NAME="localhost",
        )
        assert response.status_code == status.HTTP_200_OK
        offered_users = [row["entity_name"] for row in response.json()["results"]]
        # the global member is offered, and so is the user without membership, with
        # global public access they reach the global organisation as well
        assert user_with_membership_global.username in offered_users
        assert "nora" in offered_users
        # the member of another organisation is not
        assert "otto" not in offered_users
