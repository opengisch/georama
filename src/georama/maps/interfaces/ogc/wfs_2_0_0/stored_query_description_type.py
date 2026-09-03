from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_2 import Abstract2
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata
from georama.maps.interfaces.ogc.wfs_2_0_0.parameter_expression_type import (
    ParameterExpressionType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.query_expression_text_type import (
    QueryExpressionTextType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.title_2 import Title2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryDescriptionType:
    title: list[Title2] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    abstract: list[Abstract2] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    metadata: list[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    parameter: list[ParameterExpressionType] = field(
        default_factory=list,
        metadata={
            "name": "Parameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    query_expression_text: list[QueryExpressionTextType] = field(
        default_factory=list,
        metadata={
            "name": "QueryExpressionText",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 1,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
