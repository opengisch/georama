from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
    AbstractCoordinateOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoordinateOperation(AbstractCoordinateOperationType):
    """Gml:AbstractCoordinateOperation is a mathematical operation on coordinates
    that transforms or converts coordinates to another coordinate reference system.

    Many but not all coordinate operations (from CRS A to CRS B) also
    uniquely define the inverse operation (from CRS B to CRS A). In some
    cases, the operation method algorithm for the inverse operation is
    the same as for the forward algorithm, but the signs of some
    operation parameter values shall be reversed. In other cases,
    different algorithms are required for the forward and inverse
    operations, but the same operation parameter values are used. If
    (some) entirely different parameter values are needed, a different
    coordinate operation shall be defined. The optional
    coordinateOperationAccuracy property elements provide estimates of
    the impact of this coordinate operation on point position accuracy.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
