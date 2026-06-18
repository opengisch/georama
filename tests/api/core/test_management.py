import pytest
from rest_framework import status
from rest_framework.test import APIClient


class TestAccess:
    @pytest.mark.parametrize(
        "path",
        [
            "/manage/",
            "/manage/schema/",
            "/manage/schema/swagger-ui/",
            "/manage/schema/redoc/",
            "/manage/users/",
            "/manage/groups/",
            "/manage/permissions/",
            "/manage/organisations/",
            "/manage/fences/",
            "/manage/memberships/",
        ],
    )
    @pytest.mark.django_db
    def test_admin_has_get_access(self, admin_user, admin_user_name, admin_password, path):
        client = APIClient()
        client.login(username=admin_user_name, password=admin_password)
        response = client.get(path)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize(
        "path",
        [
            "/manage/",
            "/manage/schema/",
            "/manage/schema/swagger-ui/",
            "/manage/schema/redoc/",
            "/manage/users/",
            "/manage/groups/",
            "/manage/permissions/",
            "/manage/organisations/",
            "/manage/fences/",
            "/manage/memberships/",
        ],
    )
    @pytest.mark.django_db
    def test_anonymous_has_no_get_access(self, path):
        client = APIClient()
        response = client.get(path)
        assert response.status_code == status.HTTP_403_FORBIDDEN
