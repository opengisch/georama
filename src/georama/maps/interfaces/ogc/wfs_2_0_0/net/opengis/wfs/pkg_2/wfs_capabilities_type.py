from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.filter_capabilities import (
    FilterCapabilities,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.ows.pkg_1.capabilities_base_type import (
    CapabilitiesBaseType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.feature_type_list import (
    FeatureTypeList,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.actuate_type import (
    ActuateType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.show_type import (
    ShowType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.org.w3.pkg_1999.xlink.type_type import (
    TypeType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class WfsCapabilitiesType(CapabilitiesBaseType):
    class Meta:
        name = "WFS_CapabilitiesType"

    wsdl: Optional["WfsCapabilitiesType.Wsdl"] = field(
        default=None,
        metadata={
            "name": "WSDL",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    feature_type_list: Optional[FeatureTypeList] = field(
        default=None,
        metadata={
            "name": "FeatureTypeList",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    filter_capabilities: Optional[FilterCapabilities] = field(
        default=None,
        metadata={
            "name": "Filter_Capabilities",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )

    @dataclass
    class Wsdl:
        any_element: Optional[object] = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )
        type_value: TypeType = field(
            init=False,
            default=TypeType.SIMPLE,
            metadata={
                "name": "type",
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            },
        )
        href: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            },
        )
        role: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
                "min_length": 1,
            },
        )
        arcrole: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
                "min_length": 1,
            },
        )
        title: Optional[str] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            },
        )
        show: Optional[ShowType] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            },
        )
        actuate: Optional[ActuateType] = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/1999/xlink",
            },
        )
