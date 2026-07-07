from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.array_association_type import (
    AbstractFeatureCollectionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureCollection(AbstractFeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
