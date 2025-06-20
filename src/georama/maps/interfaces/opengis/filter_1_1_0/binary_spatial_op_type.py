from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    CompositeSolid,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import (
    CompositeCurve,
    Curve,
    OrientableCurve,
)
from georama.maps.interfaces.opengis.filter_1_1_0.envelope import Envelope
from georama.maps.interfaces.opengis.filter_1_1_0.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometric_complex import (
    GeometricComplex,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometry_array_property_type import (
    MultiGeometry,
)
from georama.maps.interfaces.opengis.filter_1_1_0.grid import Grid
from georama.maps.interfaces.opengis.filter_1_1_0.line_string import LineString
from georama.maps.interfaces.opengis.filter_1_1_0.linear_ring import LinearRing
from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve import MultiCurve
from georama.maps.interfaces.opengis.filter_1_1_0.multi_line_string import (
    MultiLineString,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_point import MultiPoint
from georama.maps.interfaces.opengis.filter_1_1_0.multi_polygon import MultiPolygon
from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid import MultiSolid
from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface import MultiSurface
from georama.maps.interfaces.opengis.filter_1_1_0.point import Point
from georama.maps.interfaces.opengis.filter_1_1_0.polygon import Polygon
from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName
from georama.maps.interfaces.opengis.filter_1_1_0.rectified_grid import RectifiedGrid
from georama.maps.interfaces.opengis.filter_1_1_0.ring import Ring
from georama.maps.interfaces.opengis.filter_1_1_0.solid import Solid
from georama.maps.interfaces.opengis.filter_1_1_0.spatial_ops_type import SpatialOpsType
from georama.maps.interfaces.opengis.filter_1_1_0.surface import Surface
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.tin import Tin
from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface import (
    TriangulatedSurface,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinarySpatialOpType(SpatialOpsType):
    property_name: list[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 2,
            "max_occurs": 2,
            "sequence": 1,
        },
    )
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: Optional[Curve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
