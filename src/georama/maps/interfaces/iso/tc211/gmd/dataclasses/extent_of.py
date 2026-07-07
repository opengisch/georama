from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_property_type import (
    SurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ExtentOf(SurfacePropertyType):
    class Meta:
        name = "extentOf"
        namespace = "http://www.opengis.net/gml"
