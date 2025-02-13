from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.wfs.pkg_2.update_action_type import UpdateActionType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class PropertyType:
    value_reference: Optional["PropertyType.ValueReference"] = field(
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

    @dataclass
    class ValueReference:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        action: UpdateActionType = field(
            default=UpdateActionType.REPLACE,
            metadata={
                "type": "Attribute",
            },
        )
