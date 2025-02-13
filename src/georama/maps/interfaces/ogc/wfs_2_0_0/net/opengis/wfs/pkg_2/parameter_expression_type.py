from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from wfs_2_0_0.net.opengis.ows.pkg_1.metadata import Metadata
from wfs_2_0_0.net.opengis.wfs.pkg_2.abstract import Abstract
from wfs_2_0_0.net.opengis.wfs.pkg_2.title import Title

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ParameterExpressionType:
    title: list[Title] = field(
        default_factory=list,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    abstract: list[Abstract] = field(
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
