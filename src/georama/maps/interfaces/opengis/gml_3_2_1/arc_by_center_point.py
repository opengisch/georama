from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.arc_by_center_point_type import (
    ArcByCenterPointType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcByCenterPoint(ArcByCenterPointType):
    """This variant of the arc requires that the points on the arc shall be
    computed instead of storing the coordinates directly.

    The single control point is the center point of the arc plus the
    radius and the bearing at start and end. This representation can be
    used only in 2D. The element radius specifies the radius of the arc.
    The element startAngle specifies the bearing of the arc at the
    start. The element endAngle specifies the bearing of the arc at the
    end. The interpolation is fixed as
    "circularArcCenterPointWithRadius". Since this type describes always
    a single arc, the attribute "numArc" is fixed to "1". The content
    model follows the general pattern for the encoding of curve
    segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
