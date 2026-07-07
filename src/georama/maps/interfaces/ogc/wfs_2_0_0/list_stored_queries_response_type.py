from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.stored_query_list_item_type import (
    StoredQueryListItemType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueriesResponseType:
    stored_query: list[StoredQueryListItemType] = field(
        default_factory=list,
        metadata={
            "name": "StoredQuery",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
