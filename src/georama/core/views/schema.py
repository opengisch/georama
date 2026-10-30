from drf_spectacular import views
from rest_framework import permissions


class GeoramaAdminSchemaView(views.SpectacularAPIView):
    permission_classes = [permissions.IsAdminUser]


class GeoramaAdminSwaggerView(views.SpectacularSwaggerView):
    permission_classes = [permissions.IsAdminUser]


class GeoramaAdminRedocView(views.SpectacularRedocView):
    permission_classes = [permissions.IsAdminUser]
