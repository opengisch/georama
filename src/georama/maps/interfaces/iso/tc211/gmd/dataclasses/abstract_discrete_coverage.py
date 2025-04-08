from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_discrete_coverage_type import (
    AbstractDiscreteCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractDiscreteCoverage(AbstractDiscreteCoverageType):
    """A discrete coverage consists of a domain set, range set and optionally a
    coverage function.

    The domain set consists of either spatial or temporal geometry
    objects, finite in number. The range set is comprised of a finite
    number of attribute values each of which is associated to every
    direct position within any single spatiotemporal object in the
    domain. In other words, the range values are constant on each
    spatiotemporal object in the domain. This coverage function maps
    each element from the coverage domain to an element in its range.
    The coverageFunction element describes the mapping function. This
    element serves as the head of a substitution group which may contain
    any discrete coverage whose type is derived from
    gml:AbstractDiscreteCoverageType.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
