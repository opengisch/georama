from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_point_coverage_type import (
    MultiPointCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointCoverage(MultiPointCoverageType):
    """In a gml:MultiPointCoverage the domain set is a gml:MultiPoint, that is a
    collection of arbitrarily distributed geometric points. The content model is
    derived by restriction from gml:AbstractDiscreteCoverageType. Note that the
    restriction replaces the generic gml:domainSet by the specific
    gml:multiPointDomain whose value is a gml:MultiPoint.

    In a gml:MultiPointCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the points of the gml:MultiPoint are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the points of the gml:MultiPoint are mapped to the members of the composite value in document order.
    -       For gml:File encodings the points of the gml:MultiPoint are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
