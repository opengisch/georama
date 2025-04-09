from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_curve_coverage_type import (
    MultiCurveCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveCoverage(MultiCurveCoverageType):
    """In a gml:MultiCurveCoverage the domain is partioned into a collection of
    curves comprising a gml:MultiCurve.  The coverage function then maps each curve
    in the collection to a value in the range set. The content model is derived by
    restriction from gml:AbstractDiscreteCoverageType. Note that the restriction
    replaces the generic gml:domainSet by the specific gml:multiCurveDomain whose
    value is a gml:MultiCurve.

    In a gml:MultiCurveCoverage the mapping from the domain to the range is straightforward.
    -       For gml:DataBlock encodings the curves of the gml:MultiCurve are mapped in document order to the tuples of the data block.
    -       For gml:CompositeValue encodings the curves of the gml:MultiCurve are mapped to the members of the composite value in document order.
    -       For gml:File encodings the curves of the gml:MultiCurve are mapped to the records of the file in sequential order.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
