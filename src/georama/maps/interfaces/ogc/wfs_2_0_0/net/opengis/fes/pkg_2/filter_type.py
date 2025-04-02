from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.abstract_selection_clause_type import (
    AbstractSelectionClauseType,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.after import After
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.any_interacts import (
    AnyInteracts,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.bbox import Bbox
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.before import Before
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.begins import Begins
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.begun_by import BegunBy
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.beyond import Beyond
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.binary_logic_op_type import (
    And,
    Not,
    Or,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.contains import (
    Contains,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.crosses import Crosses
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.disjoint import (
    Disjoint,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.during import During
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.dwithin import Dwithin
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.ended_by import EndedBy
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.ends import Ends
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.equals import Equals
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.function_type import (
    Function,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.intersects import (
    Intersects,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.meets import Meets
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.met_by import MetBy
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.overlapped_by import (
    OverlappedBy,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.overlaps import (
    Overlaps,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_between import (
    PropertyIsBetween,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_equal_to import (
    PropertyIsEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_greater_than import (
    PropertyIsGreaterThan,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_greater_than_or_equal_to import (
    PropertyIsGreaterThanOrEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_less_than import (
    PropertyIsLessThan,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_less_than_or_equal_to import (
    PropertyIsLessThanOrEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_like import (
    PropertyIsLike,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_nil import (
    PropertyIsNil,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_not_equal_to import (
    PropertyIsNotEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.property_is_null import (
    PropertyIsNull,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.resource_id import (
    ResourceId,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.tcontains import (
    Tcontains,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.tequals import Tequals
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.touches import Touches
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.toverlaps import (
    Toverlaps,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.net.opengis.fes.pkg_2.within import Within

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class FilterType(AbstractSelectionClauseType):
    property_is_between: Optional[PropertyIsBetween] = field(
        default=None,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_nil: Optional[PropertyIsNil] = field(
        default=None,
        metadata={
            "name": "PropertyIsNil",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_greater_than_or_equal_to: Optional[PropertyIsGreaterThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    any_interacts: Optional[AnyInteracts] = field(
        default=None,
        metadata={
            "name": "AnyInteracts",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    overlapped_by: Optional[OverlappedBy] = field(
        default=None,
        metadata={
            "name": "OverlappedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    toverlaps: Optional[Toverlaps] = field(
        default=None,
        metadata={
            "name": "TOverlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    met_by: Optional[MetBy] = field(
        default=None,
        metadata={
            "name": "MetBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    meets: Optional[Meets] = field(
        default=None,
        metadata={
            "name": "Meets",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    tequals: Optional[Tequals] = field(
        default=None,
        metadata={
            "name": "TEquals",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    ends: Optional[Ends] = field(
        default=None,
        metadata={
            "name": "Ends",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    ended_by: Optional[EndedBy] = field(
        default=None,
        metadata={
            "name": "EndedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    during: Optional[During] = field(
        default=None,
        metadata={
            "name": "During",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    tcontains: Optional[Tcontains] = field(
        default=None,
        metadata={
            "name": "TContains",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    begun_by: Optional[BegunBy] = field(
        default=None,
        metadata={
            "name": "BegunBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    begins: Optional[Begins] = field(
        default=None,
        metadata={
            "name": "Begins",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    before: Optional[Before] = field(
        default=None,
        metadata={
            "name": "Before",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    after: Optional[After] = field(
        default=None,
        metadata={
            "name": "After",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
    resource_id: list[ResourceId] = field(
        default_factory=list,
        metadata={
            "name": "ResourceId",
            "type": "Element",
            "namespace": "http://www.opengis.net/fes/2.0",
        },
    )
