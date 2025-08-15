from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class AddressType:
    """
    Location of the responsible individual or organization.

    :ivar delivery_point: Address line for the location.
    :ivar city: City of the location.
    :ivar administrative_area: State or province of the location.
    :ivar postal_code: ZIP or other postal code.
    :ivar country: Country of the physical address.
    :ivar electronic_mail_address: Address of the electronic mailbox of
        the responsible organization or individual.
    """

    delivery_point: list[str] = field(
        default_factory=list,
        metadata={
            "name": "DeliveryPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    city: Optional[str] = field(
        default=None,
        metadata={
            "name": "City",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    administrative_area: Optional[str] = field(
        default=None,
        metadata={
            "name": "AdministrativeArea",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    postal_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PostalCode",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    country: Optional[str] = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    electronic_mail_address: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicMailAddress",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
