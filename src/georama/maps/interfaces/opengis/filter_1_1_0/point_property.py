from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.point_property_type import (
    PointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointProperty(PointPropertyType):
    """This property element either references a point via the XLink-attributes or
    contains the point element.

    pointProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for Point.
    """

    class Meta:
        name = "pointProperty"
        namespace = "http://www.opengis.net/gml"
