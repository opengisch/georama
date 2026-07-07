from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.arc_string_by_bulge_type import (
    ArcStringByBulgeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcByBulgeType(ArcStringByBulgeType):
    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
