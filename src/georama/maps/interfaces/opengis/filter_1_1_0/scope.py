from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Scope:
    """
    Description of domain of usage, or limitations of usage, for which this CRS
    object is valid.
    """

    class Meta:
        name = "scope"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
