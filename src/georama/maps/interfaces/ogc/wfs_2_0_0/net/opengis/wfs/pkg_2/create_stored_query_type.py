from dataclasses import dataclass, field

from wfs_2_0_0.net.opengis.wfs.pkg_2.base_request_type import BaseRequestType
from wfs_2_0_0.net.opengis.wfs.pkg_2.stored_query_description_type import (
    StoredQueryDescriptionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQueryType(BaseRequestType):
    stored_query_definition: list[StoredQueryDescriptionType] = field(
        default_factory=list,
        metadata={
            "name": "StoredQueryDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
