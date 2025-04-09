from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Scope:
    """The gml:scope property provides a description of the usage, or limitations
    of usage, for which this CRS-related object is valid.

    If unknown, enter "not known".
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
