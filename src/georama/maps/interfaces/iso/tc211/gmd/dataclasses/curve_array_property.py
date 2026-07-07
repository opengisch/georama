from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_array_property_type import (
    CurveArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveArrayProperty(CurveArrayPropertyType):
    """This property element contains a list of curve elements.

    curveArrayProperty is the predefined property which may be used by
    GML Application Schemas whenever a GML feature has a property with a
    value that is substitutable for a list of curves.
    """

    class Meta:
        name = "curveArrayProperty"
        namespace = "http://www.opengis.net/gml"
