from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response

from georama.core.common.api import (
    GeoramaAsyncTemplateModelViewSet,
    GeoramaModelPermissions,
    OrganisationalModelViewSet,
)
from georama.features.api.serializers import (
    FeatureLayerSerializer,
    FieldSerializer,
)
from georama.features.models import FeatureLayer


class FeatureLayerViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = FeatureLayer.objects.all()
    serializer_class = FeatureLayerSerializer
    permission_classes = [IsAdminUser, GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    @action(detail=True, methods=["get", "post"])
    def fields(self, request: Request, pk: str):
        if request.POST:
            serializer = FieldSerializer(data=request.data)
            ...
        else:
            fields = self.get_object().fields.all()
            serializer = FieldSerializer(fields, many=True)
            return Response(serializer.data)
