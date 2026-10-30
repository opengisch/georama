import hashlib
import logging
from dataclasses import dataclass, field
from typing import Union

from xsdata.formats.dataclass.serializers.json import JsonSerializer


@dataclass
class AbstractSchema:
    # field_mapping: dict
    # django_model_class: Model

    def to_django_model_instance(self):
        raise NotImplementedError
        # TODO: Make a generic mapping function for that
        # dataclass_fields = fields(self)
        # django_model_instance_kwargs = {}
        # for field_name in dataclass_fields:
        #     django_model_instance_kwargs[self.field_mapping[field_name]] = getattr(self, field_name)  # noqa: E501
        # return self.django_model_class(
        #     **django_model_instance_kwargs
        # )


@dataclass
class Attribute(AbstractSchema):
    name: str = field(default=None, metadata={"type": "Element", "required": False})
    type: str = field(default=None, metadata={"type": "Element", "required": False})
    namespace: str = field(default=None, metadata={"type": "Element", "required": False})
    min_occurs: str = field(
        default=None, metadata={"name": "minOccurs", "type": "Element", "required": False}
    )
    max_occurs: str = field(
        default=None, metadata={"name": "maxOccurs", "type": "Element", "required": False}
    )


@dataclass
class LinkedLayer(AbstractSchema):
    name: str = field(default=None, metadata={"type": "Element", "required": False})
    attributes: list[Attribute] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )


@dataclass
class OgcServer(AbstractSchema):
    url: str = field(metadata={"type": "Element", "required": True})
    type: str = field(metadata={"type": "Element", "required": True})
    credential: bool = field(metadata={"type": "Element", "required": True})
    image_type: str = field(metadata={"name": "imageType", "type": "Element", "required": True})
    wfs_support: bool = field(metadata={"name": "wfsSupport", "type": "Element", "required": True})
    is_single_tile: bool = field(
        metadata={"name": "isSingleTile", "type": "Element", "required": True}
    )
    namespace: str = field(metadata={"type": "Element", "required": True})
    name: str = field(default=None, metadata={"type": "Element", "required": False})
    url_wfs: str = field(
        default=None, metadata={"name": "urlWfs", "type": "Element", "required": False}
    )
    # TODO: make this correctly typed
    attributes: list[LinkedLayer] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )


@dataclass
class SnappingConfig:
    edge: bool = field(default=False, metadata={"type": "Element", "required": False})
    vertex: bool = field(default=False, metadata={"type": "Element", "required": False})
    tolerance: int = field(default=0, metadata={"type": "Element", "required": False})


@dataclass
class MetaData(AbstractSchema):
    copyable: bool = field(default=False, metadata={"type": "Element", "required": False})
    directed_filter_attributes: list[str] = field(
        default_factory=list,
        metadata={"name": "directedFilterAttributes", "type": "Element", "required": False},
    )
    disclaimer: str | None = field(default=None, metadata={"type": "Element", "required": False})
    enumerated_attributes: list[str] = field(
        default_factory=list,
        metadata={"name": "enumeratedAttributes", "type": "Element", "required": False},
    )
    exclusive_group: bool | None = field(
        default=False, metadata={"name": "exclusiveGroup", "type": "Element", "required": False}
    )
    icon_url: str | None = field(
        default=None, metadata={"name": "iconUrl", "type": "Element", "required": False}
    )
    identifier_attribute_field: str | None = field(
        default=None,
        metadata={"name": "identifierAttributeField", "type": "Element", "required": False},
    )
    is_checked: bool = field(
        default=False, metadata={"name": "isChecked", "type": "Element", "required": False}
    )
    is_expanded: bool = field(
        default=False, metadata={"name": "isExpanded", "type": "Element", "required": False}
    )
    print_native_angle: bool = field(
        default=True, metadata={"name": "printNativeAngle", "type": "Element", "required": False}
    )
    is_legend_expanded: bool = field(
        default=False, metadata={"name": "isLegendExpanded", "type": "Element", "required": False}
    )
    legend: bool = field(default=False, metadata={"type": "Element", "required": False})
    legend_image: str | None = field(
        default=None, metadata={"name": "legendImage", "type": "Element", "required": False}
    )
    # TODO:
    # hiDPILegendImages
    legend_rule: str | None = field(
        default=None, metadata={"name": "legendRule", "type": "Element", "required": False}
    )
    max_resolution: int | float | None = field(
        default=None, metadata={"name": "maxResolution", "type": "Element", "required": False}
    )
    metadata_url: str | None = field(
        default=None, metadata={"name": "metadataUrl", "type": "Element", "required": False}
    )
    min_resolution: float | None = field(
        default=None, metadata={"name": "minResolution", "type": "Element", "required": False}
    )
    ogc_server: str | None = field(
        default=None, metadata={"name": "ogcServer", "type": "Element", "required": False}
    )
    opacity: float | None = field(default=None, metadata={"type": "Element", "required": False})
    print_layers: str | None = field(
        default=None, metadata={"name": "printLayers", "type": "Element", "required": False}
    )
    query_layers: str | None = field(
        default=None, metadata={"name": "queryLayers", "type": "Element", "required": False}
    )
    thumbnail: str | None = field(default=None, metadata={"type": "Element", "required": False})
    time_attribute: str | None = field(
        default=None, metadata={"name": "timeAttribute", "type": "Element", "required": False}
    )
    snapping_config: SnappingConfig | None = field(
        default=None, metadata={"name": "snappingConfig", "type": "Element", "required": False}
    )
    wms_layers: str | None = field(
        default=None, metadata={"name": "wmsLayers", "type": "Element", "required": False}
    )
    # TODO:
    # customOpenLayersOptions


@dataclass
class LayerSettings:
    name: str = field(metadata={"type": "Element", "required": True})
    min_resolution_hint: float = field(
        metadata={"name": "minResolutionHint", "type": "Element", "required": True}
    )
    max_resolution_hint: float = field(
        metadata={"name": "maxResolutionHint", "type": "Element", "required": True}
    )
    queryable: bool = field(metadata={"type": "Element", "required": True})


@dataclass
class Dimensions:
    Time: str = field(default=None, metadata={"type": "Element", "required": True})


@dataclass
class Time:
    min_value: str = field(
        default=None, metadata={"name": "minValue", "type": "Element", "required": True}
    )
    max_value: str = field(
        default=None, metadata={"name": "maxValue", "type": "Element", "required": True}
    )
    values: list[str] = field(default_factory=list, metadata={"type": "Element", "required": True})
    # TODO: make enumeration day|month|year|second
    resolution: str = field(default=None, metadata={"type": "Element", "required": True})
    # TODO: make enumeration range|value|disabled
    mode: str = field(default=None, metadata={"type": "Element", "required": True})
    # TODO: make enumeration slider|datepicker
    widget: str = field(default=None, metadata={"type": "Element", "required": True})
    min_def_value: str | None = field(
        default=None, metadata={"name": "minDefValue", "type": "Element", "required": True}
    )
    max_def_value: str | None = field(
        default=None, metadata={"name": "maxDefValue", "type": "Element", "required": True}
    )


@dataclass
class WmsLayer:
    id: str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    type: str = field(metadata={"type": "Element", "required": True})
    layers: str = field(metadata={"type": "Element", "required": True})
    image_type: str = field(metadata={"name": "imageType", "type": "Element", "required": True})
    min_resolution_hint: float = field(
        metadata={"name": "minResolutionHint", "type": "Element", "required": True}
    )
    max_resolution_hint: float = field(
        metadata={"name": "maxResolutionHint", "type": "Element", "required": True}
    )
    child_layers: list[LayerSettings] = field(
        metadata={"name": "childLayers", "type": "Element", "required": True}
    )
    ogc_server: str | None = field(
        default=None, metadata={"name": "ogcServer", "type": "Element", "required": False}
    )
    dimensions: Dimensions | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    editable: bool | None = field(default=None, metadata={"type": "Element", "required": False})
    style: str = field(default=None, metadata={"type": "Element", "required": False})
    time: Time | None = field(default=None, metadata={"type": "Element", "required": False})
    path: str | None = field(default=None, metadata={"type": "Element", "required": False})


@dataclass
class WmtsLayer:
    id: str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    url: str = field(metadata={"type": "Element", "required": True})
    layer: str = field(metadata={"type": "Element", "required": True})
    type: str = field(metadata={"type": "Element", "required": True})
    image_type: str = field(metadata={"name": "imageType", "type": "Element", "required": True})
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    style: str = field(default=None, metadata={"type": "Element", "required": False})
    matrix_set: str = field(default=None, metadata={"type": "Element", "required": False})
    dimensions: Dimensions | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    editable: bool | None = field(default=None, metadata={"type": "Element", "required": False})
    path: str | None = field(default=None, metadata={"type": "Element", "required": False})


@dataclass
class XyzLayer:
    id: str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    url: str = field(metadata={"type": "Element", "required": True})
    type: str = field(metadata={"type": "Element", "required": True})
    metadata: MetaData = field(metadata={"type": "Element", "required": True})


@dataclass
class LayerGroup:
    id: int | str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    mixed: bool | None = field(default=False, metadata={"type": "Element", "required": False})
    children: list[Union["LayerGroup", WmsLayer, WmtsLayer]] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )
    ogc_server: str | None = field(
        default=None, metadata={"name": "ogcServer", "type": "Element", "required": False}
    )
    dimensions: Dimensions | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    path: str | None = field(default=None, metadata={"type": "Element", "required": False})


@dataclass
class UniqueLayers:
    elements: list[WmsLayer | WmtsLayer] = field(metadata={"type": "Element", "required": True})


@dataclass
class Theme(AbstractSchema):
    id: int | str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    icon: str = field(metadata={"type": "Element", "required": True})
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    children: list[Union["LayerGroup", WmsLayer, WmtsLayer]] = field(
        default_factory=list, metadata={"type": "Element", "required": True}
    )
    zoom: int | None = field(default=None)
    location: list[float] = field(default_factory=list)

    @property
    def hash(self):
        return hashlib.md5(JsonSerializer().render(self).encode()).hexdigest()

    def separate_groups_and_layers(
        self,
        children: list[LayerGroup | WmsLayer | WmtsLayer],
        layer_list: list[WmsLayer | WmtsLayer],
        current_ogc_server: str | None = None,
        current_path: list | None = None,
    ):
        if current_path is None:
            # happens only once at initial call
            current_path = []
        for child in children:
            if isinstance(child, LayerGroup):
                current_path.append(str(child.name))
                child.path = ".".join(current_path)
                if hasattr(child, "ogc_server"):
                    if child.ogc_server is not None:
                        current_ogc_server = child.ogc_server
                        logging.debug(f"set current_ogc_server bygroup: {current_ogc_server}")
                    else:
                        logging.debug(
                            "New nested group but we leave ogc server becauseit was not redefined"
                        )
                self.separate_groups_and_layers(
                    child.children, layer_list, current_ogc_server, current_path
                )
            else:
                if child not in layer_list:
                    if (
                        isinstance(child, WmsLayer)
                        and child.ogc_server is None
                        and current_ogc_server is not None
                    ):
                        child.ogc_server = current_ogc_server
                    child.path = ".".join(current_path + [str(child.name)])
                    layer_list.append(child)

    @property
    def unique_layers_and_groups(self) -> UniqueLayers:
        layer_list: list[WmtsLayer | WmsLayer] = []
        self.separate_groups_and_layers(self.children, layer_list)
        return UniqueLayers(elements=layer_list)


type OgcServers = dict[str, OgcServer]


@dataclass
class ThemesJson:
    ogc_servers: OgcServers = field(
        metadata={"name": "ogcServers", "type": "Ignore", "required": False}
    )
    themes: list[Theme] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )
    errors: list[str] = field(default_factory=list)
    background_layers: list[WmsLayer | WmtsLayer] = field(default_factory=list)

    def get_ogc_server_by_name(self, name: str) -> OgcServer | None:
        return self.ogc_servers.get(name)

    def get_theme_by_name(self, name: str) -> Theme | None:
        for theme in self.themes:
            if name == theme.name:
                return theme
        return None
