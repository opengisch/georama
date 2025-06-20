from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCurveSegmentType:
    """
    Curve segment defines a homogeneous segment of a curve.

    :ivar num_derivatives_at_start: The attribute
        "numDerivativesAtStart" specifies the type of continuity between
        this curve segment and its predecessor. If this is the first
        curve segment in the curve, one of these values, as appropriate,
        is ignored. The default value of "0" means simple continuity,
        which is a mandatory minimum level of continuity. This level is
        referred to as "C 0 " in mathematical texts. A value of 1 means
        that the function and its first derivative are continuous at the
        appropriate end point: "C 1 " continuity. A value of "n" for any
        integer means the function and its first n derivatives are
        continuous: "C n " continuity. NOTE: Use of these values is only
        appropriate when the basic curve definition is an
        underdetermined system. For example, line string segments cannot
        support continuity above C 0 , since there is no spare control
        parameter to adjust the incoming angle at the end points of the
        segment. Spline functions on the other hand often have extra
        degrees of freedom on end segments that allow them to adjust the
        values of the derivatives to support C 1 or higher continuity.
    :ivar num_derivatives_at_end: The attribute "numDerivativesAtEnd"
        specifies the type of continuity between this curve segment and
        its successor. If this is the last curve segment in the curve,
        one of these values, as appropriate, is ignored. The default
        value of "0" means simple continuity, which is a mandatory
        minimum level of continuity. This level is referred to as "C 0 "
        in mathematical texts. A value of 1 means that the function and
        its first derivative are continuous at the appropriate end
        point: "C 1 " continuity. A value of "n" for any integer means
        the function and its first n derivatives are continuous: "C n "
        continuity. NOTE: Use of these values is only appropriate when
        the basic curve definition is an underdetermined system. For
        example, line string segments cannot support continuity above C
        0 , since there is no spare control parameter to adjust the
        incoming angle at the end points of the segment. Spline
        functions on the other hand often have extra degrees of freedom
        on end segments that allow them to adjust the values of the
        derivatives to support C 1 or higher continuity.
    :ivar num_derivative_interior: The attribute
        "numDerivativesInterior" specifies the type of continuity that
        is guaranteed interior to the curve. The default value of "0"
        means simple continuity, which is a mandatory minimum level of
        continuity. This level is referred to as "C 0 " in mathematical
        texts. A value of 1 means that the function and its first
        derivative are continuous at the appropriate end point: "C 1 "
        continuity. A value of "n" for any integer means the function
        and its first n derivatives are continuous: "C n " continuity.
        NOTE: Use of these values is only appropriate when the basic
        curve definition is an underdetermined system. For example, line
        string segments cannot support continuity above C 0 , since
        there is no spare control parameter to adjust the incoming angle
        at the end points of the segment. Spline functions on the other
        hand often have extra degrees of freedom on end segments that
        allow them to adjust the values of the derivatives to support C
        1 or higher continuity.
    """

    num_derivatives_at_start: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtStart",
            "type": "Attribute",
        },
    )
    num_derivatives_at_end: int = field(
        default=0,
        metadata={
            "name": "numDerivativesAtEnd",
            "type": "Attribute",
        },
    )
    num_derivative_interior: int = field(
        default=0,
        metadata={
            "name": "numDerivativeInterior",
            "type": "Attribute",
        },
    )
