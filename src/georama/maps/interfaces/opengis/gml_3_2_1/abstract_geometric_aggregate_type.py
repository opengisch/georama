from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
