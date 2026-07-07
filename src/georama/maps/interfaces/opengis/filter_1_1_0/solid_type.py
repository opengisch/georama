from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_solid_type import (
    AbstractSolidType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    SurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidType(AbstractSolidType):
    """A solid is the basis for 3-dimensional geometry.

    The extent of a solid is defined by the boundary surfaces (shells).
    A shell is represented by a composite surface, where every  shell is
    used to represent a single connected component of the boundary of a
    solid. It consists of a composite surface (a list of orientable
    surfaces) connected in a topological cycle (an object whose boundary
    is empty). Unlike a Ring, a Shell's elements have no natural sort
    order. Like Rings, Shells are simple.

    :ivar exterior: Boundaries of solids are similar to surface
        boundaries. In normal 3-dimensional Euclidean space, one
        (composite) surface is distinguished as the exterior. In the
        more general case, this is not always possible.
    :ivar interior: Boundaries of solids are similar to surface
        boundaries.
    """

    exterior: Optional[SurfacePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interior: list[SurfacePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
