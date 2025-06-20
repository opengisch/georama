from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_datum import (
    EngineeringDatum,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geodetic_datum import GeodeticDatum
from georama.maps.interfaces.opengis.filter_1_1_0.image_datum import ImageDatum
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_datum import TemporalDatum
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum import VerticalDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DatumRefType:
    """
    Association to a datum, either referencing or containing the definition of that
    datum.
    """

    geodetic_datum: Optional[GeodeticDatum] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: Optional[TemporalDatum] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: Optional[VerticalDatum] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: Optional[ImageDatum] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: Optional[EngineeringDatum] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
