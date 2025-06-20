from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_point_property_type import (
    MultiPointPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiLocation(MultiPointPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility with
    GML 2.0.

    Use "curveMember" instead. This property element either references a
    line string via the XLink-attributes or contains the line string
    element.
    """

    class Meta:
        name = "multiLocation"
        namespace = "http://www.opengis.net/gml"
