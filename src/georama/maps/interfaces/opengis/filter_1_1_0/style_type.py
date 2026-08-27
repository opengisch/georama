from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_style_type import (
    AbstractStyleType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.feature_style_2 import FeatureStyle2
from georama.maps.interfaces.opengis.filter_1_1_0.graph_style_2 import GraphStyle2

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StyleType(AbstractStyleType):
    """[complexType of] Predefined concrete value of the top-level property.

    Encapsulates all other styling information.
    """

    feature_style: list[FeatureStyle2] = field(
        default_factory=list,
        metadata={
            "name": "featureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    graph_style: GraphStyle2 | None = field(
        default=None,
        metadata={
            "name": "graphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
