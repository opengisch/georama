from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_1 import Abstract1
from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_reference_base_type import (
    AbstractReferenceBaseType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.identifier import Identifier
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ReferenceType(AbstractReferenceBaseType):
    """
    Complete reference to a remote or local resource, allowing including metadata
    about that resource.

    :ivar identifier: Optional unique identifier of the referenced
        resource.
    :ivar abstract:
    :ivar format: The format of the referenced resource. This element is
        omitted when the mime type is indicated in the http header of
        the reference.
    :ivar metadata: Optional unordered list of additional metadata about
        this resource. A list of optional metadata elements for this
        ReferenceType could be specified in the Implementation
        Specification for each use of this type in a specific OWS.
    """

    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "Identifier",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    abstract: list[Abstract1] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    format: Optional[str] = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "pattern": r"(application|audio|image|text|video|message|multipart|model)/.+(;\s*.+=.+)*",
        },
    )
    metadata: list[Metadata] = field(
        default_factory=list,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
