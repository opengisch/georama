from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_primitive_type import (
    AbstractTimePrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractTimePrimitive(AbstractTimePrimitiveType):
    """
    Gml:AbstractTimePrimitive acts as the head of a substitution group for
    geometric and topological temporal primitives.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
