from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.binary_comparison_op_type import (
    BinaryComparisonOpType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class PropertyIsGreaterThan(BinaryComparisonOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
