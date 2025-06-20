from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface_type import (
    MultiSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurface(MultiSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
