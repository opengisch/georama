from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.image_crstype import ImageCrstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrs(ImageCrstype):
    class Meta:
        name = "ImageCRS"
        namespace = "http://www.opengis.net/gml"
