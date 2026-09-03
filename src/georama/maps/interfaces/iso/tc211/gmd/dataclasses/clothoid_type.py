from dataclasses import dataclass, field
from decimal import Decimal

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.clothoid_type_ref_location import (
    ClothoidTypeRefLocation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ClothoidType(AbstractCurveSegmentType):
    ref_location: ClothoidTypeRefLocation | None = field(
        default=None,
        metadata={
            "name": "refLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    scale_factor: Decimal | None = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    start_parameter: float | None = field(
        default=None,
        metadata={
            "name": "startParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    end_parameter: float | None = field(
        default=None,
        metadata={
            "name": "endParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
