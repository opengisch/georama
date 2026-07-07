from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.discrete_coverage_type import (
    DiscreteCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointCoverage(DiscreteCoverageType):
    """In a gml:MultiPointCoverage the domain set is a gml:MultiPoint, that is a
    collection of arbitrarily distributed geometric points. The content model is
    identical with gml:DiscreteCoverageType, but that gml:domainSet shall have
    values gml:MultiPoint.

    In a gml:MultiPointCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the points of the gml:MultiPoint are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the points of the gml:MultiPoint are mapped to the members of the composite value in document order.
    -       For gml:File encodings the points of the gml:MultiPoint are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
