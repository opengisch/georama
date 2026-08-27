from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class ResourceIdentifierType:
    metadata: Metadata | None = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    name: QName | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
