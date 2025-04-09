from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_meta_data_type import (
    AbstractMetaDataType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GenericMetaDataType(AbstractMetaDataType):
    pass
