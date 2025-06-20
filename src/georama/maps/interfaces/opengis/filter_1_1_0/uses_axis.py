from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_axis_ref_type import (
    CoordinateSystemAxisRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesAxis(CoordinateSystemAxisRefType):
    """
    Association to a coordinate system axis.
    """

    class Meta:
        name = "usesAxis"
        namespace = "http://www.opengis.net/gml"
