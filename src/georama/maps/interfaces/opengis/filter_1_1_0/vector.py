from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Vector(VectorType):
    class Meta:
        name = "vector"
        namespace = "http://www.opengis.net/gml"
