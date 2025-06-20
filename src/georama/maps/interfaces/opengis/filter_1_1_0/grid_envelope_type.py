from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridEnvelopeType:
    """Provides grid coordinate values for the diametrically opposed corners of an
    envelope that bounds a section of grid.

    The value of a single coordinate is the number of offsets from the
    origin of the grid in the direction of a specific axis.
    """

    low: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
    high: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
