from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.geometric_primitive_property_type import (
    GeometricPrimitivePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GeometricComplexType(AbstractGeometryType):
    element: list[GeometricPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
