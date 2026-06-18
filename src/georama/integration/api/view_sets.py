from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import DjangoModelPermissions

from georama.integration.api.serializers import (
    CollectionSerializer,
    CustomDatasetSerializer,
    FieldSerializer,
    ProjectSerializer,
    RasterDatasetSerializer,
    VectorDatasetSerializer,
)
from georama.integration.models import Collection, Custom, Field, Project, Raster, Vector


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


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "collection__name"]

    def get_queryset(self):
        return Project.objects.filter(
            collection__organisation=self.request.georama_organisation
        ).all()


class VectorDatasetViewSet(viewsets.ModelViewSet):
    serializer_class = VectorDatasetSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def get_queryset(self):
        return Vector.objects.filter(
            project__collection__organisation=self.request.georama_organisation
        ).all()


class FieldViewSet(viewsets.ModelViewSet):
    serializer_class = FieldSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def get_queryset(self):
        return (
            Field.objects.prefetch_related("dataset__project__collection__organisation")
            .filter(dataset__project__collection__organisation=self.request.georama_organisation)
            .all()
        )


class RasterDatasetViewSet(viewsets.ModelViewSet):
    serializer_class = RasterDatasetSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def get_queryset(self):
        return Raster.objects.filter(
            project__collection__organisation=self.request.georama_organisation
        ).all()


class CustomDatasetViewSet(viewsets.ModelViewSet):
    serializer_class = CustomDatasetSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def get_queryset(self):
        return Custom.objects.filter(
            project__collection__organisation=self.request.georama_organisation
        ).all()
