from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.native_type import NativeType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Native(NativeType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
