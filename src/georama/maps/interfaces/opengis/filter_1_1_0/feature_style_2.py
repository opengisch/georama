from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.feature_style_property_type import (
    FeatureStylePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureStyle2(FeatureStylePropertyType):
    class Meta:
        name = "featureStyle"
        namespace = "http://www.opengis.net/gml"
