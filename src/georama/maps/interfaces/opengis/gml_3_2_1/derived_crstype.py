from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrstype:
    """The gml:derivedCRSType property describes the type of a derived coordinate
    reference system.

    The required codeSpace attribute shall reference a source of
    information specifying the values and meanings of all the allowed
    string values for this property.
    """

    class Meta:
        name = "derivedCRSType"
        namespace = "http://www.opengis.net/gml/3.2"
