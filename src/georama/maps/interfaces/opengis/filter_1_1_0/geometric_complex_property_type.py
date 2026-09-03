from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    CompositeSolid,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import (
    CompositeCurve,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometric_complex import (
    GeometricComplex,
)
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    CompositeSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricComplexPropertyType:
    """A property that has a geometric complex as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but neither both nor none.
    NOTE: The allowed geometry elements contained in such a property (or referenced by it) have to be modelled by an XML Schema choice element since the composites inherit both from geometric complex *and* geometric primitive and are already part of the _GeometricPrimitive substitution group.
    """

    choice: (
        GeometricComplex | CompositeCurve | CompositeSurface | CompositeSolid | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
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
