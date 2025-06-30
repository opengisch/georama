from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    CompoundCrs,
    DerivedCrs,
    ProjectedCrs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_crs import EngineeringCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geocentric_crs import GeocentricCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geographic_crs import GeographicCrs
from georama.maps.interfaces.opengis.filter_1_1_0.image_crs import ImageCrs
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_crs import TemporalCrs
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_crs import VerticalCrs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ReferenceSystemRefType:
    """
    Association to a reference system, either referencing or containing the
    definition of that reference system.
    """

    choice: Optional[
        Union[
            CompoundCrs,
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            DerivedCrs,
            ProjectedCrs,
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundCRS",
                    "type": CompoundCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCRS",
                    "type": TemporalCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageCRS",
                    "type": ImageCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringCRS",
                    "type": EngineeringCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedCRS",
                    "type": DerivedCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ProjectedCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeocentricCRS",
                    "type": GeocentricCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCRS",
                    "type": VerticalCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeographicCRS",
                    "type": GeographicCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
