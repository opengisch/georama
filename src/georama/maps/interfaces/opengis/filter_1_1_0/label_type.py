from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelType:
    """
    Label is mixed -- composed of text and XPath expressions used to extract the
    useful information from the feature.
    """

    transform: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "LabelExpression",
                    "type": str,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
