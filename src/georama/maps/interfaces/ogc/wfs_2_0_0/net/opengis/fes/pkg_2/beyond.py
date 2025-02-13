from dataclasses import dataclass

from wfs_2_0_0.net.opengis.fes.pkg_2.distance_buffer_type import DistanceBufferType

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Beyond(DistanceBufferType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
