from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.point_property_type import (
    PointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointRep(PointPropertyType):
    """Deprecated with GML version 3.1.0.

    Use "pointProperty" instead. Included for backwards compatibility
    with GML 3.0.0.
    """

    class Meta:
        name = "pointRep"
        namespace = "http://www.opengis.net/gml"
