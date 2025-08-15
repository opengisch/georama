from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.curve_array_property_type import (
    CurveArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveArrayProperty(CurveArrayPropertyType):
    class Meta:
        name = "curveArrayProperty"
        namespace = "http://www.opengis.net/gml"
