from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.line_string_property_type import (
    LineStringPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringMember(LineStringPropertyType):
    """Deprecated with GML 3.0 and included only for backwards compatibility with
    GML 2.0.

    Use "curveMember" instead. This property element either references a
    line string via the XLink-attributes or contains the line string
    element.
    """

    class Meta:
        name = "lineStringMember"
        namespace = "http://www.opengis.net/gml"
