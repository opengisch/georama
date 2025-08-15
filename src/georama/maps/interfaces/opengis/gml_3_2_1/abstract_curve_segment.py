from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCurveSegment(AbstractCurveSegmentType):
    """A curve segment defines a homogeneous segment of a curve.

    The attributes numDerivativesAtStart, numDerivativesAtEnd and
    numDerivativesInterior specify the type of continuity as specified
    in ISO 19107:2003, 6.4.9.3. The AbstractCurveSegment element is the
    abstract head of the substituition group for all curve segment
    elements, i.e. continuous segments of the same interpolation
    mechanism. All curve segments shall have an attribute interpolation
    with type gml:CurveInterpolationType specifying the curve
    interpolation mechanism used for this segment. This mechanism uses
    the control points and control parameters to determine the position
    of this curve segment.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
