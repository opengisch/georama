from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.feature_property_type import (
    FeaturePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class FeatureProperty(FeaturePropertyType):
    class Meta:
        name = "featureProperty"
        namespace = "http://www.opengis.net/gml/3.2"
