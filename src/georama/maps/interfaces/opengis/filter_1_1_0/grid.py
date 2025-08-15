from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.grid_type import GridType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Grid(GridType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
