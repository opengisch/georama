from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.get_capabilities_type_2 import (
    GetCapabilitiesType2,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetCapabilities2(GetCapabilitiesType2):
    class Meta:
        name = "GetCapabilities"
        namespace = "http://www.opengis.net/wfs/2.0"
