from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon import Polygon
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface import Surface
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tin import Tin
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangulated_surface import (
    TriangulatedSurface,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceArrayPropertyType:
    """Gml:SurfaceArrayPropertyType is a container for an array of surfaces.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements via XLinks is not
    supported.
    """

    composite_surface: list[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    orientable_surface: list[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    tin: list[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    triangulated_surface: list[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    polyhedral_surface: list[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    surface: list[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
