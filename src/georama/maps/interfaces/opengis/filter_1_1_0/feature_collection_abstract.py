from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import (
    AbstractFeatureCollectionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureCollectionAbstract(AbstractFeatureCollectionType):
    class Meta:
        name = "_FeatureCollection"
        namespace = "http://www.opengis.net/gml"
