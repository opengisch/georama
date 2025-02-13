from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.create_stored_query_response_type import (
    CreateStoredQueryResponseType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQueryResponse(CreateStoredQueryResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
