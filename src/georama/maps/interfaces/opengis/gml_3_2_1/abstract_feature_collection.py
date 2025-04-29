from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.feature_property_type import (
    AbstractFeatureCollectionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractFeatureCollection(AbstractFeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
