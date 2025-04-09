from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.list_stored_queries_response_type import (
    ListStoredQueriesResponseType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueriesResponse(ListStoredQueriesResponseType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
