from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.available_functions_type import (
    AvailableFunctionsType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.conformance_type import ConformanceType
from georama.maps.interfaces.ogc.wfs_2_0_0.extended_capabilities_type import (
    ExtendedCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.id_capabilities_type import (
    IdCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.scalar_capabilities_type import (
    ScalarCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.spatial_capabilities_type import (
    SpatialCapabilitiesType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.temporal_capabilities_type import (
    TemporalCapabilitiesType,
)

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class FilterCapabilities:
    class Meta:
        name = "Filter_Capabilities"
        namespace = "http://www.opengis.net/fes/2.0"

    conformance: ConformanceType | None = field(
        default=None,
        metadata={
            "name": "Conformance",
            "type": "Element",
            "required": True,
        },
    )
    id_capabilities: IdCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Id_Capabilities",
            "type": "Element",
        },
    )
    scalar_capabilities: ScalarCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Scalar_Capabilities",
            "type": "Element",
        },
    )
    spatial_capabilities: SpatialCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Spatial_Capabilities",
            "type": "Element",
        },
    )
    temporal_capabilities: TemporalCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Temporal_Capabilities",
            "type": "Element",
        },
    )
    functions: AvailableFunctionsType | None = field(
        default=None,
        metadata={
            "name": "Functions",
            "type": "Element",
        },
    )
    extended_capabilities: ExtendedCapabilitiesType | None = field(
        default=None,
        metadata={
            "name": "Extended_Capabilities",
            "type": "Element",
        },
    )
