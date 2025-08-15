from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.stored_query_type import StoredQueryType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQuery(StoredQueryType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
