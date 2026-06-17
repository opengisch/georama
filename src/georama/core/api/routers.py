from rest_framework import (
    permissions,
    routers,
)


class GeoramaAdminAPIRootView(routers.APIRootView):
    permission_classes = [permissions.IsAdminUser]


class GeoramaAdminRouter(routers.DefaultRouter):
    APIRootView = GeoramaAdminAPIRootView
