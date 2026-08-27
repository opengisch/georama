from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IntegerValueList:
    """Gml:integerValueList is an ordered sequence of two or more integer values of
    an operation parameter list, usually used for counts.

    These integer values do not have an associated unit of measure. An
    element of this type contains a space-separated sequence of integer
    values.
    """

    class Meta:
        name = "integerValueList"
        namespace = "http://www.opengis.net/gml"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
