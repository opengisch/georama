from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon import Polygon
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sign_type import SignType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface import Surface
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tin import Tin
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangulated_surface import (
    TriangulatedSurface,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


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
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: Optional["OrientableSurface"] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Tin | None = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: TriangulatedSurface | None = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: PolyhedralSurface | None = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Surface | None = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Polygon | None = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
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
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue | None = field(
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
            "namespace": "http://www.opengis.net/gml",
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
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    A surface element is any element, which is substitutable for
    gml:AbstractSurface.
    """

    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompositeSurfaceType(AbstractSurfaceType):
    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    """A gml:CompositeSurface is represented by a set of orientable surfaces.

    It is geometry type with all the geometric properties of a
    (primitive) surface. Essentially, a composite surface is a
    collection of surfaces that join in pairs on common boundary curves
    and which, when considered as a whole, form a single surface.
    surfaceMember references or contains inline one surface in the
    composite surface. The surfaces are contiguous.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


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
        namespace = "http://www.opengis.net/gml"
