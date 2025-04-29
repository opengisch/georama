from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.angle_1 import Angle1

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class AnglePropertyType:
    class Meta:
        name = "Angle_PropertyType"

    angle: Optional[Angle1] = field(
        default=None,
        metadata={
            "name": "Angle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
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
