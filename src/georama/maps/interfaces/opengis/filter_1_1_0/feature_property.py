from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import FeaturePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureProperty(FeaturePropertyType):
    class Meta:
        name = "featureProperty"
        namespace = "http://www.opengis.net/gml"
