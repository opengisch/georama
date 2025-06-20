from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polygon_property_type import (
    PolygonPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonProperty(PolygonPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility with
    GML 2.0.

    Use "surfaceProperty" instead. This property element either
    references a polygon via the XLink-attributes or contains the
    polygon element.
    """

    class Meta:
        name = "polygonProperty"
        namespace = "http://www.opengis.net/gml"
