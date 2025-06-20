from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    SurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ExtentOf(SurfacePropertyType):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml"
