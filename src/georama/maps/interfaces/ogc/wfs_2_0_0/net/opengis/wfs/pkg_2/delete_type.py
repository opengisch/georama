from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from wfs_2_0_0.net.opengis.fes.pkg_2.filter import Filter
from wfs_2_0_0.net.opengis.wfs.pkg_2.abstract_transaction_action_type import (
    AbstractTransactionActionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DeleteType(AbstractTransactionActionType):
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
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
