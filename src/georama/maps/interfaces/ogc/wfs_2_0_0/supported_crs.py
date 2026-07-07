from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class SupportedCrs:
    """Coordinate reference system in which data from this data(set) or resource is
    available or supported.

    More specific parameter names should be used by specific OWS
    specifications wherever applicable. More than one such parameter can
    be included for different purposes.
    """

    class Meta:
        name = "SupportedCRS"
        namespace = "http://www.opengis.net/ows/1.1"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
