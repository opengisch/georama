from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ModifiedCoordinate:
    """
    Gml:modifiedCoordinate is a positive integer defining a position in a
    coordinate tuple.
    """

    class Meta:
        name = "modifiedCoordinate"
        namespace = "http://www.opengis.net/gml/3.2"

    value: int | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
