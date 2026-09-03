from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FormulaType:
    """Paremeters of a simple formula by which a value using this unit of measure
    can be converted to the corresponding value using the preferred unit of
    measure.

    The formula element contains elements a, b, c and d, whose values
    use the XML Schema type "double". These values are used in the
    formula y = (a + bx) / (c + dx), where x is a value using this unit,
    and y is the corresponding value using the preferred unit. The
    elements a and d are optional, and if values are not provided, those
    parameters are considered to be zero. If values are not provided for
    both a and d, the formula is equivalent to a fraction with numerator
    and denominator parameters.
    """

    a: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    b: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    c: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    d: float | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
