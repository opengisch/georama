from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_surface_property_type import (
    TopoSurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurfaceProperty(TopoSurfacePropertyType):
    class Meta:
        name = "topoSurfaceProperty"
        namespace = "http://www.opengis.net/gml"
