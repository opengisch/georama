from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.resource_id import ResourceId

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreatedOrModifiedFeatureType:
    resource_id: list[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
            "min_occurs": 1,
        },
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
