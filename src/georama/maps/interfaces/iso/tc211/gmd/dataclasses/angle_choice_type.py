from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.angle_2 import Angle2
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dms_angle import DmsAngle

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AngleChoiceType:
    angle: Angle2 | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dms_angle: DmsAngle | None = field(
        default=None,
        metadata={
            "name": "dmsAngle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
