from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.get_capabilities_type_1 import (
    GetCapabilitiesType1,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetCapabilitiesType2(GetCapabilitiesType1):
    class Meta:
        name = "GetCapabilitiesType"

    service: str = field(
        init=False,
        default="WFS",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
