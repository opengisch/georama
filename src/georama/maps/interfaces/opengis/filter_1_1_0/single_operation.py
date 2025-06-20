from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractCoordinateOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleOperation(AbstractCoordinateOperationType):
    """
    A single (not concatenated) coordinate operation.
    """

    class Meta:
        name = "_SingleOperation"
        namespace = "http://www.opengis.net/gml"
