from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_array_property_type import (
    PointArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointMembers(PointArrayPropertyType):
    """This property element contains a list of points.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "pointMembers"
        namespace = "http://www.opengis.net/gml"
