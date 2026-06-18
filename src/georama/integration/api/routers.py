from rest_framework import (
    routers,
)
from rest_framework.permissions import DjangoModelPermissions


class GeoramaIntegrationManageAPIRootView(routers.APIRootView):
    permission_classes = [DjangoModelPermissions]


class GeoramaIntegrationManageRouter(routers.DefaultRouter):
    APIRootView = GeoramaIntegrationManageAPIRootView
