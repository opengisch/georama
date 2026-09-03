from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.domain_set import DomainSet
from georama.maps.interfaces.opengis.gml_3_2_1.grid_domain import GridDomain
from georama.maps.interfaces.opengis.gml_3_2_1.multi_curve_domain import (
    MultiCurveDomain,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_point_domain import (
    MultiPointDomain,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_solid_domain import (
    MultiSolidDomain,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_surface_domain import (
    MultiSurfaceDomain,
)
from georama.maps.interfaces.opengis.gml_3_2_1.range_set import RangeSet
from georama.maps.interfaces.opengis.gml_3_2_1.rectified_grid_domain import (
    RectifiedGridDomain,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoverageType(AbstractFeatureType):
    """The base type for coverages is gml:AbstractCoverageType.

    The basic elements of a coverage can be seen in this content model: the coverage contains gml:domainSet and gml:rangeSet properties. The gml:domainSet property describes the domain of the coverage and the gml:rangeSet property describes the range of the coverage.
    """

    rectified_grid_domain: RectifiedGridDomain | None = field(
        default=None,
        metadata={
            "name": "rectifiedGridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_domain: GridDomain | None = field(
        default=None,
        metadata={
            "name": "gridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_domain: MultiSolidDomain | None = field(
        default=None,
        metadata={
            "name": "multiSolidDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_domain: MultiSurfaceDomain | None = field(
        default=None,
        metadata={
            "name": "multiSurfaceDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_domain: MultiCurveDomain | None = field(
        default=None,
        metadata={
            "name": "multiCurveDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_domain: MultiPointDomain | None = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    domain_set: DomainSet | None = field(
        default=None,
        metadata={
            "name": "domainSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    range_set: RangeSet | None = field(
        default=None,
        metadata={
            "name": "rangeSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
