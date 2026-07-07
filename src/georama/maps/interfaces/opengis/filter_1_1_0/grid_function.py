from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.grid_function_type import (
    GridFunctionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridFunction(GridFunctionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
