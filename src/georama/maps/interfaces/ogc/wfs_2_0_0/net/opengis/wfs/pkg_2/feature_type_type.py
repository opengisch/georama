from dataclasses import dataclass, field
from typing import Optional
from xml.etree.ElementTree import QName

from wfs_2_0_0.net.opengis.ows.pkg_1.keywords import Keywords
from wfs_2_0_0.net.opengis.ows.pkg_1.wgs84_bounding_box import Wgs84BoundingBox
from wfs_2_0_0.net.opengis.wfs.pkg_2.abstract import Abstract
from wfs_2_0_0.net.opengis.wfs.pkg_2.extended_description_type import (
    ExtendedDescriptionType,
)
from wfs_2_0_0.net.opengis.wfs.pkg_2.metadata_urltype import MetadataUrltype
from wfs_2_0_0.net.opengis.wfs.pkg_2.output_format_list_type import OutputFormatListType
from wfs_2_0_0.net.opengis.wfs.pkg_2.title import Title

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureTypeType:
    name: Optional[QName] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "required": True,
        },
    )
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
    keywords: list[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    default_crs: Optional[str] = field(
        default=None,
        metadata={
            "name": "DefaultCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    other_crs: list[str] = field(
        default_factory=list,
        metadata={
            "name": "OtherCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    no_crs: Optional[object] = field(
        default=None,
        metadata={
            "name": "NoCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    output_formats: Optional[OutputFormatListType] = field(
        default=None,
        metadata={
            "name": "OutputFormats",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    wgs84_bounding_box: list[Wgs84BoundingBox] = field(
        default_factory=list,
        metadata={
            "name": "WGS84BoundingBox",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    metadata_url: list[MetadataUrltype] = field(
        default_factory=list,
        metadata={
            "name": "MetadataURL",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    extended_description: Optional[ExtendedDescriptionType] = field(
        default=None,
        metadata={
            "name": "ExtendedDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
