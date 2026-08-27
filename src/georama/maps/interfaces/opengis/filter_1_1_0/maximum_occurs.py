from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MaximumOccurs:
    """The maximum number of times that values for this parameter group can be
    included.

    If this attribute is omitted, the maximum number is one.
    """

    class Meta:
        name = "maximumOccurs"
        namespace = "http://www.opengis.net/gml"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
