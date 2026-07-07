from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometry_style_2 import GeometryStyle2
from georama.maps.interfaces.opengis.filter_1_1_0.label_style_2 import LabelStyle2
from georama.maps.interfaces.opengis.filter_1_1_0.query_grammar_enumeration import (
    QueryGrammarEnumeration,
)
from georama.maps.interfaces.opengis.filter_1_1_0.topology_style_2 import TopologyStyle2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureStyleType(AbstractGmltype):
    """
    [complexType of] The style descriptor for features.
    """

    feature_constraint: Optional[str] = field(
        default=None,
        metadata={
            "name": "featureConstraint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometry_style: list[GeometryStyle2] = field(
        default_factory=list,
        metadata={
            "name": "geometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topology_style: list[TopologyStyle2] = field(
        default_factory=list,
        metadata={
            "name": "topologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    label_style: Optional[LabelStyle2] = field(
        default=None,
        metadata={
            "name": "labelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "featureType",
            "type": "Attribute",
        },
    )
    base_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "baseType",
            "type": "Attribute",
        },
    )
    query_grammar: Optional[QueryGrammarEnumeration] = field(
        default=None,
        metadata={
            "name": "queryGrammar",
            "type": "Attribute",
        },
    )
