from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.online_resource_type import (
    OnlineResourceType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.responsible_party_subset_type import (
    ResponsiblePartySubsetType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ServiceProvider:
    """
    Metadata about the organization that provides this specific service instance or
    server.

    :ivar provider_name: A unique identifier for the service provider
        organization.
    :ivar provider_site: Reference to the most relevant web site of the
        service provider.
    :ivar service_contact: Information for contacting the service
        provider. The OnlineResource element within this ServiceContact
        element should not be used to reference a web site of the
        service provider.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"

    provider_name: str | None = field(
        default=None,
        metadata={
            "name": "ProviderName",
            "type": "Element",
            "required": True,
        },
    )
    provider_site: OnlineResourceType | None = field(
        default=None,
        metadata={
            "name": "ProviderSite",
            "type": "Element",
        },
    )
    service_contact: ResponsiblePartySubsetType | None = field(
        default=None,
        metadata={
            "name": "ServiceContact",
            "type": "Element",
            "required": True,
        },
    )
