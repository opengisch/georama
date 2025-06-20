from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.opengis.filter_1_1_0.null_enumeration_value import (
    NullEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DoubleOrNullTupleList:
    class Meta:
        name = "doubleOrNullTupleList"
        namespace = "http://www.opengis.net/gml"

    value: list[Union[str, NullEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
