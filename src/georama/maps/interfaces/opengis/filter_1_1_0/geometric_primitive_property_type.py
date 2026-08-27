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
from georama.maps.interfaces.opengis.filter_1_1_0.line_string import LineString
from georama.maps.interfaces.opengis.filter_1_1_0.point import Point
from georama.maps.interfaces.opengis.filter_1_1_0.polygon import Polygon
from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface import (
    PolyhedralSurface,
)
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
class GeometricPrimitivePropertyType:
    """A property that has a geometric primitive as its value domain can either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """

    choice: (
        Solid
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
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
