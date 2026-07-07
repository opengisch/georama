from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.domain_metadata_type import (
    DomainMetadataType,
)

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class ReferenceSystem(DomainMetadataType):
    """Definition of the reference system used by this set of values, including the
    unit of measure whenever applicable (as is normal).

    In this case, the xlink:href attribute can reference a URN for a
    well-known reference system, such as for a coordinate reference
    system (CRS). For example, such a URN could be a CRS identification
    URN defined in the "ogc" URN namespace.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
