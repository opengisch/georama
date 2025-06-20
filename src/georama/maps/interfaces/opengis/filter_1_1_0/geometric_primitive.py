from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricPrimitive(AbstractGeometricPrimitiveType):
    """
    The "_GeometricPrimitive" element is the abstract head of the substituition
    group for all (pre- and user-defined) geometric primitives.
    """

    class Meta:
        name = "_GeometricPrimitive"
        namespace = "http://www.opengis.net/gml"
