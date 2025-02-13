from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.wfs.pkg_2.all_some_type import AllSomeType
from wfs_2_0_0.net.opengis.wfs.pkg_2.base_request_type import BaseRequestType
from wfs_2_0_0.net.opengis.wfs.pkg_2.query import Query
from wfs_2_0_0.net.opengis.wfs.pkg_2.stored_query import StoredQuery

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeatureType(BaseRequestType):
    stored_query: list[StoredQuery] = field(
        default_factory=list,
        metadata={
            "name": "StoredQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    query: list[Query] = field(
        default_factory=list,
        metadata={
            "name": "Query",
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
    expiry: int = field(
        default=300,
        metadata={
            "type": "Attribute",
        },
    )
    lock_action: AllSomeType = field(
        default=AllSomeType.ALL,
        metadata={
            "name": "lockAction",
            "type": "Attribute",
        },
    )
