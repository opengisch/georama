from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.id_capabilities_type import (
    IdCapabilitiesType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.scalar_capabilities_type import (
    ScalarCapabilitiesType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.spatial_capabilities_type import (
    SpatialCapabilitiesType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FilterCapabilities:
    class Meta:
        name = "Filter_Capabilities"
        namespace = "http://www.opengis.net/ogc"

    spatial_capabilities: SpatialCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Spatial_Capabilities",
            "type": "Element",
            "required": True,
        },
    )
    scalar_capabilities: ScalarCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Scalar_Capabilities",
            "type": "Element",
            "required": True,
        },
    )
    id_capabilities: IdCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Id_Capabilities",
            "type": "Element",
            "required": True,
        },
    )
