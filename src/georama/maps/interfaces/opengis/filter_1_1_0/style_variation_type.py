from dataclasses import dataclass, field

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
    style_property: str | None = field(
        default=None,
        metadata={
            "name": "styleProperty",
            "type": "Attribute",
            "required": True,
        },
    )
    feature_property_range: str | None = field(
        default=None,
        metadata={
            "name": "featurePropertyRange",
            "type": "Attribute",
        },
    )
