from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from wfs_2_0_0.net.opengis.fes.pkg_2.arguments_type import ArgumentsType
from wfs_2_0_0.net.opengis.ows.pkg_1.metadata import Metadata

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AvailableFunctionType:
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    returns: Optional[QName] = field(
        default=None,
        metadata={
            "name": "Returns",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "required": True,
        },
    )
    arguments: Optional[ArgumentsType] = field(
        default=None,
        metadata={
            "name": "Arguments",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
