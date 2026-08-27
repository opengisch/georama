from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.metadata import Metadata
from georama.maps.interfaces.ogc.wfs_2_0_0.value_list import ValueList

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ElementType:
    metadata: Metadata | None = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "required": True,
        },
    )
    value_list: ValueList | None = field(
        default=None,
        metadata={
            "name": "ValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
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
