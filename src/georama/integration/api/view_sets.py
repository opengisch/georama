from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from georama.core.common.api import (
    GeoramaAsyncTemplateModelViewSet,
    GeoramaModelPermissions,
    OrganisationalModelViewSet,
)
from georama.integration.api.serializers import (
    CollectionSerializer,
    CustomDatasourceSerializer,
    FieldSerializer,
    ProjectSerializer,
    RasterDatasourceSerializer,
    VectorDatasourceSerializer,
)
from georama.integration.models import Collection, Custom, Field, Project, Raster, Vector


class CollectionViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.all()
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "organisation__name"]


class ProjectViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name", "collection__name"]


class VectorDatasourceViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = Vector.objects.all()
    serializer_class = VectorDatasourceSerializer
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]


class FieldViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]


class RasterDatasourceViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = Raster.objects.all()
    serializer_class = RasterDatasourceSerializer
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]


class CustomDatasourceViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = Custom.objects.all()
    serializer_class = CustomDatasourceSerializer
    permission_classes = [GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]
