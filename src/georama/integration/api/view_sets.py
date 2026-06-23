from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import DjangoModelPermissions

from georama.core.common.querysets import OrganisationalQuerySet
from georama.integration.api.permissions import ManageApiPermission
from georama.integration.api.serializers import (
    CollectionSerializer,
    CustomDatasourceSerializer,
    FieldSerializer,
    ProjectSerializer,
    RasterDatasourceSerializer,
    VectorDatasourceSerializer,
)
from georama.integration.models import Collection, Custom, Field, Project, Raster, Vector


class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "organisation__name"]

    def filter_queryset(self, queryset: OrganisationalQuerySet):
        return queryset.organisation_objects(self.request.georama_organisation)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "collection__name"]

    def filter_queryset(self, queryset: QuerySet):
        return queryset.filter(collection__organisation=self.request.georama_organisation)


class VectorDatasourceViewSet(viewsets.ModelViewSet):
    queryset = Vector.objects.all()
    serializer_class = VectorDatasourceSerializer
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def filter_queryset(self, queryset: QuerySet):
        return queryset.filter(project__collection__organisation=self.request.georama_organisation)


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def filter_queryset(self, queryset: QuerySet):
        return queryset.prefetch_related("datasource__project__collection__organisation").filter(
            datasource__project__collection__organisation=self.request.georama_organisation
        )


class RasterDatasourceViewSet(viewsets.ModelViewSet):
    queryset = Raster.objects.all()
    serializer_class = RasterDatasourceSerializer
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def filter_queryset(self, queryset: QuerySet):
        return queryset.filter(
            project__collection__organisation=self.request.georama_organisation
        ).all()


class CustomDatasourceViewSet(viewsets.ModelViewSet):
    queryset = Custom.objects.all()
    serializer_class = CustomDatasourceSerializer
    permission_classes = [ManageApiPermission, DjangoModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def filter_queryset(self, queryset: QuerySet):
        return queryset.filter(
            project__collection__organisation=self.request.georama_organisation
        ).all()
