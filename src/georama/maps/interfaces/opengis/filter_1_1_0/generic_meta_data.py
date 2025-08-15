from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.generic_meta_data_type import (
    GenericMetaDataType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GenericMetaData(GenericMetaDataType):
    """Concrete element in the _MetaData substitution group, which permits any
    well-formed XML content.

    Intended to act as a container for metadata defined in external
    schemas, for which it is not possible to add the concrete components
    to the GML _MetaData substitution group directly. Deprecated with
    GML version 3.1.0.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
