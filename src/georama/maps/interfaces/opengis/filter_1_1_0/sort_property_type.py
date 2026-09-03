from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName
from georama.maps.interfaces.opengis.filter_1_1_0.sort_order_type import SortOrderType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SortPropertyType:
    property_name: PropertyName | None = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
    sort_order: SortOrderType | None = field(
        default=None,
        metadata={
            "name": "SortOrder",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
