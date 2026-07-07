from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_geometry_property_type import (
    MultiGeometryPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiGeometryProperty(MultiGeometryPropertyType):
    """This property element either references a geometric aggregate via the XLink-
    attributes or contains the "multi geometry" element.

    multiGeometryProperty is the predefined property which can be used
    by GML Application Schemas whenever a GML Feature has a property
    with a value that is substitutable for _GeometricAggregate.
    """

    class Meta:
        name = "multiGeometryProperty"
        namespace = "http://www.opengis.net/gml"
