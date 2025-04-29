from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.ex_bounding_polygon import (
    ExBoundingPolygon,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ex_geographic_bounding_box import (
    ExGeographicBoundingBox,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ex_geographic_description import (
    ExGeographicDescription,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExGeographicExtentPropertyType:
    class Meta:
        name = "EX_GeographicExtent_PropertyType"

    ex_geographic_description: Optional[ExGeographicDescription] = field(
        default=None,
        metadata={
            "name": "EX_GeographicDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ex_geographic_bounding_box: Optional[ExGeographicBoundingBox] = field(
        default=None,
        metadata={
            "name": "EX_GeographicBoundingBox",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    ex_bounding_polygon: Optional[ExBoundingPolygon] = field(
        default=None,
        metadata={
            "name": "EX_BoundingPolygon",
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
