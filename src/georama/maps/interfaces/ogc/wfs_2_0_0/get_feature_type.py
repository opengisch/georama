from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.base_request_type import BaseRequestType
from georama.maps.interfaces.ogc.wfs_2_0_0.query import Query
from georama.maps.interfaces.ogc.wfs_2_0_0.resolve_value_type import ResolveValueType
from georama.maps.interfaces.ogc.wfs_2_0_0.result_type_type import ResultTypeType
from georama.maps.interfaces.ogc.wfs_2_0_0.star_string_type import StarStringType
from georama.maps.interfaces.ogc.wfs_2_0_0.stored_query import StoredQuery

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetFeatureType(BaseRequestType):
    stored_query_or_query: list[StoredQuery | Query] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StoredQuery",
                    "type": StoredQuery,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "Query",
                    "type": Query,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
            ),
        },
    )
    start_index: int = field(
        default=0,
        metadata={
            "name": "startIndex",
            "type": "Attribute",
        },
    )
    count: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    result_type: ResultTypeType = field(
        default=ResultTypeType.RESULTS,
        metadata={
            "name": "resultType",
            "type": "Attribute",
        },
    )
    output_format: str = field(
        default="application/gml+xml; version=3.2",
        metadata={
            "name": "outputFormat",
            "type": "Attribute",
        },
    )
    resolve: ResolveValueType = field(
        default=ResolveValueType.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    resolve_depth: int | StarStringType = field(
        default=StarStringType.ASTERISK,
        metadata={
            "name": "resolveDepth",
            "type": "Attribute",
        },
    )
    resolve_timeout: int = field(
        default=300,
        metadata={
            "name": "resolveTimeout",
            "type": "Attribute",
        },
    )
