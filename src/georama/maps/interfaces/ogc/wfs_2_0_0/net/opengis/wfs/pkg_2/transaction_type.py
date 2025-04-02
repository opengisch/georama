from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.all_some_type import (
    AllSomeType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.base_request_type import (
    BaseRequestType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.delete import Delete
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.insert import Insert
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.native import Native
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.replace import Replace
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.update import Update

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class TransactionType(BaseRequestType):
    native: list[Native] = field(
        default_factory=list,
        metadata={
            "name": "Native",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    delete: list[Delete] = field(
        default_factory=list,
        metadata={
            "name": "Delete",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    replace: list[Replace] = field(
        default_factory=list,
        metadata={
            "name": "Replace",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    update: list[Update] = field(
        default_factory=list,
        metadata={
            "name": "Update",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    insert: list[Insert] = field(
        default_factory=list,
        metadata={
            "name": "Insert",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
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
