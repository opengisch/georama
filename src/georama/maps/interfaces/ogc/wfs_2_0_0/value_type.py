from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ValueType:
    """A single value, encoded as a string.

    This type can be used for one value, for a spacing between allowed
    values, or for the default value of a parameter.
    """

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
