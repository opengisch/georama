from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    AbstractTimePrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimePrimitive(AbstractTimePrimitiveType):
    """
    This abstract element acts as the head of the substitution group for temporal
    primitives.
    """

    class Meta:
        name = "_TimePrimitive"
        namespace = "http://www.opengis.net/gml"
