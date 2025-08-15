from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    CoordinateReferenceSystemRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateReferenceSystemRef(CoordinateReferenceSystemRefType):
    class Meta:
        name = "coordinateReferenceSystemRef"
        namespace = "http://www.opengis.net/gml"
