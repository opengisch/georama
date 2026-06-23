import pytest
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.test import APIClient

from georama.integration.models import Collection, Custom, Field, Project, Raster, Vector
from georama.integration.models.meta import Permission as IntegrationPermission


class TestAccess:
    paths = [
        "/integration/manage/",
        "/integration/manage/collections/",
        "/integration/manage/projects/",
        "/integration/manage/vector_datasources/",
        "/integration/manage/vector_datasource_fields/",
        "/integration/manage/raster_datasources/",
        "/integration/manage/custom_datasources/",
    ]

    @pytest.mark.parametrize(
        "path",
        paths,
    )
    @pytest.mark.django_db
    def test_admin_has_get_access(self, admin_user, admin_user_name, admin_password, path):
        client = APIClient()
        client.login(username=admin_user_name, password=admin_password)
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize(
        "path",
        paths,
    )
    @pytest.mark.django_db
    def test_member_without_model_view_perm_has_no_get_access(
        self, user_with_membership_global, user_user_name, user_password, collections, path
    ):
        client = APIClient()
        client.login(username=user_user_name, password=user_user_name)
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize(
        "path",
        paths,
    )
    @pytest.mark.django_db
    def test_user_without_model_view_perm_has_no_get_access(
        self, user, user_user_name, user_password, collections, path
    ):
        client = APIClient()
        client.login(username=user_user_name, password=user_password)
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize(
        "path",
        paths,
    )
    @pytest.mark.django_db
    def test_anonymous_has_no_get_access(self, path):
        client = APIClient()
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    @pytest.mark.parametrize(
        "path, model",
        [
            ("/integration/manage/collections/", Collection),
            ("/integration/manage/projects/", Project),
            ("/integration/manage/vector_datasources/", Vector),
            ("/integration/manage/vector_datasource_fields/", Field),
            ("/integration/manage/raster_datasources/", Raster),
            ("/integration/manage/custom_datasources/", Custom),
        ],
    )
    @pytest.mark.django_db
    def test_user_with_model_view_and_api_perm_has_get_access(
        self,
        user,
        user_user_name,
        user_password,
        collections,
        path,
        model,
    ):
        view_permission = Permission.objects.get(
            content_type=ContentType.objects.get_for_model(model),
            codename=f"view_{model._meta.model_name}",
        )
        api_permission = Permission.objects.get(
            content_type=ContentType.objects.get_for_model(IntegrationPermission),
            codename="can_use_manage_api",
        )
        user.user_permissions.set([api_permission, view_permission])
        user.save()
        assert user.has_perm("integration.can_use_manage_api")
        assert user.has_perm(f"integration.view_{model._meta.model_name}")
        client = APIClient()
        client.login(username=user_user_name, password=user_password)
        response = client.get(path, SERVER_NAME="localhost")
        assert response.status_code == status.HTTP_200_OK
