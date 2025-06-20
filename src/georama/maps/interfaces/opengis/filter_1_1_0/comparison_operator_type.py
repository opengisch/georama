from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/ogc"


class ComparisonOperatorType(Enum):
    LESS_THAN = "LessThan"
    GREATER_THAN = "GreaterThan"
    LESS_THAN_EQUAL_TO = "LessThanEqualTo"
    GREATER_THAN_EQUAL_TO = "GreaterThanEqualTo"
    EQUAL_TO = "EqualTo"
    NOT_EQUAL_TO = "NotEqualTo"
    LIKE = "Like"
    BETWEEN = "Between"
    NULL_CHECK = "NullCheck"
