from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_query_expression_type import (
    AbstractQueryExpressionType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.filter import Filter
from georama.maps.interfaces.ogc.wfs_2_0_0.property_name import PropertyName
from georama.maps.interfaces.ogc.wfs_2_0_0.sort_by import SortBy

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractAdhocQueryExpressionType(AbstractQueryExpressionType):
    property_name: list[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    filter: Optional[Filter] = field(
        default=None,
        metadata={
            "name": "Filter",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    sort_by: Optional[SortBy] = field(
        default=None,
        metadata={
            "name": "SortBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    type_names: list[str] = field(
        default_factory=list,
        metadata={
            "name": "typeNames",
            "type": "Attribute",
            "pattern": r"schema\-element\(.+\)",
            "tokens": True,
        },
    )
    aliases: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "tokens": True,
        },
    )
