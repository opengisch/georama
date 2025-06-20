from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.feature_style_type import (
    FeatureStyleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureStyle1(FeatureStyleType):
    """
    The style descriptor for features.
    """

    class Meta:
        name = "FeatureStyle"
        namespace = "http://www.opengis.net/gml"
