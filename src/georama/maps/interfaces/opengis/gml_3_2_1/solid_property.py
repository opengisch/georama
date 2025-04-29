from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.solid_property_type import (
    SolidPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SolidProperty(SolidPropertyType):
    """This property element either references a solid via the XLink-attributes or
    contains the solid element.

    solidProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for AbstractSolid.
    """

    class Meta:
        name = "solidProperty"
        namespace = "http://www.opengis.net/gml/3.2"
