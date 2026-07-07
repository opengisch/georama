from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCstype(AbstractCoordinateSystemType):
    """A 1-, 2-, or 3-dimensional coordinate system.

    Gives the position of points relative to orthogonal straight axes in
    the 2- and 3-dimensional cases. In the 1-dimensional case, it
    contains a single straight coordinate axis. In the multi-dimensional
    case, all axes shall have the same length unit of measure. A
    CartesianCS shall have one, two, or three usesAxis associations.
    """

    class Meta:
        name = "CartesianCSType"
