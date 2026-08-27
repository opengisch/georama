from dataclasses import dataclass, field
from typing import ForwardRef, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.polygon import Polygon
from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.sign_type import SignType
from georama.maps.interfaces.opengis.filter_1_1_0.surface import Surface
from georama.maps.interfaces.opengis.filter_1_1_0.tin import Tin
from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface import (
    TriangulatedSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfacePropertyType:
    """A property that has a surface as its value domain can either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element must be given, but
    neither both nor none.
    """

    choice: (
        Union[
            "OrientableSurface",
            Tin,
            TriangulatedSurface,
            PolyhedralSurface,
            Surface,
            "CompositeSurface",
            Polygon,
        ]
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OrientableSurface",
                    "type": ForwardRef("OrientableSurface"),
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
                    "type": ForwardRef("CompositeSurface"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
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


@dataclass
class BaseSurface(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    A surface element is any element which is substitutable for
    "_Surface".
    """

    class Meta:
        name = "baseSurface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    A surface element is any element which is substitutable for
    "_Surface".
    """

    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompositeSurfaceType(AbstractSurfaceType):
    """A CompositeSurface is defined by a set of orientable surfaces.

    A composite surface is geometry type with all the geometric
    properties of a (primitive) surface. Essentially, a composite
    surface is a collection of surfaces that join in pairs on common
    boundary curves and which, when considered as a whole, form a single
    surface.

    :ivar surface_member: This element references or contains one
        surface in the composite surface. The surfaces are contiguous.
        NOTE: This definition allows for a nested structure, i.e. a
        CompositeSurface may use, for example, another CompositeSurface
        as a member.
    """

    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )


@dataclass
class OrientableSurfaceType(AbstractSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a Surface with an up-normal that
    reverses the direction for this OrientableSurface, the sense of "the
    top of the surface".

    :ivar base_surface: References or contains the base surface
        (positive orientation).
    :ivar orientation: If the orientation is "+", then the
        OrientableSurface is identical to the baseSurface. If the
        orientation is "-", then the OrientableSurface is a reference to
        a Surface with an up-normal that reverses the direction for this
        OrientableSurface, the sense of "the top of the surface". "+" is
        the default value.
    """

    base_surface: BaseSurface | None = field(
        default=None,
        metadata={
            "name": "baseSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class CompositeSurface(CompositeSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OrientableSurface(OrientableSurfaceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
