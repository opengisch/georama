from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_with_authority_type import (
    CodeWithAuthorityType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstype(CodeWithAuthorityType):
    """The gml:derivedCRSType property describes the type of a derived coordinate
    reference system.

    The required codeSpace attribute shall reference a source of
    information specifying the values and meanings of all the allowed
    string values for this property.
    """

    class Meta:
        name = "derivedCRSType"
        namespace = "http://www.opengis.net/gml"
