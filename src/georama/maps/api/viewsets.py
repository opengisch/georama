from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAdminUser

from georama.core.common.api import (
    GeoramaAsyncTemplateModelViewSet,
    GeoramaModelPermissions,
    OrganisationalModelViewSet,
)
from georama.maps.api.serializers import WmsLayerSerializer
from georama.maps.models import WmsLayer


class WmsLayerViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = WmsLayer.objects.all()
    serializer_class = WmsLayerSerializer
    permission_classes = [IsAdminUser, GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
