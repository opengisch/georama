from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.image_crsref_type import (
    ImageCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ImageCrsref(ImageCrsrefType):
    class Meta:
        name = "imageCRSRef"
        namespace = "http://www.opengis.net/gml"
