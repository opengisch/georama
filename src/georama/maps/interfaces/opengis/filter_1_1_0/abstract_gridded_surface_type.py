from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gridded_surface_type_row import (
    AbstractGriddedSurfaceTypeRow,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    """A gridded surface is a parametric curve surface derived from a rectangular
    grid in the parameter space.

    The rows from this grid are control points for
    horizontal surface curves; the columns are control points
    for vertical surface curves. The working assumption is that
    for a pair of parametric co-ordinates (s, t) that the
    horizontal curves for each integer offset are calculated
    and evaluated at "s". The defines a sequence of control
    points:
    cn(s) : s  1 .....columns
    From this sequence a vertical curve is calculated for "s",
    and evaluated at "t". In most cases, the order of
    calculation (horizontal-vertical vs. vertical-horizontal)
    does not make a difference. Where it does, the horizontal-
    vertical order shall be the one used.
    Logically, any pair of curve interpolation types can lead
    to a subtype of GriddedSurface. The following clauses
    define some most commonly encountered surfaces that can
    be represented in this manner.

    :ivar row:
    :ivar rows: The attribute rows gives the number of rows in the
        parameter grid.
    :ivar columns: The attribute columns gives the number of columns in
        the parameter grid.
    """

    row: list[AbstractGriddedSurfaceTypeRow] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    rows: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
