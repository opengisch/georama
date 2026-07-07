from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.dynamic_feature_type import (
    DynamicFeatureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeature(DynamicFeatureType):
    """States are captured by time-stamped instances of a feature.

    The content model extends the standard gml:AbstractFeatureType with
    the gml:dynamicProperties model group. Each time-stamped instance
    represents a 'snapshot' of a feature. The dynamic feature classes
    will normally be extended to suit particular applications.  A
    dynamic feature bears either a time stamp or a history.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
