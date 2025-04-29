from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.grid_function_type import (
    GridFunctionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridFunction(GridFunctionType):
    """Gml:GridFunction provides an explicit mapping rule for grid geometries, i.e.
    the domain shall be a geometry of type grid.

    It describes the mapping of grid posts (discrete point grid
    coverage) or grid cells (discrete surface coverage) to the values in
    the range set. The gml:startPoint is the index position of a point
    in the grid that is mapped to the first point in the range set (this
    is also the index position of the first grid post).  If the
    gml:startPoint property is omitted the gml:startPoint is assumed to
    be equal to the value of gml:low in the gml:Grid geometry.
    Subsequent points in the mapping are determined by the value of the
    gml:sequenceRule.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
