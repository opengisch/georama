from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.sort_order_type import SortOrderType
from georama.maps.interfaces.ogc.wfs_2_0_0.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortPropertyType:
    value_reference: ValueReference | None = field(
        default=None,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        },
    )
    sort_order: SortOrderType | None = field(
        default=None,
        metadata={
            "name": "SortOrder",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
