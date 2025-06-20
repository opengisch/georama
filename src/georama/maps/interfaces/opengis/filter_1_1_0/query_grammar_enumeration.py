from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class QueryGrammarEnumeration(Enum):
    """
    Used to specify the grammar of the feature query mechanism.
    """

    XPATH = "xpath"
    XQUERY = "xquery"
    OTHER = "other"
