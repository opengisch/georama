from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.arc_string_by_bulge_type import (
    ArcStringByBulgeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcStringByBulge(ArcStringByBulgeType):
    """This variant of the arc computes the mid points of the arcs instead of
    storing the coordinates directly.

    The control point sequence consists of the start and end points of
    each arc plus the bulge (see ISO 19107:2003, 6.4.17.2). The normal
    is a vector normal (perpendicular) to the chord of the arc (see ISO
    19107:2003, 6.4.17.4). The interpolation is fixed as
    "circularArc2PointWithBulge". The number of arcs in the arc string
    may be explicitly stated in the attribute numArc. The number of
    control points in the arc string shall be numArc + 1. The content
    model follows the general pattern for the encoding of curve
    segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
