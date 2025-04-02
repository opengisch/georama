from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.resource_id import (
    ResourceId,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeaturesNotLockedType:
    resource_id: list[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
