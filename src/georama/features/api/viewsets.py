from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import DjangoModelPermissions

from georama.features.api.permissions import ManageApiPermission
from georama.features.api.serializers import (
    FeatureLayerSerializer,
    FieldSerializer,
)
from georama.features.models import FeatureLayer, Field


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer

    def get_queryset(self):
        return Field.objects.filter(
            feature_layer_id=self.kwargs["feature_layer_id"],
            datasource_field__datasource__project__collection__organisation=self.request.georama_organisation,
        )

    def perform_create(self, serializer):
        serializer.save(feature_layer_id=self.kwargs["feature_layer_id"])


class FeatureLayerViewSet(viewsets.ModelViewSet):
    serializer_class = FeatureLayerSerializer
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    def get_queryset(self):
        return FeatureLayer.objects.filter(
            datasource__project__collection__organisation=self.request.georama_organisation
        )
