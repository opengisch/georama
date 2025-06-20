from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_meta_data_type import (
    AbstractMetaDataType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MetaData(AbstractMetaDataType):
    """
    Abstract element which acts as the head of a substitution group for packages of
    MetaData properties.
    """

    class Meta:
        name = "_MetaData"
        namespace = "http://www.opengis.net/gml"
