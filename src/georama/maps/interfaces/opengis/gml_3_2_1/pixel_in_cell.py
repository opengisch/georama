from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PixelInCell:
    """Gml:pixelInCell is a specification of the way an image grid is associated
    with the image data attributes.

    The required codeSpace attribute shall reference a source of
    information specifying the values and meanings of all the allowed
    string values for this property.
    """

    class Meta:
        name = "pixelInCell"
        namespace = "http://www.opengis.net/gml/3.2"
