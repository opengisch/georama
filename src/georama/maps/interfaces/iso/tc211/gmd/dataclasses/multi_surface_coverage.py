from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_surface_coverage_type import (
    MultiSurfaceCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceCoverage(MultiSurfaceCoverageType):
    """In a gml:MultiSurfaceCoverage the domain is partioned into a collection of
    surfaces comprising a gml:MultiSurface.  The coverage function than maps each
    surface in the collection to a value in the range set. The content model is
    derived by restriction from gml:AbstractDiscreteCoverageType. Note that the
    restriction replaces the generic gml:domainSet by the specific
    gml:multiSurfaceDomain whose value is a gml:MultiSurface.

    In a gml:MultiSurfaceCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the surfaces of the gml:MultiSurface are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the surfaces of the gml:MultiSurface are mapped to the members of the composite value in document order.
    -       For gml:File encodings the surfaces of the gml:MultiSurface are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
