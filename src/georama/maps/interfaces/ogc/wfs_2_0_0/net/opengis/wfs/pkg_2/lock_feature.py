from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.lock_feature_type import (
    LockFeatureType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class LockFeature(LockFeatureType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
