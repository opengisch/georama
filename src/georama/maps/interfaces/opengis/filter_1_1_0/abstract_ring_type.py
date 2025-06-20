from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometry_type import (
    AbstractGeometryType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingType(AbstractGeometryType):
    """
    An abstraction of a ring to support surface boundaries of different complexity.
    """
