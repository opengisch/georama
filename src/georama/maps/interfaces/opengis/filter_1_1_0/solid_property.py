from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    SolidPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidProperty(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes or
    contains the solid element.

    solidProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for _Solid.
    """

    class Meta:
        name = "solidProperty"
        namespace = "http://www.opengis.net/gml"
