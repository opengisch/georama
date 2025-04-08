from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CatalogSymbol(CodeType):
    """The catalogSymbol is the preferred lexical symbol used for this unit of
    measure.

    The codeSpace attribute in gml:CodeType identifies a namespace for
    the catalog symbol value, and might reference the external catalog.
    The string value in gml:CodeType contains the value of a symbol that
    should be unique within this catalog namespace. This symbol often
    appears explicitly in the catalog, but it could be a combination of
    symbols using a specified algebra of units.
    """

    class Meta:
        name = "catalogSymbol"
        namespace = "http://www.opengis.net/gml"
