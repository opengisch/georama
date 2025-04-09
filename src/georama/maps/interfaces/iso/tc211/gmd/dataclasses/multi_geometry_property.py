from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_geometry_property_type import (
    MultiGeometryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiGeometryProperty(MultiGeometryPropertyType):
    """This property element either references a geometric aggregate via the XLink-
    attributes or contains the "multi geometry" element.

    multiGeometryProperty is the predefined property, which may be used
    by GML Application Schemas whenever a GML feature has a property
    with a value that is substitutable for AbstractGeometricAggregate.
    """

    class Meta:
        name = "multiGeometryProperty"
        namespace = "http://www.opengis.net/gml"
