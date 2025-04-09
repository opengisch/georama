from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.get_capabilities_type import (
    GetCapabilitiesType as GetCapabilitiesTypeGetCapabilitiesType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetCapabilitiesType(GetCapabilitiesTypeGetCapabilitiesType):
    service: str = field(
        init=False,
        default="WFS",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
