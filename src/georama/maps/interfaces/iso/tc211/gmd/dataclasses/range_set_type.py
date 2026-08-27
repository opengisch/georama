from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_list import BooleanList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category_list import CategoryList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count_list import CountList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.data_block import DataBlock
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.file import File
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity_list import QuantityList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_array_property_type import (
    ValueArray,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RangeSetType:
    value_array: list[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: list[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: list[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: list[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: list[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    data_block: DataBlock | None = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    file: File | None = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
