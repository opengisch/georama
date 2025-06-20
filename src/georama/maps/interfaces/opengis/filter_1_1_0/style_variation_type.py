from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StyleVariationType:
    """
    Used to vary individual graphic parameters and attributes of the style, symbol
    or text.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    style_property: Optional[str] = field(
        default=None,
        metadata={
            "name": "styleProperty",
            "type": "Attribute",
            "required": True,
        },
    )
    feature_property_range: Optional[str] = field(
        default=None,
        metadata={
            "name": "featurePropertyRange",
            "type": "Attribute",
        },
    )
