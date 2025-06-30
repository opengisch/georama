from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_query_expression_type import (
    AbstractQueryExpressionType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.parameter_type import ParameterType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryType(AbstractQueryExpressionType):
    parameter: list[ParameterType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
