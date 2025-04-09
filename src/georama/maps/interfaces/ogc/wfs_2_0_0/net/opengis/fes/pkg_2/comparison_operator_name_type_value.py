from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


class ComparisonOperatorNameTypeValue(Enum):
    PROPERTY_IS_EQUAL_TO = "PropertyIsEqualTo"
    PROPERTY_IS_NOT_EQUAL_TO = "PropertyIsNotEqualTo"
    PROPERTY_IS_LESS_THAN = "PropertyIsLessThan"
    PROPERTY_IS_GREATER_THAN = "PropertyIsGreaterThan"
    PROPERTY_IS_LESS_THAN_OR_EQUAL_TO = "PropertyIsLessThanOrEqualTo"
    PROPERTY_IS_GREATER_THAN_OR_EQUAL_TO = "PropertyIsGreaterThanOrEqualTo"
    PROPERTY_IS_LIKE = "PropertyIsLike"
    PROPERTY_IS_NULL = "PropertyIsNull"
    PROPERTY_IS_NIL = "PropertyIsNil"
    PROPERTY_IS_BETWEEN = "PropertyIsBetween"
