from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.capabilities_base_type import (
    CapabilitiesBaseType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.feature_type_list import FeatureTypeList
from georama.maps.interfaces.ogc.wfs_2_0_0.filter_capabilities import FilterCapabilities
from georama.maps.interfaces.ogc.wfs_2_0_0.wfs_capabilities_type_wsdl import (
    WfsCapabilitiesTypeWsdl,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class WfsCapabilitiesType(CapabilitiesBaseType):
    class Meta:
        name = "WFS_CapabilitiesType"

    wsdl: WfsCapabilitiesTypeWsdl | None = field(
        default=None,
        metadata={
            "name": "WSDL",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    feature_type_list: FeatureTypeList | None = field(
        default=None,
        metadata={
            "name": "FeatureTypeList",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    filter_capabilities: FilterCapabilities | None = field(
        default=None,
        metadata={
            "name": "Filter_Capabilities",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
