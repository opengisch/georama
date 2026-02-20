import json
import logging

from django.apps import apps
from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission, User
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext as _
from django.views import View
from qgis_server_light.interface.qgis import BBox
from qgis_server_light.interface.qgis import Config as QslConfig
from qgis_server_light.interface.qgis import Custom as QslCustom
from qgis_server_light.interface.qgis import Group as QslGroup
from qgis_server_light.interface.qgis import Raster as QslRaster
from qgis_server_light.interface.qgis import Vector as QslVector
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.core.menu import BreadCrumb
from georama.core.services.permission import DBService
from georama.core.views.generic.delete import GeoramaDeleteView
from georama.core.views.generic.detail import GeoramaDetailView
from georama.core.views.generic.list import GeoramaListView
from georama.core.views.generic.mixins import (
    GeoramaAnyPermissionRequiredMixin,
    GeoramaLoginRequiredMixin,
)
from georama.core.views.generic.update import GeoramaUpdateView
from georama.data_integration.models import (
    CustomDataSet,
    Project,
    RasterDataSet,
    VectorDataSet,
)
from georama.data_integration.services.project import FSService
from georama.maps.views import OgcServer
from georama.webgis.apps import central_app_label
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    Theme,
    ThemesJson,
)
from georama.webgis.models import LayerGroupMp
from georama.webgis.models import OgcServer as WebGisOgcServer
from georama.webgis.models import PublishedAsLayerWms, PublishedAsTheme


class PublishThemeFromProject(GeoramaLoginRequiredMixin, PermissionRequiredMixin, View):
    model = PublishedAsTheme
    permission_required = model.perm_add()

    @staticmethod
    def extend_bbox(bbox: BBox, bbox_extension: BBox):
        if bbox_extension.x_min < bbox.x_min or bbox.x_min == 0:
            bbox.x_min = bbox_extension.x_min
        if bbox_extension.y_min < bbox.y_min or bbox.y_min == 0:
            bbox.y_min = bbox_extension.y_min
        if bbox_extension.x_max > bbox.x_max or bbox.x_max == 0:
            bbox.x_max = bbox_extension.x_max
        if bbox_extension.y_max > bbox.y_max or bbox.y_max == 0:
            bbox.y_max = bbox_extension.y_max

    @staticmethod
    def bbox_center_position(bbox: BBox):
        return (
            (bbox.x_max + bbox.x_min) / 2,
            (bbox.y_max + bbox.y_min) / 2,
        )

    @staticmethod
    def find_dataset_by_name(
        dataset_name: str,
        datasets: list[QslGroup] | list[QslRaster] | list[QslVector] | list[QslCustom],
    ) -> QslGroup | QslVector | QslRaster | QslCustom | None:
        # TODO: This should be move directly to the QSL interface!
        for element in datasets:
            if element.name == dataset_name:
                return element
        return None

    def assemble_tree_to_treebeard(
        self,
        children: list[str],
        current_parent: LayerGroupMp,
        theme: PublishedAsTheme,
        project: Project,
        project_config: QslConfig,
        bbox: BBox,
        current_ogc_server: str | None = None,
    ):
        for child in children:
            node = current_parent.add_child(name=child)
            db_node = LayerGroupMp.objects.get(pk=node.pk)
            db_node.theme = theme
            db_node.save()
            group_match = self.find_dataset_by_name(child, project_config.datasets.group)
            if group_match:
                # TODO: Improve regarding GMF possibilities!
                db_node.title = group_match.title
                db_node.metadata = {}
                db_node.mixed = False
                db_node.ogc_server = current_ogc_server
                db_node.dimensions = {}
                db_node.save()
                self.assemble_tree_to_treebeard(
                    project_config.tree.find_by_name(child).children,
                    db_node,
                    theme,
                    project,
                    project_config,
                    bbox,
                    current_ogc_server,
                )
            else:
                raster_match = self.find_dataset_by_name(child, project_config.datasets.raster)
                vector_match = self.find_dataset_by_name(child, project_config.datasets.vector)
                custom_match = self.find_dataset_by_name(child, project_config.datasets.custom)
                if raster_match:
                    query = RasterDataSet.objects.filter(project=project, name=child)
                    if query.exists():
                        dataset = query.get()
                    else:
                        logging.error(f"Could not find raster dataset with name '{child}'")
                        raise AttributeError()
                    bbox_extenstion = BBox.from_string(dataset.bbox)
                    self.extend_bbox(bbox, bbox_extenstion)
                    PublishedAsLayerWms(
                        ogc_server=current_ogc_server,
                        name=dataset.name,
                        title=dataset.title,
                        raster_dataset=dataset,
                        layer_group=db_node,
                        dimensions={},
                        public=True,
                    ).save()
                elif vector_match:
                    query = VectorDataSet.objects.filter(project=project, name=child)
                    if query.exists():
                        dataset = query.get()
                    else:
                        logging.error(f"Could not find vector dataset with name '{child}'")
                        raise AttributeError()
                    bbox_extenstion = BBox.from_string(dataset.bbox)
                    self.extend_bbox(bbox, bbox_extenstion)
                    PublishedAsLayerWms(
                        ogc_server=current_ogc_server,
                        name=dataset.name,
                        title=dataset.title,
                        vector_dataset=dataset,
                        layer_group=db_node,
                        dimensions={},
                        public=True,
                    ).save()
                elif custom_match:
                    query = CustomDataSet.objects.filter(project=project, name=child)
                    if query.exists():
                        dataset = query.get()
                    else:
                        logging.error(f"Could not find custom dataset with name '{child}'")
                        raise AttributeError()
                    PublishedAsLayerWms(
                        ogc_server=current_ogc_server,
                        name=dataset.name,
                        title=dataset.title,
                        custom_dataset=dataset,
                        layer_group=db_node,
                        dimensions={},
                        public=True,
                    ).save()
                else:
                    logging.debug(f"Child {child} was not recognized as WebGIS Layer type")

    def get(self, request: HttpRequest, pk: str, **kwargs):
        project_db = Project.objects.get(pk=pk)
        highest_theme = self.model.objects.order_by("ordering").last()
        theme = self.model(
            name=project_db.name,
            title=project_db.title,
            project=project_db,
            metadata={"isLegendExpanded": True, "legend": False},
            ordering=highest_theme.ordering + 1 if highest_theme else 1,
            zoom=4,
        )
        theme.save()
        ogc_server = insert_internal_ogc_server(request)
        fss_project = FSService()
        project_from_config = fss_project.get(project_db.mandant.name, project_db.name)
        root_group = LayerGroupMp.add_root(name=theme.name)
        db_root_node = LayerGroupMp.objects.get(pk=root_group.pk)
        db_root_node.theme = theme
        db_root_node.save()
        bbox = BBox(0.0, 0.0, 0.0, 0.0)
        # Highly recursive task, we flatten the tree into treebeard structure
        self.assemble_tree_to_treebeard(
            # the element with empty string as name is always the root of the tree
            project_from_config.config.tree.find_by_name("").children,
            db_root_node,
            theme,
            project_db,
            project_from_config.config,
            bbox,
            ogc_server.name,
        )
        x, y = self.bbox_center_position(bbox)
        theme.location = [x, y]
        theme.save()
        next_url = request.GET.get("next")
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={request.get_host()},
        ):
            return redirect(next_url)
        return redirect(f"{central_app_label}:theme-list")


class Index(GeoramaListView):
    """
    This view is the apps landing page. It shows the available published
    layers a user can access. This is also available in public and shows
    layers which are public too. However, the important part is, that we
    use the Georama inherent ObjectPermissionSystem `PublishedAs` here.
    Not the Django model permission system.
    """

    model = PublishedAsTheme
    template_name = "webgis/index.html"

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
        ]

    def get_queryset(self):
        permitted_themes = []
        themes = self.model.objects.all()
        for theme in themes:
            if theme.has_general_permission(self.request.user, central_app_label):
                permitted_themes.append(theme)
        return permitted_themes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if (
            self.request.user.has_perm(self.model.perm_view())
            or self.request.user.has_perm(self.model.perm_change())
            or self.request.user.has_perm(self.model.perm_delete())
            or self.request.user.has_perm(self.model.perm_add())
            or self.request.user.has_perm(self.model.perm_manage_permissions())
        ):
            context["breadcrumb_action_url"] = f"{central_app_label}:theme-list"
            context["breadcrumb_action_icon"] = "fa fa-wrench"
            context["breadcrumb_action_title"] = _("Manage Themes")
            context["breadcrumb_action_tooltip"] = _("Manage and publish themes")
        context["webgis_url"] = settings.WEBGISURL

        return context


class ThemesListView(
    GeoramaLoginRequiredMixin, GeoramaAnyPermissionRequiredMixin, GeoramaListView
):
    model = PublishedAsTheme
    template_name = "webgis/list.html"
    permission_required = [
        model.perm_view(),
        model.perm_change(),
        model.perm_delete(),
        model.perm_add(),
        model.perm_manage_permissions(),
    ]

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes")),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.has_perm(self.model.perm_add()):
            context["breadcrumb_action_url"] = f"{central_app_label}:theme-add-project-list"
            context["breadcrumb_action_icon"] = "fa fa-circle-plus"
            context["breadcrumb_action_title"] = _("Publish Theme")
            context["breadcrumb_action_tooltip"] = _("Publish a new theme from QGIS project")
        return context


class PublishProjectListView(
    GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView
):
    model = Project
    template_name = "webgis/publish.html"
    permission_required = PublishedAsTheme.perm_add()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(_("Add")),
        ]


class ThemeDetailView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDetailView):
    model = PublishedAsTheme
    permission_required = model.perm_view()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(self.object.title or self.object.name),
        ]

    def get_context_data(self, **kwargs):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        context = super().get_context_data(**kwargs)
        context["update_view_name"] = f"{app_menu.app_label}:theme-update"
        context["delete_view_name"] = f"{app_menu.app_label}:theme-delete"
        context["permission_view_name"] = f"{app_menu.app_label}:theme-permission-list"
        context["perm_change"] = self.request.user.has_perm(self.model.perm_change())
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context


class ThemeUpdateView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaUpdateView):
    model = PublishedAsTheme
    fields = [
        "title",
        "name",
        "description",
        "public",
    ]
    permission_required = model.perm_change()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{app_menu.app_label}:theme-detail", kwargs={"pk": self.kwargs["pk"]}
                ),
            ),
        ]

    def get_context_data(self, **kwargs):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        context = super().get_context_data(**kwargs)
        context["delete_view_name"] = f"{app_menu.app_label}:theme-delete"
        context["permission_view_name"] = f"{app_menu.app_label}:theme-permission-list"
        context["perm_manage_permission"] = self.request.user.has_perm(
            self.model.perm_manage_permissions()
        )
        context["perm_delete"] = self.request.user.has_perm(self.model.perm_delete())
        return context


class ThemeDeleteView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDeleteView):
    model = PublishedAsTheme
    success_url = reverse_lazy(f"{central_app_label}:theme-list")
    permission_required = model.perm_delete()

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(
                self.object.title or self.object.name,
                reverse(
                    f"{app_menu.app_label}:theme-detail", kwargs={"pk": self.kwargs["pk"]}
                ),
            ),
        ]


class PermissionView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaDetailView):
    model = Permission
    template_name = "core/permission.html"
    permission_required = PublishedAsTheme.perm_manage_permissions()

    def get_object(self, queryset=None):
        object_pk = self.kwargs.get("pk")
        dbs_permission = DBService(PublishedAsTheme, central_app_label)
        return dbs_permission.get_permission_lookup(object_pk)

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(
                PublishedAsTheme.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:theme-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["add_user_url"] = reverse(
            f"{central_app_label}:theme-permission-user-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        context["add_group_url"] = reverse(
            f"{central_app_label}:theme-permission-group-list",
            kwargs={"pk": self.kwargs.get("pk")},
        )
        return context


class UserListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    model = User
    template_name = "core/user.html"
    permission_required = PublishedAsTheme.perm_manage_permissions()

    def get_queryset(self):
        return (
            User.objects.exclude(
                user_permissions__codename__icontains=str(self.kwargs.get("pk"))
            )
            .exclude(pk=None)
            .filter(is_superuser=False)
        )

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Themes"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(
                PublishedAsTheme.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:theme-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(
                PermissionView.model._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:theme-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(PublishedAsTheme, central_app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            f"{central_app_label}:theme-permission-list", kwargs={"pk": self.kwargs.get("pk")}
        )
        return context


class GroupListView(GeoramaLoginRequiredMixin, PermissionRequiredMixin, GeoramaListView):
    model = Group
    template_name = "core/group.html"
    permission_required = PublishedAsTheme.perm_manage_permissions()

    def get_queryset(self):
        return Group.objects.exclude(
            permissions__codename__icontains=str(self.kwargs.get("pk"))
        )

    def get_breadcrumbs(self):
        app_menu = apps.get_app_config(central_app_label).app_menu()
        return [
            BreadCrumb(app_menu.title, reverse(f"{app_menu.app_label}:index")),
            BreadCrumb(_("Manage Layers"), reverse(f"{app_menu.app_label}:theme-list")),
            BreadCrumb(
                PublishedAsTheme.objects.get(pk=self.kwargs.get("pk")).title,
                reverse(
                    f"{app_menu.app_label}:theme-detail", kwargs={"pk": self.kwargs.get("pk")}
                ),
            ),
            BreadCrumb(
                PermissionView.model._meta.verbose_name,
                reverse(
                    f"{app_menu.app_label}:theme-permission-list",
                    kwargs={"pk": self.kwargs.get("pk")},
                ),
            ),
            BreadCrumb(self.model._meta.verbose_name),
        ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dbs_permission = DBService(PublishedAsTheme, central_app_label)
        context["read_permission_id"] = (
            dbs_permission.get_by_object_pk(self.kwargs.get("pk"))
            .filter(codename__icontains="read")
            .get()
            .pk
        )
        context["success_url"] = reverse(
            f"{central_app_label}:theme-permission-list", kwargs={"pk": self.kwargs.get("pk")}
        )
        return context


class Themes(View):
    def assemble_themes_tree_from_treebeard(
        self,
        node: LayerGroupMp,
        layer_group: LayerGroup | Theme,
        config: ThemesJson,
        user: User,
    ):
        for child in node.get_children():
            if child.get_children():
                # this is a group to unpack
                group = child.as_dataclass()
                layer_group.children.append(group)
                self.assemble_themes_tree_from_treebeard(child, group, config, user)
            else:
                if hasattr(child, "wms_datasets"):
                    # we filter for permission on the one-to-one field connected
                    # published_as element
                    if child.wms_datasets.has_read_permission(user, central_app_label):
                        layer_group.children.append(child.wms_datasets.as_dataclass(config))
                elif hasattr(child, "wmts_datasets"):
                    layer_group.children.append(child.wmts_datasets.as_dataclass())
                else:
                    logging.debug(
                        f"We are not aware of the passed type of {child}"
                        f"in group {node}, skipping ..."
                    )

    def get(self, request: HttpRequest, format: str):
        geogirafe_config = ThemesJson()
        for ogc_server in WebGisOgcServer.objects.all():
            geogirafe_config.ogc_servers.append(ogc_server.as_dataclass())
        for theme in PublishedAsTheme.objects.all():
            if theme.has_general_permission(self.request.user, central_app_label):
                theme_object = theme.as_dataclass()
                if theme_object.icon is None:
                    theme_object.icon = request.build_absolute_uri(theme.icon_default)
                geogirafe_config.themes.append(theme_object)
                root_node = theme.tree_elements.first().get_root()
                self.assemble_themes_tree_from_treebeard(
                    root_node, theme_object, geogirafe_config, request.user
                )
        result_dict = {
            "themes": DictEncoder().encode(geogirafe_config.themes),
            "ogcServers": {},
            "errors": [],
            "background_layers": [],
        }
        for ogc_server in geogirafe_config.ogc_servers:
            result_dict["ogcServers"][ogc_server.name] = DictEncoder().encode(ogc_server)
        return HttpResponse(
            json.dumps(result_dict, indent=2), status=200, content_type="application/json"
        )


class GeoGirafe(View):
    # TODO: This is prepared for later approach where we serve GeoGirafe
    #  directly through Django

    def get(self, request: HttpRequest, mandant_name: str):
        return render(request, "geogirafe/index.html")


class Config(View):
    # TODO: This is prepared for later approach where we serve GeoGirafe
    #  directly through Django

    def get(self, request: HttpRequest, mandant_name: str):
        config_dict = {
            "general": {"locale": "en"},
            "languages": {
                "translations": {
                    "de": ["Mock/de.json"],
                    "en": ["Mock/en.json"],
                    "fr": ["Mock/fr.json"],
                },
                "defaultLanguage": "en",
            },
            "themes": {"url": "themes.json", "defaultTheme": "cadastre"},
            "basemaps": {
                "show": True,
                "defaultBasemap": "orthophoto",
                "OSM": False,
                "SwissTopoVectorTiles": True,
            },
            "treeview": {"useLegendIcons": False},
            "search": {
                "url": "https://geomapfish-demo-2-8.camptocamp.com/search?limit=30&partitionlimit=5&interface=desktop&query=###SEARCHTERM###&lang=###SEARCHLANG###"
            },
            "print": {
                "url": "https://geomapfish-demo-2-8.camptocamp.com/printproxy/",
                "formats": ["png", "pdf", "jpg", "jpeg", "notvalid"],
                "defaultFormat": "pdf",
                "layouts": ["1 A4 portrait", "4 A3 landscape"],
                "defaultLayout": "1 A4 portrait",
                "scales": [500000, 25000, 10000, 99999, 5000, 2500],
                "attributeNames": ["legend", "title", "comments"],
                "printLegend": {"showGroupsTitle": True},
            },
            "share": {  # TODO: This is prepared for later approach where we serve GeoGirafe directly through Django  # noqa: E501
                "service": "lstu",
                "createUrl": "https://lstu.fr/a",
            },
            "projections": {"EPSG:3857": "W-M", "EPSG:4326": "WGS84", "EPSG:2056": "LV95"},
            "map": {
                "srid": "EPSG:2056",
                "scales": [
                    1000000,
                    500000,
                    200000,
                    100000,
                    50000,
                    20000,
                    10000,
                    5000,
                    2000,
                    1000,
                    500,
                    200,
                ],
                "startPosition": "2612500,1268050",
                "startZoom": 8,
                "maxExtent": "2200000,1040000,3000000,1310000",
            },
            "map3d": {
                "terrainUrl": "https://terrain100.geo.admin.ch/1.0.0/ch.swisstopo.terrain.3d/",
                "tilesetsUrls": [
                    "https://vectortiles100.geo.admin.ch/3d-tiles/ch.swisstopo.swisstlm3d.3d/20201020/tileset.json"
                ],
            },
            "bookmarks": {"service": "localStorage", "get": "", "post": ""},
        }
        return HttpResponse(
            json.dumps(config_dict, indent=2), status=200, content_type="application/json"
        )


class OgcServerWebgis(OgcServer):
    model = PublishedAsLayerWms


def insert_internal_ogc_server(request: HttpRequest) -> WebGisOgcServer:
    """
    Checks if internal OGC server was already added. If it was added, it returns
    the DB entity if it was not added, it adds it and returns the added one.

    Args:
        request: Django request as it comes from framework request.

    Returns:
        The ogc server db entity or None if a more then one match was found
        (that would be an error).
    Raises:
        AttributeError: If more than one OGC-Server was found with the name.
    """
    webgis_ogc_server_name = "georama.webgis"
    url = f'{request.build_absolute_uri("/webgis")}/maps?'
    ogc_servers = WebGisOgcServer.objects.filter(name=webgis_ogc_server_name).all()
    if len(ogc_servers) == 0:
        ogc_server = WebGisOgcServer(
            url=url,
            url_wfs=url,
            type=webgis_ogc_server_name,
            credential=False,
            image_type="image/png",
            wfs_support=True,
            is_single_tile=False,
            namespace="https://www.opengis.ch/georama",
            name=webgis_ogc_server_name,
            description="The Georama OGC Server which publishes "
            "all configured WebGIS Layers.",
            attributes={},
        )
        ogc_server.save()
    elif len(ogc_servers) == 1:
        ogc_server = ogc_servers[0]
    else:
        logging.error(f"More than one OGC-Server was found for name {webgis_ogc_server_name}")
        raise AttributeError()
    return ogc_server


def admin_publish_dataset_as_wms(request: HttpRequest, dataset_type: str, dataset_id: str):
    """
    helper function to hide actual connection in the database but make publishing straight
    forward.
    """
    allowed_dataset_types = ["raster", "vector", "custom"]
    ogc_server = insert_internal_ogc_server(request)
    if dataset_type not in allowed_dataset_types:
        return HttpResponseNotFound()
    if dataset_type == "raster":
        published_as_wms = PublishedAsLayerWms(
            raster_dataset=RasterDataSet.objects.filter(id=dataset_id)[0]
        )
    elif dataset_type == "vector":
        published_as_wms = PublishedAsLayerWms(
            vector_dataset=VectorDataSet.objects.filter(id=dataset_id)[0]
        )
    elif dataset_type == "custom":
        published_as_wms = PublishedAsLayerWms(
            custom_dataset=CustomDataSet.objects.filter(id=dataset_id)[0]
        )
    else:
        return HttpResponseNotFound()
    published_as_wms.ogc_server = ogc_server.name
    published_as_wms.save()
    return redirect("admin:webgis_publishedaslayerwms_changelist")


def translation_json(request: HttpRequest):
    translation = {"de": {}}
    for layer_group in LayerGroupMp.objects.all():
        translation["de"][layer_group.name] = layer_group.title
    for theme in PublishedAsTheme.objects.all():
        translation["de"][theme.name] = theme.title
    for layer in PublishedAsLayerWms.objects.all():
        translation["de"][layer.name] = layer.title
    return HttpResponse(
        json.dumps(translation, indent=2), status=200, content_type="application/json"
    )
