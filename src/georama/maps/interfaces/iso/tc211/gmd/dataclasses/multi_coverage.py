from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_surface_property_type import (
    MultiSurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCoverage(MultiSurfacePropertyType):
    class Meta:
        name = "multiCoverage"
        namespace = "http://www.opengis.net/gml"
