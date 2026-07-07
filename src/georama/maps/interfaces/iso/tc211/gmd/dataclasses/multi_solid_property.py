from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_solid_property_type import (
    MultiSolidPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidProperty(MultiSolidPropertyType):
    """This property element either references a solid aggregate via the XLink-
    attributes or contains the "multi solid" element.

    multiSolidProperty is the predefined property, which may be used by
    GML Application Schemas whenever a GML feature has a property with a
    value that is substitutable for MultiSolid.
    """

    class Meta:
        name = "multiSolidProperty"
        namespace = "http://www.opengis.net/gml"
