from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface_property_type import (
    MultiSurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiExtentOf(MultiSurfacePropertyType):
    class Meta:
        name = "multiExtentOf"
        namespace = "http://www.opengis.net/gml"
