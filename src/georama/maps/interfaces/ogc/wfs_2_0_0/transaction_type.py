from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.all_some_type import AllSomeType
from georama.maps.interfaces.ogc.wfs_2_0_0.base_request_type import BaseRequestType
from georama.maps.interfaces.ogc.wfs_2_0_0.delete import Delete
from georama.maps.interfaces.ogc.wfs_2_0_0.insert import Insert
from georama.maps.interfaces.ogc.wfs_2_0_0.native import Native
from georama.maps.interfaces.ogc.wfs_2_0_0.replace import Replace
from georama.maps.interfaces.ogc.wfs_2_0_0.update import Update

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionType(BaseRequestType):
    choice: list[Union[Native, Delete, Replace, Update, Insert]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Native",
                    "type": Native,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "Delete",
                    "type": Delete,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "Replace",
                    "type": Replace,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "Update",
                    "type": Update,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "Insert",
                    "type": Insert,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
            ),
        },
    )
    lock_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "lockId",
            "type": "Attribute",
        },
    )
    release_action: AllSomeType = field(
        default=AllSomeType.ALL,
        metadata={
            "name": "releaseAction",
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
