from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.generic_meta_data_type import (
    GenericMetaDataType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GenericMetaData(GenericMetaDataType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
