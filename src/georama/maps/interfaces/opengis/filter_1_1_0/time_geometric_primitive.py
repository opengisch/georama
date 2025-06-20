from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    AbstractTimeGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeGeometricPrimitive(AbstractTimeGeometricPrimitiveType):
    """
    This abstract element acts as the head of the substitution group for temporal
    geometric primitives.
    """

    class Meta:
        name = "_TimeGeometricPrimitive"
        namespace = "http://www.opengis.net/gml"
