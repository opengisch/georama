from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.filter import Filter

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ReplaceType(AbstractTransactionActionType):
    other_element: object | None = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##other",
        },
    )
    filter: Filter | None = field(
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
    srs_name: str | None = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
