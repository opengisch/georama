import pytest
from rest_framework.test import APIRequestFactory, force_authenticate

from georama.core.common.api import GeoramaModelPermissions
from georama.integration.models import Collection


class TestGeoramaModelPermission:
    def test_get_permission(self, user):
        with pytest.mock(
            "georama.core.common.api.GeoramaModelPermissions._queryset", Collection.objects.all()
        ):
            perm = GeoramaModelPermissions()
            factory = APIRequestFactory()
            request = factory.get("")
            force_authenticate(request, user=user)
            assert perm.has_permission(request, "bla")
