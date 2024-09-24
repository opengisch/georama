import json
import logging
from textwrap import indent

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from xsdata.formats.dataclass.serializers import DictEncoder, JsonSerializer

from georama.clogs.forms import GEOPORTAL_URLS, HomeForm
from georama.clogs.interfaces.geomapfish import load_geoportal_config_from_url
from georama.clogs.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup, WmsLayer, WmtsLayer, ThemesJson, Theme
)
from georama.qmeleon.models import Project, RasterDataSet, Mandant
from qgis_server_light.interface.qgis import Crs, WmtsSource, WmsSource
from georama.clogs.models import (
    PublishedAsTheme, LayerGroupMp, PublishedAsLayerWms, PublishedAsLayerWmts,
    OgcServer
)


def home(request):
    form = HomeForm()

    return render(request, "home.html", {"form": form})


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
        db_node.save()
        if isinstance(child, LayerGroup):
            if hasattr(child, 'ogcServer'):
                if child.ogcServer is not None:
                    current_ogc_server = child.ogcServer
                    logging.debug(f"set current_ogc_server by group: {current_ogc_server}")
                else:
                    logging.debug("New nested group but we leave ogc server because it was not redefined")
            db_node.metadata = DictEncoder().encode(child.metadata)
            db_node.mixed = child.mixed
            db_node.ogc_server = current_ogc_server
            db_node.dimensions = DictEncoder().encode(child.dimensions)
            db_node.themes_json_id = child.id
            db_node.save()
            assemble_tree_to_treebeard(
                child.children,
                db_node,
                theme,
                project,
                geoportal_config,
                current_ogc_server
            )
        else:
            if isinstance(child, WmsLayer):
                if child.ogcServer is None and current_ogc_server is not None:
                    child.ogcServer = current_ogc_server
                ogc_server = geoportal_config.get_ogc_server_by_name(child.ogcServer)
                source = WmsSource(
                    # TODO: This comes from QGIS and seem to bool if legend is shown or not, we need to know
                    #  how this transports to geogirafe
                    contextual_wms_legend='0',
                    # TODO: This we should make configurable or read it from capabilities of OGC Server
                    crs="EPSG:2056",
                    # TODO: This is normally a QGIS/Client specific thing, probably we can remove it from the
                    #  dataclass
                    dpi_mode='',
                    # TODO: Find why, how this is possible to fill
                    feature_count=0,
                    format=child.imageType,
                    layers=child.layers,
                    url=ogc_server.url
                )
                dataset = RasterDataSet(
                    project=project,
                    name=child.name,
                    # TODO: Fix this to correct title (via translation?)
                    title=child.name.title(),
                    # TODO: should we fetch this from capabilities?
                    bbox="TODO",
                    # TODO: should we fetch this from capabilities?
                    bbox_wgs84="TODO",
                    path=geoportal_config.get_ogc_server_by_name(child.ogcServer).url,
                    style='',
                    # this is wms for WMTS & WMS since (that comes from QGIS which handle both through
                    #   the same driver)
                    driver='wms',
                    source=DictEncoder().encode(source),
                    qgis_layer_id=child.id,
                    # TODO: should we fetch this from capabilities?
                    crs=DictEncoder().encode(Crs())
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
                    dimensions=DictEncoder().encode(child.dimensions)
                ).save()
            elif isinstance(child, WmtsLayer):
                dataset = RasterDataSet(
                    project=project,
                    name=child.name,
                    # TODO: Fix this to correct title (via translation?)
                    title=child.name.title(),
                    # TODO: should we fetch this from capabilities?
                    bbox="TODO",
                    # TODO: should we fetch this from capabilities?
                    bbox_wgs84="TODO",
                    path=child.url,
                    style='',
                    # this is wms for WMTS & WMS since (that comes from QGIS which handle both through
                    #   the same driver)
                    driver='wms',
                    source=DictEncoder().encode(
                        WmtsSource(
                            url=child.url,
                            layers=child.layer,
                            format=child.imageType,
                            contextual_wms_legend="0",
                            styles="default",
                            dpi_mode='7',
                            feature_count=10,
                            tile_dimensions="",
                            tile_matrix_set="",
                            crs="",
                            tile_pixel_ratio="0"
                        )
                    ),
                    qgis_layer_id=child.id,
                    # TODO: should we fetch this from capabilities?
                    crs=DictEncoder().encode(Crs())
                )
                dataset.save()
                PublishedAsLayerWmts(
                    themes_json_id=child.id,
                    name=dataset.name,
                    title=dataset.title,
                    metadata=DictEncoder().encode(child.metadata),
                    dataset=dataset,
                    layer_group=db_node,
                    dimensions=DictEncoder().encode(child.dimensions)
                ).save()
            else:
                raise NotImplementedError(f"Layer type is not implemented: {child.__class__.__name__}")


class RegisterThemesJson(View):

    def post(self, request: HttpRequest):
        form = HomeForm(request.POST)
        if form.is_valid():
            url = GEOPORTAL_URLS[form.cleaned_data["geoportal_url"]]
            geoportal_config = load_geoportal_config_from_url(url)
            if geoportal_config is None:
                return redirect('admin:clogs_publishedastheme_changelist')
            mandant_qs = Mandant.objects.filter(
                name=form.cleaned_data["geoportal_url"]
            )
            if not mandant_qs.exists():
                mandant_db = Mandant(
                    name=form.cleaned_data["geoportal_url"],
                    description=url
                )
                mandant_db.save()
            else:
                # we can do so, because name is unique in DB
                mandant_db = mandant_qs.get()
            for ogc_server in geoportal_config.ogc_servers:
                OgcServer.from_dataclass(ogc_server, mandant_db).save()
            for order, theme in enumerate(geoportal_config.themes):
                project_qs = Project.objects.filter(
                    name=theme.name,
                    mandant=mandant_db
                )
                if not project_qs.exists():
                    project_db = Project(
                        mandant=mandant_db,
                        name=theme.name,
                        hash=theme.hash,
                        # TODO: Fix this to correct title (via translation?)
                        title=theme.name.title()
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
                        metadata=DictEncoder().encode(theme.metadata)
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
                        geoportal_config
                    )
                else:
                    # TODO: Handle update etc. of projects
                    logging.debug(
                        'Theme existed. Updating process not implemented '
                        'yet => delete the project and integrate it again!'
                    )
        else:
            # TODO: Add appropriate handling
            logging.debug(
                'Form was not valid!'
            )
        return redirect('admin:clogs_publishedastheme_changelist')



class Themes(View):

    def assemble_themes_tree_from_treebeard(
            self,
            node: LayerGroupMp,
            layer_group: LayerGroup | Theme,
            config: ThemesJson
    ):
        for child in node.get_children():
            if child.get_children():
                # this is a group to unpack
                group = node.as_dataclass()
                layer_group.children.append(group)
                self.assemble_themes_tree_from_treebeard(child, group, config)
            else:
                if hasattr(child, 'wms_datasets'):
                    layer_group.children.append(
                        child.wms_datasets.as_dataclass(
                            config
                        )
                    )
                elif hasattr(child, 'wmts_datasets'):
                    layer_group.children.append(child.wmts_datasets.as_dataclass())
                else:
                    raise NotImplementedError(f'We are not aware of the passed type {node}')

    def get(self, request: HttpRequest, mandant_name: str, format: str):
        geogirafe_config = ThemesJson()

        for ogc_server in Mandant.objects.get(name=mandant_name).ogc_servers.all():
            geogirafe_config.ogc_servers.append(ogc_server.as_dataclass())
        for theme in PublishedAsTheme.objects.all():
            theme_object = theme.as_dataclass()
            geogirafe_config.themes.append(theme_object)
            root_node = theme.tree_elements.first().get_root()
            self.assemble_themes_tree_from_treebeard(
                root_node,
                theme_object,
                geogirafe_config
            )
        result_dict = {
            'themes': DictEncoder().encode(geogirafe_config.themes),
            'ogcServers': {},
            'errors': []
        }
        for ogc_server in geogirafe_config.ogc_servers:
            result_dict['ogcServers'][ogc_server.name] = DictEncoder().encode(ogc_server)
        return HttpResponse(
            json.dumps(result_dict, indent=2), status=200, content_type='application/json'
        )


class GeoGirafe(View):
    # TODO: This is prepared for later approach where we serve GeoGirafe directly through Django

    def get(self, request: HttpRequest, mandant_name: str):
        return render(request, "geogirafe/index.html")


class Config(View):
    # TODO: This is prepared for later approach where we serve GeoGirafe directly through Django

    def get(self, request: HttpRequest, mandant_name: str):
        config_dict = {
          "general": {
            "locale": "en"
          },
          "languages": {
            "translations": {
              "de": ["Mock/de.json"],
              "en": ["Mock/en.json"],
              "fr": ["Mock/fr.json"]
            },
            "defaultLanguage": "en"
          },
          "themes": {
            "url": "themes.json",
            "defaultTheme": "cadastre"
          },
          "basemaps": {
            "show": True,
            "defaultBasemap": "orthophoto",
            "OSM": False,
            "SwissTopoVectorTiles": True
          },
          "treeview": {
            "useLegendIcons": False
          },
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
            "printLegend": {
              "showGroupsTitle": True
            }
          },

          "share": {# TODO: This is prepared for later approach where we serve GeoGirafe directly through Django
            "service": "lstu",
            "createUrl": "https://lstu.fr/a"
          },
          "projections": {
            "EPSG:3857": "W-M",
            "EPSG:4326": "WGS84",
            "EPSG:2056": "LV95"
          },
          "map": {
            "srid": "EPSG:2056",
            "scales": [1000000, 500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200],
            "startPosition": "2612500,1268050",
            "startZoom": 8,
            "maxExtent": "2200000,1040000,3000000,1310000"
          },
          "map3d": {
            "terrainUrl": "https://terrain100.geo.admin.ch/1.0.0/ch.swisstopo.terrain.3d/",
            "tilesetsUrls": ["https://vectortiles100.geo.admin.ch/3d-tiles/ch.swisstopo.swisstlm3d.3d/20201020/tileset.json"]
          },
          "bookmarks": {
            "service": "localStorage",
            "get": "",
            "post": ""
          }
        }
        return HttpResponse(
            json.dumps(config_dict, indent=2), status=200, content_type='application/json'
        )
