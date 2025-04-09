from dataclasses import dataclass, field

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.all_some_type import (
    AllSomeType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.get_feature_type import (
    GetFeatureType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetFeatureWithLockType(GetFeatureType):
    expiry: int = field(
        default=300,
        metadata={
            "type": "Attribute",
        },
    )
    lock_action: AllSomeType = field(
        default=AllSomeType.ALL,
        metadata={
            "name": "lockAction",
            "type": "Attribute",
        },
    )
