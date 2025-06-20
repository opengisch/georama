from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gridded_surface_type import (
    AbstractGriddedSurfaceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_interpolation_type import (
    CurveInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphereType(AbstractGriddedSurfaceType):
    """A sphere is a gridded surface given as a family of circles whose positions
    vary linearly along the axis of the sphere, and whise radius varies in
    proportions to the cosine function of the central angle.

    The horizontal
    circles resemble lines of constant latitude, and the vertical
    arcs resemble lines of constant longitude.
    NOTE! If the control points are sorted in terms of increasing
    longitude, and increasing latitude, the upNormal of a sphere
    is the outward normal.
    EXAMPLE If we take a gridded set of latitudes and longitudes
    in degrees,(u,v) such as
    (-90,-180)  (-90,-90)  (-90,0)  (-90,  90) (-90, 180)
    (-45,-180)  (-45,-90)  (-45,0)  (-45,  90) (-45, 180)
    (  0,-180)  (  0,-90)  (  0,0)  (  0,  90) (  0, 180)
    ( 45,-180)  ( 45,-90)  ( 45,0)  ( 45, -90) ( 45, 180)
    ( 90,-180)  ( 90,-90)  ( 90,0)  ( 90, -90) ( 90, 180)
    And map these points to 3D using the usual equations (where R
    is the radius of the required sphere).
    z = R sin u
    x = (R cos u)(sin v)
    y = (R cos u)(cos v)
    We have a sphere of Radius R, centred at (0,0), as a gridded
    surface. Notice that the entire first row and the entire last
    row of the control points map to a single point in each 3D
    Euclidean space, North and South poles respectively, and that
    each horizontal curve closes back on itself forming a
    geometric cycle. This gives us a metrically bounded (of finite
    size), topologically unbounded (not having a boundary, a
    cycle) surface.
    """

    horizontal_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "horizontalCurveType",
            "type": "Attribute",
        },
    )
    vertical_curve_type: CurveInterpolationType = field(
        init=False,
        default=CurveInterpolationType.CIRCULAR_ARC3_POINTS,
        metadata={
            "name": "verticalCurveType",
            "type": "Attribute",
        },
    )
