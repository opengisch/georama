from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.direct_position_type import (
    DirectPositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VectorType(DirectPositionType):
    """
    For some applications the components of the position may be adjusted to yield a
    unit vector.
    """
