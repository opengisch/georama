from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.distance_buffer_type import (
    DistanceBufferType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Dwithin(DistanceBufferType):
    class Meta:
        name = "DWithin"
        namespace = "http://www.opengis.net/ogc"
