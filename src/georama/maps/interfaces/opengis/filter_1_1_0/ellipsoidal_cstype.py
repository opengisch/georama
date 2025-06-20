from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCstype(AbstractCoordinateSystemType):
    """A two- or three-dimensional coordinate system in which position is specified
    by geodetic latitude, geodetic longitude, and (in the three-dimensional case)
    ellipsoidal height.

    An EllipsoidalCS shall have two or three usesAxis associations.
    """

    class Meta:
        name = "EllipsoidalCSType"
