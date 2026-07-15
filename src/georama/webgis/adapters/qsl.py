from qgis_server_light.interface.common import BBox
from qgis_server_light.interface.exporter.extract import Config, DataSet, TreeGroup

from georama.webgis.interfaces.geomapfish.themes_json_2_8.dataclasses import (
    LayerGroup,
    MetaData,
    Theme,
    WmsLayer,
    WmtsLayer,
)
from georama.webgis.models import WmsLayer as GeoramaWmsLayer

type QgisLayerId = str
type WmsLayerIndex = dict[QgisLayerId, GeoramaWmsLayer]

MIN_RESOLUTION_HINT = 0.0
MAX_RESOLUTION_HINT = 999999999.0


def extend_bbox(bbox: BBox, bbox_extension: BBox):
    if bbox_extension.x_min < bbox.x_min or bbox.x_min == 0:
        bbox.x_min = bbox_extension.x_min
    if bbox_extension.y_min < bbox.y_min or bbox.y_min == 0:
        bbox.y_min = bbox_extension.y_min
    if bbox_extension.x_max > bbox.x_max or bbox.x_max == 0:
        bbox.x_max = bbox_extension.x_max
    if bbox_extension.y_max > bbox.y_max or bbox.y_max == 0:
        bbox.y_max = bbox_extension.y_max


async def handle_dataset(
    qsl_dataset: DataSet,
    gg_children: list[LayerGroup | WmsLayer | WmtsLayer],
    bbox: BBox,
    wms_layer_index: WmsLayerIndex,
):
    wms_layer = wms_layer_index[qsl_dataset.id]
    if wms_layer.extent is not None:
        extend_bbox(bbox, BBox.from_string(wms_layer.extent))
    gg_wms_layer = wms_layer.as_gg_wms_layer
    gg_children.append(gg_wms_layer)


async def unwrap_group(
    qsl_group: TreeGroup,
    config: Config,
    gg_children: list[LayerGroup | WmsLayer | WmtsLayer],
    bbox: BBox,
    wms_layer_index: WmsLayerIndex,
):
    for child in qsl_group.children:
        qsl_tree_match = config.tree.find_by_name(child)

        if qsl_tree_match:
            qsl_layer_group = config.datasets.find_group_by_id(qsl_tree_match.id)
            gg_group = LayerGroup(
                id=qsl_tree_match.id,
                name=qsl_layer_group.title,
                metadata=MetaData(),
            )
            gg_children.append(gg_group)
            # its a group again
            await unwrap_group(
                qsl_tree_match,
                config,
                gg_group.children,
                bbox,
                wms_layer_index,
            )
        else:
            ds = config.datasets.find_dataset_by_id(child)
            if ds:
                await handle_dataset(
                    ds,
                    gg_children,
                    bbox,
                    wms_layer_index,
                )
            else:
                raise LookupError(f"Dataset with id {child} was not found in config!")


async def theme_json_from_project_config(
    theme_id: str,
    icon: str,
    project_config: Config,
    wms_layer_index: WmsLayerIndex,
) -> Theme:
    bbox = BBox(0.0, 0.0, 0.0, 0.0)
    children = []
    await unwrap_group(
        project_config.tree.root,
        project_config,
        children,
        bbox,
        wms_layer_index,
    )
    gg_theme = Theme(
        id=theme_id,
        name=project_config.project.name,
        icon=icon,
        metadata=MetaData(),
        children=children,
        zoom=4,
    )
    return gg_theme
