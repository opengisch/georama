from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureListType:
    """
    Gml:MeasureListType provides for a list of quantities.
    """

    value: list[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    uom: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        },
    )
