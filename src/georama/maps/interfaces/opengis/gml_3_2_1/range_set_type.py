from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.boolean_list import BooleanList
from georama.maps.interfaces.opengis.gml_3_2_1.category_list import CategoryList
from georama.maps.interfaces.opengis.gml_3_2_1.count_list import CountList
from georama.maps.interfaces.opengis.gml_3_2_1.data_block import DataBlock
from georama.maps.interfaces.opengis.gml_3_2_1.file import File
from georama.maps.interfaces.opengis.gml_3_2_1.quantity_list import QuantityList
from georama.maps.interfaces.opengis.gml_3_2_1.value_array_property_type import (
    ValueArray,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RangeSetType:
    value_array: list[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity_list: list[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    count_list: list[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    category_list: list[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    boolean_list: list[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    file: Optional[File] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
