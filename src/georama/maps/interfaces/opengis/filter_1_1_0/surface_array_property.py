from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.surface_array_property_type import (
    SurfaceArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceArrayProperty(SurfaceArrayPropertyType):
    class Meta:
        name = "surfaceArrayProperty"
        namespace = "http://www.opengis.net/gml"
