from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.double_or_nil_reason_tuple_list import (
    DoubleOrNilReasonTupleList,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.range_parameters import (
    RangeParameters,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tuple_list import TupleList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataBlockType:
    range_parameters: RangeParameters | None = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    tuple_list: TupleList | None = field(
        default=None,
        metadata={
            "name": "tupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    double_or_nil_reason_tuple_list: DoubleOrNilReasonTupleList | None = field(
        default=None,
        metadata={
            "name": "doubleOrNilReasonTupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
