from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property_type import (
    PointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointProperty(PointPropertyType):
    """This property element either references a point via the XLink-attributes or
    contains the point element.

    pointProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for Point.
    """

    class Meta:
        name = "pointProperty"
        namespace = "http://www.opengis.net/gml"
