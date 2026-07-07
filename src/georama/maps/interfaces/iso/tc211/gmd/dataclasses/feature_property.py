from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.array_association_type import (
    FeaturePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureProperty(FeaturePropertyType):
    class Meta:
        name = "featureProperty"
        namespace = "http://www.opengis.net/gml"
