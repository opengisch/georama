from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.null_enumeration_value import (
    NullEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CountExtent:
    """Utility element to store a 2-point range of frequency values.

    If one member is a null, then this is a single ended interval.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: list[str | NullEnumerationValue] = field(
        default_factory=list,
        metadata={
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
