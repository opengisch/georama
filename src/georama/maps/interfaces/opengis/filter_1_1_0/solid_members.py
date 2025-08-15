from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.solid_array_property_type import (
    SolidArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidMembers(SolidArrayPropertyType):
    """This property element contains a list of solids.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "solidMembers"
        namespace = "http://www.opengis.net/gml"
