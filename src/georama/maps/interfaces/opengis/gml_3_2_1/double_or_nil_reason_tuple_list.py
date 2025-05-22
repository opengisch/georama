from dataclasses import dataclass, field
from typing import Union

from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DoubleOrNilReasonTupleList:
    """Gml:doubleOrNilReasonList consists of a list of gml:doubleOrNilReason
    values, each separated by a whitespace.

    The gml:doubleOrNilReason values are grouped into tuples where the
    dimension of each tuple in the list is equal to the number of range
    parameters.
    """

    class Meta:
        name = "doubleOrNilReasonTupleList"
        namespace = "http://www.opengis.net/gml/3.2"

    value: list[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        },
    )
