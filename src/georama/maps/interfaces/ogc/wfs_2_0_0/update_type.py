from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.filter import Filter
from georama.maps.interfaces.ogc.wfs_2_0_0.property import Property

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class UpdateType(AbstractTransactionActionType):
    property: list[Property] = field(
        default_factory=list,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    type_name: Optional[QName] = field(
        default=None,
        metadata={
            "name": "typeName",
            "type": "Attribute",
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
