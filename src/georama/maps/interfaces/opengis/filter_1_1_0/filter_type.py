from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.bbox import Bbox
from georama.maps.interfaces.opengis.filter_1_1_0.beyond import Beyond
from georama.maps.interfaces.opengis.filter_1_1_0.binary_logic_op_type import (
    And,
    Not,
    Or,
)
from georama.maps.interfaces.opengis.filter_1_1_0.contains import Contains
from georama.maps.interfaces.opengis.filter_1_1_0.crosses import Crosses
from georama.maps.interfaces.opengis.filter_1_1_0.disjoint import Disjoint
from georama.maps.interfaces.opengis.filter_1_1_0.dwithin import Dwithin
from georama.maps.interfaces.opengis.filter_1_1_0.equals import Equals
from georama.maps.interfaces.opengis.filter_1_1_0.feature_id import FeatureId
from georama.maps.interfaces.opengis.filter_1_1_0.gml_object_id import GmlObjectId
from georama.maps.interfaces.opengis.filter_1_1_0.intersects import Intersects
from georama.maps.interfaces.opengis.filter_1_1_0.overlaps import Overlaps
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_between import (
    PropertyIsBetween,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_equal_to import (
    PropertyIsEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_greater_than import (
    PropertyIsGreaterThan,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_greater_than_or_equal_to import (
    PropertyIsGreaterThanOrEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_less_than import (
    PropertyIsLessThan,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_less_than_or_equal_to import (
    PropertyIsLessThanOrEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_like import PropertyIsLike
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_not_equal_to import (
    PropertyIsNotEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_null import PropertyIsNull
from georama.maps.interfaces.opengis.filter_1_1_0.touches import Touches
from georama.maps.interfaces.opengis.filter_1_1_0.within import Within

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FilterType:
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_between: Optional[PropertyIsBetween] = field(
        default=None,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than_or_equal_to: Optional[PropertyIsGreaterThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    not_value: Optional[Not] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    gml_object_id: list[GmlObjectId] = field(
        default_factory=list,
        metadata={
            "name": "GmlObjectId",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    feature_id: list[FeatureId] = field(
        default_factory=list,
        metadata={
            "name": "FeatureId",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
