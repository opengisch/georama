from dataclasses import dataclass, field
from typing import Optional
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
    language: Optional[str] = field(
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
