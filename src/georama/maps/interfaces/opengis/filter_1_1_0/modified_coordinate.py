from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ModifiedCoordinate:
    """
    A positive integer defining a position in a coordinate tuple.
    """

    class Meta:
        name = "modifiedCoordinate"
        namespace = "http://www.opengis.net/gml"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
