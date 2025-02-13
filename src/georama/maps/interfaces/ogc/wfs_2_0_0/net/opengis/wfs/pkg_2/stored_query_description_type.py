from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.ows.pkg_1.metadata import Metadata
from wfs_2_0_0.net.opengis.wfs.pkg_2.abstract import Abstract
from wfs_2_0_0.net.opengis.wfs.pkg_2.parameter_expression_type import (
    ParameterExpressionType,
)
from wfs_2_0_0.net.opengis.wfs.pkg_2.query_expression_text_type import (
    QueryExpressionTextType,
)
from wfs_2_0_0.net.opengis.wfs.pkg_2.title import Title

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryDescriptionType:
    title: list[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    abstract: list[Abstract] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
