from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractCoordinateOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperation(AbstractCoordinateOperationType):
    class Meta:
        name = "_CoordinateOperation"
        namespace = "http://www.opengis.net/gml"
