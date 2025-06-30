from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.describe_feature_type_type import (
    DescribeFeatureTypeType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DescribeFeatureType(DescribeFeatureTypeType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
