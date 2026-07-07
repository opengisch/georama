from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.meta_data_property_type import (
    MetaDataPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MetaDataProperty(MetaDataPropertyType):
    class Meta:
        name = "metaDataProperty"
        namespace = "http://www.opengis.net/gml/3.2"
