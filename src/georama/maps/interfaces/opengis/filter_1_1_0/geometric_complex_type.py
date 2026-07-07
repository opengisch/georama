from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometric_primitive_property_type import (
    GeometricPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricComplexType(AbstractGeometryType):
    """
    A geometric complex.
    """

    element: list[GeometricPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
