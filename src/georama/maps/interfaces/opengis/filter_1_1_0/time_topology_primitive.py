from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    AbstractTimeTopologyPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyPrimitive(AbstractTimeTopologyPrimitiveType):
    """
    This abstract element acts as the head of the substitution group for temporal
    topology primitives.
    """

    class Meta:
        name = "_TimeTopologyPrimitive"
        namespace = "http://www.opengis.net/gml"
