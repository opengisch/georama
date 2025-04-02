from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.address_type import (
    AddressType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.online_resource_type import (
    OnlineResourceType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.telephone_type import (
    TelephoneType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ContactType:
    """Information required to enable contact with the responsible person and/or
    organization.

    For OWS use in the service metadata document, the optional
    hoursOfService and contactInstructions elements were retained, as
    possibly being useful in the ServiceProvider section.

    :ivar phone: Telephone numbers at which the organization or
        individual may be contacted.
    :ivar address: Physical and email address at which the organization
        or individual may be contacted.
    :ivar online_resource: On-line information that can be used to
        contact the individual or organization. OWS specifics: The
        xlink:href attribute in the xlink:simpleAttrs attribute group
        shall be used to reference this resource. Whenever practical,
        the xlink:href attribute with type anyURI should be a URL from
        which more contact information can be electronically retrieved.
        The xlink:title attribute with type "string" can be used to name
        this set of information. The other attributes in the
        xlink:simpleAttrs attribute group should not be used.
    :ivar hours_of_service: Time period (including time zone) when
        individuals can contact the organization or individual.
    :ivar contact_instructions: Supplemental instructions on how or when
        to contact the individual or organization.
    """

    phone: Optional[TelephoneType] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    address: Optional[AddressType] = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    online_resource: Optional[OnlineResourceType] = field(
        default=None,
        metadata={
            "name": "OnlineResource",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    hours_of_service: Optional[str] = field(
        default=None,
        metadata={
            "name": "HoursOfService",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    contact_instructions: Optional[str] = field(
        default=None,
        metadata={
            "name": "ContactInstructions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
