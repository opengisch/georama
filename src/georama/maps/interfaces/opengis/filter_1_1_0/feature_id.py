from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.feature_id_type import FeatureIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FeatureId(FeatureIdType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
