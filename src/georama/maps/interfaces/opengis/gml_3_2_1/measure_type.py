from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MeasureType:
    """Gml:MeasureType supports recording an amount encoded as a value of XML
    Schema double, together with a units of measure indicated by an attribute uom,
    short for "units Of measure".

    The value of the uom attribute identifies a reference system for the
    amount, usually a ratio or interval scale.
    """

    value: float | None = field(
        default=None,
        metadata={
            "required": True,
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
