from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.geometry_array_property_type import (
    MultiGeometry,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve import MultiCurve
from georama.maps.interfaces.opengis.filter_1_1_0.multi_line_string import (
    MultiLineString,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_point import MultiPoint
from georama.maps.interfaces.opengis.filter_1_1_0.multi_polygon import MultiPolygon
from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid import MultiSolid
from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface import MultiSurface
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiGeometryPropertyType:
    """A property that has a geometric aggregate as its value domain can either be
    an appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """

    choice: (
        MultiLineString
        | MultiPolygon
        | MultiSolid
        | MultiSurface
        | MultiCurve
        | MultiPoint
        | MultiGeometry
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
