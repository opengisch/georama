from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.second_defining_parameter_2 import (
    SecondDefiningParameter2,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.semi_major_axis import (
    SemiMajorAxis,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidType(IdentifiedObjectType):
    semi_major_axis: Optional[SemiMajorAxis] = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    second_defining_parameter: Optional[SecondDefiningParameter2] = field(
        default=None,
        metadata={
            "name": "secondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
