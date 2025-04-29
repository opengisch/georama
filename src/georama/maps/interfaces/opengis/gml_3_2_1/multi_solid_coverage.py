from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.discrete_coverage_type import (
    DiscreteCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidCoverage(DiscreteCoverageType):
    """In a gml:MultiSolidCoverage the domain is partioned into a collection of
    solids comprising a gml:MultiSolid.  The coverage function than maps each solid
    in the collection to a value in the range set. The content model is identical
    with gml:DiscreteCoverageType, but that gml:domainSet shall have values
    gml:MultiSolid.

    In a gml:MultiSolidCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the solids of the gml:MultiSolid are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the solids of the gml:MultiSolid are mapped to the members of the composite value in document order.
    -       For gml:File encodings the solids of the gml:MultiSolid are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
