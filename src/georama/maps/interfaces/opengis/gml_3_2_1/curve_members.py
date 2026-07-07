from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.curve_array_property_type import (
    CurveArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveMembers(CurveArrayPropertyType):
    """This property element contains a list of curves.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "curveMembers"
        namespace = "http://www.opengis.net/gml/3.2"
