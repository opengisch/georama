from dataclasses import dataclass, field

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

    choice: (
        GeodeticDatum
        | TemporalDatum
        | VerticalDatum
        | ImageDatum
        | EngineeringDatum
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeodeticDatum",
                    "type": GeodeticDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalDatum",
                    "type": TemporalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalDatum",
                    "type": VerticalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageDatum",
                    "type": ImageDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringDatum",
                    "type": EngineeringDatum,
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
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
