from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.contact_info import ContactInfo
from georama.maps.interfaces.ogc.wfs_2_0_0.individual_name import IndividualName
from georama.maps.interfaces.ogc.wfs_2_0_0.organisation_name import OrganisationName
from georama.maps.interfaces.ogc.wfs_2_0_0.position_name import PositionName
from georama.maps.interfaces.ogc.wfs_2_0_0.role import Role

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ResponsiblePartyType:
    """Identification of, and means of communication with, person responsible for
    the server.

    At least one of IndividualName, OrganisationName, or PositionName
    shall be included.
    """

    individual_name: IndividualName | None = field(
        default=None,
        metadata={
            "name": "IndividualName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    organisation_name: OrganisationName | None = field(
        default=None,
        metadata={
            "name": "OrganisationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    position_name: PositionName | None = field(
        default=None,
        metadata={
            "name": "PositionName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    contact_info: ContactInfo | None = field(
        default=None,
        metadata={
            "name": "ContactInfo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    role: Role | None = field(
        default=None,
        metadata={
            "name": "Role",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "required": True,
        },
    )
