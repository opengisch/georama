from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface_type import (
    PolyhedralSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolyhedralSurface(PolyhedralSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
