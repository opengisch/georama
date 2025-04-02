from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.list_stored_queries_type import (
    ListStoredQueriesType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueries(ListStoredQueriesType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
