from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.double_or_nil_reason_tuple_list import (
    DoubleOrNilReasonTupleList,
)
from georama.maps.interfaces.opengis.gml_3_2_1.range_parameters import RangeParameters
from georama.maps.interfaces.opengis.gml_3_2_1.tuple_list import TupleList

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DataBlockType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    tuple_list: Optional[TupleList] = field(
        default=None,
        metadata={
            "name": "tupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    double_or_nil_reason_tuple_list: Optional[DoubleOrNilReasonTupleList] = field(
        default=None,
        metadata={
            "name": "doubleOrNilReasonTupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
