from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.spatial_ops_type import SpatialOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class SpatialOps(SpatialOpsType):
    class Meta:
        name = "spatialOps"
        namespace = "http://www.opengis.net/ogc"
