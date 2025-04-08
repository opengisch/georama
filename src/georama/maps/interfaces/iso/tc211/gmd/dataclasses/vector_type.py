from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direct_position_type import (
    DirectPositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VectorType(DirectPositionType):
    """
    For some applications the components of the position may be adjusted to yield a
    unit vector.
    """
