from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
