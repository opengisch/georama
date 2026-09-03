from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MinimumOccurs:
    """Gml:minimumOccurs is the minimum number of times that values for this
    parameter group or parameter are required.

    If this attribute is omitted, the minimum number shall be one.
    """

    class Meta:
        name = "minimumOccurs"
        namespace = "http://www.opengis.net/gml"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
