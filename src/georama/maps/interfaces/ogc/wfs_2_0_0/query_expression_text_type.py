from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class QueryExpressionTextType:
    return_feature_types: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "returnFeatureTypes",
            "type": "Attribute",
            "tokens": True,
        },
    )
    language: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    is_private: bool = field(
        default=False,
        metadata={
            "name": "isPrivate",
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )
