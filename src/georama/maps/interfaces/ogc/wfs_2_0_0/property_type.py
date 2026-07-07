from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.property_type_value_reference import (
    PropertyTypeValueReference,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class PropertyType:
    value_reference: Optional[PropertyTypeValueReference] = field(
        default=None,
        metadata={
            "name": "ValueReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
        },
    )
    value: Optional[object] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
