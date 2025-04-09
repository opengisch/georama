from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.stored_query_description_type import (
    StoredQueryDescriptionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeStoredQueriesResponseType:
    stored_query_description: list[StoredQueryDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "StoredQueryDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
