from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_adhoc_query_expression_type import (
    AbstractAdhocQueryExpressionType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class QueryType(AbstractAdhocQueryExpressionType):
    srs_name: str | None = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    feature_version: str | None = field(
        default=None,
        metadata={
            "name": "featureVersion",
            "type": "Attribute",
        },
    )
