from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.angle_1 import Angle1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.distance import Distance
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.length import Length
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_1 import Measure1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.scale import Scale

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MeasurePropertyType:
    class Meta:
        name = "Measure_PropertyType"

    scale: Scale | None = field(
        default=None,
        metadata={
            "name": "Scale",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    angle: Angle1 | None = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    distance: Distance | None = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    length: Length | None = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    measure: Measure1 | None = field(
        default=None,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
