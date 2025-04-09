from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_solid_coverage_type import (
    MultiSolidCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidCoverage(MultiSolidCoverageType):
    """In a gml:MultiSolidCoverage the domain is partioned into a collection of
    solids comprising a gml:MultiSolid.  The coverage function than maps each solid
    in the collection to a value in the range set. The content model is derived by
    restriction from gml:AbstractDiscreteCoverageType. Note that the restriction
    replaces the generic gml:domainSet by the specific gml:multiSolidDomain whose
    value is a gml:MultiSolid.

    In a gml:MultiSolidCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the solids of the gml:MultiSolid are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the solids of the gml:MultiSolid are mapped to the members of the composite value in document order.
    -       For gml:File encodings the solids of the gml:MultiSolid are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
