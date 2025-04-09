from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.metadata import (
    Metadata,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.value_list import (
    ValueList,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ElementType:
    metadata: Optional[Metadata] = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
            "required": True,
        },
    )
    value_list: Optional[ValueList] = field(
        default=None,
        metadata={
            "name": "ValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[QName] = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        },
    )
