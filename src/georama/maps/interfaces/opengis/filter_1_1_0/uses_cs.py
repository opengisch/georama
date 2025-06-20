from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_ref_type import (
    CoordinateSystemRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCs(CoordinateSystemRefType):
    """
    Association to the coordinate system used by this CRS.
    """

    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml"
