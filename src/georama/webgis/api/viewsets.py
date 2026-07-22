from django.apps import apps
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, renderers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.common.api import (
    GeoramaManagerWithPermissionsViewSet,
    GeoramaModelPermissions,
    GeoramaObjPermViewSetReadOnly,
)
from georama.core.common.menu import ActionType, Breadcrumb, BreadcrumbAction
from georama.core.common.request import GeoramaDrfRequest
from georama.integration.models import Project
from georama.maps.services.wfs_2_0_0 import WfsOperation
from georama.webgis.adapters.qsl import WmsLayerIndex, theme_json_from_project_config
from georama.webgis.api.serializers import (
    ThemeGroupObjectPermissionSerializer,
    ThemeGroupPermissionBulkActionSerializer,
    ThemeSerializer,
    ThemeUserObjectPermissionSerializer,
    ThemeUserPermissionBulkActionSerializer,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    OgcServer as GGOgcServer,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import OgcServers
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import Theme as GGTheme
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    ThemesJson as GGThemesJson,
)
from georama.webgis.interfaces.geomapfish.themes_json_2_8.parsers import CustomDictDecoder
from georama.webgis.models import Metadata, Theme, WmsLayer


class ManageThemeViewSet(GeoramaManagerWithPermissionsViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []

    user_permissions_serializer_class = ThemeUserObjectPermissionSerializer
    group_permissions_serializer_class = ThemeGroupObjectPermissionSerializer
    user_permissions_bulk_action_serializer_class = ThemeUserPermissionBulkActionSerializer
    group_permissions_bulk_action_serializer_class = ThemeGroupPermissionBulkActionSerializer

    @property
    async def bread_crumb_action_context(self):
        """Prepares the breadcrumb action to add a theme.

        Returns:
            The context with an action to add a new theme in case the user has add-permission
            on the theme model and is permitted to view projects.
        """
        context = {}
        perm_checker = GeoramaModelPermissions()
        # post is the DRF method which is used for add/create a new object
        local_perms = perm_checker.get_required_permissions("POST", self.queryset.model)
        # we also check if the remote data can be used (view)
        remote_perms = perm_checker.get_required_permissions("GET", Project)
        if all(
            [
                await self.request.user.ahas_perms(local_perms),
                await self.request.user.ahas_perms(remote_perms),
            ]
        ):
            context["breadcrumb_action"] = BreadcrumbAction(
                url=reverse("integration:manager-project-list"),
                tooltip=_("Publish a Project as Theme"),
                hint=_("Select a project to publish it as a new Theme"),
                title=_("Theme"),
                type=ActionType.EMBEDDED,
                icon="fa fa-circle-plus",
            )
        return context

    @staticmethod
    async def transfer_to_theme(project: Project) -> Theme:
        highest_theme = await Theme.objects.order_by("ordering").alast()
        metadata = Metadata(title=project.name)
        await metadata.asave()

        theme = Theme(
            project=project,
            metadata=metadata,
            public=False,
            ordering=highest_theme.ordering + 1 if highest_theme else 1,
            zoom=4,
            # temporarily we set this
            theme_json={},
        )
        await theme.asave()
        return theme

    @property
    def publish_from_project_url_name(self):
        return self.url_name("publish-from-project")

    @action(detail=False, methods=["post"], url_path="publish_from_project")
    async def publish_from_project(self, request: GeoramaDrfRequest, *args, **kwargs):
        qs = Project.objects.organisation_objects(request.georama_organisation)
        project = await qs.aget(id=request.data["pk"])
        wms_layer_index: WmsLayerIndex = {}
        theme = await self.transfer_to_theme(project)
        async for ds in project.datasources.all():
            wl = WmsLayer(
                datasource=ds,
                extent=ds.bbox,
                extent_wgs84=ds.bbox_wgs84,
                metadata=Metadata(title=ds.name),
                theme=theme,
            )
            wms_layer_index[ds.qgis_layer_id] = wl
        await Metadata.objects.abulk_create(
            [wms_layer.metadata for wms_layer in wms_layer_index.values()]
        )
        await WmsLayer.objects.abulk_create(wms_layer_index.values())
        gg_theme = await theme_json_from_project_config(
            str(theme.id), theme.icon_default, project.config_as_dataclass, wms_layer_index
        )
        theme.theme_json = DictEncoder().encode(gg_theme)
        await theme.asave()
        return redirect(reverse(self.url_name_list))


class ThemeViewSet(GeoramaObjPermViewSetReadOnly):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
    required_obj_perms = ["webgis.view_published_theme"]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["metadata__title"]
    ordering_fields = ["metadata__title", "public"]
    filterset_fields = []

    async def get_breadcrumbs(self):
        app_menu = apps.get_app_config(self.queryset.model._meta.app_label).app_menu()
        return [
            Breadcrumb(app_menu.title),
            Breadcrumb(self.queryset.model._meta.verbose_name_plural),
        ]

    def georama_ogc_server(self, request: GeoramaDrfRequest) -> GGOgcServer:
        return GGOgcServer(
            url=request.build_absolute_uri(reverse("webgis:ows_entry")),
            urlWfs=request.build_absolute_uri(reverse("webgis:ows_entry")),
            type=settings.WEBGIS_OGC_SERVER_NAME,
            credential=False,
            imageType="image/png",
            isSingleTile=False,
            name=settings.WEBGIS_OGC_SERVER_NAME,
            namespace=WfsOperation.own_namespace_domain,
            wfsSupport=True,
        )

    @action(detail=False, methods=["GET"], renderer_classes=[renderers.JSONRenderer])
    async def geogirafe(self, request: GeoramaDrfRequest, *args, **kwargs):
        qs = await self.public_or_object_permission(self.get_queryset())

        themes_json = GGThemesJson(
            ogc_servers=OgcServers(georama_webgis=self.georama_ogc_server(request)), themes=[]
        )

        async for theme in qs.all():
            # this is necessary, since the automatically generated demo data has no valid json
            if theme.theme_json != {}:
                gg_theme = CustomDictDecoder().decode(theme.theme_json, GGTheme)
                gg_theme.icon = request.build_absolute_uri(gg_theme.icon)
                themes_json.themes.append(
                    # NOTE: We use a special extended encoder here, not the default XSData variant!
                    gg_theme
                )

        return Response(data=DictEncoder().encode(themes_json), status=status.HTTP_200_OK)
