from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Vector(VectorType):
    class Meta:
        name = "vector"
        namespace = "http://www.opengis.net/gml/3.2"
