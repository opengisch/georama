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
    minOccurs: str = field(default=None, metadata={"type": "Element", "required": False})
    maxOccurs: str = field(default=None, metadata={"type": "Element", "required": False})


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
    imageType: str = field(metadata={"type": "Element", "required": True})
    wfsSupport: bool = field(metadata={"type": "Element", "required": True})
    isSingleTile: bool = field(metadata={"type": "Element", "required": True})
    namespace: str = field(metadata={"type": "Element", "required": True})
    name: str = field(default=None, metadata={"type": "Element", "required": False})
    urlWfs: str = field(default=None, metadata={"type": "Element", "required": False})
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
    copyable: bool | None = field(
        default=False, metadata={"type": "Element", "required": False}
    )
    directedFilterAttributes: list[str] | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    disclaimer: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    enumeratedAttributes: list[str] | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    exclusiveGroup: bool | None = field(
        default=False, metadata={"type": "Element", "required": False}
    )
    iconUrl: str | None = field(default=None, metadata={"type": "Element", "required": False})
    identifierAttributeField: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    isChecked: bool | None = field(
        default=False, metadata={"type": "Element", "required": False}
    )
    isExpanded: bool | None = field(
        default=False, metadata={"type": "Element", "required": False}
    )
    printNativeAngle: bool | None = field(
        default=True, metadata={"type": "Element", "required": False}
    )
    isLegendExpanded: bool | None = field(
        default=False, metadata={"type": "Element", "required": False}
    )
    legend: bool | None = field(default=False, metadata={"type": "Element", "required": False})
    legendImage: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    # TODO:
    # hiDPILegendImages
    legendRule: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    maxResolution: int | float | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    metadataUrl: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    minResolution: float | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    ogcServer: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    opacity: float | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    printLayers: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    queryLayers: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    thumbnail: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    timeAttribute: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    snappingConfig: SnappingConfig | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    wmsLayers: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    # TODO:
    # customOpenLayersOptions


@dataclass
class LayerSettings:
    name: str = field(metadata={"type": "Element", "required": True})
    minResolutionHint: float = field(metadata={"type": "Element", "required": True})
    maxResolutionHint: float = field(metadata={"type": "Element", "required": True})
    queryable: bool = field(metadata={"type": "Element", "required": True})


@dataclass
class Dimensions:
    Time: str = field(default=None, metadata={"type": "Element", "required": True})


@dataclass
class Time:
    minValue: str = field(default=None, metadata={"type": "Element", "required": True})
    maxValue: str = field(default=None, metadata={"type": "Element", "required": True})
    values: list[str] = field(
        default_factory=list, metadata={"type": "Element", "required": True}
    )
    # TODO: make enumeration day|month|year|second
    resolution: str = field(default=None, metadata={"type": "Element", "required": True})
    # TODO: make enumeration range|value|disabled
    mode: str = field(default=None, metadata={"type": "Element", "required": True})
    # TODO: make enumeration slider|datepicker
    widget: str = field(default=None, metadata={"type": "Element", "required": True})
    minDefValue: str | None = field(
        default=None, metadata={"type": "Element", "required": True}
    )
    maxDefValue: str | None = field(
        default=None, metadata={"type": "Element", "required": True}
    )


@dataclass
class WmsLayer:
    id: str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    # TODO: This has to be modeled differntly because its to ambiguous
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    type: str = field(metadata={"type": "Element", "required": True})
    layers: str = field(metadata={"type": "Element", "required": True})
    imageType: str = field(metadata={"type": "Element", "required": True})
    minResolutionHint: float = field(metadata={"type": "Element", "required": True})
    maxResolutionHint: float = field(metadata={"type": "Element", "required": True})
    childLayers: list[LayerSettings] = field(metadata={"type": "Element", "required": True})
    ogcServer: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    dimensions: Dimensions | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    editable: bool | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
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
    imageType: str = field(metadata={"type": "Element", "required": True})
    # TODO: This has to be modeled differntly because its to ambiguous
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    style: str = field(default=None, metadata={"type": "Element", "required": False})
    matrix_set: str = field(default=None, metadata={"type": "Element", "required": False})
    dimensions: Dimensions | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    editable: bool | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    path: str | None = field(default=None, metadata={"type": "Element", "required": False})


@dataclass
class LayerGroup:
    id: int | str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    # TODO: This has to be modeled differntly because its to ambiguous
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    mixed: bool | None = field(default=False, metadata={"type": "Element", "required": False})
    children: list[Union["LayerGroup", WmsLayer, WmtsLayer]] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )
    ogcServer: str | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    dimensions: Dimensions | None = field(
        default=None, metadata={"type": "Element", "required": False}
    )
    path: str | None = field(default=None, metadata={"type": "Element", "required": False})


@dataclass
class UniqueLayers:
    elements: list[WmsLayer | WmtsLayer] = field(
        metadata={"type": "Element", "required": True}
    )


@dataclass
class Theme(AbstractSchema):
    id: int | str = field(metadata={"type": "Element", "required": True})
    name: str = field(metadata={"type": "Element", "required": True})
    icon: str = field(metadata={"type": "Element", "required": True})
    metadata: MetaData = field(metadata={"type": "Element", "required": True})
    children: list[LayerGroup] = field(
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
                if hasattr(child, "ogcServer"):
                    if child.ogcServer is not None:
                        current_ogc_server = child.ogcServer
                        logging.debug(
                            f"set current_ogc_server by" f"group: {current_ogc_server}"
                        )
                    else:
                        logging.debug(
                            "New nested group but we leave ogc server because"
                            "it was not redefined"
                        )
                self.separate_groups_and_layers(
                    child.children, layer_list, current_ogc_server, current_path
                )
            else:
                if child not in layer_list:
                    if (
                        isinstance(child, WmsLayer)
                        and child.ogcServer is None
                        and current_ogc_server is not None
                    ):
                        child.ogcServer = current_ogc_server
                    child.path = ".".join(current_path + [str(child.name)])
                    layer_list.append(child)

    @property
    def unique_layers_and_groups(self) -> UniqueLayers:
        layer_list: list[WmtsLayer | WmsLayer] = []
        self.separate_groups_and_layers(self.children, layer_list)
        return UniqueLayers(elements=layer_list)


@dataclass
class Themes:
    themes: list[Theme] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )


@dataclass
class ThemesJson:
    themes: list[Theme] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )
    ogc_servers: list[OgcServer] = field(
        default_factory=list, metadata={"type": "Element", "required": False}
    )

    def get_ogc_server_by_name(self, name: str) -> OgcServer | None:
        for ogc_server in self.ogc_servers:
            if name == ogc_server.name:
                return ogc_server
        return None

    def get_theme_by_name(self, name: str) -> Theme | None:
        for theme in self.themes:
            if name == theme.name:
                return theme
        return None
