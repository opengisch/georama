from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.rectified_grid_type import (
    RectifiedGridType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGrid(RectifiedGridType):
    """
    Should be substitutionGroup="gml:Grid" but changed in order to accomplish
    Xerces-J schema validation.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
