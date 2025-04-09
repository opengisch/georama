from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.get_capabilities_type import (
    GetCapabilitiesType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class GetCapabilities(GetCapabilitiesType):
    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
