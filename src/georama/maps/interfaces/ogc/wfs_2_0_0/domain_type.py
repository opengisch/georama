from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.un_named_domain_type import UnNamedDomainType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DomainType(UnNamedDomainType):
    """
    Valid domain (or allowed set of values) of one quantity, with its name or
    identifier.

    :ivar name: Name or identifier of this quantity.
    """

    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
