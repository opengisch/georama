from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.distance_buffer_type import (
    DistanceBufferType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Dwithin(DistanceBufferType):
    class Meta:
        name = "DWithin"
        namespace = "http://www.opengis.net/fes/2.0"
