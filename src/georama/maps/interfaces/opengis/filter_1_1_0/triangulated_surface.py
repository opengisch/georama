from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface_type import (
    TriangulatedSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurface(TriangulatedSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
