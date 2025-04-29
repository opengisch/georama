from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.md_metadata_type import (
    DsPlatform,
    DsProductionSeries,
    DsSensor,
    DsSeries,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsSeriesPropertyType:
    class Meta:
        name = "DS_Series_PropertyType"

    ds_production_series: Optional[DsProductionSeries] = field(
        default=None,
        metadata={
            "name": "DS_ProductionSeries",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_sensor: Optional[DsSensor] = field(
        default=None,
        metadata={
            "name": "DS_Sensor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_platform: Optional[DsPlatform] = field(
        default=None,
        metadata={
            "name": "DS_Platform",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ds_series: Optional[DsSeries] = field(
        default=None,
        metadata={
            "name": "DS_Series",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
