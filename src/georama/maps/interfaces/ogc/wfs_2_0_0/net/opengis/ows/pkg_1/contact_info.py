from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.contact_type import (
    ContactType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ContactInfo(ContactType):
    """
    Address of the responsible party.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
