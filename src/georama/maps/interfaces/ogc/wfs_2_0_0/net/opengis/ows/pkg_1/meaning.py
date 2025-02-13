from dataclasses import dataclass

from wfs_2_0_0.net.opengis.ows.pkg_1.domain_metadata_type import DomainMetadataType

__NAMESPACE__ = "http://www.opengis.net/ows/1.1"


@dataclass
class Meaning(DomainMetadataType):
    """Definition of the meaning or semantics of this set of values.

    This Meaning can provide more specific, complete, precise, machine
    accessible, and machine understandable semantics about this
    quantity, relative to other available semantic information. For
    example, other semantic information is often provided in
    "documentation" elements in XML Schemas or "description" elements in
    GML objects.
    """

    class Meta:
        namespace = "http://www.opengis.net/ows/1.1"
