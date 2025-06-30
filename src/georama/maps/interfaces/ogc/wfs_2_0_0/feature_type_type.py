from dataclasses import dataclass, field
from typing import Optional, Union
from xml.etree.ElementTree import QName

from georama.maps.interfaces.ogc.wfs_2_0_0.abstract_2 import Abstract2
from georama.maps.interfaces.ogc.wfs_2_0_0.default_crs import DefaultCrs
from georama.maps.interfaces.ogc.wfs_2_0_0.extended_description_type import (
    ExtendedDescriptionType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.feature_type_type_no_crs import (
    FeatureTypeTypeNoCrs,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.keywords import Keywords
from georama.maps.interfaces.ogc.wfs_2_0_0.metadata_urltype import MetadataUrltype
from georama.maps.interfaces.ogc.wfs_2_0_0.other_crs import OtherCrs
from georama.maps.interfaces.ogc.wfs_2_0_0.output_format_list_type import (
    OutputFormatListType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.title_2 import Title2
from georama.maps.interfaces.ogc.wfs_2_0_0.wgs84_bounding_box import Wgs84BoundingBox

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
    keywords: list[Keywords] = field(
        default_factory=list,
        metadata={
            "name": "Keywords",
            "type": "Element",
            "namespace": "http://www.opengis.net/ows/1.1",
        },
    )
    default_crs_or_other_crs_or_no_crs: list[
        Union[DefaultCrs, OtherCrs, FeatureTypeTypeNoCrs]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DefaultCRS",
                    "type": DefaultCrs,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "OtherCRS",
                    "type": OtherCrs,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "NoCRS",
                    "type": FeatureTypeTypeNoCrs,
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
            ),
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
