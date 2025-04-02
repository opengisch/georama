from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.contact_info import (
    ContactInfo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.individual_name import (
    IndividualName,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.position_name import (
    PositionName,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.role import Role

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ResponsiblePartySubsetType:
    """Identification of, and means of communication with, person responsible for
    the server.

    For OWS use in the ServiceProvider section of a service metadata
    document, the optional organizationName element was removed, since
    this type is always used with the ProviderName element which
    provides that information. The mandatory "role" element was changed
    to optional, since no clear use of this information is known in the
    ServiceProvider section.
    """

    individual_name: Optional[IndividualName] = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    position_name: Optional[PositionName] = field(
        default=None,
        metadata={
            "name": "PositionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    contact_info: Optional[ContactInfo] = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    role: Optional[Role] = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
