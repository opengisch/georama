from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.operations_metadata import OperationsMetadata
from georama.maps.interfaces.ogc.wfs_2_0_0.service_identification import (
    ServiceIdentification,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.service_provider import ServiceProvider

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class CapabilitiesBaseType:
    """XML encoded GetCapabilities operation response.

    This document provides clients with service metadata about a
    specific service instance, usually including metadata about the
    tightly-coupled data served. If the server does not implement the
    updateSequence parameter, the server shall always return the
    complete Capabilities document, without the updateSequence
    parameter. When the server implements the updateSequence parameter
    and the GetCapabilities operation request included the
    updateSequence parameter with the current value, the server shall
    return this element with only the "version" and "updateSequence"
    attributes. Otherwise, all optional elements shall be included or
    not depending on the actual value of the Contents parameter in the
    GetCapabilities operation request. This base type shall be extended
    by each specific OWS to include the additional contents needed.

    :ivar service_identification:
    :ivar service_provider:
    :ivar operations_metadata:
    :ivar version:
    :ivar update_sequence: Service metadata document version, having
        values that are "increased" whenever any change is made in
        service metadata document. Values are selected by each server,
        and are always opaque to clients. When not supported by server,
        server shall not return this attribute.
    """

    service_identification: ServiceIdentification | None = field(
        default=None,
        metadata={
            "name": "ServiceIdentification",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    service_provider: ServiceProvider | None = field(
        default=None,
        metadata={
            "name": "ServiceProvider",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    operations_metadata: OperationsMetadata | None = field(
        default=None,
        metadata={
            "name": "OperationsMetadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"\d+\.\d?\d\.\d?\d",
        },
    )
    update_sequence: str | None = field(
        default=None,
        metadata={
            "name": "updateSequence",
            "type": "Attribute",
        },
    )
