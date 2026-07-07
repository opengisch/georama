from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_coverage_type import (
    AbstractCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCoverage(AbstractCoverageType):
    """This element serves as the head of a substitution group which may contain
    any coverage whose type is derived from gml:AbstractCoverageType.

    It may act as a variable in the definition of content models where
    it is required to permit any coverage to be valid.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
