from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class StringValue:
    """Gml:stringValue is a character string value of an operation parameter.

    A string value does not have an associated unit of measure.
    """

    class Meta:
        name = "stringValue"
        namespace = "http://www.opengis.net/gml/3.2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
