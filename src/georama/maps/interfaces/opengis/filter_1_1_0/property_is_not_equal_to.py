from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.binary_comparison_op_type import (
    BinaryComparisonOpType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsNotEqualTo(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
