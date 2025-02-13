from dataclasses import dataclass, field
from typing import Optional

from wfs_2_0_0.net.opengis.ows.pkg_1.contact_info import ContactInfo
from wfs_2_0_0.net.opengis.ows.pkg_1.individual_name import IndividualName
from wfs_2_0_0.net.opengis.ows.pkg_1.organisation_name import OrganisationName
from wfs_2_0_0.net.opengis.ows.pkg_1.position_name import PositionName
from wfs_2_0_0.net.opengis.ows.pkg_1.role import Role

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ResponsiblePartyType:
    """Identification of, and means of communication with, person responsible for
    the server.

    At least one of IndividualName, OrganisationName, or PositionName
    shall be included.
    """

    individual_name: Optional[IndividualName] = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    organisation_name: Optional[OrganisationName] = field(
        default=None,
        metadata={
            "name": "OrganisationName",
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
            "required": True,
        },
    )
