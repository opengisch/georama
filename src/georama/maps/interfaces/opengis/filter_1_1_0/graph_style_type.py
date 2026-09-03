from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.aeshetic_criteria_type import (
    AesheticCriteriaType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.base_style_descriptor_type import (
    BaseStyleDescriptorType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.drawing_type_type import (
    DrawingTypeType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.graph_type_type import GraphTypeType
from georama.maps.interfaces.opengis.filter_1_1_0.line_type_type import LineTypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GraphStyleType(BaseStyleDescriptorType):
    """[complexType of] The style descriptor for a graph consisting of a number of
    features.

    Describes graph-specific style attributes.
    """

    planar: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    min_distance: float | None = field(
        default=None,
        metadata={
            "name": "minDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    min_angle: float | None = field(
        default=None,
        metadata={
            "name": "minAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    graph_type: GraphTypeType | None = field(
        default=None,
        metadata={
            "name": "graphType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    drawing_type: DrawingTypeType | None = field(
        default=None,
        metadata={
            "name": "drawingType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_type: LineTypeType | None = field(
        default=None,
        metadata={
            "name": "lineType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    aesthetic_criteria: list[AesheticCriteriaType] = field(
        default_factory=list,
        metadata={
            "name": "aestheticCriteria",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
