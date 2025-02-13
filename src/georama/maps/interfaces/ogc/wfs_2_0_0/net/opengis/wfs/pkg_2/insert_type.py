from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.wfs.pkg_2.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class InsertType(AbstractTransactionActionType):
    other_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    input_format: str = field(
        default="application/gml+xml; version=3.2",
        metadata={
            "name": "inputFormat",
            "type": "Attribute",
        },
    )
    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
