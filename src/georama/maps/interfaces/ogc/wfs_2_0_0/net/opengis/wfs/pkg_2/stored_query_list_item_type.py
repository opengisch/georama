from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from wfs_2_0_0.net.opengis.wfs.pkg_2.title import Title

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class StoredQueryListItemType:
    title: list[Title] = field(
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
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
