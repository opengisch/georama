from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_surface_type import (
    TopoSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoSurface(TopoSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
