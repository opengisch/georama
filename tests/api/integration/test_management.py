import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APIClient

from georama.integration.models import Collection
from georama.integration.models.meta import Permission as IntegrationPermission
from tests.api.common import api_perm, view_perm


class TestCollection:
    client = APIClient()

    @pytest.mark.django_db
    def test_anonymous_can_not_get_list(self):
        list_url = "/integration/manage/collections/"
        response = self.client.get(list_url, format="json", SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_user_without_perm_can_not_get_list(
        self,
        user,
        user_user_name,
        user_password,
    ):
        list_url = "/integration/manage/collections/"
        self.client.login(username=user_user_name, password=user_password)
        response = self.client.get(list_url, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_user_with_only_model_view_can_not_get_list(
        self,
        user,
        user_user_name,
        user_password,
    ):
        list_url = "/integration/manage/collections/"
        user.user_permissions.set([view_perm(Collection)])
        self.client.login(username=user_user_name, password=user_password)
        response = self.client.get(list_url, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_user_with_model_view_and_api_perm_can_get_list(
        self,
        user,
        user_user_name,
        user_password,
        collections,
    ):
        list_url = "/integration/manage/collections/"
        user.user_permissions.set([api_perm(IntegrationPermission), view_perm(Collection)])
        self.client.login(username=user_user_name, password=user_password)
        response = self.client.get(list_url, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_admin_can_get_list(
        self,
        admin_user,
        admin_user_name,
        admin_password,
        organisation,
        collections,
    ):
        list_url = "/integration/manage/collections/"
        self.client.login(username=admin_user_name, password=admin_password)
        response = self.client.get(list_url, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_list_contains_organisational_entries_only(
        self,
        user,
        user_user_name,
        user_password,
        admin_user,
        admin_user_name,
        admin_password,
        collections,
        organisation,
    ):
        list_url = "/integration/manage/collections/"

        # testing api permission only
        user.user_permissions.set([api_perm(IntegrationPermission)])
        self.client.login(username=user_user_name, password=user_password)
        ## test global organisation
        response = self.client.get(list_url, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == Collection.objects.filter(organisation=None).count()
        assert all(item["organisation_id"] is None for item in response.data["results"])
        ## test dedicated organisation (testuser is only member of global organisation)
        response = self.client.get(list_url, SERVER_NAME=f"{organisation.domain}.localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

        # admin is also allowed to see organisation based only
        self.client.login(username=admin_user_name, password=admin_password)
        ## test global organisation
        response = self.client.get(list_url, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data["results"]) == Collection.objects.filter(organisation=None).count()
        assert all(item["organisation_id"] is None for item in response.data["results"])
        ## test dedicated organisation
        response = self.client.get(list_url, SERVER_NAME=f"{organisation.domain}.localhost")
        assert response.status_code == status.HTTP_200_OK
        assert (
            len(response.data["results"])
            == Collection.objects.filter(organisation=organisation).count()
        )
        assert all(item["organisation_id"] == organisation.id for item in response.data["results"])


class TestApiRoot:
    endpoint = "/integration/manage/"

    @pytest.mark.django_db
    def test_admin_has_get_access(
        self,
        admin_user,
        admin_user_name,
        admin_password,
    ):
        client = APIClient()
        client.login(username=admin_user_name, password=admin_password)
        response = client.get(self.endpoint, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_user_without_perms_has_no_get_access(
        self,
        user,
        user_user_name,
        user_password,
        collections,
    ):
        client = APIClient()
        client.login(username=user_user_name, password=user_password)
        response = client.get(self.endpoint, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.django_db
    def test_user_with_only_api_perm_has_get_access(
        self,
        user,
        user_user_name,
        user_password,
        collections,
    ):
        api_permission = Permission.objects.get(
            content_type=ContentType.objects.get_for_model(IntegrationPermission),
            codename="can_use_manage_api",
        )
        user.user_permissions.set([api_permission])
        client = APIClient()
        client.login(username=user_user_name, password=user_password)
        response = client.get(self.endpoint, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.django_db
    def test_anonymous_has_no_get_access(self):
        client = APIClient()
        response = client.get(self.endpoint, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN
