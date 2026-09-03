from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractCoordinateOperationType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.modified_coordinate import (
    ModifiedCoordinate,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_operation import UsesOperation

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationType(AbstractCoordinateOperationType):
    """
    A pass-through operation specifies that a subset of a coordinate tuple is
    subject to a specific coordinate operation.

    :ivar modified_coordinate: Ordered sequence of positive integers
        defining the positions in a coordinate tuple of the coordinates
        affected by this pass-through operation.
    :ivar uses_operation:
    """

    modified_coordinate: list[ModifiedCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "modifiedCoordinate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    uses_operation: UsesOperation | None = field(
        default=None,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
