from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Surface(SurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
