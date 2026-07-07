from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.accept_formats_type import AcceptFormatsType
from georama.maps.interfaces.ogc.wfs_2_0_0.accept_versions_type import (
    AcceptVersionsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.sections_type import SectionsType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class GetCapabilitiesType1:
    """XML encoded GetCapabilities operation request.

    This operation allows clients to retrieve service metadata about a
    specific service instance. In this XML encoding, no "request"
    parameter is included, since the element name specifies the specific
    operation. This base type shall be extended by each specific OWS to
    include the additional required "service" attribute, with the
    correct value for that OWS.

    :ivar accept_versions: When omitted, server shall return latest
        supported version.
    :ivar sections: When omitted or not supported by server, server
        shall return complete service metadata (Capabilities) document.
    :ivar accept_formats: When omitted or not supported by server,
        server shall return service metadata document using the MIME
        type "text/xml".
    :ivar update_sequence: When omitted or not supported by server,
        server shall return latest complete service metadata document.
    """

    class Meta:
        name = "GetCapabilitiesType"

    accept_versions: Optional[AcceptVersionsType] = field(
        default=None,
        metadata={
            "name": "AcceptVersions",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    sections: Optional[SectionsType] = field(
        default=None,
        metadata={
            "name": "Sections",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    accept_formats: Optional[AcceptFormatsType] = field(
        default=None,
        metadata={
            "name": "AcceptFormats",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    update_sequence: Optional[str] = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        },
    )
