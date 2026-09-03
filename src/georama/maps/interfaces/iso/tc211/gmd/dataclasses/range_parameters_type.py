from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_1 import Boolean1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_list import BooleanList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category import Category
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category_extent import (
    CategoryExtent,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category_list import CategoryList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count import Count
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count_extent import CountExtent
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count_list import CountList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity import Quantity
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity_extent import (
    QuantityExtent,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity_list import QuantityList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_array_property_type import (
    CompositeValue,
    ValueArray,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RangeParametersType:
    """Gml:RangeParameterType is a framework for the description of the range
    parameters each of which is a gml:AbstractValue.

    Specific range parameters are defined through the creation of a GML
    Application Schema that provides elements that are substitutable for
    gml:AbstractValue.
    """

    quantity_extent: QuantityExtent | None = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: CountExtent | None = field(
        default=None,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_extent: CategoryExtent | None = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: ValueArray | None = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: CompositeValue | None = field(
        default=None,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: QuantityList | None = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: CountList | None = field(
        default=None,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: CategoryList | None = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: BooleanList | None = field(
        default=None,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    count: Count | None = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    category: Category | None = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    boolean: Boolean1 | None = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
