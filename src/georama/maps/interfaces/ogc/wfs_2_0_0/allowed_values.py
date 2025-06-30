from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.ogc.wfs_2_0_0.range import Range
from georama.maps.interfaces.ogc.wfs_2_0_0.value_1 import Value1

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AllowedValues:
    """List of all the valid values and/or ranges of values for this quantity.

    For numeric quantities, signed values should be ordered from
    negative infinity to positive infinity.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    value_or_range: list[Union[Value1, Range]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Value",
                    "type": Value1,
                },
                {
                    "name": "Range",
                    "type": Range,
                },
            ),
        },
    )
