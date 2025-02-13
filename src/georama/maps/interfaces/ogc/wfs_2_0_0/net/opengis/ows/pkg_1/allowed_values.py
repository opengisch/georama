from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.ows.pkg_1.range import Range
from wfs_2_0_0.net.opengis.ows.pkg_1.value import Value

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AllowedValues:
    """List of all the valid values and/or ranges of values for this quantity.

    For numeric quantities, signed values should be ordered from
    negative infinity to positive infinity.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value: list[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    range: list[Range] = field(
        default_factory=list,
        metadata={
            "name": "Range",
            "type": "Element",
        },
    )
