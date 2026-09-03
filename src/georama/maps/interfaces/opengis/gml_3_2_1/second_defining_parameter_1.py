from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.length_type import LengthType
from georama.maps.interfaces.opengis.gml_3_2_1.measure_type import MeasureType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SecondDefiningParameter1:
    class Meta:
        name = "SecondDefiningParameter"
        namespace = "http://www.opengis.net/gml/3.2"

    inverse_flattening: MeasureType | None = field(
        default=None,
        metadata={
            "name": "inverseFlattening",
            "type": "Element",
        },
    )
    semi_minor_axis: LengthType | None = field(
        default=None,
        metadata={
            "name": "semiMinorAxis",
            "type": "Element",
        },
    )
    is_sphere: bool = field(
        default=True,
        metadata={
            "name": "isSphere",
            "type": "Element",
        },
    )
