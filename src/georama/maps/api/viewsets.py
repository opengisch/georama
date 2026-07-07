from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from georama.core.common.api import GeoramaModelPermissions
from georama.maps.api.serializers import WmsLayerSerializer
from georama.maps.models import WmsLayer


class WmsLayerViewSet(viewsets.ModelViewSet):
    serializer_class = WmsLayerSerializer
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    def get_queryset(self):
        return WmsLayer.objects.filter(
            datasource__project__organisation=self.request.georama_organisation
        )
