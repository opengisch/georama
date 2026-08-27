from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.features_locked_type import (
    FeaturesLockedType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.features_not_locked_type import (
    FeaturesNotLockedType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeatureResponseType:
    features_locked: FeaturesLockedType | None = field(
        default=None,
        metadata={
            "name": "FeaturesLocked",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    features_not_locked: FeaturesNotLockedType | None = field(
        default=None,
        metadata={
            "name": "FeaturesNotLocked",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    lock_id: str | None = field(
        default=None,
        metadata={
            "name": "lockId",
            "type": "Attribute",
        },
    )
