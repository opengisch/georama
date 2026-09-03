from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    CompositeSolid,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import (
    CompositeCurve,
    Curve,
    OrientableCurve,
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
from georama.maps.interfaces.opengis.filter_1_1_0.location_key_word import (
    LocationKeyWord,
)
from georama.maps.interfaces.opengis.filter_1_1_0.location_string import LocationString
from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve import MultiCurve
from georama.maps.interfaces.opengis.filter_1_1_0.multi_line_string import (
    MultiLineString,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_point import MultiPoint
from georama.maps.interfaces.opengis.filter_1_1_0.multi_polygon import MultiPolygon
from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid import MultiSolid
from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface import MultiSurface
from georama.maps.interfaces.opengis.filter_1_1_0.null import Null
from georama.maps.interfaces.opengis.filter_1_1_0.point import Point
from georama.maps.interfaces.opengis.filter_1_1_0.polygon import Polygon
from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.rectified_grid import RectifiedGrid
from georama.maps.interfaces.opengis.filter_1_1_0.ring import Ring
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.solid import Solid
from georama.maps.interfaces.opengis.filter_1_1_0.surface import Surface
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.tin import Tin
from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface import (
    TriangulatedSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LocationPropertyType:
    """Convenience property for generalised location.

    A representative location for plotting or analysis. Often augmented
    by one or more additional geometry properties with more specific
    semantics. Deprecated in GML 3.1.0
    """

    choice: (
        MultiLineString
        | MultiPolygon
        | MultiSolid
        | MultiSurface
        | MultiCurve
        | MultiPoint
        | MultiGeometry
        | RectifiedGrid
        | Grid
        | GeometricComplex
        | Ring
        | LinearRing
        | Solid
        | CompositeSolid
        | OrientableSurface
        | Tin
        | TriangulatedSurface
        | PolyhedralSurface
        | Surface
        | CompositeSurface
        | Polygon
        | OrientableCurve
        | Curve
        | CompositeCurve
        | LineString
        | Point
        | LocationKeyWord
        | LocationString
        | Null
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MultiLineString",
                    "type": MultiLineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPolygon",
                    "type": MultiPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolid",
                    "type": MultiSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurve",
                    "type": MultiCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPoint",
                    "type": MultiPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiGeometry",
                    "type": MultiGeometry,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGrid",
                    "type": RectifiedGrid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Grid",
                    "type": Grid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableSurface",
                    "type": OrientableSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Tin",
                    "type": Tin,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TriangulatedSurface",
                    "type": TriangulatedSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolyhedralSurface",
                    "type": PolyhedralSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Surface",
                    "type": Surface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Point",
                    "type": Point,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LocationKeyWord",
                    "type": LocationKeyWord,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LocationString",
                    "type": LocationString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Null",
                    "type": Null,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
