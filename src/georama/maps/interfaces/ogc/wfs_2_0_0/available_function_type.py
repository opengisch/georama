from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.arguments_type import ArgumentsType
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AvailableFunctionType:
    metadata: Metadata | None = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    returns: QName | None = field(
        default=None,
        metadata={
            "name": "Returns",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        },
    )
    arguments: ArgumentsType | None = field(
        default=None,
        metadata={
            "name": "Arguments",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
