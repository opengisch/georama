from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.surface_property_type import (
    SurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ExtentOf(SurfacePropertyType):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml/3.2"
