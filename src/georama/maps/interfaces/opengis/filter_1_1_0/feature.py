from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_feature_type import (
    AbstractFeatureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Feature(AbstractFeatureType):
    class Meta:
        name = "_Feature"
        namespace = "http://www.opengis.net/gml"
