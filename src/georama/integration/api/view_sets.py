from pathlib import Path

import httpx
from adrf.mixins import get_data
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from qgis_server_light.interface.exporter.api import ExportParameters
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from xsdata.formats.dataclass.serializers import JsonSerializer

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
from georama.integration.lib.qgis_project_file_structure import QgisProject, QgisProjectCollection
from georama.integration.models import Custom, Project, Raster, Vector, VectorField


class ProjectViewSet(OrganisationalModelViewSet, GeoramaAsyncTemplateModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminUser, GeoramaModelPermissions]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]
    list_path_template_name: str = "integration/drf/project/path_list.html"

    async def _get_model_permissions(self):
        """
        We do not want to allow this from the GUI, everything should be done through
        the integration process (integrate non-integrated projects).
        Returns:
            The action lookup
        """
        return {
            "can_add": False,
            "can_change": False,
            "can_delete": False,
        }

    @staticmethod
    async def call_qsl_exporter(path: Path):
        url = settings.QSL_EXPORTER_URL
        async with httpx.AsyncClient() as client:
            r = await client.post(
                url,
                data=JsonSerializer().render(
                    ExportParameters(
                        path,
                        output_format="json",
                    )
                ),
                headers={"Content-Type": "application/json"},
            )
            return r

    @action(detail=False, methods=["get", "post"], url_path="non_integrated")
    async def non_integrated(self, request: GeoramaDrfRequest, *args, **kwargs):
        organisation_folder = settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER
        if request.georama_organisation:
            organisation_folder = request.georama_organisation.domain

        if request.POST:
            project_path = request.data["path"]
            project_file = QgisProject(path=project_path, organisation=organisation_folder)  # noqa: F841
            project = await Project.objects.acreate(  # noqa: F841
                path=project_path, organisation=request.georama_organisation
            )

        existing_project_paths = {
            Path(p) async for p in Project.objects.values_list("path", flat=True)
        }
        collection = QgisProjectCollection(organisation_folder)
        filtered_file_list = collection.projects_filtered(existing_project_paths)
        pqs = await self.apaginate_queryset(filtered_file_list)

        if request.accepted_renderer.format == "html":
            context = await self._prepare_many_context()
            context["organisation"] = organisation_folder
            context["object_list"] = pqs
            context["limit"] = self.paginator.limit
            context.update(await self._get_model_permissions())
            context.update(self.paginator.get_html_context())

            return Response(context, template_name=self.list_path_template_name)
        else:
            if pqs is not None:
                serializer = FileSystemProjectSerializer(
                    [
                        {
                            "project_path": p.path_from_orga,
                            "config_path": p.config_path_from_orga if p.has_config else None,
                        }
                        for p in pqs
                    ],
                    many=True,
                )
                data = await get_data(serializer)
                return await self.get_apaginated_response(data)
            serializer = FileSystemProjectSerializer(
                [
                    {
                        "project_path": p.path_from_orga,
                        "config_path": p.config_path_from_orga if p.has_config else None,
                    }
                    for p in filtered_file_list
                ],
                many=True,
            )
            data = await get_data(serializer)
            return Response(data, status=status.HTTP_200_OK)


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
