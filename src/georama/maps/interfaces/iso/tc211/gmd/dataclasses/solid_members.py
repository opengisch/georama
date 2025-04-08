from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.solid_array_property_type import (
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
