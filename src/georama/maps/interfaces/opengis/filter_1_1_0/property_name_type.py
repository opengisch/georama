from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.expression_type import ExpressionType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyNameType(ExpressionType):
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
