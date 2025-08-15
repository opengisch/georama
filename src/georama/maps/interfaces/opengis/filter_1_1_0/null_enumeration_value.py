from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class NullEnumerationValue(Enum):
    INAPPLICABLE = "inapplicable"
    MISSING = "missing"
    TEMPLATE = "template"
    UNKNOWN = "unknown"
    WITHHELD = "withheld"
