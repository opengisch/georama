from dataclasses import dataclass

from wfs_2_0_0.net.opengis.fes.pkg_2.binary_spatial_op_type import BinarySpatialOpType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Crosses(BinarySpatialOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
