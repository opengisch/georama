import base64
import math
from urllib.parse import unquote

from django.conf import settings
from httpx import RequestError
from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.exporter.extract import (
    Config,
    DataSet,
    TreeGroup,
    WmsSource,
    WmtsSource,
    XYZSource,
)

from georama.maps.adapter.qsl import render_image
from georama.maps.services.wfs_2_0_0 import WfsOperation
from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    LayerSettings,
    MetaData,
    OgcServer,
    OgcServers,
    Theme,
    WmsLayer,
    WmtsLayer,
    XyzLayer,
)
from georama.webgis.models import WmsLayer as GeoramaWmsLayer

type QgisLayerId = str
type WmsLayerIndex = dict[QgisLayerId, GeoramaWmsLayer]

MIN_RESOLUTION_HINT = 0.0
MAX_RESOLUTION_HINT = 999999999.0
# size/aspect ratio of the built-in background thumbnails of GeoGirafe
BACKGROUND_THUMBNAIL_DIMENSIONS = (220, 120)


def extend_bbox(bbox: BBox, bbox_extension: BBox):
    bbox.x_min = min(bbox_extension.x_min, bbox.x_min)
    bbox.y_min = min(bbox_extension.y_min, bbox.y_min)
    bbox.x_max = max(bbox_extension.x_max, bbox.x_max)
    bbox.y_max = max(bbox_extension.y_max, bbox.y_max)


async def render_background_thumbnail(wms_layer: GeoramaWmsLayer) -> str | None:
    """Renders the thumbnail of a background layer through QSL.

    Args:
        wms_layer: The background layer.

    Returns:
        The png as data url or `None` if rendering failed.
    """
    try:
        image = await render_image(
            wms_layer,
            BBox.from_string(settings.WEBGIS_BACKGROUND_THUMBNAIL_EXTENT),
            settings.WEBGIS_BACKGROUND_THUMBNAIL_CRS,
            *BACKGROUND_THUMBNAIL_DIMENSIONS,
        )
    except RequestError:
        # already logged, publishing must not fail because of a missing thumbnail
        return None
    if image is None:
        return None
    return f"data:image/png;base64,{base64.b64encode(image).decode()}"


async def handle_dataset(
    qsl_dataset: DataSet,
    gg_children: list[LayerGroup | WmsLayer | WmtsLayer],
    bbox: BBox,
    wms_layer_index: WmsLayerIndex,
    background_layers: list[WmsLayer | WmtsLayer],
    ogc_servers: OgcServers,
):
    # Vector layers without geometries are skipped during data integration
    if not qsl_dataset.is_spatial:
        return
    wms_layer = wms_layer_index[qsl_dataset.id]
    gg_wms_layer = wms_layer.as_gg_wms_layer
    if qsl_dataset.is_background:
        source = qsl_dataset.source.definition
        if source.remote:
            if isinstance(source, XYZSource):
                source_url = unquote(source.url)
                gg_wms_layer = XyzLayer(
                    id=wms_layer.identifier,
                    name=wms_layer.metadata.title,
                    url=source_url,
                    metadata=MetaData(),
                    type="XYZ",
                )
            elif isinstance(source, (WmsSource, WmtsSource)):
                source_url = unquote(source.url)
                source_format = unquote(source.format)
                ogc_server = OgcServer(
                    name=f"remote_{source_url}_{source_format}",
                    url=source_url,
                    type="WMS",
                    credential=False,
                    image_type=source_format,
                    wfs_support=False,
                    is_single_tile=False,
                    namespace="",
                )
                ogc_servers[ogc_server.name] = ogc_server
                if isinstance(source, WmtsSource):
                    gg_wms_layer = WmtsLayer(
                        id=wms_layer.identifier,
                        name=wms_layer.metadata.title,
                        url=source_url,
                        layer=source.layers,
                        type="WMTS",
                        image_type=source_format,
                        style=source.styles or "default",
                        matrix_set=source.tile_matrix_set,
                        metadata=MetaData(ogc_server=ogc_server.name),
                    )
                elif isinstance(source, WmsSource):
                    gg_wms_layer = WmsLayer(
                        id=WfsOperation.encode_layer_name(wms_layer.identifier),
                        name=wms_layer.metadata.title,
                        type="WMS",
                        layers=source.layers,
                        image_type=source_format,
                        min_resolution_hint=wms_layer.min_resolution_hint,
                        max_resolution_hint=wms_layer.max_resolution_hint,
                        child_layers=[
                            LayerSettings(
                                name=WfsOperation.encode_layer_name(wms_layer.identifier),
                                min_resolution_hint=wms_layer.min_resolution_hint,
                                max_resolution_hint=wms_layer.max_resolution_hint,
                                queryable=False,
                            )
                        ],
                        ogc_server=ogc_server.name,
                        editable=False,
                        style=source.styles or "default",
                        metadata=MetaData(),
                    )
        gg_wms_layer.metadata.is_checked = qsl_dataset.is_checked
        gg_wms_layer.metadata.thumbnail = await render_background_thumbnail(wms_layer)
        background_layers.append(gg_wms_layer)
        return
    gg_wms_layer.metadata.is_checked = qsl_dataset.is_checked
    if wms_layer.extent is not None:
        extend_bbox(bbox, BBox.from_string(wms_layer.extent))
    gg_children.append(gg_wms_layer)


async def unwrap_group(
    qsl_group: TreeGroup,
    config: Config,
    gg_children: list[LayerGroup | WmsLayer | WmtsLayer],
    bbox: BBox,
    wms_layer_index: WmsLayerIndex,
    background_layers: list[WmsLayer | WmtsLayer],
    ogc_servers: OgcServers,
):
    for child in qsl_group.children:
        qsl_tree_match = config.tree.find_by_name(child)

        if qsl_tree_match:
            qsl_layer_group = config.datasets.find_group_by_id(qsl_tree_match.id)
            if qsl_layer_group is None:
                raise LookupError(f"Group with id {child} was not found in config!")

            gg_group = LayerGroup(
                id=qsl_tree_match.id,
                name=qsl_layer_group.title,
                metadata=MetaData(is_expanded=qsl_layer_group.is_expanded),
            )
            # its a group again
            await unwrap_group(
                qsl_tree_match,
                config,
                gg_group.children,
                bbox,
                wms_layer_index,
                background_layers,
                ogc_servers,
            )
            # skip groups left empty because all their layers were background
            # layers (moved to `background_layers`) or not spatial
            if gg_group.children:
                gg_children.append(gg_group)
        else:
            ds = config.datasets.find_dataset_by_id(child)
            if ds is None:
                raise LookupError(f"Dataset with id {child} was not found in config!")

            await handle_dataset(
                ds,
                gg_children,
                bbox,
                wms_layer_index,
                background_layers,
                ogc_servers,
            )


async def theme_json_from_project_config(
    theme_id: str,
    icon: str,
    project_config: Config,
    wms_layer_index: WmsLayerIndex,
) -> tuple[Theme, list[WmsLayer | WmtsLayer], OgcServers]:
    bbox = BBox(math.inf, math.inf, -math.inf, -math.inf)
    children = []
    background_layers: list[WmsLayer | WmtsLayer] = []
    ogc_servers: OgcServers = {}
    await unwrap_group(
        project_config.tree.root,
        project_config,
        children,
        bbox,
        wms_layer_index,
        background_layers,
        ogc_servers,
    )
    if any(math.isinf(n) for n in bbox.to_2d_list()):
        location = [0.0, 0.0]
    else:
        location = [(bbox.x_max + bbox.x_min) / 2, (bbox.y_max + bbox.y_min) / 2]

    gg_theme = Theme(
        id=theme_id,
        name=project_config.project.name,
        icon=icon,
        metadata=MetaData(),
        children=children,
        zoom=4,
        location=location,
    )
    return gg_theme, background_layers, ogc_servers
