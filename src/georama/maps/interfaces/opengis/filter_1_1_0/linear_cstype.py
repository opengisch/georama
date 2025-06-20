from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearCstype(AbstractCoordinateSystemType):
    """A one-dimensional coordinate system that consists of the points that lie on
    the single axis described.

    The associated ordinate is the distance from the specified origin to
    the point along the axis. Example: usage of the line feature
    representing a road to describe points on or along that road. A
    LinearCS shall have one usesAxis association.
    """

    class Meta:
        name = "LinearCSType"
