from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import (
    CurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveProperty(CurvePropertyType):
    """This property element either references a curve via the XLink-attributes or
    contains the curve element.

    curveProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for _Curve.
    """

    class Meta:
        name = "curveProperty"
        namespace = "http://www.opengis.net/gml"
