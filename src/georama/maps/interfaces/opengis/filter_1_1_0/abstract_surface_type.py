from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_primitive_type import (
    AbstractGeometricPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """An abstraction of a surface to support the different levels of complexity.

    A surface is always a continuous region of a plane.
    """
