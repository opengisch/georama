from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.meta_data_property_type import (
    MetaDataPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MetaDataProperty(MetaDataPropertyType):
    class Meta:
        name = "metaDataProperty"
        namespace = "http://www.opengis.net/gml"
