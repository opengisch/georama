from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.comparison_ops_type import (
    ComparisonOpsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNullType(ComparisonOpsType):
    property_name: PropertyName | None = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
