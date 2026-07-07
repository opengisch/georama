from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CatalogSymbol(CodeType):
    """For global understanding of a unit of measure, it is often possible to
    reference an item in a catalog of units, using a symbol in that catalog.

    The "codeSpace" attribute in "CodeType" identifies a namespace for
    the catalog symbol value, and might reference the catalog. The
    "string" value in "CodeType" contains the value of a symbol that is
    unique within this catalog namespace. This symbol often appears
    explicitly in the catalog, but it could be a combination of symbols
    using a specified algebra of units. For example, the symbol "cm"
    might indicate that it is the "m" symbol combined with the "c"
    prefix.
    """

    class Meta:
        name = "catalogSymbol"
        namespace = "http://www.opengis.net/gml"
