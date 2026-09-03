from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.length_type import LengthType
from georama.maps.interfaces.opengis.filter_1_1_0.line_string_segment_array_property_type import (
    LineStringSegmentArrayPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.tin_type_control_point import (
    TinTypeControlPoint,
)
from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface_type import (
    TriangulatedSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TinType(TriangulatedSurfaceType):
    """A tin is a triangulated surface that uses the Delauny algorithm or a similar
    algorithm complemented with consideration of breaklines, stoplines, and maximum
    length of triangle sides.

    These networks satisfy the Delauny's criterion
    away from the modifications: Fore each triangle in the
    network, the circle passing through its vertices does not
    contain, in its interior, the vertex of any other triangle.

    :ivar stop_lines: Stoplines are lines where the local continuity or
        regularity of the surface is questionable. In the area of these
        pathologies, triangles intersecting a stopline shall be removed
        from the tin surface, leaving holes in the surface. If
        coincidence occurs on surface boundary triangles, the result
        shall be a change of the surface boundary. Stoplines contains
        all these pathological segments as a set of line strings.
    :ivar break_lines: Breaklines are lines of a critical nature to the
        shape of the surface, representing local ridges, or depressions
        (such as drainage lines) in the surface. As such their
        constituent segments must be included in the tin eve if doing so
        violates the Delauny criterion. Break lines contains these
        critical segments as a set of line strings.
    :ivar max_length: Areas of the surface where data is not
        sufficiently dense to assure reasonable calculation shall be
        removed by adding a retention criterion for triangles based on
        the length of their sides. For many triangle sides exceeding
        maximum length, the adjacent triangles to that triangle side
        shall be removed from the surface.
    :ivar control_point: The corners of the triangles in the TIN are
        often referred to as pots. ControlPoint shall contain a set of
        the GM_Position used as posts for this TIN. Since each TIN
        contains triangles, there must be at least 3 posts. The order in
        which these points are given does not affect the surface that is
        represented. Application schemas may add information based on
        ordering of control points to facilitate the reconstruction of
        the TIN from the control points.
    """

    stop_lines: list[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "stopLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    break_lines: list[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "breakLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    max_length: LengthType | None = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    control_point: TinTypeControlPoint | None = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
