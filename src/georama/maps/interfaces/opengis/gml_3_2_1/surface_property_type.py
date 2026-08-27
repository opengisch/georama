from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.polygon import Polygon
from georama.maps.interfaces.opengis.gml_3_2_1.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.sign_type import SignType
from georama.maps.interfaces.opengis.gml_3_2_1.surface import Surface
from georama.maps.interfaces.opengis.gml_3_2_1.tin import Tin
from georama.maps.interfaces.opengis.gml_3_2_1.triangulated_surface import (
    TriangulatedSurface,
)
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfacePropertyType:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes geometry
    elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """

    composite_surface: Optional["CompositeSurface"] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    shell: Optional["Shell"] = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_surface: Optional["OrientableSurface"] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    tin: Tin | None = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    triangulated_surface: TriangulatedSurface | None = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polyhedral_surface: PolyhedralSurface | None = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    surface: Surface | None = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: Polygon | None = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BaseSurface(SurfacePropertyType):
    """The property baseSurface references or contains the base surface.

    The property baseSurface either references the base surface via the
    XLink-attributes or contains the surface element. A surface element
    is any element which is substitutable for gml:AbstractSurface. The
    base surface has positive orientation.
    """

    class Meta:
        name = "baseSurface"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    A surface element is any element, which is substitutable for
    gml:AbstractSurface.
    """

    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompositeSurfaceType(AbstractSurfaceType):
    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class OrientableSurfaceType(AbstractSurfaceType):
    base_surface: BaseSurface | None = field(
        default=None,
        metadata={
            "name": "baseSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class ShellType(AbstractSurfaceType):
    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class CompositeSurface(CompositeSurfaceType):
    """A gml:CompositeSurface is represented by a set of orientable surfaces.

    It is geometry type with all the geometric properties of a
    (primitive) surface. Essentially, a composite surface is a
    collection of surfaces that join in pairs on common boundary curves
    and which, when considered as a whole, form a single surface.
    surfaceMember references or contains inline one surface in the
    composite surface. The surfaces are contiguous.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OrientableSurface(OrientableSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a gml:AbstractSurface with an
    up-normal that reverses the direction for this OrientableSurface,
    the sense of "the top of the surface".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Shell(ShellType):
    """A shell is used to represent a single connected component of a solid
    boundary as specified in ISO 19107:2003, 6.3.8.

    Every gml:surfaceMember references or contains one surface, i.e. any
    element which is substitutable for gml:AbstractSurface. In the
    context of a shell, the surfaces describe the boundary of the solid.
    If provided, the aggregationType attribute shall have the value
    "set".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
