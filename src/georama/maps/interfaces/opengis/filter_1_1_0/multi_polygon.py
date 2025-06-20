from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_polygon_type import (
    MultiPolygonType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPolygon(MultiPolygonType):
    """Deprecated with GML 3.0 and included for backwards compatibility with GML 2.

    Use the "MultiSurface" element instead.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
