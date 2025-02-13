from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.create_stored_query_type import (
    CreateStoredQueryType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQuery(CreateStoredQueryType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
