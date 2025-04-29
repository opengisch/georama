from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_meta_data_type import (
    AbstractMetaDataType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractMetaData(AbstractMetaDataType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
