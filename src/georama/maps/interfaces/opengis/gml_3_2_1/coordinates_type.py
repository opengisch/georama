from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinatesType:
    """This type is deprecated for tuples with ordinate values that are numbers.

    CoordinatesType is a text string, intended to be used to record an
    array of tuples or coordinates. While it is not possible to enforce
    the internal structure of the string through schema validation, some
    optional attributes have been provided in previous versions of GML
    to support a description of the internal structure. These attributes
    are deprecated. The attributes were intended to be used as follows:
    Decimal symbol used for a decimal point (default="." a stop or
    period) cs              symbol used to separate components within a
    tuple or coordinate string (default="," a comma) ts
    symbol used to separate tuples or coordinate strings (default=" " a
    space) Since it is based on the XML Schema string type,
    CoordinatesType may be used in the construction of tables of tuples
    or arrays of tuples, including ones that contain mixed text and
    numeric values.
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
