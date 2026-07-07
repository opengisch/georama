from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.code_with_authority_type import (
    CodeWithAuthorityType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Identifier(CodeWithAuthorityType):
    """Often, a special identifier is assigned to an object by the maintaining
    authority with the intention that it is used in references to the object For
    such cases, the codeSpace shall be provided.

    That identifier is usually unique either globally or within an
    application domain. gml:identifier is a pre-defined property for
    such identifiers.
    """

    class Meta:
        name = "identifier"
        namespace = "http://www.opengis.net/gml/3.2"
