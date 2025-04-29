from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.clothoid_type_ref_location import (
    ClothoidTypeRefLocation,
)
from georama.maps.interfaces.opengis.gml_3_2_1.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ClothoidType(AbstractCurveSegmentType):
    ref_location: Optional[ClothoidTypeRefLocation] = field(
        default=None,
        metadata={
            "name": "refLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    scale_factor: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    start_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "startParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    end_parameter: Optional[float] = field(
        default=None,
        metadata={
            "name": "endParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    interpolation: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CLOTHOID,
        metadata={
            "type": "Attribute",
        },
    )
