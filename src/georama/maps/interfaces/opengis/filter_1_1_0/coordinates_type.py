from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinatesType:
    """Tables or arrays of tuples.

    May be used for text-encoding of values from a table. Actually just
    a string, but allows the user to indicate which characters are used
    as separators. The value of the 'cs' attribute is the separator for
    coordinate values, and the value of the 'ts' attribute gives the
    tuple separator (a single space by default); the default values may
    be changed to reflect local usage. Defaults to CSV within a tuple,
    space between tuples. However, any string content will be schema-
    valid.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    decimal: str = field(
        default=".",
        metadata={
            "type": "Attribute",
        },
    )
    cs: str = field(
        default=",",
        metadata={
            "type": "Attribute",
        },
    )
    ts: str = field(
        default=" ",
        metadata={
            "type": "Attribute",
        },
    )
