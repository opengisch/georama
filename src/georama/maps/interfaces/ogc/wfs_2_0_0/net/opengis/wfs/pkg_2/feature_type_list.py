from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.wfs.pkg_2.feature_type_list_type import (
    FeatureTypeListType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureTypeList(FeatureTypeListType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
