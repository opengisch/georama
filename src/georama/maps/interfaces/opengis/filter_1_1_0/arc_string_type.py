from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coordinates import Coordinates
from georama.maps.interfaces.opengis.filter_1_1_0.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.point_property import PointProperty
from georama.maps.interfaces.opengis.filter_1_1_0.point_rep import PointRep
from georama.maps.interfaces.opengis.filter_1_1_0.pos import Pos
from georama.maps.interfaces.opengis.filter_1_1_0.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcStringType(AbstractCurveSegmentType):
    """
    An ArcString is a curve segment that uses three-point circular arc
    interpolation.

    :ivar choice:
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For an ArcString
        the interpolation is fixed as "circularArc3Points".
    :ivar num_arc: The number of arcs in the arc string can be
        explicitly stated in this attribute. The number of control
        points in the arc string must be 2 * numArc + 1.
    """

    choice: list[Union[Pos, PointProperty, PointRep, PosList, Coordinates]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "pos",
                    "type": Pos,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "pointProperty",
                    "type": PointProperty,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "pointRep",
                    "type": PointRep,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "posList",
                    "type": PosList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "coordinates",
                    "type": Coordinates,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "type": "Attribute",
        },
    )
    num_arc: Optional[int] = field(
        default=None,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
