from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.curve_array_property_type import (
    CurveArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CurveArrayProperty(CurveArrayPropertyType):
    class Meta:
        name = "curveArrayProperty"
        namespace = "http://www.opengis.net/gml/3.2"
