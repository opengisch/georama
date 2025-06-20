from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolarCstype(AbstractCoordinateSystemType):
    """A two-dimensional coordinate system in which position is specified by the
    distance from the origin and the angle between the line from the origin to a
    point and a reference direction.

    A PolarCS shall have two usesAxis associations.
    """

    class Meta:
        name = "PolarCSType"
