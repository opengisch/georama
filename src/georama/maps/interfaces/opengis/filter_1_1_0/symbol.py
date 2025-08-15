from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.symbol_type import SymbolType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Symbol(SymbolType):
    """The symbol property.

    Extends the gml:AssociationType to allow for remote referencing of
    symbols.
    """

    class Meta:
        name = "symbol"
        namespace = "http://www.opengis.net/gml"
