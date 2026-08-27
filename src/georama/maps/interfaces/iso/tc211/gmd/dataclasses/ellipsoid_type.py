from dataclasses import dataclass, field

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
    semi_major_axis: SemiMajorAxis | None = field(
        default=None,
        metadata={
            "name": "semiMajorAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    second_defining_parameter: SecondDefiningParameter2 | None = field(
        default=None,
        metadata={
            "name": "secondDefiningParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
