from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_string_type import (
    ArcStringType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcString(ArcStringType):
    """An ArcString is a curve segment that uses three-point circular arc
    interpolation (“circularArc3Points”).

    The number of arcs in the arc string may be explicitly stated in the
    attribute numArc. The number of control points in the arc string
    shall be 2 * numArc + 1. The content model follows the general
    pattern for the encoding of curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
