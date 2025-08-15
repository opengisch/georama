from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.create_stored_query_response_type import (
    CreateStoredQueryResponseType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQueryResponse(CreateStoredQueryResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
