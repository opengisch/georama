from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.manifest_type import (
    ManifestType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class OperationResponse(ManifestType):
    """Response from an OWS operation, allowing including multiple output data
    items with each item either included or referenced.

    This OperationResponse element, or an element using the ManifestType
    with a more specific element name, shall be used whenever applicable
    for responses from OWS operations. This element is specified for use
    where the ManifestType contents are needed for an operation
    response, but the Manifest element name is not fully applicable.
    This element or the ManifestType shall be used instead of using the
    ows:ReferenceType proposed in OGC 04-105.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
