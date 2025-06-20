from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.distance_buffer_type import (
    DistanceBufferType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Beyond(DistanceBufferType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
