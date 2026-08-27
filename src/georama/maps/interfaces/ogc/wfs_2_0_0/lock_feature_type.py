from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.all_some_type import AllSomeType
from georama.maps.interfaces.ogc.wfs_2_0_0.base_request_type import BaseRequestType
from georama.maps.interfaces.ogc.wfs_2_0_0.query import Query
from georama.maps.interfaces.ogc.wfs_2_0_0.stored_query import StoredQuery

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeatureType(BaseRequestType):
    stored_query_or_query: list[StoredQuery | Query] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StoredQuery",
                    "type": StoredQuery,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "Query",
                    "type": Query,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
            ),
        },
    )
    lock_id: str | None = field(
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
