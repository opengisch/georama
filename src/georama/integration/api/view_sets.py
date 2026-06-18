from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import DjangoModelPermissions

from georama.integration.api.serializers import CollectionSerializer
from georama.integration.models import Collection


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "organisation__name"]

    def get_queryset(self):
        return Collection.objects.organisation_objects(self.request.georama_organisation)
