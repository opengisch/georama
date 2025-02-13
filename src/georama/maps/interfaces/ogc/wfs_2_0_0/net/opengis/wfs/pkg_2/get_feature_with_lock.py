from dataclasses import dataclass

from wfs_2_0_0.net.opengis.wfs.pkg_2.get_feature_with_lock_type import (
    GetFeatureWithLockType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class GetFeatureWithLock(GetFeatureWithLockType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
