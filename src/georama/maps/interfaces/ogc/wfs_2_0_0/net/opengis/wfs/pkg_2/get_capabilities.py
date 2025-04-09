from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.get_capabilities_type import (
    GetCapabilitiesType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetCapabilities(GetCapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
