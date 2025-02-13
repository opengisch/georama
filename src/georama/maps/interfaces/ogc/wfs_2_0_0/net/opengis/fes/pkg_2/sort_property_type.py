from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.fes.pkg_2.sort_order_type import SortOrderType
from wfs_2_0_0.net.opengis.fes.pkg_2.value_reference import ValueReference

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class SortPropertyType:
    value_reference: Optional[ValueReference] = field(
        default=None,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        },
    )
    sort_order: Optional[SortOrderType] = field(
        default=None,
        metadata={
            "name": "SortOrder",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
