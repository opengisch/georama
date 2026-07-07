from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.direct_position_type import (
    DirectPositionType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffinePlacementType:
    """A placement takes a standard geometric construction and places it in
    geographic space.

    It defines a transformation from a constructive parameter space to
    the co-ordinate space of the co-ordinate reference system being
    used. Parameter spaces in formulae in this International Standard
    are given as (u, v) in 2D and(u, v, w) in 3D. Co-ordinate reference
    systems positions are given in formulae, in this International
    Standard, by either (x, y) in 2D, or (x, y, z) in 3D. Affine
    placements are defined by linear transformations from parameter
    space to the target co-ordiante space. 2-dimensional Cartesian
    parameter space,(u,v) transforms into 3-dimensional co- ordinate
    reference systems,(x,y,z) by using an affine
    transformation,(u,v)-&gt;(x,y,z) which is defined : x       ux vx
    x0 u y =     uy vy   + y0 v x       uz vz   z0 Then, given this
    equation, the location element of the AffinePlacement is the direct
    position (x0, y0, z0), which is the target position of the origin in
    (u, v). The two reference directions (ux, uy, uz) and (vx, vy, vz)
    are the target directions of the unit vectors at the origin in (u,
    v).

    :ivar location: The location property gives the target of the
        parameter space origin. This is the vector (x0, y0, z0) in the
        formulae above.
    :ivar ref_direction: The attribute refDirection gives the target
        directions for the co-ordinate basis vectors of the parameter
        space. These are the columns of the matrix in the formulae given
        above. The number of directions given shall be inDimension. The
        dimension of the directions shall be outDimension.
    :ivar in_dimension: Dimension of the constructive parameter space.
    :ivar out_dimension: Dimension of the co-ordinate space.
    """

    location: Optional[DirectPositionType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    ref_direction: list[VectorType] = field(
        default_factory=list,
        metadata={
            "name": "refDirection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    in_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "inDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    out_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "outDimension",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
