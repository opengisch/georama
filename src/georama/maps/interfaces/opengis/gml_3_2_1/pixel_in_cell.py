from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.code_with_authority_type import (
    CodeWithAuthorityType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PixelInCell(CodeWithAuthorityType):
    """Gml:pixelInCell is a specification of the way an image grid is associated
    with the image data attributes.

    The required codeSpace attribute shall reference a source of
    information specifying the values and meanings of all the allowed
    string values for this property.
    """

    class Meta:
        name = "pixelInCell"
        namespace = "http://www.opengis.net/gml/3.2"
