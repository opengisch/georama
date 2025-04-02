from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.filter import Filter
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ReplaceType(AbstractTransactionActionType):
    other_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
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
