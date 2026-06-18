from rest_framework import (
    routers,
)
from rest_framework.permissions import IsAuthenticated

from georama.integration.api.permissions import ManageApiPermission


class GeoramaIntegrationManageAPIRootView(routers.APIRootView):
    permission_classes = [IsAuthenticated, ManageApiPermission]


class GeoramaIntegrationManageRouter(routers.DefaultRouter):
    APIRootView = GeoramaIntegrationManageAPIRootView
