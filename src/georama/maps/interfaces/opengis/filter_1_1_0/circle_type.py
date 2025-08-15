from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.arc_type_1 import ArcType1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CircleType(ArcType1):
    """A Circle is an arc whose ends coincide to form a simple closed loop.

    The "start" and "end" bearing are equal and shall be the bearing for
    the first controlPoint listed. The three control points must be
    distinct non-co-linear points for the Circle to be unambiguously
    defined. The arc is simply extended past the third control point
    until the first control point is encountered.
    """
