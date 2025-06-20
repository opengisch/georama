from dataclasses import dataclass, field
from typing import Optional

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
class LineStringSegmentType(AbstractCurveSegmentType):
    """A LineStringSegment is a curve segment that is defined by two or more
    coordinate tuples, with linear interpolation between them.

    Note: LineStringSegment implements GM_LineString of ISO 19107.

    :ivar pos:
    :ivar point_property:
    :ivar point_rep: Deprecated with GML version 3.1.0. Use
        "pointProperty" instead. Included for backwards compatibility
        with GML 3.0.0.
    :ivar pos_list:
    :ivar coordinates: Deprecated with GML version 3.1.0. Use "posList"
        instead.
    :ivar interpolation: The attribute "interpolation" specifies the
        curve interpolation mechanism used for this segment. This
        mechanism uses the control points and control parameters to
        determine the position of this curve segment. For a
        LineStringSegment the interpolation is fixed as "linear".
    """

    pos: list[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_property: list[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_rep: list[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pos_list: Optional[PosList] = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinates: Optional[Coordinates] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.LINEAR,
        metadata={
            "type": "Attribute",
        },
    )
