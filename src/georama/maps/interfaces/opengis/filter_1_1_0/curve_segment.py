from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveSegment(AbstractCurveSegmentType):
    """
    The "_CurveSegment" element is the abstract head of the substituition group for
    all curve segment elements, i.e. continuous segments of the same interpolation
    mechanism.
    """

    class Meta:
        name = "_CurveSegment"
        namespace = "http://www.opengis.net/gml"
