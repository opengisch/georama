from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.describe_stored_queries_type import (
    DescribeStoredQueriesType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeStoredQueries(DescribeStoredQueriesType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
