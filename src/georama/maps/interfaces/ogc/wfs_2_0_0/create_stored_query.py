from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.create_stored_query_type import (
    CreateStoredQueryType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQuery(CreateStoredQueryType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
