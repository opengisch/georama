from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BooleanValue:
    """Gml:booleanValue is a boolean value of an operation parameter.

    A Boolean value does not have an associated unit of measure.
    """

    class Meta:
        name = "booleanValue"
        namespace = "http://www.opengis.net/gml/3.2"

    value: bool | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
