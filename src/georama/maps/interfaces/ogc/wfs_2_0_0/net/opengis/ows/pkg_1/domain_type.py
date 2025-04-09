from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.un_named_domain_type import (
    UnNamedDomainType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DomainType(UnNamedDomainType):
    """
    Valid domain (or allowed set of values) of one quantity, with its name or
    identifier.

    :ivar name: Name or identifier of this quantity.
    """

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
