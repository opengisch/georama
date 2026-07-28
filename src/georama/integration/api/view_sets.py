import logging
from pathlib import Path

from adrf.mixins import get_data
from django.apps import apps
from django.conf import settings
from django.http import Http404, HttpResponseServerError
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from qgis_server_light.interface.exporter.api import ExportResult
from qgis_server_light.interface.exporter.extract import Config
from qgis_server_light.interface.exporter.extract import Custom as QslCustom
from qgis_server_light.interface.exporter.extract import Raster as QslRaster
from qgis_server_light.interface.exporter.extract import Vector as QslVector
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from xsdata.formats.dataclass.parsers import DictDecoder, JsonParser
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.api import (
    GeoramaManagerViewSet,
    GeoramaModelPermissions,
    OrganisationalModelViewSet,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.api.serializers import (
    CustomDatasourceSerializer,
    DatasourceSerializer,
    FieldSerializer,
    FileSystemProjectSerializer,
    ProjectSerializer,
    RasterDatasourceSerializer,
    VectorDatasourceSerializer,
)
from georama.integration.lib.qgis_project_file_structure import QgisProject, QgisProjectCollection
from georama.integration.models import Custom, Project, Raster, Vector, VectorField
from georama.integration.models.datasource import Datasource
from georama.maps.adapter.qsl import call_qsl_exporter


class ManageProjectViewSet(GeoramaManagerViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name", "path"]
    ordering_fields = ["name", "path"]
    filterset_fields = ["name"]
    list_body_path_partial_template_name: str = (
        "integration/drf/project/partials/list_body_path.html"
    )
    list_body_partial_template_name: str = "integration/drf/project/partials/list_body.html"
    show_template_name = "integration/drf/project/show.html"

    @property
    async def bread_crumb_action_context(self):
        """Prepares the breadcrumb action to add a project.

        Returns:
            The context with an action to add a new project in case the user has either
            add, delete or change permission or is admin user.
        """
        context = {}
        model_perms = await self._get_model_permissions()
        url_action_target = reverse(self.non_integrated_url_name)
        if (
            any(model_perms.values()) or self.request.user.is_superuser
        ) and self.request.path != url_action_target:
            context["breadcrumb_action"] = BreadcrumbAction(
                url=url_action_target,
                tooltip=_("Integrate projects from QGIS files available on disk"),
                hint=_("Select a project to integrate it into Georama"),
                title=_("QGIS Project"),
                type=ActionType.LINKED,
                icon="fa fa-circle-plus",
            )
        return context

    async def _get_model_permissions(self) -> dict:
        """
        Returns a dictionary of permissions.
        Projects do not have object permissions, so set this permission to False.
        """
        # TODO PI: Is this a valid way to deactivate the permission button for integration?
        permissions = await super()._get_model_permissions()
        permissions["can_manage_permissions"] = False
        return permissions

    @staticmethod
    async def integrate_project(project_db: Project, project_json: Config):
        project_json_datasets = (
            project_json.datasets.vector
            + project_json.datasets.raster
            + project_json.datasets.custom
        )
        for layer in project_json_datasets:
            if layer.is_spatial:
                if isinstance(layer, QslVector):
                    datasource_model = Vector
                elif isinstance(layer, QslRaster):
                    datasource_model = Raster
                elif isinstance(layer, QslCustom):
                    datasource_model = Custom
                else:
                    raise LookupError("Unexpected datasource type was passed")
                # We don't need to filter for organisation here again, since the project_db
                # is bound to it already.
                qs = datasource_model.objects.filter(qgis_layer_id=layer.id, project=project_db)
                if await qs.aexists():
                    logging.debug(
                        f" Dataset was found and will be updated {layer.name}"
                        f" (qgis-layer-id: {layer.id})"
                    )
                    datasource = await qs.aget()
                else:
                    logging.debug(
                        f" New dataset will be added {layer.name} (qgis-layer-id: {layer.id}) "
                    )
                    datasource = datasource_model(qgis_layer_id=layer.id, project=project_db)
                await datasource.set_values_from_qsl(layer)
                await datasource.asave()
                logging.debug(
                    f" ✓ Dataset {layer.name} (qgis-layer-id: {layer.id})"
                    f" was written to DB successfully."
                )
                if isinstance(datasource, Vector):
                    logging.debug(" Handling of related fields.")
                    layer: QslVector
                    for qsl_field in layer.fields:
                        field_qs = VectorField.objects.filter(
                            name=qsl_field.name,
                            datasource=datasource,
                        )
                        if not await field_qs.aexists():
                            logging.debug(
                                f"   New Field {qsl_field.name} "
                                f"(type: {qsl_field.type}) will be added."
                            )
                            field = VectorField(
                                datasource=datasource,
                            )
                        else:
                            logging.debug(
                                f"   Field {qsl_field.name} (type: {qsl_field.type})"
                                f" was found and will be updated."
                            )
                            field: VectorField = await field_qs.aget()
                        await field.set_values_from_qsl(qsl_field)
                        await field.asave()
                        logging.debug(
                            f"   ✓ Field {field.name} (type: {field.type})"
                            f" was written to DB successfully."
                        )
                    logging.debug("   Cleaning out old fields...")
                    async for field_db in VectorField.objects.filter(datasource=datasource).all():
                        field_match = layer.get_field_by_name(field_db.name)
                        if field_match is None:
                            logging.debug(
                                f'    Deleting field "{field_db.name}" of vector '
                                f"dataset {datasource.name}"
                                f" since it was"
                                " not in project config anymore"
                            )
                            await field_db.adelete()
                    logging.debug("   ✓ Finished - Cleaning out old fields...")
        logging.debug(" Cleaning out old datasources.")
        async for datasource_db in Datasource.objects.filter(project=project_db).all():
            dataset_match = project_json.datasets.find_dataset_by_id(datasource_db.qgis_layer_id)
            if dataset_match is None:
                logging.debug(
                    f"    Deleting datasource {datasource_db.name} since it was not"
                    f" in project config anymore"
                )
                await datasource_db.adelete()
        logging.debug(" ✓ Finished - Cleaning out old datasources.")
        return None

    @property
    def non_integrated_url_name(self):
        return self.url_name("non-integrated")

    @action(detail=False, methods=["get", "post"], url_path="non_integrated")
    async def non_integrated(self, request: GeoramaDrfRequest, *args, **kwargs):
        organisation_folder = settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER
        if request.georama_organisation:
            organisation_folder = request.georama_organisation.domain

        if request.POST:
            project_path = request.data["path"]
            project_file = QgisProject(path=project_path, organisation=organisation_folder)  # noqa: F841
            if not project_file.project_path.exists():
                raise Http404(f"Project with path {project_file.project_path} not found")
            response = await call_qsl_exporter(project_file.path_from_root)
            if response.status_code != status.HTTP_200_OK:
                msg = _("Communication with Exporter API was not successful STATUSCODE:")
                return HttpResponseServerError(f"{msg} {response.status_code}")
            else:
                result = DictDecoder().decode(response.json(), ExportResult)
            if not result.successful:
                msg = result.content if settings.DEBUG else _("A problem occurred while exporting.")
                return HttpResponseServerError(msg)
            project_json = JsonParser().from_string(result.content, Config)
            qs = Project.objects.filter(
                path=project_path,
                organisation=request.georama_organisation,
            )
            if await qs.aexists():
                project_db = await qs.aget()
            else:
                project_db = Project(
                    path=project_path,
                    organisation=request.georama_organisation,
                )
            project_db.config = DictEncoder().encode(project_json)
            project_db.name = project_json.project.name
            project_db.qgis_version = project_json.project.version
            await project_db.asave()

            await self.integrate_project(project_db, project_json)
            return redirect(reverse("integration:manager-project-non-integrated"))

        existing_project_paths = {
            Path(p)
            async for p in Project.objects.organisation_objects(
                organisation=request.georama_organisation
            ).values_list("path", flat=True)
        }
        collection = QgisProjectCollection(organisation_folder)
        filtered_file_list = collection.projects_filtered(existing_project_paths)
        pqs = await self.apaginate_queryset(filtered_file_list)

        if request.accepted_renderer.format == "html":
            context = await super()._prepare_many_context()
            context["breadcrumbs"][-1].view_name = self.reverse_action("list")
            context["breadcrumbs"].append(Breadcrumb(_("Non integrated Projects")))
            context["organisation"] = organisation_folder
            context["object_list"] = pqs
            context["limit"] = self.paginator.limit
            context["list_body_partial"] = self.list_body_path_partial_template_name
            context.update(await self._get_model_permissions())
            context.update(self.paginator.get_html_context())
            return Response(context, template_name=self.list_template_name)
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

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]


class ManageDatasourceViewSet(GeoramaManagerViewSet):
    queryset = Datasource.objects.all()
    serializer_class = DatasourceSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]
    list_body_partial_template_name: str = "integration/drf/datasource/partials/list_body.html"

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]


class ManageVectorDatasourceViewSet(GeoramaManagerViewSet):
    queryset = Vector.objects.all()
    serializer_class = VectorDatasourceSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]


class ManageFieldViewSet(OrganisationalModelViewSet):
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


class ManageRasterDatasourceViewSet(OrganisationalModelViewSet):
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


class ManageCustomDatasourceViewSet(OrganisationalModelViewSet):
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
