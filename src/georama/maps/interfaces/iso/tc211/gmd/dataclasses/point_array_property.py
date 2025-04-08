from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_array_property_type import (
    PointArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointArrayProperty(PointArrayPropertyType):
    """This property element contains a list of point elements.

    pointArrayProperty is the predefined property which may be used by
    GML Application Schemas whenever a GML feature has a property with a
    value that is substitutable for a list of points.
    """

    class Meta:
        name = "pointArrayProperty"
        namespace = "http://www.opengis.net/gml"
