import json
import logging
from typing import List

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.views import View
from qgis_server_light.interface.qgis import Config as QslConfig
from qgis_server_light.interface.qgis import Crs
from qgis_server_light.interface.qgis import Custom as QslCustom
from qgis_server_light.interface.qgis import Group as QslGroup
from qgis_server_light.interface.qgis import Raster as QslRaster
from qgis_server_light.interface.qgis import Vector as QslVector
from qgis_server_light.interface.qgis import WmsSource, WmtsSource
from xsdata.formats.dataclass.serializers import DictEncoder

from georama.data_integration.models import (
    CustomDataSet,
    Mandant,
    Project,
    RasterDataSet,
    VectorDataSet,
)
from georama.data_integration.views import RegisterQgisProject
from georama.maps.views import OgcServer
from georama.webgis.apps import WebgisConfig
from georama.webgis.forms import GEOPORTAL_URLS, HomeForm
from georama.webgis.interfaces.geomapfish import load_geoportal_config_from_url
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    Theme,
    ThemesJson,
    WmsLayer,
    WmtsLayer,
)
from georama.webgis.models import LayerGroupMp
from georama.webgis.models import OgcServer as WebGisOgcServer
from georama.webgis.models import (
    PublishedAsLayerWms,
    PublishedAsLayerWmts,
    PublishedAsTheme,
)

appname = WebgisConfig.get_simple_appname()


def home(request):
    form = HomeForm()

    return render(request, "webgis.html", {"form": form})


def assemble_tree_to_treebeard(
    children: list[LayerGroup | WmsLayer | WmtsLayer],
    current_parent: LayerGroupMp,
    theme: PublishedAsTheme,
    project: Project,
    geoportal_config: ThemesJson,
    current_ogc_server: str | None = None,
):
    for child in children:
        node = current_parent.add_child(name=child.name)
        db_node = LayerGroupMp.objects.get(pk=node.pk)
        db_node.theme = theme
        db_node.themes_json_id = child.id
        db_node.save()
        if isinstance(child, LayerGroup):
            if hasattr(child, "ogcServer"):
                if child.ogcServer is not None:
                    current_ogc_server = child.ogcServer
                    logging.debug(f"set current_ogc_server by group: {current_ogc_server}")
                else:
                    logging.debug(
                        "New nested group but we leave ogc server because it was not redefined"
                    )
            db_node.metadata = DictEncoder().encode(child.metadata)
            db_node.mixed = child.mixed
            db_node.ogc_server = current_ogc_server
            db_node.dimensions = DictEncoder().encode(child.dimensions)

            db_node.save()
            assemble_tree_to_treebeard(
                child.children, db_node, theme, project, geoportal_config, current_ogc_server
            )
        else:
            if isinstance(child, WmsLayer):
                if child.ogcServer is None and current_ogc_server is not None:
                    child.ogcServer = current_ogc_server
                ogc_server = geoportal_config.get_ogc_server_by_name(child.ogcServer)
                query = RasterDataSet.objects.filter(project=project, name=child.name)
                if query.exists():
                    dataset = query.get()
                else:
                    source = WmsSource(
                        # TODO: This comes from QGIS and seem to bool if legend is shown or not, we need to know
                        #  how this transports to geogirafe
                        contextual_wms_legend="0",
                        # TODO: This we should make configurable or read it from capabilities of OGC Server
                        crs="EPSG:2056",
                        # TODO: This is normally a QGIS/Client specific thing, probably we can remove it from the
                        #  dataclass
                        dpi_mode="",
                        # TODO: Find why, how this is possible to fill
                        feature_count=0,
                        format=child.imageType,
                        layers=child.layers,
                        url=ogc_server.url,
                    )
                    dataset = RasterDataSet(
                        project=project,
                        name=child.name,
                        # TODO: Fix this to correct title (via translation?)
                        title=child.name.title(),
                        # TODO: should we fetch this from capabilities?
                        bbox="0,0,0,4000000,4000000,4000000",
                        # TODO: should we fetch this from capabilities?
                        bbox_wgs84="-90.0,-180.0,0.0,90.0,180.0,10000",
                        path=geoportal_config.get_ogc_server_by_name(child.ogcServer).url,
                        style="",
                        # this is wms for WMTS & WMS since (that comes from QGIS which handle both through
                        #   the same driver)
                        driver="wms",
                        source=DictEncoder().encode(source),
                        qgis_layer_id=child.id,
                        # TODO: should we fetch this from capabilities?
                        crs=DictEncoder().encode(Crs()),
                    )
                    dataset.save()
                PublishedAsLayerWms(
                    ogc_server=ogc_server.name,
                    themes_json_id=child.id,
                    name=dataset.name,
                    title=dataset.title,
                    metadata=DictEncoder().encode(child.metadata),
                    dataset=dataset,
                    layer_group=db_node,
                    min_resolution_hint=child.minResolutionHint,
                    max_resolution_hint=child.maxResolutionHint,
                    child_layers=DictEncoder().encode(child.childLayers),
                    dimensions=DictEncoder().encode(child.dimensions),
                ).save()
            elif isinstance(child, WmtsLayer):
                query = RasterDataSet.objects.filter(project=project, name=child.name)
                if query.exists():
                    dataset = query.get()
                else:
                    dataset = RasterDataSet(
                        project=project,
                        name=child.name,
                        # TODO: Fix this to correct title (via translation?)
                        title=child.name.title(),
                        # TODO: should we fetch this from capabilities?
                        bbox="0,0,0,4000000,4000000,4000000",
                        # TODO: should we fetch this from capabilities?
                        bbox_wgs84="-90.0,-180.0,0.0,90.0,180.0,10000",
                        path=child.url,
                        style="",
                        # this is wms for WMTS & WMS since (that comes from QGIS which handle both through
                        #   the same driver)
                        driver="wms",
                        source=DictEncoder().encode(
                            WmtsSource(
                                url=child.url,
                                layers=child.layer,
                                format=child.imageType,
                                contextual_wms_legend="0",
                                styles="default",
                                dpi_mode="7",
                                feature_count=10,
                                tile_dimensions="",
                                tile_matrix_set="",
                                crs="",
                                tile_pixel_ratio="0",
                            )
                        ),
                        qgis_layer_id=child.id,
                        # TODO: should we fetch this from capabilities?
                        crs=DictEncoder().encode(Crs()),
                    )
                    dataset.save()
                PublishedAsLayerWmts(
                    themes_json_id=child.id,
                    name=dataset.name,
                    title=dataset.title,
                    metadata=DictEncoder().encode(child.metadata),
                    dataset=dataset,
                    layer_group=db_node,
                    dimensions=DictEncoder().encode(child.dimensions),
                ).save()
            else:
                raise NotImplementedError(
                    f"Layer type is not implemented: {child.__class__.__name__}"
                )


class RegisterThemesJson(View):
    def post(self, request: HttpRequest):
        form = HomeForm(request.POST)
        if form.is_valid():
            url = GEOPORTAL_URLS[form.cleaned_data["geoportal_url"]]
            geoportal_config = load_geoportal_config_from_url(url)
            if geoportal_config is None:
                return redirect("admin:clogs_publishedastheme_changelist")
            mandant_qs = Mandant.objects.filter(name=form.cleaned_data["geoportal_url"])
            if not mandant_qs.exists():
                mandant_db = Mandant(name=form.cleaned_data["geoportal_url"], description=url)
                mandant_db.save()
            else:
                # we can do so, because name is unique in DB
                mandant_db = mandant_qs.get()
            for ogc_server in geoportal_config.ogc_servers:
                OgcServer.from_dataclass(ogc_server, mandant_db).save()
            for order, theme in enumerate(geoportal_config.themes):
                project_qs = Project.objects.filter(name=theme.name, mandant=mandant_db)
                if not project_qs.exists():
                    project_db = Project(
                        mandant=mandant_db,
                        name=theme.name,
                        hash=theme.hash,
                        # TODO: Fix this to correct title (via translation?)
                        title=theme.name.title(),
                    )
                    project_db.save()

                    published_theme = PublishedAsTheme(
                        themes_json_id=theme.id,
                        project=project_db,
                        name=theme.name,
                        public=True,
                        ordering=order,
                        icon=theme.icon,
                        # TODO: we go the cheap way here, lets investigate later....
                        metadata=DictEncoder().encode(theme.metadata),
                    )
                    published_theme.save()
                    root_group = LayerGroupMp.add_root(name=theme.name)
                    db_root_node = LayerGroupMp.objects.get(pk=root_group.pk)
                    db_root_node.theme = published_theme
                    db_root_node.save()
                    # Highly recursive task, we flatten the tree into treebeard structure
                    assemble_tree_to_treebeard(
                        theme.children,
                        db_root_node,
                        published_theme,
                        project_db,
                        geoportal_config,
                    )
                else:
                    # TODO: Handle update etc. of projects
                    logging.debug(
                        "Theme existed. Updating process not implemented "
                        "yet => delete the project and integrate it again!"
                    )
        else:
            # TODO: Add appropriate handling
            logging.debug("Form was not valid!")
        return redirect("admin:clogs_publishedastheme_changelist")


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
                    # we filter for permission on the onetoone field connected published_as element
                    if child.wms_datasets.has_read_permission(user, appname):
                        layer_group.children.append(child.wms_datasets.as_dataclass(config))
                elif hasattr(child, "wmts_datasets"):
                    layer_group.children.append(child.wmts_datasets.as_dataclass())
                else:
                    raise NotImplementedError(f"We are not aware of the passed type {node}")

    def get(self, request: HttpRequest, format: str):
        geogirafe_config = ThemesJson()

        for ogc_server in WebGisOgcServer.objects.all():
            geogirafe_config.ogc_servers.append(ogc_server.as_dataclass())
        for theme in PublishedAsTheme.objects.all():
            theme_object = theme.as_dataclass()
            if theme_object.icon is None:
                theme_object.icon = request.build_absolute_uri(
                    static("/webgis/assets/images/georama.coming_soon.png")
                )
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
    # TODO: This is prepared for later approach where we serve GeoGirafe directly through Django

    def get(self, request: HttpRequest, mandant_name: str):
        return render(request, "geogirafe/index.html")


class Config(View):
    # TODO: This is prepared for later approach where we serve GeoGirafe directly through Django

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
            "share": {  # TODO: This is prepared for later approach where we serve GeoGirafe directly through Django
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


class PublishProject(View):
    @staticmethod
    def find_dataset_by_name(
        dataset_name: str,
        datasets: List[QslGroup] | List[QslRaster] | List[QslVector] | List[QslCustom],
    ) -> QslGroup | QslVector | QslRaster | QslCustom | None:
        # TODO: This should be move directly to the QSL interface!
        for element in datasets:
            if element.name == dataset_name:
                return element
        return None

    def assemble_tree_to_treebeard(
        self,
        children: List[str],
        current_parent: LayerGroupMp,
        theme: PublishedAsTheme,
        project: Project,
        project_config: QslConfig,
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
                    raise NotImplementedError(
                        f"Layer type is not implemented: {child.__class__.__name__}"
                    )

    def get(self, request: HttpRequest, project_id: int, **kwargs):
        project_db = Project.objects.get(id=project_id)
        highest_theme = PublishedAsTheme.objects.order_by("ordering").last()
        theme = PublishedAsTheme(
            name=project_db.name,
            title=project_db.title,
            project=project_db,
            metadata={"isLegendExpanded": True, "legend": False},
            ordering=highest_theme.ordering + 1 if highest_theme else 1,
        )
        theme.save()
        ogc_server = insert_internal_ogc_server(request)
        project_from_config, project_config = RegisterQgisProject.load_project_config(
            project_db.mandant.name, project_db.name
        )
        root_group = LayerGroupMp.add_root(name=theme.name)
        db_root_node = LayerGroupMp.objects.get(pk=root_group.pk)
        db_root_node.theme = theme
        db_root_node.save()
        # Highly recursive task, we flatten the tree into treebeard structure
        self.assemble_tree_to_treebeard(
            # the element with empty string as name is always the root of the tree
            project_config.tree.find_by_name("").children,
            db_root_node,
            theme,
            project_db,
            project_config,
            ogc_server.name,
        )
        return redirect("admin:webgis_publishedastheme_changelist")


class OgcServerWebgis(OgcServer):
    model = PublishedAsLayerWms


def insert_internal_ogc_server(request: HttpRequest) -> WebGisOgcServer:
    """
    Checks if internal OGC server was already added. If it was added, it returns the DB entity
    if it was not added, it adds it and returns the added one.

    Args:
        request: Django request as it comes from framework request.

    Returns:
        The ogc server db entity or None if a more then one match was found (that would be an error).
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
    helper function to hide actual connection in the database but make publishing straight forward.
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
