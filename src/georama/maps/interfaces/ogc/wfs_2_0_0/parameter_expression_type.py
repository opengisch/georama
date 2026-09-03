from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_2 import Abstract2
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata
from georama.maps.interfaces.ogc.wfs_2_0_0.title_2 import Title2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ParameterExpressionType:
    title: list[Title2] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    abstract: list[Abstract2] = field(
        default_factory=list,
        metadata={
            "name": "Abstract",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
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
    name: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: QName | None = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
