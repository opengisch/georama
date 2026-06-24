from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.request import Request
from rest_framework.response import Response

from georama.features.api.permissions import ManageApiPermission
from georama.features.api.serializers import (
    FeatureLayerSerializer,
    FieldSerializer,
)
from georama.features.models import FeatureLayer


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

    @action(detail=True, methods=["get", "post"])
    def fields(self, request: Request, pk: str):
        if request.POST:
            serializer = FieldSerializer(data=request.data)
            ...
        else:
            fields = self.get_object().fields.all()
            serializer = FieldSerializer(fields, many=True)
            return Response(serializer.data)


# "feature_layers/<feature_layer_id>/permissions/users"
