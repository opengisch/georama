from rest_framework import routers
from rest_framework.permissions import IsAuthenticated

from georama.features.api.permissions import ManageApiPermission


class GeoramaFeaturesManageAPIRootView(routers.APIRootView):
    permission_classes = [IsAuthenticated, ManageApiPermission]


class GeoramaFeaturesManageRouter(routers.DefaultRouter):
    APIRootView = GeoramaFeaturesManageAPIRootView
