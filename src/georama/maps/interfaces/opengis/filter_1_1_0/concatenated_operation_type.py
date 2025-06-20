from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractCoordinateOperationType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_single_operation import (
    UsesSingleOperation,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationType(AbstractCoordinateOperationType):
    """An ordered sequence of two or more single coordinate operations.

    The sequence of operations is constrained by the requirement that
    the source coordinate reference system of step (n+1) must be the
    same as the target coordinate reference system of step (n). The
    source coordinate reference system of the first step and the target
    coordinate reference system of the last step are the source and
    target coordinate reference system associated with the concatenated
    operation. Instead of a forward operation, an inverse operation may
    be used for one or more of the operation steps mentioned above, if
    the inverse operation is uniquely defined by the forward operation.

    :ivar uses_single_operation: Ordered sequence of associations to the
        two or more single operations used by this concatenated
        operation.
    """

    uses_single_operation: list[UsesSingleOperation] = field(
        default_factory=list,
        metadata={
            "name": "usesSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        },
    )
