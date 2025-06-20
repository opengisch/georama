from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractCoordinateOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Operation(AbstractCoordinateOperationType):
    """A parameterized mathematical operation on coordinates that transforms or
    converts coordinates to another coordinate reference system.

    This coordinate operation uses an operation method, usually with
    associated parameter values. However, operation methods and
    parameter values are directly associated with concrete subtypes, not
    with this abstract type. This abstract complexType shall not be
    directly used, extended, or restricted in a compliant Application
    Schema.
    """

    class Meta:
        name = "_Operation"
        namespace = "http://www.opengis.net/gml"
