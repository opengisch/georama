from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_curve_segment_type import (
    AbstractCurveSegmentType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinates import Coordinates
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_interpolation_type import (
    CurveInterpolationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.knot_property_type import (
    KnotPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.knot_types_type import (
    KnotTypesType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_property import (
    PointProperty,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_rep import PointRep
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos import Pos
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BsplineType(AbstractCurveSegmentType):
    class Meta:
        name = "BSplineType"

    pos: list[Pos] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_property: list[PointProperty] = field(
        default_factory=list,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_rep: list[PointRep] = field(
        default_factory=list,
        metadata={
            "name": "pointRep",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pos_list: PosList | None = field(
        default=None,
        metadata={
            "name": "posList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinates: Coordinates | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    degree: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    knot: list[KnotPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        },
    )
    interpolation: CurveInterpolationType = field(
        default=CurveInterpolationType.POLYNOMIAL_SPLINE,
        metadata={
            "type": "Attribute",
        },
    )
    is_polynomial: bool | None = field(
        default=None,
        metadata={
            "name": "isPolynomial",
            "type": "Attribute",
        },
    )
    knot_type: KnotTypesType | None = field(
        default=None,
        metadata={
            "name": "knotType",
            "type": "Attribute",
        },
    )
