from pathlib import Path

from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response

from georama.core.common.api import (
    GeoramaAsyncTemplateModelViewSet,
    GeoramaModelPermissions,
    OrganisationalModelViewSet,
)
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.api.serializers import (
    CustomDatasourceSerializer,
    FieldSerializer,
    FileSystemProjectSerializer,
    ProjectSerializer,
    RasterDatasourceSerializer,
    VectorDatasourceSerializer,
)
from georama.integration.models import Custom, Project, Raster, Vector, VectorField


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
    filterset_fields = ["name"]

    @action(detail=False, methods=["get"], url_path="non_integrated")
    async def non_integrated(self, request: GeoramaDrfRequest, *args, **kwargs):
        organisation_folder = (
            request.georama_organisation or settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER
        )
        integration_root: Path = settings.DATA_INTEGRATION_ROOT / organisation_folder
        existing_project_paths = {p async for p in Project.objects.values_list("path", flat=True)}
        project_paths = settings.DATA_INTEGRATION_ROOT.rglob("*.qg[sz]")
        serializer = FileSystemProjectSerializer(
            [
                {"path": path.relative_to(integration_root)}
                for path in project_paths
                if path not in existing_project_paths
            ],
            many=True,
        )
        return Response(serializer.data)


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
    queryset = VectorField.objects.all()
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
