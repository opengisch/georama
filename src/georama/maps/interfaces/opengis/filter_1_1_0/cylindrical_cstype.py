from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCstype(AbstractCoordinateSystemType):
    """A three-dimensional coordinate system consisting of a polar coordinate
    system extended by a straight coordinate axis perpendicular to the plane
    spanned by the polar coordinate system.

    A CylindricalCS shall have three usesAxis associations.
    """

    class Meta:
        name = "CylindricalCSType"
