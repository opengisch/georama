from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SymbolTypeEnumeration(Enum):
    """
    Used to specify the type of the symbol used.
    """

    SVG = "svg"
    XPATH = "xpath"
    OTHER = "other"
