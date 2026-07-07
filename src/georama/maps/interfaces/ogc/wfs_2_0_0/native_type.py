from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class NativeType(AbstractTransactionActionType):
    vendor_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "vendorId",
            "type": "Attribute",
            "required": True,
        },
    )
    safe_to_ignore: Optional[bool] = field(
        default=None,
        metadata={
            "name": "safeToIgnore",
            "type": "Attribute",
            "required": True,
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
