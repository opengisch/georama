import pytest
from rest_framework.test import APIRequestFactory

from georama.core.common.api import GeoramaModelPermissions
from georama.integration.models.collection import Collection
from tests.api.common import view_perm


class CollectionMockView:
    def get_queryset():
        return Collection.objects.all()


class TestGeoramaModelPermission:
    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "method",
        [
            "get",
            "head",
            "options",
        ],
    )
    def test_user_with_view_perm(self, user, organisation, method):
        user.user_permissions.add(view_perm(Collection))
        factory = APIRequestFactory()
        request = getattr(factory, method)("")
        request.user = user
        request.georama_organisation = organisation
        assert GeoramaModelPermissions().has_permission(request, CollectionMockView)

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "method",
        [
            "get",
            "head",
            "options",
        ],
    )
    def test_user_without_view_perm(self, user, organisation, method):
        factory = APIRequestFactory()
        request = getattr(factory, method)("")
        request.user = user
        request.georama_organisation = organisation
        assert not GeoramaModelPermissions().has_permission(request, CollectionMockView)
