from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid_property_type import (
    MultiSolidPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidProperty(MultiSolidPropertyType):
    """This property element either references a solid aggregate via the XLink-
    attributes or contains the "multi solid" element.

    multiSolidProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiSolid.
    """

    class Meta:
        name = "multiSolidProperty"
        namespace = "http://www.opengis.net/gml"
