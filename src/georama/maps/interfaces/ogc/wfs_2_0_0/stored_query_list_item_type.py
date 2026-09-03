from dataclasses import dataclass, field
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.title_2 import Title2

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryListItemType:
    title: list[Title2] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    return_feature_type: list[QName] = field(
        default_factory=list,
        metadata={
            "name": "ReturnFeatureType",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
