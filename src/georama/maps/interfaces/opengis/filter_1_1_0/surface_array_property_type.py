from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.polygon import Polygon
from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.surface import Surface
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.tin import Tin
from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface import (
    TriangulatedSurface,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceArrayPropertyType:
    """A container for an array of surfaces.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """

    orientable_surface: list[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: list[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: list[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: list[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: list[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: list[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
