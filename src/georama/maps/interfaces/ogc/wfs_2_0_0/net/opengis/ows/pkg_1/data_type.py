from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.domain_metadata_type import DomainMetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class DataType(DomainMetadataType):
    """Definition of the data type of this set of values.

    In this case, the xlink:href attribute can reference a URN for a
    well-known data type. For example, such a URN could be a data type
    identification URN defined in the "ogc" URN namespace.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
